# Proyecto 8: LLM
# Chatbot de Atención al Cliente con OpenAI

## Descripción

Este proyecto implementa un chatbot de atención al cliente utilizando la API de OpenAI. El sistema puede responder preguntas, simular consultas a bases de datos y generar tickets de soporte.

## Requisitos

* Python 3.8+
* API Key de OpenAI

## Instalación

```bash
git clone <tu-repo>
cd chatbot_soporte
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Configuración

Crear un archivo `.env`:

```
OPENAI_API_KEY=tu_api_key
```

## Ejecución

```bash
python main.py
```

## Funcionalidades

* Respuestas automáticas a clientes
* Simulación de base de datos
* Generación de tickets
* Recomendaciones básicas

## Ejemplo

```
Tú: No puedo iniciar sesión
Bot: Estoy consultando la base de datos...
Bot: Parece que tu contraseña es incorrecta.
```

