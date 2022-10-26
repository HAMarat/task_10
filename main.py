from flask import Flask
from utils import load_candidates, get_by_pk

JSON_DATA = 'candidates.json'

app = Flask(__name__)
candidates_data = load_candidates(JSON_DATA)


@app.route('/')
def candidates():
    list_data = []
    for candidate_data in candidates_data:
        list_data.append(f"<pre>Имя кандидата - {candidate_data['name']}\n"
                         f"Позиция кандидата - {candidate_data['position']}\n"
                         f"Навыки: {candidate_data['skills']}</pre>")
    return ''.join(list_data)


@app.route('/candidates/<x>')
def candidate(x):
    candidate_x = get_by_pk(candidates_data, x)
    candidate_x_return = (f"<img src='{candidate_x['picture']}'>"
                          f"<pre>Имя кандидата - {candidate_x['name']}\n"
                          f"Позиция кандидата - {candidate_x['position']}\n"
                          f"Навыки: {candidate_x['skills']}</pre>")
    return candidate_x_return


if __name__ == "__main__":
    app.run()
