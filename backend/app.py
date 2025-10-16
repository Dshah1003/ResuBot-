from flask import Flask, request, jsonify
import json, pandas as pd, spacy

app = Flask(__name__)

# Load Data
intents = json.load(open("../nlp/intents.json", encoding="utf-8"))
responses = pd.read_csv("../nlp/responses.csv")
nlp = spacy.load("en_core_web_md")

@app.route("/chat", methods=["POST"])
def chat():
    user_input = request.json["message"]
    intent = predict_intent(user_input)
    reply = get_response(intent)
    return jsonify({"reply": reply})

def predict_intent(text):
    doc = nlp(text)
    scores = {}
    for intent in intents:
        for example in intent["examples"]:
            score = nlp(example).similarity(doc)
            scores[intent["intent"]] = max(scores.get(intent["intent"], 0), score)
    return max(scores, key=scores.get)

def get_response(intent):
    return responses.loc[responses["intent"] == intent, "response"].values[0]

if __name__ == "__main__":
    print("✅ Flask is starting...")
    app.run(debug=True)
