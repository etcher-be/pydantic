from pydantic import BaseModel

class BarModel(BaseModel):
    whatever: int

class FooBarModel(BaseModel):
    banana: float
    foo: str
    bar: BarModel

m = FooBarModel(banana=3.14, foo='hello', bar={'whatever': 123})

print(dict(m))
#> {'banana': 3.14, 'foo': 'hello', 'bar': <BarModel whatever=123>}

for name, value in m:
    print(f'{name}: {value}')

#> banana: 3.14
#> foo: hello
#> bar: BarModel whatever=123
