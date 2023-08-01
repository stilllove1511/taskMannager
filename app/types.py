from typing import List
import strawberry


@strawberry.type
class TableType:
    id: int
    title: str
    lists:List['ListType']

@strawberry.type
class ListType:
    id: int
    title: str
    table:TableType
    cards:List['CardType']

@strawberry.type
class CardType:
    id: int
    title: str
    list:ListType
