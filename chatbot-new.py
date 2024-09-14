import openai
import gradio as gr


openai.api_key = 'your-openai-api-key'


def chatbot_response(user_input):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=user_input,
        max_tokens=150
    )
    return response.choices[0].text.strip()


iface = gr.Interface(
    fn=chatbot_response,
    inputs="text",
    outputs="text",
    title="Chatbot",
    description="Ask anything to the chatbot!"
)

iface.launch()