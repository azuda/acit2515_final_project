import os, json


def stage_select(input):
  data_list = os.listdir("data/")
  data_list.remove("scores.json")
  data_list.remove("this_score.json")
  input_file = f"{input}.json"

  if input_file in data_list:
    with open("./handler/stage_select.json", "w") as f:
      json.dump({ "stage": input_file }, f)
    return input_file
  else:
    return False


def get_stage():
  with open("./handler/stage_select.json", "r") as f:
    data = json.load(f)
  return data["stage"]


def get_scores():
  with open("data/scores.json", "r") as f:
    return json.load(f)
