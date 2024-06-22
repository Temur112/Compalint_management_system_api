import asyncclick as click
from models.enums import RoleType
from db import databse
from managers.user import UserManager


@click.command
@click.option("-f", "--first_name", type=str, required=True)
@click.option("-l", "--last_name", type=str, required=True)
@click.option("-e", "--email", type=str, required=True)
@click.option("-p", "--phone", type=str, required=True)
@click.option("-i", "--iban", type=str, required=True)
@click.option("-pas", "--password", type=str, required=True)
async def create_user(first_name, last_name, email, phone, iban, password):
    user_data = {
        "first_name": first_name,
        "last_name": last_name,
        "email": email,
        "password": password,
        "phone": phone,
        "iban": iban,
        "role": RoleType.admin,
    }
    await databse.connect()
    UserManager.register(user_data)
    await databse.disconnect()


if __name__ == "__main__":
    create_user(_anyio_backend="asyncio")
