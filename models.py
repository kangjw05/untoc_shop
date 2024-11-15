from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey, Boolean
from database import item_Base


# Item 모델 정의
class Item(item_Base):
    __tablename__ = "item"

    item_id = Column(Integer, primary_key=True, index=True)
    item_name = Column(String(255), nullable=False)
    item_price = Column(Integer, nullable=False)
    amount = Column(Integer, nullable=False)
    create_at = Column(String(30), nullable=False)
    create_date = Column(DateTime, nullable=False)