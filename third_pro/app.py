from fastapi import FastAPI

from third_pro.api.routes import clients, products

app = FastAPI()

app.include_router(clients.router)
app.include_router(products.router)


@app.get('/')
def home():
    return {'message', 'success'}
