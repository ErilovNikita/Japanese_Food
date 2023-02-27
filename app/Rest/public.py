from fastapi import FastAPI, APIRouter
from app.Utils.db import generalPosrgresBase, engine, session, User, Order, Foot

router = APIRouter()

@router.post("/orders")
async def orders():
    list = await Order.objects.all()
    return list

@router.post("/users")
async def users():
    list = await User.objects.all()
    return list

@router.post("/foots")
async def foots():
    list = await Foot.objects.all()
    return list