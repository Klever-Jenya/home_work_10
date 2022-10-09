import json

def load_candidates():  # которая загрузит данные из файла
    with open("candidates.json", "r", encoding="UTF-8") as file:
        return json.load(file)


def get_all():  # которая покажет всех кандидатов
    return load_candidates()  # список словарей

def get_by_pk(pk):  # которая вернет кандидата по pk
    for candidate in load_candidates():
        if candidate["pk"] == pk:
            return candidate
    return "Not found"

def get_by_skill(skill):  # которая вернет кандидатов по навыку
    result = []
    for candidate in load_candidates():
        if skill.lower() in candidate["skills"].lower().split(", "):
            result.append(candidate)
    return result

