import json
from typing import Union


def load_candidates(filename: str) -> list[dict]:
    """
    Загружает данные из файла
    """
    with open(filename, 'r', encoding='utf-8') as file:
        candidates_data = json.load(file)
        return candidates_data


def get_all(candidates: list[dict]) -> list[str]:
    """
    Возвращает данные всех кандидатов
    """
    candidates_name = []
    for candidate_dict in candidates:
        candidate_name = (f"<pre>Имя кандидата - {candidate_dict['name']}\n"
                          f"Позиция кандидата - {candidate_dict['position']}\n"
                          f"Навыки: {candidate_dict['skills']}</pre>")
        candidates_name.append(candidate_name)
    return candidates_name


def get_by_pk(candidates: list[dict], pk_number: str) -> str:
    """
    Возвращает данные кандидата по указанному "pk"
    """
    for candidate_dict in candidates:
        if candidate_dict["pk"] == int(pk_number):
            url_pk = candidate_dict['picture']
            candidate_by_pk = (f"<img src='{url_pk}'>"
                               f"<pre>Имя кандидата - {candidate_dict['name']}\n"
                               f"Позиция кандидата - {candidate_dict['position']}\n"
                               f"Навыки: {candidate_dict['skills']}</pre>")
            return candidate_by_pk
    return "Пользователь с таким 'pk' отсутствует"


def get_by_skill(candidates: list[dict], skill_name: str) -> Union[list[str], str]:
    """
    Возвращает данные кандидатов с указанными навыками
    """
    list_candidates_by_skill = []
    for candidate_dict in candidates:
        if skill_name.lower() in candidate_dict['skills'].lower():
            candidate_by_skill = (f"<pre>Имя кандидата - {candidate_dict['name']}\n"
                                  f"Позиция кандидата - {candidate_dict['position']}\n"
                                  f"Навыки: {candidate_dict['skills']}</pre>")
            list_candidates_by_skill.append(candidate_by_skill)
    if list_candidates_by_skill:
        return list_candidates_by_skill
    return "Кандидатов с таким навыком нет"
