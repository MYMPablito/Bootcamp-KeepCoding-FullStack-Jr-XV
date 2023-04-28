from appcoints.models import AllCoinApiIo, Exchange, ModelError
from appcoints.config import APIKEY
import pytest


def test_allcoint():
    todo = AllCoinApiIo()
    assert isinstance(todo, AllCoinApiIo)
    todo.getAllCoins(APIKEY)
    total = len(todo.lista_criptos) + len(todo.lista_no_criptos)
    assert total == 16379

def test_exchange():
    cambio = Exchange("ETH")
    cambio.updateExchange(APIKEY)
    assert cambio.rate > 0
    assert cambio.rate != None

def text_exchange_error():
    cambio2 = Exchange("ÑIÑO")
    with pytest.raises(ModelError) as exceptionInfo:
        cambio2.updateExchange(APIKEY)
    assert str(exceptionInfo.value) ==  "status: 550, error: You requested specific single item that we don't have at this moment."
    assert cambio2.status_code == 550










