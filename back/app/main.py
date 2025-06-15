from dotenv import load_dotenv

load_dotenv()


from app.routers import courses, instructors, lessons  # noqa: E402
from fastapi import FastAPI  # noqa: E402
from fastapi.middleware.cors import CORSMiddleware  # noqa: E402
from fastapi.responses import JSONResponse  # noqa: E402
from psycopg2.extensions import AsIs, register_adapter  # noqa: E402
from pydantic import HttpUrl  # noqa: E402
from sqlalchemy.exc import SQLAlchemyError  # noqa: E402

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Exception handlers


@app.exception_handler(SQLAlchemyError)
async def sqlalchemy_exception_handler(_, exc: SQLAlchemyError):
    return JSONResponse(status_code=400, content={"error": exc._message()})


@app.exception_handler(Exception)
async def exception_handler(*_):
    return JSONResponse(status_code=500, content={"error": "An unknown error ocurred"})


def adapt_httpurl(url: HttpUrl):
    return AsIs(f"'{str(url)}'")


# Adapters

register_adapter(HttpUrl, adapt_httpurl)

# Routes

app.include_router(instructors.router)
app.include_router(courses.router)
app.include_router(lessons.router)


@app.get("/")
def home():
    return "Hello"
