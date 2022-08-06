

class ValidationCode(BaseModel):
    code_id: UUID = Field(...)
    secret_code: str = Field(..., example="ARMYCRIHARMYCRIH")
    enabled: bool = Field(default=False)
    
    project: Optional[Project] = Field(default=None)