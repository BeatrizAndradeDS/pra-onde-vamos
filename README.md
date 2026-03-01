# Pra onde vamos? ✈️ — Assistente de Viagens com IA

🚀 **App ao vivo:** https://pra-onde-vamos-bxa7kmj2haacvhrfgnbrpj.streamlit.app

---

## Sobre o Projeto

O **"Pra onde vamos?"** e uma assistente de viagens com personalidade própria —
fala como uma amiga que já viajou muito, com dicas honestas, práticas e economicas.

O usuário informa destino, orçamento e estilo de viagem, e a IA monta um roteiro
completo dia a dia com estimativa de gastos, alertas culturais e dicas de hospedagem.

## Demonstração

![Demonstracao do app](pra-onde-vamos.gif)

## Funcionalidades

- Chat interativo com histórico de conversa completo
- Roteiro estruturado dia a dia (manha, tarde e noite)
- Estimativa de gastos por categoria
- Alertas culturais e dicas de seguranca
- Foco em viagens economicas e acessíveis
- Interface intuitiva com sidebar para configuração

## Tecnologias Utilizadas

| Tecnologia | Função |
|---|---|
| Groq API | Inferência ultra-rápida com LLMs |
| Llama 3.3 70B | Modelo de linguagem base |
| Streamlit | Interface web interativa |
| Streamlit Cloud | Plataforma de deploy e hospedagem |
| Streamlit Secrets | Gerenciamento seguro da chave de API |
| Python | Linguagem principal |

## Como Executar Localmente

```bash
# Clone o repositório
git clone https://github.com/BeatrizAndradeDS/pra-onde-vamos.git
cd pra-onde-vamos

# Instale as dependencias
pip install -r requirements.txt

# Crie o arquivo de secrets local
mkdir .streamlit
echo 'GROQ_API_KEY = "sua-chave-aqui"' > .streamlit/secrets.toml

# Execute o app
streamlit run ba_assistente.py
```

## Estrutura do Projeto

```
pra-onde-vamos/
├── ba_assistente.py      # Codigo principal do app
├── requirements.txt      # Dependencias do projeto
└── pra-onde-vamos.gif    # Demonstracao do app
```

## Sobre a Autora

Beatriz Andrade — Cientista de dados em transicao de carreira.

- 💼 [LinkedIn](https://linkedin.com/in/andrade-beatriz)
- 🌐 [Portfolio](https://beatrizandradeds.github.io/portfolio)
- ✉️ biasandrade@gmail.com
