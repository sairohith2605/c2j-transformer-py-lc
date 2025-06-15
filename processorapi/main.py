from dotenv import load_dotenv
from fastapi import FastAPI, HTTPException, Response, UploadFile
from fastapi.responses import FileResponse

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

@app.post("/api/v1/transformation/j2c")
async def transform_json_to_csv(data: list[dict[str, object]]):
    try:
        csv_data = await processor.json_to_csv(data=data)
        return Response(
            content=csv_data,
            headers={"Content-Disposition": "attachment;filename=csv_data.csv"},
            media_type="text/plain"
        )
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
