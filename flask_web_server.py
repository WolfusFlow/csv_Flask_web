from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)

df = pd.DataFrame({'name': ['apple', 'orange'], 'price': ['$1', '$2']})
df.to_csv('data.csv', index=None)

@app.route("/")
def show_tables():
    data = pd.read_csv('data.csv')

    return render_template('index.html',tables=[data.to_html()],
                           titles = ['na', 'Title one', 'Title Two'])

if __name__ == "__main__":
    app.run(debug=True)