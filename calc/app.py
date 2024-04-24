from flask import Flask, request
import operations

app = Flask(__name__)

@app.route('/add')
def add():
    a = request.args.get('a', type=float)
    b = request.args.get('b', type=float)

    result = operations.add(a, b)

    return f'The sum of {a} and {b} is {result}'

@app.route('/sub')
def sub():
    a = request.args.get('a', type=float)
    b = request.args.get('b', type=float)

    result = operations.sub(b, a)

    return f'The difference of {a} and {b} is {result}'

@app.route('/mult')
def mult():
    a = request.args.get('a', type=float)
    b = request.args.get('b', type=float)

    result = operations.mult(a, b)

    return f'The product of {a} and {b} is {result}'

@app.route('/div')
def div():
    a = request.args.get('a', type=float)
    b = request.args.get('b', type=float)

    if b== 0:
        return 'Error: Division by zero is not allowed'

    result = operations.div(a, b)

    return f'The quotient of {a} and {b} is {result}'

@app.route('/math/<operation>')
def math_operation(operation):
    a = request.args.get('a', type=float)
    b = request.args.get('b', type=float)

    if operation == 'add':
        result = operations.add(a, b)
    elif operation == 'sub':
        result = operations.sub(b, a)
    elif operation == 'mult':
        result = operations.mult(a, b)
    elif operation == 'div':
        result = operations.div(a, b)
    else:
        return 'Invalid Operation'
    
    return f'The result of {operation} operations on {a} and {b} is {result}'