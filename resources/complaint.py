from fastapi import APIRouter, Depends
from starlette.requests import Request
from managers.complaint import ComplaintManager
from managers.auth import oauth2_bearer, is_complainer, is_admin, is_approver
from schemas.request.complaint import ComplaintIn
from typing import List
from schemas.response.complaint import ComplaintOut


router = APIRouter(tags=["Complaints"], prefix="/complaints")


@router.get(
    "/getComplaints",
    dependencies=[Depends(oauth2_bearer)],
    response_model=List[ComplaintOut],
)
async def get_complaints(
    request: Request,
):
    user = request.state.user
    return await ComplaintManager.get_complaints(user)


@router.post(
    "/create",
    response_model=ComplaintOut,
    dependencies=[Depends(oauth2_bearer), Depends(is_complainer)],
)
async def create_complaint(request: Request, complaint: ComplaintIn):
    user = request.state.user
    return await ComplaintManager.create_complaint(complaint.model_dump(), user)


@router.delete(
    "/deleteComplaint/{complaint_id}",
    dependencies=[Depends(oauth2_bearer), Depends(is_admin)],
    status_code=204,
)
async def delete_complaint_by_id(complaint_id: int):
    await ComplaintManager.delete_complaint(complaint_id)


@router.put(
    "/{complaint_id}/approve",
    dependencies=[Depends(oauth2_bearer), Depends(is_approver)],
    status_code=204,
)
async def approve_complaint(complaint_id):
    await ComplaintManager.approve(complaint_id)


@router.put(
    "/{complaint_id}/reject",
    dependencies=[Depends(oauth2_bearer), Depends(is_approver)],
    status_code=204,
)
async def reject_complaint(complaint_id):
    await ComplaintManager.approve(complaint_id)
