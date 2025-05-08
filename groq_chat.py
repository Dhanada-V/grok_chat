import groq

#Setting API key
api_key = "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"

#Creation  of client
client = groq.Groq(api_key=api_key)

#  Send a message and get a response
def ask_groq(question):
    # Create a chat completion request
    response = client.chat.completions.create(
        model="llama3-8b-8192",  # smaller model for faster responses
        messages=[
            {"role": "user", "content": question}
        ]
    )

    # Get the response text
    answer = response.choices[0].message.content

    # Print the response
    print("\nGroq's response:")
    print(answer)

#  Getting user input and send to Groq
user_question = input("Ask Groq something: ")
ask_groq(user_question)