from fastapi import FastAPI

app = FastAPI()


@app.get("/api/v1/info")
async def app_info():
    return {
        "status": "live",
        "version": "1.0",
        "apiInfo": "API integrated with Gemini AI via LangChain to inter-transform JSON & CSV data",
        "health": "green"
    }
