from functools import total_ordering
import re
from unittest import result
from flask import Flask, request, abort
import json
from data import me, catalog
import random
from flask_cors import CORS
from config import db
from bson import ObjectId

app = Flask(__name__)
CORS(app)

@app.get("/")
def home():
    return "Hello from Flask!"


@app.get("/test")
def test():
    return "This is another endpoint"


# get /about returns  your name
@app.get("/about")
def about():
    return "This is just 'Eduardo Reynoso Server'"


#####################################################
######################API PRODUCTS ##################
#####################################################
def fix_id(obj):
    obj["_id"] = str(obj["_id"])
    return obj

@app.get("/api/test")
def test_api():
    return json.dumps("OK")


# get /api/about return the me dict json
@app.get("/api/about")
def about_api():
    return json.dumps(me)




@app.get("/api/catalog")
def get_catalog():
    cursor = db.Products.find({})
    results = []
    for prod in cursor:
        prod = fix_id(prod)
        results.append(prod)

    return json.dumps(results)
    # return the list of product

@app.post("/api/catalog")
def save_product():
    
    product = request.get_json()

    # validating
    if not "title" in product:
        return abort(400, "ERROR: Title is required")
    elif not "price" in product:
        return abort(400, "ERROR: Price is required")        
    elif  product["price"] < 1:
        return abort(400, "ERROR: Price must be greater than 1") 
    elif len(product["title"]) < 5:
        return abort(400, "ERROR: Title should have at least 5 characters")
    
    
    db.Products.insert_one(product)

    product["_id"] = str(product["_id"])
    print(product)

    return json.dumps(product)




@app.get("/api/product/<id>")
def get_product_by_id(id):

    prod = db.Products.find_one({"_id": ObjectId(id)}) # One Object
    prod = fix_id(prod)
    
    if not prod:
        return abort(400, "ERROR: ID not valid")
    else:
        return json.dumps(prod)



@app.get("/api/product/<category>")
def get_product_by_category(category):

    cursor = db.Products.find({ "category": category })
    results = []
    for prod in cursor:
        prod = fix_id(prod)
        results.append(prod)

    if not results:
        return json.dumps("Error: there's no product with that category.")
    else:
        return json.dumps(results)


@app.get("/api/count")
def count_catalog():
    cursor = db.Products.find({})
    prods = []

    for prod in cursor:
        prods.append(prod)


    
    count = len(prods)
    
    return json.dumps("Number of products: " + str(count))


@app.get("/api/catalog/total")
def catalog_total():
    cursor = db.Products.find({})
    total = 0
    for prod in cursor:
        total += prod["price"]
    return json.dumps("Total: " + str(total))

@app.get("/api/catalog/cheapest")
def catalog_cheapest():
    cheapest = catalog[0]
    for prod in catalog:
        if(prod["price"] < cheapest["price"]):
            cheapest = prod

    return json.dumps("Cheapest: " + str(cheapest))



@app.get("/api/game/<pick>")
def PaperRockSci(pick):
    
    

    # 0 = paper, 1 = scissors, 2 = rock
    computerChoice = random.randint(0,2)
    if pick != "paper" and pick != "scissors" and pick != "rock":
        return abort(400, "ERROR: the choices must be paper, rock or scissors")
    else:
        if computerChoice == 0:
            pc = "paper"
        elif computerChoice == 1:
            pc = "scissors"
        else:
            pc = "rock"

        winner = ""
        
        if pick == "paper":
            if pc == "rock":
                winner = "you"
            elif pc == "scissors":
                winner = "pc"
            else: 
                winner = "draw"
        elif pick == "rock":
            if pc == "scissors":
                winner = "you"
            elif pc == "paper":
                winner = "pc"
            else: 
                winner = "draw"
        elif pick == "scissors":
            if pc == "paper":
                winner = "you"
            elif pc == "rock":
                winner = "pc"
            else: 
                winner = "draw"
            
 
        results = {
            "you": pick,
            "pc": pc,
            "winner": winner

        }

        return json.dumps(results)
    

@app.get("/api/coupons")
def getCoupon():
    cursor = db.CouponCodes.find({})
    results = []

    for cp in cursor:
        cp = fix_id(cp)
        results.append(cp)

    return json.dumps(results)


@app.post("/api/coupons")
def saveCoupon():
    coupon = request.get_json()

    # validations
    if not 'code' in coupon:
        abort(400, "code is required")
    if not 'discount' in coupon:
        abort(400, "discount is required")
    
    db.CouponCodes.insert_one(coupon)
    coupon = fix_id(coupon)
    return json.dumps(coupon)

app.debug = True
app.run()