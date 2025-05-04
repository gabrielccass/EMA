from llama_cpp import Llama

# Caminho para o seu modelo GGUF
CAMINHO_MODELO = "llama-2-7b.Q8_0.gguf"

# Inicializa o modelo
llama = Llama(
    model_path="C:\\Users\\dash\\Downloads\\llama-2-7b.Q4_K_M.gguf",
    n_ctx=4096,          # Contexto máximo
    n_gpu_layers=40, # Ajuste para seu processador
    n_batch=9           # Processamento por lote (pode deixar 8)
)

# Prompt simples
prompt = "Quem scobriu o Brasil?"

# Gera resposta
resposta = llama(
    prompt,
    max_tokens=80,
    temperature=0.7,
    top_p=0.9
)

# Exibe resultado
print("Resposta:")
print(resposta["choices"][0]["text"].strip())
