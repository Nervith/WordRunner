from fastapi import FastAPI, UploadFile, File
import pathlib
app = FastAPI()

TEXTS_DIR = pathlib.Path(__file__).parent.resolve() / "texts"
TEXTS_DIR.mkdir(exist_ok=True)


@app.get("/")
def home():
    return {"message":"Hello World"}

@app.post("/upload")
async def upload(file: UploadFile = File(...)):
    data = await file.read()
    with open(TEXTS_DIR / file.filename, "wb") as f:
        f.read(data)
    return {"filename": file.filename}
@app.get("/start")
def start():
    return {"message":"In a hole in the ground, there lived a Hobbit."}