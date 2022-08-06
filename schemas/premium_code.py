




class PremiumCode(BaseModel):
    code_id: UUID = Field(...)
    premium_code: str = Field(..., example="ARMYCRIHARMYCRIH")
    enabled: bool = Field(default=False)
    
    user: Optional[User] = Field(default=None)