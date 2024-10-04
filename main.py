from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root() :
    return{"message" : "hello UNTOC"}

# create - post
# read - get
# update - put/patch
# delete - delete

#make items....

items = [
    {"item_id" : 1, "item_name" : "water1", "item_price" : 100},
    {"item_id" : 2, "item_name" : "water2", "item_price" : 200},
    {"item_id" : 3, "item_name" : "water3", "item_price" : 300},
    {"item_id" : 4, "item_name" : "water4", "item_price" : 400},
    {"item_id" : 5, "item_name" : "water5", "item_price" : 500},
    {"item_id" : 6, "item_name" : "water6", "item_price" : 600}
]

# 1. get
# 1-1. get all item
@app.get("/item/get_all_item")
def get_all_item(skip: int = 0, limit: int = 10):
    return items[skip : skip + limit]  # 자료 10개 씩 보여줌.

# 1-2. get one item
@app.get("/item/get_item/{item_id}")
def get_item(item_id: int) :
    for item in items:
        if item["item_id"] == item_id:
            return item

# 2. post
# 2-1. create item
@app.post("/item/create_item")
def create_item(item_id : int, item_name : str, item_price : int):
    # item_id가 중복되어 있는지 확인
    for item in items:
        if item["item_id"] == item_id:
            return {"error message" : "같은 아이디에 해당하는 아이템이 있습니다."}
    
    # 입력한 item을 append
    items.append({"item_id" : item_id,
                 "item_name" : item_name,
                 "item_price" : item_price})
    
    return items

# 3. put (전체 수정) (cf: patch - 일부 수정)
# 3-1. modify item
@app.put("/item/update_item/{item_id}")
def update_item(item_id : int, item_name : str, item_price : int):
    for item in items:
        if item["item_id"] == item_id:
            item["item_name"] = item_name
            item["item_price"] = item_price
            return item

# 4. delete
# 4-1. delete item
@app.delete("/item/delete_item/{item_id}")
def delete_item(item_id : int):
    for item in items:
        if item["item_id"] == item_id:
            deleted_item = items.pop(item_id-1)
            return{"message" : "deleted", "deleted_item" : deleted_item}
    return {"error" : "Item not found"}



# if __name__ == "__main__":
#     import uvicorn
    
#     uvicorn.run("main:app", host="127.0.0.1", port = 8000, reload=True)

# uvicorn main:app --reload