class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []

    def deposit(self, amount, description=""):
        self.ledger.append({"amount": amount, "description": description})

    def withdraw(self, amount, description=""):
        if self.check_funds(amount):
            self.ledger.append({"amount": -amount, "description": description})
            return True
        return False

    def get_balance(self):
        balance = 0
        for item in self.ledger:
            balance += item["amount"]
        return balance

    def transfer(self, amount, category):
        if self.check_funds(amount):
            self.withdraw(amount, f"Transfer to {category.name}")
            category.deposit(amount, f"Transfer from {self.name}")
            return True
        return False

    def check_funds(self, amount):
        return amount <= self.get_balance()

    def __str__(self):
        title = f"{self.name:*^30}\n"
        items = ""
        total = 0
        for item in self.ledger:
            items += f"{item['description'][:23]:23}" + f"{item['amount']:7.2f}\n"
            total += item['amount']
        output = title + items + "Total: " + str(total)
        return output


def create_spend_chart(categories):
    # Calculate category spending
    category_spending = []
    total_spending = 0
    for category in categories:
        spending = 0
        for item in category.ledger:
            if item["amount"] < 0:
                spending -= item["amount"]
        category_spending.append(spending)
        total_spending += spending

    # Calculate spending percentages
    percentages = []
    for spending in category_spending:
        percentage = (spending / total_spending) * 100
        percentages.append(int(percentage // 10) * 10)

    # Create the spend chart
    chart = "Percentage spent by category\n"
    for i in range(100, -10, -10):
        chart += f"{i:3}| "
        for percentage in percentages:
            if percentage >= i:
                chart += "o  "
            else:
                chart += "   "
        chart += "\n"
    chart += "    " + "-" * (3 * len(categories) + 1) + "\n"

    # Determine the longest category name
    max_length = max(len(category.name) for category in categories)

    # Add category names below the chart
    for i in range(max_length):
        chart += "     "
        for category in categories:
            if i < len(category.name):
                chart += category.name[i] + "  "
            else:
                chart += "   "
        if i < max_length - 1:
            chart += "\n"

    return chart
