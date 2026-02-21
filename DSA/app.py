from flask import Flask, render_template, request
from src.sliding_window import max_profit, length_of_longest_substring, character_replacement
from src.two_pointers import is_palindrome, two_sum_sorted, three_sum
from src.fast_slow import ListNode, has_cycle, middle_node, detect_cycle
from src.trees import Solution, build_tree, tree_to_list

app = Flask(__name__)

def create_linked_list(arr, pos=-1):
    if not arr: return None
    head = ListNode(arr[0])
    curr = head
    nodes = [head]

    for i in range(1, len(arr)):
        node = ListNode(arr[i])
        curr.next = node
        curr = node
        nodes.append(node)

    if pos != -1 and 0 <= pos < len(nodes):
        curr.next = nodes[pos]

    return head

def parse_tree_input(raw_input):
    vals = []
    for x in raw_input.split(','):
        x = x.strip()
        if x.lower() == 'none' or x.lower() == 'null' or x == '':
            vals.append(None)
        else:
            vals.append(int(x))
    return vals

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

            elif algo == 'middle_node':
                raw = request.form.get('middle_input')
                nums = [int(x.strip()) for x in raw.split(',')]
                head = create_linked_list(nums)
                mid = middle_node(head)
                result = mid.val if mid else 'None'
                input_val = raw
                algo_name = "Middle of Linked List"

            elif algo == 'has_cycle':
                raw = request.form.get('cycle_input')
                pos = int(request.form.get('cycle_pos'))
                nums = [int(x.strip()) for x in raw.split(',')]
                head = create_linked_list(nums, pos)
                result = has_cycle(head)
                input_val = f"List: {raw}, Pos: {pos}"
                algo_name = "Linked List Cycle"

            elif algo == 'detect_cycle':
                raw = request.form.get('detect_input')
                pos = int(request.form.get('detect_pos'))
                nums = [int(x.strip()) for x in raw.split(',')]
                head = create_linked_list(nums, pos)
                start_node = detect_cycle(head)
                result = start_node.val if start_node else 'None'
                input_val = f"List: {raw}, Pos: {pos}"
                algo_name = "Detect Cycle Start"

            elif algo == 'invert_tree':
                raw = request.form.get('tree_input')
                vals = parse_tree_input(raw)
                root = build_tree(vals)
                sol = Solution()
                inverted = sol.invertTree(root)
                result = tree_to_list(inverted)
                input_val = raw
                algo_name = "Invert Binary Tree"

            elif algo == 'max_depth':
                raw = request.form.get('depth_input')
                vals = parse_tree_input(raw)
                root = build_tree(vals)
                sol = Solution()
                result = sol.maxDepth(root)
                input_val = raw
                algo_name = "Maximum Depth of Binary Tree"

        except Exception as e:
            result = f"Error: {e}"

    return render_template('index.html', result=result, input_val=input_val, algo_name=algo_name)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
