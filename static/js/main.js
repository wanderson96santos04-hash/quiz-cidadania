const steps = document.querySelectorAll(".step");
const nextBtn = document.getElementById("nextBtn");
const prevBtn = document.getElementById("prevBtn");
const stepCounter = document.getElementById("stepCounter");
const progressFill = document.getElementById("progressFill");
const form = document.getElementById("multiStepForm");
const summaryBox = document.getElementById("summaryBox");

const fields = {
    nome: "",
    whatsapp: "",
    sobrenome_italiano: "",
    familia_cidadania: "",
    documentos: "",
    interesse: "",
    urgencia: "",
    consentimento: false
};

let currentStep = 1;
const finalStep = 8;
const visibleStepsForCounter = 7;

function updateHiddenFields() {
    document.getElementById("hidden_nome").value = fields.nome;
    document.getElementById("hidden_whatsapp").value = fields.whatsapp;
    document.getElementById("hidden_sobrenome_italiano").value = fields.sobrenome_italiano;
    document.getElementById("hidden_familia_cidadania").value = fields.familia_cidadania;
    document.getElementById("hidden_documentos").value = fields.documentos;
    document.getElementById("hidden_interesse").value = fields.interesse;
    document.getElementById("hidden_urgencia").value = fields.urgencia;
    document.getElementById("hidden_consentimento").value = fields.consentimento ? "sim" : "nao";
}

function renderSummary() {
    if (!summaryBox) return;

    summaryBox.innerHTML = `
        <div class="summary-row">
            <div class="summary-label">Nome</div>
            <div class="summary-value">${fields.nome || "-"}</div>
        </div>
        <div class="summary-row">
            <div class="summary-label">WhatsApp</div>
            <div class="summary-value">${fields.whatsapp || "-"}</div>
        </div>
        <div class="summary-row">
            <div class="summary-label">Sobrenome italiano</div>
            <div class="summary-value">${fields.sobrenome_italiano || "-"}</div>
        </div>
        <div class="summary-row">
            <div class="summary-label">Família com cidadania</div>
            <div class="summary-value">${fields.familia_cidadania || "-"}</div>
        </div>
        <div class="summary-row">
            <div class="summary-label">Documentos</div>
            <div class="summary-value">${fields.documentos || "-"}</div>
        </div>
        <div class="summary-row">
            <div class="summary-label">Interesse</div>
            <div class="summary-value">${fields.interesse || "-"}</div>
        </div>
        <div class="summary-row">
            <div class="summary-label">Urgência</div>
            <div class="summary-value">${fields.urgencia || "-"}</div>
        </div>
    `;
}

function updateUI() {
    steps.forEach((step) => {
        step.classList.remove("active");

        if (Number(step.dataset.step) === currentStep) {
            step.classList.add("active");
        }
    });

    const stepNumberForCounter = currentStep > 7 ? 7 : currentStep;

    if (stepCounter) {
        stepCounter.textContent = `Etapa ${stepNumberForCounter} de ${visibleStepsForCounter}`;
    }

    if (progressFill) {
        const progressPercent = (currentStep / finalStep) * 100;
        progressFill.style.width = `${progressPercent}%`;
    }

    if (prevBtn) {
        prevBtn.style.display = currentStep === 1 ? "none" : "inline-flex";
    }

    if (nextBtn) {
        nextBtn.style.display = currentStep === finalStep ? "none" : "inline-flex";
        nextBtn.textContent = currentStep === 1 ? "Continuar análise" : "Continuar";
    }

    if (currentStep === finalStep) {
        renderSummary();
    }

    window.scrollTo({
        top: 0,
        behavior: "smooth"
    });
}

function validateCurrentStep() {
    if (currentStep === 1) {
        const nomeInput = document.getElementById("nome");
        const nome = nomeInput ? nomeInput.value.trim() : "";

        if (nome.length < 3) {
            return false;
        }

        fields.nome = nome;
    }

    if (currentStep === 2) {
        const whatsappInput = document.getElementById("whatsapp");
        const whatsapp = whatsappInput ? whatsappInput.value.trim() : "";

        if (whatsapp.length < 8) {
            return false;
        }

        fields.whatsapp = whatsapp;
    }

    if (currentStep === 3 && !fields.sobrenome_italiano) {
        return false;
    }

    if (currentStep === 4 && !fields.familia_cidadania) {
        return false;
    }

    if (currentStep === 5 && !fields.documentos) {
        return false;
    }

    if (currentStep === 6 && !fields.interesse) {
        return false;
    }

    if (currentStep === 7 && !fields.urgencia) {
        return false;
    }

    updateHiddenFields();
    return true;
}

function goNext() {
    if (!validateCurrentStep()) return;

    if (currentStep < finalStep) {
        currentStep += 1;
        updateUI();
    }
}

function goPrev() {
    if (currentStep > 1) {
        currentStep -= 1;
        updateUI();
    }
}

if (nextBtn) {
    nextBtn.addEventListener("click", goNext);
}

if (prevBtn) {
    prevBtn.addEventListener("click", goPrev);
}

document.querySelectorAll(".option-btn").forEach((button) => {
    button.addEventListener("click", function () {
        const field = this.dataset.field;
        const value = this.dataset.value;

        document
            .querySelectorAll(`.option-btn[data-field="${field}"]`)
            .forEach((btn) => btn.classList.remove("selected"));

        this.classList.add("selected");
        fields[field] = value;
        updateHiddenFields();

        setTimeout(() => {
            goNext();
        }, 180);
    });
});

const nomeInput = document.getElementById("nome");

if (nomeInput) {
    nomeInput.addEventListener("keydown", function (e) {
        if (e.key === "Enter") {
            e.preventDefault();

            const nome = nomeInput.value.trim();

            if (nome.length < 3) {
                nomeInput.focus();
                return;
            }

            fields.nome = nome;
            updateHiddenFields();

            setTimeout(() => {
                goNext();
            }, 250);
        }
    });
}

const whatsappInput = document.getElementById("whatsapp");

if (whatsappInput) {
    whatsappInput.addEventListener("input", function (e) {
        let value = e.target.value.replace(/\D/g, "");

        if (value.length > 11) {
            value = value.slice(0, 11);
        }

        if (value.length > 10) {
            value = value.replace(/^(\d{2})(\d{5})(\d{0,4}).*/, "($1) $2-$3");
        } else if (value.length > 6) {
            value = value.replace(/^(\d{2})(\d{4})(\d{0,4}).*/, "($1) $2-$3");
        } else if (value.length > 2) {
            value = value.replace(/^(\d{2})(\d{0,5})/, "($1) $2");
        } else if (value.length > 0) {
            value = value.replace(/^(\d*)/, "($1");
        }

        e.target.value = value;
    });

    whatsappInput.addEventListener("keydown", function (e) {
        if (e.key === "Enter") {
            e.preventDefault();

            const whatsapp = whatsappInput.value.trim();

            if (whatsapp.length < 8) {
                whatsappInput.focus();
                return;
            }

            fields.whatsapp = whatsapp;
            updateHiddenFields();

            setTimeout(() => {
                goNext();
            }, 250);
        }
    });
}

const consentCheckbox = document.getElementById("consentimento_checkbox");

if (consentCheckbox) {
    consentCheckbox.addEventListener("change", function () {
        fields.consentimento = this.checked;
        updateHiddenFields();
    });
}

if (form) {
    form.addEventListener("submit", function (e) {
        updateHiddenFields();

        if (!fields.consentimento) {
            e.preventDefault();
            alert("Você precisa autorizar o compartilhamento dos dados para concluir.");
            return;
        }

        if (
            !fields.nome ||
            !fields.whatsapp ||
            !fields.sobrenome_italiano ||
            !fields.familia_cidadania ||
            !fields.documentos ||
            !fields.interesse ||
            !fields.urgencia
        ) {
            e.preventDefault();
            alert("Preencha todas as etapas antes de concluir.");
        }
    });
}

updateUI();
updateHiddenFields();