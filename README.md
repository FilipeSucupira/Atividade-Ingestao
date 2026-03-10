# 🛠️ Pipeline de Dados: Etapa de Extração (Extract)

Este repositório contém a solução para a atividade de construção da etapa de extração de uma pipeline de dados. O projeto consome dados da API pública do IBGE, simulando a ingestão de dados para a camada *Raw* (bruta) de um Data Lake.

## 📌 Objetivo
Realizar a extração automatizada de dados sobre os estados brasileiros utilizando requisições HTTP (REST) e salvar a resposta localmente em formato estruturado.

## ⚙️ Tecnologias e Bibliotecas Utilizadas
* **Python 3.x**: Linguagem principal do projeto.
* **`requests`**: Para realizar as requisições HTTP na API do IBGE.
* **`pathlib`**: (Built-in) Para manipulação e criação segura de diretórios locais.
* **`json`**: (Built-in) Para estruturação e salvamento do *payload*.

## 📂 Estrutura do Projeto

Após a execução, o projeto terá a seguinte estrutura:

```text
├── extract.py            # Script principal de extração
├── requirements.txt      # Dependências do projeto
├── README.md             # Documentação
└── dados/
    └── raw/              # Diretório gerado automaticamente
        └── estados_ibge.json  # Arquivo final extraído da API
```

## 🚀 Como Executar

**1. Clone ou baixe este repositório**
Navegue até a pasta do projeto através do seu terminal.

**2. Instale as dependências**
Recomenda-se o uso de um ambiente virtual (venv). Para instalar a biblioteca `requests`, execute:

```bash
pip install -r requirements.txt
```

**3. Execute o script de extração**

```bash
python extract.py
```

## 🏗️ Decisões de Arquitetura e Boas Práticas
* **Camada Raw:** O script isola os dados baixados em um diretório `dados/raw/`, adotando o padrão de organização de Data Lakes estruturados.
* **Resiliência:** Implementação de `timeout` (10 segundos) nas requisições HTTP para evitar travamentos, além de blocos `try/except` para captura e tratamento de quedas de rede ou instabilidades da API.
* **Formatação (Encoding):** Uso explícito de `utf-8` e `ensure_ascii=False` para garantir que a acentuação dos estados brasileiros seja preservada no arquivo JSON final.

---
**Desenvolvido por:** [Filipe César - CC5MA]  
**Disciplina:** [Ciência de Dados - CESUPA ARGO]
