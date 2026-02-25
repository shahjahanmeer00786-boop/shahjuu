from google import genai

# Yahan apni copy ki hui API Key dalein
client = genai.Client(api_key="AAPKI_API_KEY_YAHAN_DALEIN")

response = client.models.generate_content(
    model="gemini-2.0-flash",
    contents="Hello! Kya tum mere chatbot banoge?",
)

print(response.text)
