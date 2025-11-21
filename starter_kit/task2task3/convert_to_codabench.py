import json
import argparse

def convert(input_jsonl, output_json):
    results = []
    with open(input_jsonl, "r", encoding="utf-8") as f:
        for line in f:
            obj = json.loads(line)
            entry = {"id": obj["ID"], "quads": []}

            for q in obj.get("Quadruplet", []):
                valence, arousal = q["VA"].split("#")
                entry["quads"].append({
                    "aspect": q["Aspect"],
                    "category": q["Category"],
                    "opinion": q["Opinion"],
                    "valence": float(valence),
                    "arousal": float(arousal)
                })

            results.append(entry)

    with open(output_json, "w", encoding="utf-8") as f:
        json.dump(results, f, ensure_ascii=False, indent=2)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True)
    parser.add_argument("--output", required=True)
    args = parser.parse_args()
    convert(args.input, args.output)
