from sqlalchemy import Table, String, Integer, Column, Text, Float, DateTime, func, Enum, ForeignKey
from db import metadata
from models.enums import State

complaints = Table(
    "complaints",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("title", String(255), nullable=False),
    Column("desciption", Text, nullable=False),
    Column("photo_url", String(255), nullable=False),
    Column("amount", Float, nullable= False),
    Column("crated_at", DateTime, server_default=func.now()),
    Column("status", Enum(State), server_default=State.pending.name),
    Column("complainer_id", Integer, ForeignKey("users.id"), nullable=False)
)