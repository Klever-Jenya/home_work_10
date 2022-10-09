from flask import Flask
import utils

app = Flask(__name__)  # экземпляр приложения

@app.route('/') # заглушка для стартовой страницы
def index():
    result = "<br>"
    candidates = utils.get_all()

    for candidate in candidates:
        result += candidate["name"] + "<br>"
        result += candidate["position"] + "<br>"
        result += candidate["skills"] + "<br>"
        result += "<br>"

    return f"<pre> {result} </pre>"


@app.route('/candidate/<int:pk>')  # 2 страница кандидата
def get_by_pk(pk):
    candidate = utils.get_by_pk(pk)

    if candidate == "Not found":
        return "Not found"

    result = "<br>"
    result += candidate["name"] + "\n"
    result += candidate["position"] + "<br>"
    result += candidate["skills"] + "<br>"
    result += "<br>"

    return f"""
    <img src="{candidate['picture']}">
    <pre> {result} </pre>
"""


@app.route('/candidate/<skill>') # 3 страница скилов кандидата
def get_by_skill(skill):
    result = "<br>"
    candidates = utils.get_by_skill(skill)

    for candidate in candidates:
      result += candidate["name"] + "<br>"
      result += candidate["position"] + "<br>"
      result += candidate["skills"] + "<br>"
      result += "<br>"

    return f"<pre> {result} </pre>"


app.run(debug=True)  # запуск (отображает ошибки)












# def main():
#     filename = ""
#
#     load_candidates(filename)
#
#
#
# if __name__ == '__main__':
#     main()