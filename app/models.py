from pydantic import BaseModel, Field


class LeadForm(BaseModel):
    nome: str = Field(..., min_length=2, max_length=120)
    whatsapp: str = Field(..., min_length=8, max_length=30)
    sobrenome_italiano: str
    familia_cidadania: str
    documentos: str
    interesse: str
    urgencia: str
    consentimento: bool