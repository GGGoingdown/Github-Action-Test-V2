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


@router.get("/items/{item_id}/users/{user_id}")
def read_item_user(item_id: int, user_id: str, q: str = None):
    return {"item_id": item_id, "user_id": user_id, "q": q}


@router.get("/items/{item_id}/users/{user_id}/items/{item_id2}")
def read_item_user_item(item_id: int, user_id: str, item_id2: int, q: str = None):
    return {"item_id": item_id, "user_id": user_id, "item_id2": item_id2, "q": q}


@router.get("/items/{item_id}/users/{user_id}/items/{item_id2}/users/{user_id2}")
def read_item_user_item_user(item_id: int, user_id: str, item_id2: int, user_id2: str, q: str = None):
    return {"item_id": item_id, "user_id": user_id, "item_id2": item_id2, "user_id2": user_id2, "q": q}

@router.get("/items/{item_id}/users/{user_id}/items/{item_id2}/users/{user_id2}/items/{item_id3}")
def read_item_user_item_user_item(item_id: int, user_id: str, item_id2: int, user_id2: str, item_id3: int, q: str = None):
    return {"item_id": item_id, "user_id": user_id, "item_id2": item_id2, "user_id2": user_id2, "item_id3": item_id3, "q": q}