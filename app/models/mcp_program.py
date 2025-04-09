from pydantic import BaseModel

class MCPProgram(BaseModel):
    id: int
    name: str
    description: str
    version: str