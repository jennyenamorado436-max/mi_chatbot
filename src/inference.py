from transformers import pipeline

# Cargar modelo GPT-2
chat = pipeline("text-generation", model="gpt2")

def responder(mensaje):
    respuesta = chat(mensaje, max_length=100, num_return_sequences=1)
    return respuesta[0]['generated_text']