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
    posts = model.get_posts()

    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={"posts": posts}
    )

#--------------------------
# Pagina de Quartos
#--------------------------

# LISTAR TODOS OS QUARTOS
@app.get("/quartos", response_class=HTMLResponse)
async def quartos(request: Request):

    return templates.TemplateResponse(
        request=request,
        name="quartos.html",
        context={"request": request, "quartos": model.consulta_quartos()}
    )

# ADICIONAR QUARTOS
@app.get("/add_quarto", response_class=HTMLResponse)
async def add_quarto(request: Request):

    return templates.TemplateResponse(
        request=request,
        name="add_quarto.html",
        context={"request": request}
    )


# SALVAR A ADIÇAO DE QUARTOS
@app.post("/add_quarto", response_class=HTMLResponse)
async def salvar_quarto(request: Request):

    form = await request.form()

    add_quarto(
        form.get("numero"),
        form.get("tipo"),
        form.get("valor_diaria"),
        form.get("status")
    )

    return RedirectResponse(url="/quartos", status_code=303)


# EDITAR QUARTOS
@app.get("/edit_quarto/{id}", response_class=HTMLResponse)
async def editar_quarto(request: Request, id: int):

    return templates.TemplateResponse(
        request=request,
        name="edit_quarto.html",
        context={"request": request, "quarto": model.consulta_quarto_id(id)}
    )

# SALVAR A EDIÇÃO DOS QUARTOS
@app.post("/edit_quarto/{id}")
async def salvar_edicao_quarto(request: Request, id: int):

    form = await request.form()

    model.update_quarto(
        id,
        form.get("numero"),
        form.get("tipo"),
        form.get("valor_diaria"),
        form.get("status")
    )

    return RedirectResponse(url="/quartos", status_code=303)


# DELETAR UM QUARTO
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

    add_hospede(
        form.get("nome"),
        form.get("email"),
        form.get("telefone"),
        form.get("cpf")
    )

    return RedirectResponse(url="/hospedes", status_code=303)