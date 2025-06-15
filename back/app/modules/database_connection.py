import os

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


def get_sqlalchemy_url_env_var():
    environment = os.getenv("BACK_ENV", "dev")
    return os.environ[f"{environment.upper()}_SQLALCHEMY_URL"]


engine = create_engine(get_sqlalchemy_url_env_var())
SessionFactory = sessionmaker(bind=engine)


class SessionManager:
    def __enter__(self):
        self.session = SessionFactory()
        return self.session

    def __exit__(self, exc_type, exc_value, traceback):
        if exc_type is None:
            self.session.commit()
        else:
            self.session.rollback()
        self.session.close()
