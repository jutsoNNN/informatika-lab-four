import re
import time

start_time = time.time()

def withRegs(filename, output_filename):
    with open(filename, 'r', encoding="UTF-8") as yamlIn, open(output_filename, "w", encoding="UTF-8") as jsonOut:
        flag_last = False
        a = yamlIn.readlines()
        jsonOut.write("{\n")
        for line in a:
            temp = re.findall(r"^\w+:", line)
            if len(temp) > 0:
                result = re.sub(r"^\w+:", " " * 2 + '"' + temp[0].rstrip(":") + '": [', line)
                jsonOut.write(result)
            temp = re.findall(r"\s+-", line)
            if len(temp) > 0:
                if "практика2" in line:
                    flag_last = True
                jsonOut.write("    {\n")
                temp = line.lstrip("  - ").rstrip(":\n")
                jsonOut.write(6 * " " + '"' + temp + '": {\n')
            temp = re.findall(r"^\s+.+: .+", line)
            if len(temp) > 0:
                temp_2 = temp[0].lstrip().split(":")
                temp_2[1] = temp_2[1].lstrip(" '").rstrip("'")
                if len(temp_2) == 3:
                    jsonOut.write(
                        ' ' * 8 + '"' + temp_2[0] + '": "' + temp_2[1] + ":" + temp_2[2].rstrip("'") + '",\n')
                elif "преподаватель" not in temp_2[0]:
                    jsonOut.write(' ' * 8 + '"' + temp_2[0] + '": "' + temp_2[1] + '",\n')
                else:
                    jsonOut.write(' ' * 8 + '"' + temp_2[0] + '": "' + temp_2[1] + '"\n')
                    if not flag_last:
                        jsonOut.write(6 * ' ' + '}\n' + "    },\n")
                    else:
                        jsonOut.write(6 * ' ' + '}\n' + "    }\n" + "  ]\n" + "}")

withRegs("schedule.yaml", "schedule.json")
print(time.time() - start_time)