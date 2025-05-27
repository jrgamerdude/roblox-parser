from fastapi import FastAPI, UploadFile, File
from fastapi.responses import JSONResponse
import uvicorn

app = FastAPI()

@app.post("/parse-roblox-file")
async def read_roblox_script(file: UploadFile = File(...)):
    if not file.filename.endswith((".rbxl", ".lua")):
        return JSONResponse(
            status_code=400,
            content={"error": "Invalid file type. Only .rbxl and .lua supported."}
        )

    contents = await file.read()
    try:
        # Simpel parsing eller behandling
        text_preview = contents.decode("utf-8", errors="ignore")[:1000]
        return {
            "filename": file.filename,
            "preview": text_preview
        }
    except Exception as e:
        return JSONResponse(
            status_code=500,
            content={"error": str(e)}
        )

# Kun hvis du kører lokalt
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
