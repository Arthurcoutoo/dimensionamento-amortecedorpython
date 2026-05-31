import math

def dimensionar_amortecimento(massa, frequencia_natural_hz, zeta):
    """
    Calcula os parâmetros do sistema de amortecimento.
    massa: kg (por roda)
    frequencia_natural_hz: Hz (frequência desejada para o sistema)
    zeta: fator de amortecimento (zeta < 1 subamortecido, zeta = 1 crítico)
    """
    # 1. Frequência natural angular (omega_n)
    omega_n = 2 * math.pi * frequencia_natural_hz
    
    # 2. Cálculo da rigidez da mola (k) -> k = m * omega_n^2
    k_mola = massa * (omega_n ** 2)
    
    # 3. Amortecimento crítico (c_critico) -> c_c = 2 * m * omega_n
    c_critico = 2 * massa * omega_n
    
    # 4. Coeficiente de amortecimento real (c) -> c = zeta * c_critico
    c_amortecedor = zeta * c_critico
    
    # 5. Deflexão estática da mola (x_estatica) -> x = (m * g) / k
    g = 9.81
    deflexao_estatica = (massa * g) / k_mola

    # Exibição dos resultados formatados
    print(f"--- RESULTADOS DO DIMENSIONAMENTO ---")
    print(f"Massa por Roda: {massa} kg")
    print(f"Frequência Natural: {frequencia_natural_hz} Hz")
    print(f"Fator de Amortecimento (Zeta): {zeta}")
    print(f"-------------------------------------")
    print(f"Rigidez da Mola (k): {k_mola:.2f} N/m ({k_mola/1000:.2f} N/mm)")
    print(f"Coeficiente do Amortecedor (c): {c_amortecedor:.2f} N.s/m")
    print(f"Amortecimento Crítico (Cc): {c_critico:.2f} N.s/m")
    print(f"Deflexão Estática da Mola: {deflexao_estatica * 1000:.2f} mm")
    print(f"-------------------------------------")
    
    if zeta < 1:
        print("Status do Sistema: Subamortecido (Ideal para conforto automotivo, com oscilação controlada).")
    elif zeta == 1:
        print("Status do Sistema: Amortecimento Crítico (Retorna ao equilíbrio o mais rápido possível sem oscilar).")
    else:
        print("Status do Sistema: Superamortecido (Retorno lento ao equilíbrio).")

# Exemplo de uso: Carro médio com 350kg por roda, freq. alvo de 1.5 Hz e zeta de 0.4 (padrão comercial)
dimensionar_amortecimento(massa=350, frequencia_natural_hz=1.5, zeta=0.4)
