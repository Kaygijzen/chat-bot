import json
import codecs

# Opening JSON file
file = open('C:/Users/kaygi/Downloads/ambignq_light/dev_light.json')
data = json.load(file)

print(len(data))
file.close()
list = []

for item in data:
    if item["annotations"][0]["type"] == "multipleQAs":
        for x in item["annotations"]:
            if hasattr(x, "qaPairs"):
                for question in x["qaPairs"]:
                    q = question["question"]
                    if len(question["answer"]) > 1:
                        a = max(question["answer"], key=len)
                    else:
                        a = question["answer"][0]
    else:
        q = item["question"]
        a = item["annotations"][0]["answer"][0]
    list.append([q, a])


header = ["categories:\n",
          "  - misc\n", "conversations:\n"]

file = codecs.open(
    "C:/Users/kaygi/Projects/chat-bot/webscraper/Lib/site-packages/chatterbot_corpus/data/mycorpus/ambignq_light.yml", "w", "utf-8")

file.writelines(header)
i = 0
for item in list:
    # print(i)
    try:
        file.write("  - - " + item[0] + "\n")
        file.write("    - " + item[1] + "\n")
        i = i + 1
    except UnicodeEncodeError:
        print(item)


file.close()
