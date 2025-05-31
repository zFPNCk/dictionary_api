from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/api/v1/<word>')
def word(word):
    filename = "dictionary.csv"
    df = pd.read_csv(filename)
    result = df.loc[df['word'] == word, 'definition']
    definition = result.iloc[0] if not result.empty else "Definition not found."
    return {"definition": definition,
            "word": word}

if __name__ == '__main__':
    app.run(debug=True)