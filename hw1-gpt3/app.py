import os

import openai
from flask import Flask, redirect, render_template, request, url_for

app = Flask(__name__)
openai.api_key = os.getenv("OPENAI_API_KEY")


@app.route("/", methods=("GET", "POST"))
def index():
    if request.method == "POST":
        ingredient = request.form["ingredient"]
        response = openai.Completion.create(
            model="text-davinci-002",
            prompt=generate_prompt(ingredient),
            temperature=0.6,
            max_tokens=50,
        )
        return redirect(url_for("index", result=response.choices[0].text))

    result = request.args.get("result")
    return render_template("index.html", result=result)


def generate_prompt(ingredient):
    return """Suggest three dessert recipes that include the ingredient.

Ingredient: Banana
Dessert Recipe: Banana and Walnut Bread, Banana Pudding, Roasted Bananas with Vanilla Ice Cream

Ingredient: Pineapple
Dessert Recipe: Pineapple Upside-Down Cake, Pineapple Carrot Cake, Piña Colada Popsicles

Ingredient: Strawberry
Dessert Recipe: Strawberry Chocolate Mousse Cake, Strawberry Shortcake, Strawberry Rhubarb Pie

Ingredient: Nutella
Dessert Recipe: Nutella Hand Pies, Nutella Brownies, Nutella-Filled Strawberries

Ingredient: {}
Dessert Recipe:""".format(
        ingredient.capitalize()
    )
