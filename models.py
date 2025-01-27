"""Tables models definition"""

from datetime import datetime
from sqlalchemy import Column, Integer, String, func
from sqlalchemy.ext.declarative import declarative_base
from pydantic import BaseModel, ConfigDict
from sqlalchemy.sql.sqltypes import DateTime

Base = declarative_base()

class WalletRequest(Base):
    __tablename__ = 'wallet_requests'

    id = Column(Integer, primary_key=True, index=True)
    wallet_address = Column(String, index=True)
    bandwidth = Column(String)
    energy = Column(String)
    trx_balance = Column(String)
    timestamp = Column(DateTime, server_default=func.now(), nullable=False)


# Pydantic model for response
class WalletRequestResponse(BaseModel):
    id: int
    wallet_address: str
    bandwidth: str
    energy: str
    trx_balance: str
    timestamp: datetime

    model_config = ConfigDict(
        from_attributes=True, json_encoders={datetime: lambda dt: dt.isoformat()}
    )
