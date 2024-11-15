from fastapi import APIRouter, HTTPException, Depends, Response,Security

from sqlalchemy.orm import Session
from database import get_itemdb

from item.item_schema import Item, Create_item, Modify_item
from models import Item as Item_model

router = APIRouter(
    prefix="/item"
)


def insert_data(db, table):
    db.add(table)
    db.commit()
    db.refresh(table)



@router.get("/get_items")
def get_items(skip:int = 0, limit:int = 10,
              item_db: Session = Depends(get_itemdb)):
    
    item = item_db.query(Item_model).all()

    return item[skip : skip + limit]

@router.get("/get_item")
def get_item(item_id:int,
             item_db: Session = Depends(get_itemdb)):
    
    item = item_db.query(Item_model).filter(Item_model.item_id == item_id).first()
    if not item:
        raise HTTPException(status_code=404, detail=f"item_id : {item_id} is None")
    
    return item


@router.post("/create_item", response_model=Create_item)
def create_item(item:Create_item, 
                item_db: Session = Depends(get_itemdb)):
    
    create_items = Item_model(item_name=item.item_name, 
                item_price=item.item_price,
                amount=item.amount,
                create_at=item.create_at,
                create_date=item.create_date
                )

    insert_data(item_db, create_items)

    return create_items

@router.put("/update_item", response_model=Modify_item)
def update_item(item: Modify_item,
                item_id: int,
                item_db: Session = Depends(get_itemdb)):
    
    modify_item = Modify_item(item_name=item.item_name,
                              item_price=item.item_price,
                              amount=item.amount)

    item = item_db.query(Item_model).filter(Item_model.item_id == item_id).first()

    if not item:
        raise HTTPException(status_code=404, detail=f"item_id : {item_id} 내역이 없습니다.")

    item.item_name = modify_item.item_name
    item.item_price = modify_item.item_price
    item.amount = modify_item.amount

    item_db.commit()
    item_db.refresh(item)

    return modify_item

@router.delete("/delete_item/{item_id}")
def delete_item(item_id: int,
                item_db: Session = Depends(get_itemdb)):
    
    item = item_db.query(Item_model).filter(Item_model.item_id == item_id)
    if not item.first():
        raise HTTPException(status_code=404, detail=f"item_id : {item_id} is None")
    
    item.delete()

    item_db.commit()

    return {"message":f"item_id : {item_id} - success delete"}