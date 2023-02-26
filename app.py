import openai
from typing import List

# set the OpenAI API key
openai.api_key = "your_api_key_here" 


def get_api_response(prompt: str) -> str:
    """Get the response from OpenAI API for a given prompt."""
    try:
        response = openai.Completion.create(
            model='text-davinci-003',
            prompt=prompt,
            temperature=0.9,
            max_tokens=150,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0.6,
            stop=[' Human:', ' AI:']
        )
        
        choices = response.get('choices')[0]
        return choices.get('text')
        
    except Exception as e:
        print('ERROR', e)


def update_prompt_list(message: str, prompt_list: List[str]) -> None:
    """Update the prompt list with the latest message."""
    prompt_list.append(f'\nHuman: {message}')


def create_prompt(message: str, prompt_list: List[str]) -> str:
    """Create a prompt string for OpenAI API from the prompt list."""
    update_prompt_list(message, prompt_list)
    prompt = ''.join(prompt_list)
    return prompt


def get_bot_response(message: str, prompt_list: List[str]) -> str:
    """Get the response from the AI bot for a given message."""
    prompt = create_prompt(message, prompt_list)
    bot_response = get_api_response(prompt)

    if bot_response:
        update_prompt_list(bot_response, prompt_list)
        pos = bot_response.find('\nAI: ')
        bot_response = bot_response[pos + 5:]
    else:
        bot_response = 'Something went wrong...'

    return bot_response


def main():
    """Main function to run the chatbot program."""
    prompt_list = [
        "You are a cool 20 year old who speaks slang in most of your answers",
        "\nHuman: What time is it?",
        "\nAI: Yo what's up! It's all good, it's currently 14:20."
    ]

    try:
        while True:
            user_input = input('you: ')
            response = get_bot_response(user_input, prompt_list)
            print(f'Bot: {response}')
    except KeyboardInterrupt:
        print('Exiting the program...')


if __name__ == '__main__':
    main()
