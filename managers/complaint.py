from db import databse
from models import complaints, RoleType, State


class ComplaintManager:
    @staticmethod
    async def get_complaints(user):
        q = complaints.select()
        if user["role"] == RoleType.complainer:
            q = q.where(complaints.c.complainer_id == user["id"])
        elif user["role"] == RoleType.approver:
            q = q.where(complaints.c.state == State.pending)

        return await databse.fetch_all(q)

    @staticmethod
    async def create_complaint(complaint_data, user):
        complaint_data["complainer_id"] = user["id"]
        id_ = await databse.execute(complaints.insert().values(complaint_data))
        return await databse.fetch_one(
            complaints.select().where(complaints.c.id == id_)
        )

    @staticmethod
    async def delete_complaint(id_):
        await databse.execute(complaints.delete().where(complaints.c.id == id_))

    @staticmethod
    async def approve(id_):
        await databse.execute(
            complaints.update()
            .where(complaints.c.id == id_)
            .values(status=State.approved)
        )

    @staticmethod
    async def reject(id_):
        await databse.execute(
            complaints.update()
            .where(complaints.c.id == id_)
            .values(status=State.rejected)
        )
