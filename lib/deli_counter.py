katz_deli = []

def line(katz_deli):
    if not katz_deli:
        return "The line is currently empty."
    else:
        customer_list = ", ".join(f"{index + 1}. {customer}" for index, customer in enumerate(katz_deli))
        return f"The line is currently: {customer_list}"

def take_a_number(customers, new_customer):
    customers.append(new_customer)
    position = len(customers)
    return f"Welcome, {new_customer}. You are number {position} in line."

def now_serving(customers):
    if not customers:
        return "There is nobody waiting to be served!"
    else:
        serving_customer = customers.pop(0)
        return f"Currently serving {serving_customer}."