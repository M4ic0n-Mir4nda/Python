# test_estacionamento.py

import pytest
from datetime import datetime
from estacionamento import Estacionamento
from ticket import Ticket

@pytest.fixture
def estacionamento():
    return Estacionamento()

def test_emitir_ticket(estacionamento):
    # Given
    placa = "ABC-4321"
    modelo = "Picape"
    
    # When
    ticket = Ticket(placa, modelo)
    estacionamento.emitir_ticket(ticket)
    
    # Then
    assert ticket in estacionamento.tickets_em_aberto

def test_calcular_valor_devido(estacionamento):
    # Given
    placa = "XYZ-8765"
    modelo = "Esportivo"
    entrada = datetime(2024, 5, 31, 21, 0)  # Entrada às 21:00
    
    # When
    ticket = Ticket(placa, modelo, entrada=entrada)
    estacionamento.registrar_saida(ticket)
    valor_devido = estacionamento.calcular_valor_devido(ticket)
    
    # Then
    assert valor_devido == 15  # R$ 15 para a primeira hora + R$ 5 para a segunda hora

if __name__ == "__main__":
    pytest.main()
