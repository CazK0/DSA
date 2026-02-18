from flask import Flask, render_template, request
from src.sliding_window import max_profit, length_of_longest_substring, character_replacement

app = Flask(__name__)
@app.route('/', methods=['GET', 'POST'])
def sliding_window():
    result = None
    input_val = None
    algo_name = None
    if request.method == 'POST':
        algo = request.form.get('algo')

        try:
            if algo == 'stock':
                raw = request.form.get('stock_input')
                prices = [int(x.strip()) for x in raw.split(',')]
                result = max_profit(prices)
                input_val = raw
                algo_name = "Best Time to Buy/Sell Stock"

            elif algo == 'substring':
                s = request.form.get('substring_input')
                result = length_of_longest_substring(s)
                input_val = s
                algo_name = "Longest Substring Without Repeats"

            elif algo == 'replacement':
                s = request.form.get('rep_string')
                k = int(request.form.get('rep_k'))
                result = character_replacement(s, k)
                input_val = f"String: {s}, K: {k}"
                algo_name = "Longest Repeating Char Replacement"
        except Exception as e:
            result = f"Error: {e}"
    return render_template('sliding_window.html', result=result, input_val=input_val, algo_name=algo_name)

if __name__ == '__main__':
    app.run(debug=True, port=5000)