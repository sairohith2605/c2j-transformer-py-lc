from dotenv import load_dotenv
from fastapi import FastAPI, HTTPException, UploadFile

from processor import Processor

app = FastAPI()
processor = Processor()

load_dotenv()

@app.get("/api/v1/info")
async def app_info() -> dict[str, str]:
    return {
        "status": "live",
        "version": "1.0",
        "apiInfo": "API integrated with Gemini AI via LangChain to inter-transform JSON & CSV data",
        "health": "green"
    }

@app.post("/api/v1/transformation/c2j")
async def transform_csv_to_json(file: UploadFile):
    csv_contents = await file.read()
    try:
        return await processor.csv_to_json(csv_data_bytes=csv_contents)
    except UnicodeDecodeError:
        raise  HTTPException(
            status_code=400, 
            detail={
                "error": "Invalid file supplied. Only text based files are supported"
            }
        )
    except ValueError as ve:
        raise  HTTPException(
            status_code=400, 
            detail={
                "error": str(ve)
            }
        )
