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

#---- PAgina Quartos ----
@app.get("/quartos", response_class=HTMLResponse)
async def quartos(request: Request):

    return templates.TemplateResponse(
        request=request,
        name="quartos.html",
        context={"request": request, "quartos": model.consulta_quartos()}
    )

#adicionar um quarto
@app.get("/add_quarto", response_class=HTMLResponse)
async def add_quarto(request: Request):

    return templates.TemplateResponse(
        request=request,
        name="add_quarto.html",
        context={"request": request}
    )


#salvar quarto
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

#deletar um quarto
@app.post("/delete_quarto/{id}")
async def deletar_quarto(id: int):

    delete_quarto(id)

    return RedirectResponse(
        url="/quartos",
        status_code=303
    )

#editar um quarto
@app.get("/edit_quarto/{id}", response_class=HTMLResponse)
async def editar_quarto(request: Request, id: int):

    return templates.TemplateResponse(
        request=request,
        name="edit_quarto.html",
        context={"request": request, "quarto": model.consulta_quarto_id(id)}
    )

# SALVAR A EDIÇÃO 
@app.post("/edit_quarto/{id}")
async def salvar_edicao_quarto(request: Request, id: int):

    form = await request.form()

    update_quarto(
        id,
        form.get("numero"),
        form.get("tipo"),
        form.get("valor_diaria"),
        form.get("status")
    )

    return RedirectResponse(
        url="/quartos",
        status_code=303
    )




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


