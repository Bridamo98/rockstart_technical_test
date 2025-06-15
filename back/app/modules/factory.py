from contextlib import contextmanager
from dataclasses import dataclass
from typing import Any, Generic, Optional, Protocol, Type, TypeVar

from app.modules.database_connection import SessionManager
from pydantic import BaseModel
from sqlalchemy import func, select
from sqlalchemy.inspection import inspect
from sqlalchemy.orm import Session

T = TypeVar("T", bound=Any)


class SerializerProtocol(Protocol[T]):
    @staticmethod
    def serialize(
        obj: T, *, include: list[str] | None = None, exclude: list[str] | None = None
    ) -> dict[str, Any]: ...

    @classmethod
    def serialize_many(
        cls,
        objs: list[T],
        *,
        include: list[str] | None = None,
        exclude: list[str] | None = None,
    ) -> list[dict[str, Any]]: ...


class SAJsonSerializer:
    @staticmethod
    def serialize(
        obj: T,  # type: ignore
        *,
        include: list[str] | None = None,
        exclude: list[str] | None = None,
    ) -> dict[str, Any]:
        mapper = inspect(obj).mapper
        columns = [c.key for c in mapper.column_attrs]

        if include is not None:
            columns = [c for c in columns if c in include]
        if exclude is not None:
            columns = [c for c in columns if c not in exclude]

        return {c: getattr(obj, c) for c in columns}

    @classmethod
    def serialize_many(
        cls,
        objs: list[T],
        *,
        include: list[str] | None = None,
        exclude: list[str] | None = None,
    ) -> list[dict[str, Any]]:
        return [cls.serialize(o, include=include, exclude=exclude) for o in objs]


@dataclass
class DynamicFactory(Generic[T]):
    model: Type[T]
    session: Session
    serializer: type[SerializerProtocol] = SAJsonSerializer

    def get_by_id(self, id_: Any) -> Optional[T]:
        return self.session.get(self.model, id_)

    def get_one_by(self, **filters) -> Optional[T]:
        return self.session.query(self.model).filter_by(**filters).first()

    def get_all(self) -> list[T]:
        return self.session.query(self.model).all()

    def filter(self, *criterion, **filters) -> list[T]:
        q = self.session.query(self.model)
        if criterion:
            q = q.filter(*criterion)
        if filters:
            q = q.filter_by(**filters)
        return q.all()

    def count(self, **filters) -> int:
        return (
            self.session.query(func.count(self.model.id)).filter_by(**filters).scalar()
        )

    def exists(self, **filters) -> bool:
        stmt = select(self.model).filter_by(**filters).exists()
        return self.session.query(stmt).scalar()

    def create(self, obj: T, *, flush: bool = False, refresh: bool = False) -> T:
        self.session.add(obj)
        if flush:
            self.session.flush()
        else:
            self.session.commit()
        if refresh:
            self.session.refresh(obj)
        return obj

    def bulk_create(self, objs: list[T]) -> list[T]:
        self.session.bulk_save_objects(list(objs))
        self.session.commit()
        return objs

    def update_by_id(
        self, id_: Any, *, refresh: bool = False, **changes
    ) -> Optional[T]:
        obj = self.get_by_id(id_)
        if not obj:
            return None
        for key, value in changes.items():
            setattr(obj, key, value)
        self.session.commit()
        if refresh:
            self.session.refresh(obj)
        return obj

    def update_by_model(
        self,
        pydantic_model: BaseModel,
        lookup_field: str = "id",
        *,
        refresh: bool = False,
    ) -> Optional[T]:
        lookup_value = getattr(pydantic_model, lookup_field, None)
        if lookup_value is None:
            raise ValueError(
                f"Field'{lookup_field}' is not present in the Pydantic model. Please contact support."
            )

        obj = self.get_by_id(lookup_value)
        if not obj:
            return None

        update_data = pydantic_model.model_dump(exclude_unset=True)
        update_data.pop(lookup_field, None)

        for key, value in update_data.items():
            setattr(obj, key, value)

        self.session.commit()
        if refresh:
            self.session.refresh(obj)
        return obj

    def upsert(self, defaults: dict[str, Any] | None = None, **keys) -> T:
        defaults = defaults or {}
        obj = self.get_one_by(**keys)
        if obj:
            for k, v in defaults.items():
                setattr(obj, k, v)
        else:
            params = {**keys, **defaults}
            obj = self.model(**params)
            self.session.add(obj)
        self.session.commit()
        return obj

    def delete(self, id_: Any) -> bool:
        obj = self.get_by_id(id_)
        if not obj:
            return False
        self.session.delete(obj)
        self.session.commit()
        return True

    def bulk_delete(self, *criterion, **filters) -> int:
        query = self.session.query(self.model)
        if criterion:
            query = query.filter(*criterion)
        if filters:
            query = query.filter_by(**filters)
        rows = query.delete(synchronize_session=False)
        self.session.commit()
        return rows

    def serialize(self, obj: T, *, include=None, exclude=None):
        return self.serializer.serialize(obj, include=include, exclude=exclude)

    def serialize_many(self, objs: list[T], *, include=None, exclude=None):
        return self.serializer.serialize_many(objs, include=include, exclude=exclude)


@contextmanager
def factory_for(model: Type[T]):
    with SessionManager() as session:
        yield DynamicFactory(model=model, session=session)
