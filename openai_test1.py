import openai

# Read API key from api-key.txt in the current directory
with open("api-key.txt", "r") as key_file:
    key = key_file.read().strip()

# Set API key
openai.api_key = key

# Define conversation messages
messages = [
    {
        "role": "System",
        "content": "あなたは極端に発言するAIです"
    },
    {
        "role": "user",
        "content": "こんにちは"
    }
]

# Make API call
res = openai.ChatCompletion.create(
    model="gpt-4",
    messages=messages,
)

# Print the response
print(res)