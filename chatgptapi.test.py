import openai
import senha

openai.api_key=senha.api_key
model_engine = "text-davinci-003"
prompt = "Hello, how are you?"
completion = openai.Completion. create(
engine=model_engine,
prompt=prompt,
max_tokens=1024,
n=1,
stop=None,
temperature=0.5,
)

response = completion.choices[0]
print ( response )