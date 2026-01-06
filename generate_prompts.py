import json

TEMPLATE_FILE = "dogbench_template.json"
GLOSSARY_FILE = "dogwhistle_glossary.json"
OUTPUT_FILE = "dogwhistle_prompts.json"


def load_json(path):
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


if __name__ == "__main__":
    templates = load_json(TEMPLATE_FILE)
    glossary = load_json(GLOSSARY_FILE)

    results = [
        {
            "type": tpl["type"],
            "tendency": tpl["tendency"],
            "template_id": tpl["id"],
            "term": item["term"],
            "prompt": tpl["template"].replace("<TERM>", item["term"])
        }
        for item in glossary
        for tpl in templates
    ]

    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        json.dump(results, f, ensure_ascii=False, indent=2)
