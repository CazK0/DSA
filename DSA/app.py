from flask import Flask, render_template, request
from src.sliding_window import max_profit, length_of_longest_substring, character_replacement
from src.two_pointers import is_palindrome, two_sum_sorted, three_sum

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
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

            elif algo == 'palindrome':
                s = request.form.get('pal_string')
                result = is_palindrome(s)
                input_val = s
                algo_name = "Valid Palindrome"

            elif algo == 'twosum':
                raw = request.form.get('twosum_input')
                target = int(request.form.get('twosum_target'))
                nums = [int(x.strip()) for x in raw.split(',')]
                result = two_sum_sorted(nums, target)
                input_val = f"Array: {raw}, Target: {target}"
                algo_name = "Two Sum II"

            elif algo == 'threesum':
                raw = request.form.get('threesum_input')
                nums = [int(x.strip()) for x in raw.split(',')]
                result = three_sum(nums)
                input_val = raw
                algo_name = "3Sum"

        except Exception as e:
            result = f"Error: {e}"

    return render_template('index.html', result=result, input_val=input_val, algo_name=algo_name)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
