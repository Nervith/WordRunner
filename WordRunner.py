from fastapi import FastAPI, UploadFile, File
import pathlib
app = FastAPI()
app = FastAPI(title="Tiny Uploader")
TEXTS_DIR = pathlib.Path(__file__).parent.resolve() / "texts"
TEXTS_DIR.mkdir(exist_ok=True)


@app.get("/")
def home():
    return {"message":"Hello World"}

@app.post("/upload")
async def upload(file: UploadFile = File(...)):
    dst = TEXTS_DIR / file.filename
    with dst.open("wb") as f:
        while True:
            chunk = await file.read(1024 * 1024)
            if not chunk:
                break
            f.write(chunk)
    await file.close()
    return {"saved_to": str(dst)}

@app.get("/start")
def start():
    return {"message":"In a hole in the ground, there lived a Hobbit."}