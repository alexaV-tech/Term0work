from flask import Flask, render_template

app=Flask(__name__)

    
products = { 
    "1234": {
        "name": "apple",
        "price": 1.75,
        "description": "yummy"
    },
    "5678": {
        "name": "watermelom",
        "price": 2.00,
        "description":"splendid"
    },
    "91011":{
         "name": "blackberries",
        "price": 4.00,
        "description":"overpriced"

    }
}

@app.route('/products')
def display():
    # This route will display all products on the home page
    return render_template('home.html', products=products)

@app.route('/products/<productID>')
def get_product(productID):
    if productID in products:
        product = products[productID]
        return render_template('home.html', product=product)
    else:
        return render_template('home.html', productID=productID)
    





 
