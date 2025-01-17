from fastapi import APIRouter

router = APIRouter()


@router.get("/")
def read_root():
    return {"Hello": "World"}


@router.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    print("item_id: ", item_id)
    return {"item_id": item_id, "q": q}


@router.get("/users/me")
def read_user_me():
    return {"user_id": "the current user"}


@router.get("/users/{user_id}")
def read_user(user_id: str):
    return {"user_id": user_id}


@router.get("/items/")
def read_items(q: str = None):
    return {"q": q}