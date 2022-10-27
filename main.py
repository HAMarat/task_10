from flask import Flask
from utils import load_candidates, get_by_pk, get_by_skill

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


@app.route('/candidates/<pk_number>')
def candidate_by_pk(pk_number: str):
    candidate_pk_number = get_by_pk(candidates_data, pk_number)
    candidate_pk_return = (f"<img src='{candidate_pk_number['picture']}'>"
                           f"<pre>Имя кандидата - {candidate_pk_number['name']}\n"
                           f"Позиция кандидата - {candidate_pk_number['position']}\n"
                           f"Навыки: {candidate_pk_number['skills']}</pre>")
    return candidate_pk_return


@app.route('/skills/<skill>')
def candidates_by_skill(skill: str):
    list_candidates_by_skill = []
    candidates_by_skill_dict = get_by_skill(candidates_data, skill)
    for candidate_skill in candidates_by_skill_dict:
        candidate_skill_return = (f"<pre>Имя кандидата - {candidate_skill['name']}\n"
                                  f"Позиция кандидата - {candidate_skill['position']}\n"
                                  f"Навыки: {candidate_skill['skills']}</pre>")
        list_candidates_by_skill.append(candidate_skill_return)
    if ''.join(list_candidates_by_skill):
        return ''.join(list_candidates_by_skill)
    return "Кандидатов с таким навыком нет"


if __name__ == "__main__":
    app.run()
