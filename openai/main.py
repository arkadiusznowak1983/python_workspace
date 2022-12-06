import openai

openai.api_key = ''
with open("input.txt", "rt") as file:
    response = openai.Completion.create(
      model="text-davinci-003",
      prompt=file.read(),
      temperature=0.7,
      max_tokens=256,
      top_p=1,
      frequency_penalty=0,
      presence_penalty=0
    )

print("\noutput.py\n", response["choices"][0]["text"])
with open("output.py", "wt") as file:
    file.write(response["choices"][0]["text"])

