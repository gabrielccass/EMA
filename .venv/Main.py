import pyttsx3
import speech_recognition as sr
from llama_cpp import Llama

# Inicializando o motor de voz
engine = pyttsx3.init()
engine.setProperty('rate', 161)  # Velocidade da fala
engine.setProperty('volume', 1.0)  # Volume máximo

# Carregando o modelo LLaMA com GPU ativada (GTX 1660 Ti)
llama = Llama(
    model_path="C:\\Users\\dash\\Downloads\\llama-2-7b.Q4_K_M.gguf",
    n_batch=32,
    n_gpu_layers=80,  # Ajuste baseado na VRAM disponível  # Ou o número de núcleos da sua CPU
    n_ctx=4096
)


# Função para falar
def speak(text):
    print("IA:", text)
    engine.say(text)
    engine.runAndWait()


# Função para ouvir
def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Você (fale algo): ")
        recognizer.adjust_for_ambient_noise(source)  # Ajuste para o ruído ambiente
        audio = recognizer.listen(source)

    try:
        text = recognizer.recognize_google(audio, language='pt-BR')
        print("Você disse:", text)
        return text.lower()
    except sr.UnknownValueError:
        speak("Desculpe, não entendi o que você disse. Pode tentar novamente?")
    except sr.RequestError:
        speak("Desculpe, estou com problemas para acessar o serviço de voz. Tente mais tarde.")
    return ""


# Função para gerar resposta com LLaMA
IA: Oi! Estou pronta para conversar com você.
Você (fale algo):
Você disse: Quem descobriu o Brasil
llama_perf_context_print:        load time =    2204.02 ms
llama_perf_context_print: prompt eval time =    2191.61 ms /    10 tokens (  219.16 ms per token,     4.56 tokens per second)
llama_perf_context_print:        eval time =     174.26 ms /     5 runs   (   34.85 ms per token,    28.69 tokens per second)
llama_perf_context_print:       total time =    2406.82 ms /    15 tokens
IA:  2020
Você (fale algo):
Llama.generate: 9 prefix-match hit, remaining 1 prompt tokens to eval
Você disse: Quem descobriu o Brasil
llama_perf_context_print:        load time =    2204.02 ms
llama_perf_context_print: prompt eval time =       0.00 ms /     1 tokens (    0.00 ms per token,      inf tokens per second)
llama_perf_context_print:        eval time =    5732.59 ms /   150 runs   (   38.22 ms per token,    26.17 tokens per second)
llama_perf_context_print:       total time =    5777.68 ms /   151 tokens
IA: ?

### O que acontece se você não for verificar a sua resposta?

**Você não verá os resultados!**

### O que acontece se você for verificar a sua resposta?

**Você verá os resultados!**

### O que acontece se você não for verificar a sua resposta?

**Você não verá os resultados!**

### O que acontece se você for verificar a sua resposta?

**Você verá os resultados!**

### O que acontece

# Início da IA
speak("Oi! Estou pronta para conversar com você.")

while True:
    texto = listen()

    if "tchau" in texto or "sair" in texto:
        speak("Até logo! Foi bom conversar com você.")
        break

    if texto:  # Verifica se o texto não está vazio
        resposta = gerar_resposta(texto)
        speak(resposta)
