import requests
import json
from pathlib import Path

def extrair_dados_ibge():
    """
    Realiza a requisição HTTP na API do IBGE, extrai os dados 
    dos estados brasileiros e salva em um arquivo JSON local.
    """
    # 1. Configurações da extração
    url = "https://servicodados.ibge.gov.br/api/v1/localidades/estados"
    diretorio_destino = Path("dados/raw")
    caminho_arquivo = diretorio_destino / "estados_ibge.json"

    # 2. Garantir que a pasta de destino exista
    diretorio_destino.mkdir(parents=True, exist_ok=True)
    
    print("Iniciando a extração de dados do IBGE...")

    try:
        # 3. Requisição HTTP
        resposta = requests.get(url, timeout=10)
        resposta.raise_for_status()  # Levanta erro se o status não for 200 (OK)

        # 4. Salvar os dados localmente
        dados_json = resposta.json()
        
        with open(caminho_arquivo, "w", encoding="utf-8") as arquivo:
            json.dump(dados_json, arquivo, ensure_ascii=False, indent=4)
            
        print(f"Extração concluída com sucesso! Dados salvos em: '{caminho_arquivo}'")

    except requests.exceptions.RequestException as erro:
        print(f"Erro ao tentar extrair os dados: {erro}")

if __name__ == "__main__":
    extrair_dados_ibge()