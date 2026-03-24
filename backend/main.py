from fastapi import FastAPI, UploadFile, File
import pandas as pd
from db import get_session
from models import create_transaction

app = FastAPI()

@app.get("/")
def home():
    return {"status": "BHAVYA backend running"}

@app.post("/upload-csv")
async def upload_csv(file: UploadFile = File(...)):
    df = pd.read_csv(file.file)

    with get_session() as session:
        for _, row in df.iterrows():
            session.execute_write(
                create_transaction,
                row['sender'],
                row['receiver'],
                float(row['amount']),
                row['timestamp']
            )

    return {"message": "Data uploaded successfully"}
