from fastapi import APIRouter, Form, Request
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates

from app.config import TEMPLATES_DIR
from app.lead_manager import save_lead

router = APIRouter()
templates = Jinja2Templates(directory=str(TEMPLATES_DIR))


@router.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@router.get("/obrigado", response_class=HTMLResponse)
async def obrigado(request: Request):
    return templates.TemplateResponse("obrigado.html", {"request": request})


@router.post("/lead")
async def create_lead(
    nome: str = Form(...),
    whatsapp: str = Form(...),
    sobrenome_italiano: str = Form(...),
    familia_cidadania: str = Form(...),
    documentos: str = Form(...),
    interesse: str = Form(...),
    urgencia: str = Form(...),
    consentimento: str = Form(...),
):
    consent = consentimento.lower() == "sim"

    lead = {
        "nome": nome.strip(),
        "whatsapp": whatsapp.strip(),
        "sobrenome_italiano": sobrenome_italiano.strip(),
        "familia_cidadania": familia_cidadania.strip(),
        "documentos": documentos.strip(),
        "interesse": interesse.strip(),
        "urgencia": urgencia.strip(),
        "consentimento": consent,
    }

    save_lead(lead)

    return RedirectResponse(url="/obrigado", status_code=303)