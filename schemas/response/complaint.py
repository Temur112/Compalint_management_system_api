from schemas.base import BaseComplaint
import datetime
from models import State

class ComplaintOut(BaseComplaint):
    id: int
    crated_at: datetime.datetime
    status: State