from flask import Flask,request,jsonify
from flask_restful import reqparse, abort, Api, Resource
import pickle
import numpy as np

app = Flask(__name__)
# api = Api(app)


clf_path = 'lib/models/nlp_model.pkl'
clf = pickle.load(open(clf_path,'rb'))

vec_path = 'lib/models/tranform.pkl'
vectorizer = pickle.load(open(vec_path,'rb'))

# argument parsing
# parser = reqparse.RequestParser()
# parser.add_argument('query')

@app.route("/")
def home():
    return "Bad Request"
# class PredictSentiment(Resource):
@app.route("/predict",methods=["GET","POST"])
def predict():
    user_query = request.json['query']
    print(user_query)
    if user_query == None:
        return "Bad Request"
    # vectorize the user's query and make a prediction
    vectorized = vectorizer.transform(np.array([user_query]))
    prediction = clf.predict(vectorized)

    # Output either 'Negative' or 'Positive' along with the score
    if prediction == 0:
        pred_text = 'Negative'
    else:
        pred_text = 'Positive'
            
    # create JSON object
    output = {'prediction': pred_text}
        
    return output


# Setup the Api resource routing here
# Route the URL to the resource
# api.add_resource(PredictSentiment, '/')


if __name__ == '__main__':
    app.run(port=8080)