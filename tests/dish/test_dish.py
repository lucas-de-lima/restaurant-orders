from src.models.dish import Dish  # noqa: F401, E261, E501
from src.models.ingredient import Ingredient, Restriction

import pytest


# Req 2
def test_dish():
    mocotó = Dish("Mocotó", 30.0)
    feijoada = Dish("Feijoada", 45.0)

    assert mocotó.name == "Mocotó"
    assert mocotó.price == 30.0

    assert feijoada.name == "Feijoada"
    assert feijoada.price == 45.0

    assert hash(mocotó) != hash(feijoada)
    assert hash(mocotó) == hash(Dish("Mocotó", 30.0))
    assert mocotó == Dish("Mocotó", 30.0)

    assert hash(feijoada) != hash(mocotó)
    assert hash(feijoada) == hash(Dish("Feijoada", 45.0))
    assert feijoada == Dish("Feijoada", 45.0)   

    assert str(mocotó) == "Dish('Mocotó', R$30.00)"
    assert str(feijoada) == "Dish('Feijoada', R$45.00)"

    with pytest.raises(TypeError):
        Dish("Mocotó", "preço estranho")

    with pytest.raises(ValueError):
        Dish("Mocotó", -1.0)
    
    ingredient_mocoto = Ingredient("carne")
    mocotó.add_ingredient_dependency(ingredient_mocoto, 1)

    assert ingredient_mocoto in mocotó.get_ingredients()
    assert Restriction.ANIMAL_DERIVED in mocotó.get_restrictions()

    with pytest.raises(TypeError):
        Dish("Feijoada", "preço estranho")
    
    with pytest.raises(ValueError):
        Dish("Feijoada", -1.0)

    ingredient_feijoada = Ingredient("bacon")
    feijoada.add_ingredient_dependency(ingredient_feijoada, 1)

    assert ingredient_feijoada in feijoada.get_ingredients()
    assert Restriction.ANIMAL_DERIVED in feijoada.get_restrictions()
