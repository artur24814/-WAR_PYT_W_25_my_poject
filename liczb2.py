from flask import Flask, request, render_template

app = Flask(__name__)


@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        min = int(request.form.get("min"))
        max = int(request.form.get("max"))
        user_answer = request.form.get("user_answer")
        guess = int(request.form.get("guess", 500))
        if user_answer == "Too big!":
            max = guess
        elif user_answer == "Too small!":
            min = guess
        elif user_answer == "you won!":
            return render_template('win.html', guess=guess)
        guess = (max - min) // 2 + min
        return render_template('index.html', guess=guess, max=max, min=min)
    else:
        return render_template('hello.html')

if __name__ == "__main__":
    app.run(debug=True)


