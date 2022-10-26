from flask import Flask
from utils import load_candidates,

JSON_DATA = 'candidates.json'

app = Flask(__name__)
candidates_data = load_candidates(JSON_DATA)


@app.route('/')
def candidates():
    list_data = []
    for candidate_data in candidates_data:
        list_data.append(f"<pre>Имя кандидата -{candidate_data['name']}\n"
                         f"Позиция кандидата - {candidate_data['position']}\n"
                         f"Навыки: {candidate_data['skills']}</pre>")
    return ''.join(list_data)


@app.route('/candidates/<x>')
def candidate():


    list_data.append(f"<pre>Имя кандидата -{candidate_data['name']}\n"
                     f"Позиция кандидата - {candidate_data['position']}\n"
                     f"Навыки: {candidate_data['skills']}</pre>")
    return ''.join(list_data)




if __name__ == "__main__":
    app.run()
