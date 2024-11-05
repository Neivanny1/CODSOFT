from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.middleware.cors import CORSMiddleware

from app import models
from app.database import engine
from app.routers import task, user, auth
from app.config import settings



models.Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="To-Do List API",
    description="An API for managing your To-Do tasks",
    version="1.0.0",
)

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(auth.router)
app.include_router(user.router)
app.include_router(task.router)

@app.get("/", response_class=HTMLResponse, tags=["HOMEPAGE"], summary="HOMEPAGE OF THE TODO",
description="EXPLAINS EVERYTHING ABOUT THE APP")
def root():
    html_content = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Welcome to My To-Do Project</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                text-align: center;
                margin: 50px;
                background-color: #f5f5f5;
            }
            h1 {
                color: #333;
            }
            p {
                color: #666;
                font-size: 1.2em;
            }
            a {
                display: inline-block;
                margin-top: 20px;
                padding: 10px 20px;
                color: white;
                background-color: #007acc;
                text-decoration: none;
                font-size: 1.1em;
                border-radius: 5px;
            }
            a:hover {
                background-color: #005f99;
            }
        </style>
    </head>
    <body>
        <h1>Welcome to My To-Do Project!</h1>
        <p>This project is part of my internship at CodSoft.</p>
        <p>I'm Eric Mwakazi, a Backend Developer.</p>
        <p>Click the link below to explore the API documentation and try out the endpoints.</p>
        <a href="/docs">Go to Swagger UI</a>
    </body>
    </html>
    """
    return HTMLResponse(content=html_content)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
