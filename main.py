from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from typing import List
from datetime import time
import json

app = FastAPI(title="Medecine Dose Tracker", description="API pour le suivi des médicaments")


class Medecine(BaseModel):
    id: int = Field(..., description="ID unique du médicament")
    name: str = Field(..., description="Nom du médicament")
    dosage: str = Field(..., description="Dosage recommandé (ex: 1 comprimé)")
    reminder_time: time = Field(..., description="Heure de rappel quotidienne")
    notes: str = Field(None, description="Notes facultatives")


def read_data():
    with open("data.json", "r", encoding="utf-8") as f:
        return json.load(f)

def write_data(data):
    with open("data.json", "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)


@app.get("/", summary="Bienvenue", description="Page d'accueil de l'API")
def root():
    return {"message": "Bienvenue sur l'API Medecine Dose Tracker"}


@app.get("/medecines", response_model=List[Medecine], summary="Lister les médicaments")
def get_medecines():
    data = read_data()
    return data


@app.post("/medecines", response_model=Medecine, status_code=201, summary="Ajouter un médicament")
def add_medecine(med: Medecine):
    data = read_data()
    if any(m["id"] == med.id for m in data):
        raise HTTPException(status_code=400, detail="Ce ID existe déjà")
    data.append(med.dict())
    write_data(data)
    return med


@app.get("/medecines/{med_id}", response_model=Medecine, summary="Afficher un médicament")
def get_medecine_by_id(med_id: int):
    data = read_data()
    med = next((m for m in data if m["id"] == med_id), None)
    if not med:
        raise HTTPException(status_code=404, detail="Médicament introuvable")
    return med


@app.delete("/medecines/{med_id}", summary="Supprimer un médicament")
def delete_medecine(med_id: int):
    data = read_data()
    new_data = [m for m in data if m["id"] != med_id]
    if len(new_data) == len(data):
        raise HTTPException(status_code=404, detail="ID non trouvé")
    write_data(new_data)
    return {"message": "Médicament supprimé"}


# uvicorn main:app --reload

