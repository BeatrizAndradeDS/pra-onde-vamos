# Pra onde vamos? Sua AI assistente de viagens

# Imports
import os
import streamlit as st

# Importa a classe Groq para se conectar à API da plataforma Groq e acessar o LLM
from groq import Groq

# Configura a página do Streamlit com título, ícone layout, e estado inicial da sidebar
st.set_page_config(
	page_title="Pra onde vamos?",
	page_icon="✈️",
	layout="wide",
	initial_sidebar_state="expanded"
)

# Define um prompt de sistema que descreve as regras/comportamento do assistente de IA
CUSTOM_PROMPT = """
Você é o "Pra onde vamos?", uma assistente de viagens experiente e apaixonada por explorar o mundo gastando pouco.
Você fala como uma amiga que já viajou muito — com entusiasmo, gírias leves, dicas honestas e aquele jeito de 
quem conhece os atalhos que os guias turísticos não contam.

SEU PERFIL:
- Você é especialista em viagens econômicas, mochilão e turismo acessível.
- Você já "dormiu em hostel ruim e comeu o melhor street food da vida" — ou seja, conhece os dois lados.
- Você prioriza experiências autênticas, baratas e seguras.

REGRAS DE OPERAÇÃO:
1. **Foco em Viagens**: Responda apenas perguntas relacionadas a viagens, destinos, roteiros, transporte, hospedagem,
   cultura local, gastronomia e segurança. Se o usuário perguntar sobre outro assunto, diga com bom humor que sua 
   especialidade é ajudar a montar a mala — nada mais.

2. **Informações que você precisa do usuário antes de montar o roteiro**:
   Antes de gerar qualquer roteiro, confirme que você tem estas informações. Se faltar alguma, pergunte de forma 
   descontraída:
   - 🌍 Destino (cidade/país)
   - 📅 Duração da viagem (número de dias)
   - 💰 Orçamento total aproximado (em reais ou outra moeda)
   - 🎒 Estilo de viagem (aventura, cultural, praia, urbano, natureza, misto...)
   - 👤 Perfil do viajante (solo, casal, grupo)

3. **Estrutura do Roteiro**: Ao gerar um roteiro, sempre siga este formato:
   - **Resumo Geral**: Uma introdução empolgante sobre o destino com 2-3 frases no estilo "olha, esse lugar é incrível porque..."
   - **Roteiro Dia a Dia**: Para cada dia, inclua:
     * 🌅 Manhã / 🌞 Tarde / 🌙 Noite — atividades sugeridas
     * 🍽️ Dica de comida local barata e boa
     * 💡 Dica de mochileiro (truque, economia, cuidado)
   - **💸 Estimativa de Gastos**: Breakdown aproximado por categoria (hospedagem, alimentação, transporte, atrações)
   - **⚠️ Alertas Culturais**: Costumes locais, o que evitar, como se vestir, segurança
   - **🏨 Onde Ficar**: Indicação de tipo de hospedagem econômica (hostels, guesthouses, etc.)
   - **🚌 Como Chegar e se Locomover**: Transporte mais barato de/para o destino e dentro dele

4. **Tom e Estilo**: 
   - Fale como uma amiga animada, não como um guia formal.
   - Use emojis com moderação para tornar a leitura mais visual.
   - Seja honesto: se um lugar tem algum ponto negativo importante, mencione.
   - Prefira dicas práticas a descrições genéricas.
"""

# Cria o conteúdo da barra lateral no Streamlit
with st.sidebar:
    
    # Define o título da barra lateral
    st.title("✈️ Pra onde vamos?")
    
    # Mostra um texto explicativo sobre o assistente
    st.markdown("Sua assistente de IA para planejamento de viagens.")
    
    # Chave da API carregada de forma segura via Streamlit Secrets
    groq_api_key = st.secrets["GROQ_API_KEY"]

    # Adiciona linhas divisórias e explicações extras na barra lateral
    st.markdown("---")
    st.markdown("Desenvolvida para auxiliar no planejamento da sua viagem. IA pode cometer erros. Sempre verifique as respostas.")

    st.markdown("---")
    st.markdown("Conheça mais dos meus projetos:")

    # Link para o site da BA
    st.markdown("🔗 [Beatriz Andrade Portfólio](https://beatrizandradeds.github.io/portfolio/)")
    
    # Botão de link para enviar e-mail
    st.link_button("✉️ E-mail Para comentários ou dúvidas", "mailto:biasandrade@gmail.com")

# Título principal do app
st.title("Pra onde vamos?")

# Subtítulo adicional
st.title("Sou sua Assistente Pessoal de Planejamento de viagens ✈️")

# Texto auxiliar abaixo do título
st.caption("Me conta seu destino, orçamento e estilo — e eu monto o roteiro perfeito pra você!")

# Inicializa o histórico de mensagens na sessão, caso ainda não exista
if "messages" not in st.session_state:
    st.session_state.messages = []

# Exibe todas as mensagens anteriores armazenadas no estado da sessão
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Inicializa a variável do cliente Groq como None
client = None

# Verifica se o usuário forneceu a chave de API da Groq
if groq_api_key:
    
    try:
        
        # Cria cliente Groq com a chave de API fornecida
        client = Groq(api_key = groq_api_key)
    
    except Exception as e:
        
        # Exibe erro caso haja problema ao inicializar cliente
        st.sidebar.error(f"Erro ao inicializar o cliente Groq: {e}")
        st.stop()


# Captura a entrada do usuário no chat
if prompt := st.chat_input("E aí, para onde vamos?"):
    
    # Armazena a mensagem do usuário no estado da sessão
    st.session_state.messages.append({"role": "user", "content": prompt})
    
    # Exibe a mensagem do usuário no chat
    with st.chat_message("user"):
        st.markdown(prompt)

    # Prepara mensagens para enviar à API, incluindo prompt de sistema
    messages_for_api = [{"role": "system", "content": CUSTOM_PROMPT}]
    for msg in st.session_state.messages:
        
        messages_for_api.append(msg)

    # Cria a resposta do assistente no chat
    with st.chat_message("assistant"):
        
        with st.spinner("Analisando sua pergunta..."):
            
            try:
                
                # Chama a API da Groq para gerar a resposta do assistente
                chat_completion = client.chat.completions.create(
                    messages = messages_for_api,
                    model = "llama-3.3-70b-versatile", 
                    temperature = 0.7, # quanto maior, mais criativa a resposta
                    max_tokens = 2048,
                )
                
                # Extrai a resposta gerada pela API (sem os metadados)
                ba_ai_resposta = chat_completion.choices[0].message.content
                
                # Exibe a resposta no Streamlit
                st.markdown(ba_ai_resposta)
                
                # Armazena resposta do assistente no estado da sessão
                st.session_state.messages.append({"role": "assistant", "content": ba_ai_resposta})

            # Caso ocorra erro na comunicação com a API, exibe mensagem de erro
            except Exception as e:
                st.error(f"Ocorreu um erro ao se comunicar com a API da Groq: {e}")

st.markdown(
    """
    <div style="text-align: center; color: gray;">
        <hr>
        <p>Esse projeto foi inspirado no Curso de Fundamentos de Linguagem Python da Data Science Academy</p>
    </div>
    """,
    unsafe_allow_html=True
)