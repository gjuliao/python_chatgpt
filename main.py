from openai import OpenAI
from flask import Flask, request, render_template_string
import config

client = OpenAI(api_key=config.API_KEY)
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def chat_with_gpt():
    response_text = ""

    # when calling the OpenAI API
    if request.method == 'POST':
        prompt = request.form.get('prompt')
        response = client.chat.completions.create(
            model="gpt-4-turbo",
            messages=[{"role": "user", "content": prompt}]
        )
        response_text = response.choices[0].message.content.strip()

    # HTML template for displaying the prompt and response
    html_template = """
    <h1>Chat with GPT-4</h1>
    <form method="post">
        <label for="prompt">Enter your message:</label>
        <input type="text" id="prompt" name="prompt" required>
        <button type="submit">Submit</button>
    </form>
    <p><strong>Response:</strong> {{ response_text }}</p>
    """
    return render_template_string(html_template, response_text=response_text)

if __name__ == "__main__":
    app.run(debug=True)
