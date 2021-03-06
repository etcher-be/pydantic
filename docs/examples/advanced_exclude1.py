from pydantic import BaseModel, SecretStr

class User(BaseModel):
    id: int
    username: str
    password: SecretStr

class Transaction(BaseModel):
    id: str
    user: User
    value: int

transaction = Transaction(
    id="1234567890",
    user=User(
        id=42,
        username="JohnDoe",
        password="hashedpassword"
    ),
    value=9876543210
)

# using a set:
print(transaction.dict(exclude={'user', 'value'}))
#> {'id': '1234567890'}

# using a dict:
print(transaction.dict(exclude={'user': {'username', 'password'}, 'value': ...}))
#> {'id': '1234567890', 'user': {'id': 42}}

print(transaction.dict(include={'id': ..., 'user': {'id'}}))
#> {'id': '1234567890', 'user': {'id': 42}}
