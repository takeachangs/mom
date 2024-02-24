import cohere 
co = cohere.Client("6yJnofp1XcVL54HTVCh19zBlXnGLuDm9GdAqyQJi")

initial_message = "How can I help you? Enter \"EXIT\" at any time to exit the conversation.\n"

while __name__ == "__main__":
    documents = [] # TODO: add documents
    chat_history = []
    prompt = input(initial_message)
    chat_history.append({"role": "CHATBOT", "message": initial_message.strip()})

    # continuously generate responses
    while prompt.lower() != "exit":

        # generate response
        response = co.chat(
            chat_history=chat_history,
            message=prompt,
            temperature=0,
            documents=documents
        )

        # record chat history
        user_message = {"user_name": "USER", "text": prompt}
        bot_message = {"user_name": "CHATBOT", "text": response.text}

        chat_history.append(user_message)
        chat_history.append(bot_message)

        # print response
        print(response.text)

        # take a new prompt
        prompt = input("")