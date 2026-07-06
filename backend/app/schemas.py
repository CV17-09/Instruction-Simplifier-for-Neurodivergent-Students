from pydantic import BaseModel
from typing import List, Optional

class AssignmentRequest(BaseModel):
    text: str

class SimplifiedResponse(BaseModel):
    plain_summary: str
    start_here: str
    checklist: List[str]
    timeline: List[str]
    deadlines: List[str]
    materials_needed: List[str]
    rubric_simplified: Optional[str]
    time_estimate: str