from flask import Flask, render_template, request, redirect, url_for
import openai
import os

app = Flask(__name__)

openai.api_key = os.getenv('OPENAI_API_KEY')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    prompt = request.form['prompt']
    response = openai.ChatCompletion.create(
        messages=[
            {"role": "system", "content": "你是一位專業營養師，請針對食物名稱說出營養成分及合理的功效"},{"role": "user", "content":text1}
        ],
        model="gpt-4o-mini-2024-07-18",
        temperature = 0.5,
    )
    generated_text = response['choices'][0]['message']['content'].strip()
    return render_template('index1.html', response=generated_text)

if __name__ == '__main__':
    app.run(debug=True)
