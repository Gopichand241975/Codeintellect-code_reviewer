from fastapi import FastAPI, UploadFile, File
from analyzer import analyze_code

app = FastAPI(
    title="CodeIntellect API",
    description="AI Code Intelligence Reviewer",
    version="1.0"
)

@app.get("/")
def home():
    return {"message": "Welcome to CodeIntellect AI Reviewer"}

@app.post("/analyze/")
async def analyze(file: UploadFile = File(...)):
    content = await file.read()
    code_text = content.decode("utf-8")

    result = analyze_code(code_text)

    return result
