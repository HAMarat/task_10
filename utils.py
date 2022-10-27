import json
from typing import List, Dict


def load_candidates(filename: str) -> List[Dict]:
    with open(filename, 'r', encoding='utf-8') as file:
        candidates_data = json.load(file)
        return candidates_data


def get_all(candidates) -> list[dict]:
    candidates_name = []
    for candidates_dict in candidates:
        candidates_name.append(candidates_dict['name'])
    return candidates_name


def get_by_pk(candidates, pk):
    for candidates_dict in candidates:
        if candidates_dict["pk"] == int(pk):
            return candidates_dict


def get_by_skill(candidates, skill_name):
    candidates_by_skill = []
    for candidate_dict in candidates:
        if skill_name.lower() in candidate_dict['skills'].lower():
            candidates_by_skill.append(candidate_dict)
            return candidates_by_skill
