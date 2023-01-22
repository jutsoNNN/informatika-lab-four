import yaml
import json
import time

start_time = time.time()

def yamlToJson(filename, output_filename):
    with open(filename, 'r', encoding="UTF-8") as yaml_in, open(output_filename, "w", encoding="UTF-8") as json_out:
        yaml_object = yaml.safe_load(yaml_in)
        json.dump(yaml_object, json_out, ensure_ascii=False, sort_keys=True, indent=2)

yamlToJson("schedule.yaml", "schedule.json")
print(time.time() - start_time)