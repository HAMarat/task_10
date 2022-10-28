from flask import Flask
from utils import load_candidates, get_all, get_by_pk, get_by_skill

# ссылка на файл с данными кандидатов
JSON_DATA = 'candidates.json'

app = Flask(__name__)

# Загружаем данные кандидатов
candidates_data: list[dict] = load_candidates(JSON_DATA)


def main():
    """
    Запускаем программу только если она запущена напрямую из файла main.py
    """
    @app.route('/')
    def candidates() -> str:
        """
        Возвращаем данные всех кандидатов по адресу "/"
        """
        candidates_name = get_all(candidates_data)
        return f"<p align='center'>{''.join(candidates_name)}</>"

    @app.route('/candidates/<pk_number>')
    def candidate_by_pk(pk_number: str) -> str:
        """
        Выводим данные кандидата по адресу "/candidates/<pk_number>"
        """
        if not pk_number.isdigit():
            return "Пользователь с таким 'pk' отсутствует"
        candidate_pk_number = get_by_pk(candidates_data, pk_number)
        return candidate_pk_number

    @app.route('/skills/<skill>')
    def candidates_by_skill(skill: str) -> str:
        """
        Выводим данные кандидатов по адресу "/skills/<skill>"
        """
        list_candidates_by_skill = get_by_skill(candidates_data, skill)
        return ''.join(list_candidates_by_skill)


if __name__ == "__main__":
    app.run(debug=True, host='127.0.0.1', port=3000)
