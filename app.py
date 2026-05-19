from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles

import model

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):

    listar_hospedes = model.get_hospedes()
    listar_quartos = model.get_quartos()
    listar_reservas_ativas = model.get_reservas_ativas()

    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={
            "listar_hospedes": listar_hospedes,
            "listar_quartos": listar_quartos,
            "listar_reservas_ativas": listar_reservas_ativas
        }
    )

#--------------------------
# Pagina de Quartos
#--------------------------

# Listar quartos
@app.get("/quartos", response_class=HTMLResponse)
async def quartos(request: Request):

    return templates.TemplateResponse(
        request=request,
        name="quartos.html",
        context={"request": request, "quartos": model.consulta_quartos()}
    )

# Adicionar quartos
@app.get("/add_quarto", response_class=HTMLResponse)
async def add_quarto(request: Request):

    return templates.TemplateResponse(
        request=request,
        name="add_quarto.html",
        context={"request": request}
    )


# Salvar adição do quarto
@app.post("/add_quarto", response_class=HTMLResponse)
async def salvar_quarto(request: Request):

    form = await request.form()

    model.add_quarto(
        form.get("numero"),
        form.get("tipo"),
        form.get("valor_diaria"),
        form.get("status")
    )

    return RedirectResponse(url="/quartos", status_code=303)


# editar quartos
@app.get("/edit_quarto/{id}", response_class=HTMLResponse)
async def editar_quarto(request: Request, id: int):

    return templates.TemplateResponse(
        request=request,
        name="edit_quarto.html",
        context={"request": request, "quarto": model.consulta_quarto_id(id)}
    )

# salvar edição de quartos
@app.post("/edit_quarto/{id}")
async def salvar_edit_quarto(request: Request, id: int):

    form = await request.form()

    model.edit_quarto(
        id,
        form.get("numero"),
        form.get("tipo"),
        form.get("valor_diaria"),
        form.get("status")
    )

    return RedirectResponse(url="/quartos", status_code=303)


# Excluir um quarto
@app.post("/delete_quarto/{id}")
async def deletar_quarto(id: int):

    model.delete_quarto(id)

    return RedirectResponse(url="/quartos", status_code=303)

#--------------------------
# Pagina de Hospedes
#--------------------------

# LISTAR TODOS OS HOSPEDES
@app.get("/hospedes", response_class=HTMLResponse)
async def hospedes(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="hospedes.html",
        context={
            "request": request,
            "hospedes": model.consulta_hospedes()
        }
    )

#Adcionar Hospede
@app.get("/add_hospede", response_class=HTMLResponse)
async def add_hospedes(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="add_hospedes.html",
        context={
            "request": request,
            "hospedes": model.consulta_hospedes()
        }
    )

@app.post("/add_hospede", response_class=HTMLResponse)
async def salvar_hospede(request: Request):

    form = await request.form()

    model.add_hospede(
        form.get("nome"),
        form.get("email"),
        form.get("telefone"),
        form.get("cpf")
    )

    return RedirectResponse(url="/hospedes", status_code=303)

# Atualizar Hospede
@app.get("/edit_hospede/{id}", response_class=HTMLResponse)
async def update_hospede(request: Request, id: int):

    hospede = model.get_hospede(id)

    return templates.TemplateResponse(
        request=request,
        name="update_hospede.html",
        context={
            "request": request,
            "hospede": hospede
        }
    )

@app.post("/edit_hospede/{id}", response_class=HTMLResponse)
async def salvar_update_hospede(request: Request, id: int):

    form = await request.form()

    model.update_hospede(
        id,
        form.get("nome"),
        form.get("email"),
        form.get("telefone"),
        form.get("cpf")
    )

    return RedirectResponse(url="/hospedes", status_code=303)

#Excluir hospede
@app.get("/delete_hospede/{id}", response_class=HTMLResponse)
async def excluir_hospede(id: int):

    model.elete_hospede(id)

    return RedirectResponse(
        url="/hospedes",
        status_code=303
    )


#reservaas 
@app.get("/reservas", response_class=HTMLResponse)
async def lista_reservas(request: Request):

    return templates.TemplateResponse(
        request=request,
        name="reservas.html",
        context={"request": request, "reservas": model.consulta_reservas()}
    )