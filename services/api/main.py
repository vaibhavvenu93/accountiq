"""AccountIQ API. Run: uvicorn main:app --reload (from services/api)."""
from pathlib import Path
import json
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field
from scoring import rank_accounts

ROOT = Path(__file__).resolve().parents[2]
app = FastAPI(title="AccountIQ API", version="0.1.0")
app.add_middleware(CORSMiddleware, allow_origins=["http://localhost:3000"], allow_methods=["GET", "POST"], allow_headers=["*"])

class ICP(BaseModel):
    industries: list[str] = Field(default_factory=lambda: ["B2B SaaS"])
    regions: list[str] = Field(default_factory=lambda: ["UK", "EU"])
    min_employees: int = Field(default=10, ge=0)
    max_employees: int = Field(default=500, ge=0)

@app.get("/health")
def health(): return {"status": "ok", "version": "0.1.0"}

@app.get("/demo/accounts")
def accounts(): return json.loads((ROOT / "data/demo/accounts.json").read_text())

@app.post("/score")
def score(icp: ICP):
    if icp.min_employees > icp.max_employees: raise HTTPException(422, "min_employees cannot exceed max_employees")
    return {"accounts": rank_accounts(accounts(), icp.model_dump()), "method": "deterministic-v1", "disclaimer": "All demo companies and signals are fictional."}
