from fastapi import FastAPI
from app.database import Base, engine
from app.routers import menu_views, submenu_views, dish_views

Base.metadata.create_all(bind=engine)


app = FastAPI()

app.include_router(menu_views.router)
app.include_router(submenu_views.router)
app.include_router(dish_views.router)






