class Cart:
    def __init__(self):
        self.data = [{'drugName': 'paracetamol', 'drugPrice': 750, 'drugQuantity': 3}]

    def addToCart(self, data):
        self.data.append(data)
        return True

    def getAllCart(self):
        return self.data
    
    def removeFromCart(self, value):
        self.data.remove(value)
        return True

    def clearCart(self):
        self.data.clear()
        return True