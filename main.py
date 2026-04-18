from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hola, chatbot listo!"}

def responder(mensaje):
    if "hola" in mensaje.lower():
        return "¡Hola! ¿Cómo estás?"
    elif "python" in mensaje.lower():
        return "Python es un lenguaje de programación muy usado en IA."
    elif "adiós" in mensaje.lower():
        return "Hasta pronto, cuídate."
    else:
        return "No entendí bien, ¿puedes repetirlo?"

while True:
    mensaje = input("Tú: ")
    if mensaje.lower() in ["salir", "exit", "quit"]:
        print("Bot: ¡Adiós!")
        break
    print("Bot:", responder(mensaje))
    from src.inference import responder

while True:
    mensaje = input("Tú: ")
    if mensaje.lower() in ["salir", "exit", "quit"]:
        print("Bot: ¡Adiós!")
        break
    print("Bot:", responder(mensaje))