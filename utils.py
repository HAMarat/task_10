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
    candidate_data_skill_name = []
    for candidates_dict in candidates:
        candidate_data_skill_name.append(candidates_dict[skill_name])
    return candidate_data_skill_name
