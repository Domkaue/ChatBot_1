# ChatBot_llm.py

from transformers import pipeline

pipe = pipeline("text-generation", model="TinyLlama/TinyLlama-1.1B-Chat-v1.0")


def receber_pergunta():
    """Receber a pergunta do usuário """
    return input("Digite sua pergunta:")

def gerar_resposta(pergunta):
    """ Gera uma resposta"""
    messages=[
            {"role": "system","content":"Assistente."},
            {"role": "user","content":pergunta}
        ]
    resultado = pipe(
        messages,
        max_new_tokens = 300,
        temperature=0.7
    )
    return resultado[0]['generated_text'][-1]['content']

def exibir_resposta(resposta):
    """Exibe a resposta para o usuario"""
    print("\nResposta:", resposta)

def chatbot():
    """Fluxo principal do chatbot"""
    print('Bem vindo ao chatbot!(Digite "sair" para encerrar a conversa)')
    historico_conversa = [
       {"role": "system", "content": "Você é um assistente amigável"}   
    ]
    while True:
     pergunta = receber_pergunta().strip()
     if pergunta.lower() in ['sair', 'exit', 'quit']:
         print('Encerrando o chatbot. Até logo!')
         break
     if not pergunta:
         print('Favdor digite uma pergunta valida.')
         continue
    historico_conversa.append({"role": "user", "content": pergunta})
    print('\n Gerando uma resposta...')
    resposta = gerar_resposta(pergunta)
    print('\nResposta:', exibir_resposta(resposta))

if __name__ == "__main__":
    chatbot()