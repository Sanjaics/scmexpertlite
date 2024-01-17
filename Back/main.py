from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from Routes import account, shipment, user, device,feedback

app = FastAPI()

# CORS middleware configuration
origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(account.router)
app.include_router(shipment.router)
app.include_router(user.router)
app.include_router(device.router)
app.include_router(feedback.router)