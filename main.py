import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def obtener_respuesta(mensaje_usuario):
    respuesta = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[
            {"role": "system", "content": "Eres un asistente de atención al cliente útil, claro y profesional."},
            {"role": "user", "content": mensaje_usuario}
        ]
    )
    return respuesta.choices[0].message.content

def simular_accion(mensaje):
    if "problema" in mensaje or "error" in mensaje:
        print("🔍 Consultando base de datos...")
    elif "comprar" in mensaje:
        print("🛒 Buscando productos...")
    elif "queja" in mensaje:
        print("📩 Generando ticket de soporte...")

def chat():
    print("🤖 Chatbot de Atención al Cliente (escribe 'salir' para terminar)\n")
    
    while True:
        user_input = input("Tú: ")
        
        if user_input.lower() == "salir":
            break
        
        simular_accion(user_input)
        
        respuesta = obtener_respuesta(user_input)
        print(f"Bot: {respuesta}\n")

if __name__ == "__main__":
    chat()