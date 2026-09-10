def monitorar_suporte_de_vida(oxigenio: float, temperatura: float, pressao: float) -> str:
    """
    Monitora os níveis do ambiente da estação espacial.
    Retorna o status dos sistemas com base nos parâmetros recebidos.
    """
    alertas = []

    # Validação de Oxigênio (Padrão: 19.5% a 23.5%)
    if oxigenio < 19.5 or oxigenio > 23.5:
        alertas.append(f"CRITICO: Nível de Oxigênio fora do padrão ({oxigenio}%).")
    
    # Validação de Temperatura (Padrão: 18°C a 26°C)
    if temperatura < 18.0 or temperatura > 26.0:
        alertas.append(f"ALERTA: Temperatura fora do padrão ({temperatura}°C).")
        
    # Validação de Pressão (Padrão: 98 kPa a 104 kPa)
    if pressao < 98.0 or pressao > 104.0:
        alertas.append(f"ALERTA: Pressão atmosférica fora do padrão ({pressao} kPa).")

    if not alertas:
        return "SUCESSO: Todos os sistemas de suporte de vida estão NOMINAIS."
    
    return "FALHA DETECTADA:\n- " + "\n- ".join(alertas)

# Teste básico de integração (Boas práticas de QA)
if __name__ == "__main__":
    print("--- Iniciando Monitoramento ---")
    print(monitorar_suporte_de_vida(21.0, 22.5, 101.3))
    print("\n--- Simulando Falha ---")
    print(monitorar_suporte_de_vida(15.0, 30.0, 95.0))