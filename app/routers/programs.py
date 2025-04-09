from fastapi import APIRouter
from app.models.mcp_program import MCPProgram

router = APIRouter()

# Sample data
programs = [
    MCPProgram(id=1, name="Program A", description="Description of Program A", version="1.0"),
    MCPProgram(id=2, name="Program B", description="Description of Program B", version="2.0")
]

@router.get("/programs", response_model=list[MCPProgram])
async def get_programs():
    return programs

@router.get("/programs/{program_id}", response_model=MCPProgram)
async def get_program(program_id: int):
    for program in programs:
        if program.id == program_id:
            return program
    return None