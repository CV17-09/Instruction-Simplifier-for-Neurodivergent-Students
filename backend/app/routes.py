import json
from fastapi import APIRouter, Depends, UploadFile, File
from sqlalchemy.orm import Session

from app.database import get_db
from app.models import Assignment
from app.schemas import AssignmentRequest
from app.ai_service import simplify_assignment
from app.utils import validate_text, safe_json_dumps

router = APIRouter()

@router.post("/simplify")
def simplify(request: AssignmentRequest, db: Session = Depends(get_db)):
    text = validate_text(request.text)

    result = simplify_assignment(text)

    assignment = Assignment(
        original_text=text,
        simplified_output=safe_json_dumps(result)
    )

    db.add(assignment)
    db.commit()
    db.refresh(assignment)

    return {
        "id": assignment.id,
        "result": result
    }

@router.get("/history")
def get_history(db: Session = Depends(get_db)):
    assignments = db.query(Assignment).order_by(Assignment.created_at.desc()).all()

    return [
        {
            "id": item.id,
            "original_text": item.original_text[:150],
            "simplified_output": json.loads(item.simplified_output),
            "created_at": item.created_at
        }
        for item in assignments
    ]