
from flask import render_template, request, Flask
from predictor import predictor

app = Flask(__name__)

if __name__ == '__main__':
   app.run(debug=True)

@app.route('/', methods=["POST", "GET"])
def home():
    review_text = []
    if request.method == "POST":
        film_name = request.form["Name-of-Film"]   
        review_item = request.form["review-text"]
        review_text.append(review_item)    
        res = predictor(review_text)
        return render_template("./index.html", res=res, review_text=review_text, film_name=film_name)
    return render_template("./index.html", res="", review_text="")


