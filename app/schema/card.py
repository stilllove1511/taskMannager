# file: myapp/schema.py
import strawberry

from app.types import CardType
from ..models import Card
from typing import List

@strawberry.type
class CardQuery:
    @strawberry.field
    def getCard (self) -> List[CardType]:
        return Card.objects.all()
    @strawberry.field
    def getCardById(self, id: int) -> CardType:
        return Card.objects.get(id=id)

@strawberry.type
class CardMutation:
    @strawberry.mutation
    def addCard(self, title: str, list: int) -> CardType:
        return Card.objects.create(title=title, list=list)
    @strawberry.mutation
    def updateCard(self, id: int, title: str, list: int) -> CardType:
        return Card.objects.filter(id=id).update(title=title, list_=list)
    @strawberry.mutation
    def deleteCard(self, id: int) -> CardType:
        return Card.objects.filter(id=id).delete()