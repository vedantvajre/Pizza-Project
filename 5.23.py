prompt = "Welcome to Vedant's Pizza Store. Here is a list of our base pizzas and toppings."
prompt += "\n[Cheese pizza, Chicken pizza]"
prompt += "\n[Onions, Cheese, Chicken, Jalapenos.]"
prompt2 = "\nWhat is your name?"
prompt3 = "What is your phone number?"
prompt += "\nWhich pizza would you like?"
prompt += "\n(Type 'done' when finished.)"
pizza = ['Cheese pizza', 'Chicken pizza']
toppings = ['Onions', 'Cheese', 'Chicken', 'Jalapenos']
finished_list = []
Pizza_Price = '5$'
Customer = True
while Customer:
    Name = input(prompt2)
    Phone_Number = input(prompt3)
    pizzas = input(prompt)
    finished_list.append("Name: " + Name)
    finished_list.append("Phone number: " + Phone_Number)
    if pizzas == 'Cheese pizza':
        quantity = True
        while quantity:
            prompt4 = "How many would you like?"
            Amount = input(prompt4)
            if Amount != "1":
                finished_list.append(pizzas + " quantity: " + Amount + ", One Pizza Price: " + "5$")
                quantity = False
            else:
                finished_list.append(pizzas + " is " + Pizza_Price)
                quantity = False
        print("One pizza is " + str(Pizza_Price))
        question = "Would you like toppings? They cost an additional 1$ each."
        food = input(question)
        if food == 'yes':
            question_5 = "What toppings would you like?"
            topping = input(question_5)
            if topping in toppings:
                finished_list.append("Toppings: " + topping + ", 1$")
                question_6 = "Would you like more?"
                answer = input(question_6)
                if answer == 'yes':
                    question_7 = "What topping?"
                    topping_2 = input(question_7)
                    if topping_2 in toppings:
                        finished_list.append(topping_2 + ", 1$")
                        question_8 = "Would you like more?"
                        answer_2 = input(question_8)
                        if answer_2 == 'yes':
                            question_9 = "What topping?"
                            answer_3 = input(question_9)
                            if answer_3 in toppings:
                                finished_list.append(answer_3 + ", 1$")
                                question_10 = "Would you like more?"
                                answer_4 = input(question_10)
                                if answer_4 == 'yes':
                                    question_11 = "What topping?"
                                    answer_5 = input(question_11)
                                    if answer_5 in toppings:
                                        finished_list.append(answer_5 + ", 1$")
                                        print("That is the maximum amount of toppings.")
                                        Customer = False
                                if answer_4 == 'no':
                                    break
                        if answer_2 == 'no':
                            break
                if answer == 'no':
                    break
        if food == 'no':
            break
    if pizzas == 'Chicken pizza':
        while True:
            prompt = "How many would you like?"
            if input(prompt) != "1":
                finished_list.append(pizzas + " quantity: " + input(prompt) + ", One Pizza Price: " + "5$")
                break
            else:
                finished_list.append(pizzas + " is " + Pizza_Price)
                break
        finished_list.append(pizzas + " is " + Pizza_Price)
        print("Base pizza is " + str(Pizza_Price))
        question = "Would you like toppings? They cost an additional 1$ each."
        food = input(question)
        if food == 'yes':
            question_5 = "What toppings would you like?"
            topping = input(question_5)
            if topping in toppings:
                finished_list.append("Toppings: " + topping + ", 1$")
                question_6 = "Would you like more?"
                answer = input(question_6)
                if answer == 'yes':
                    question_7 = "What topping?"
                    topping_2 = input(question_7)
                    if topping_2 in toppings:
                        finished_list.append(topping_2 + ", 1$")
                        question_8 = "Would you like more?"
                        answer_2 = input(question_8)
                        if answer_2 == 'yes':
                            question_9 = "What topping?"
                            answer_3 = input(question_9)
                            if answer_3 in toppings:
                                finished_list.append(answer_3 + ", 1$")
                                question_10 = "Would you like more?"
                                answer_4 = input(question_10)
                                if answer_4 == 'yes':
                                    question_11 = "What topping?"
                                    answer_5 = input(question_11)
                                    if answer_5 in toppings:
                                        finished_list.append(answer_5 + ", 1$")
                                        print("That is the maximum amount of toppings.")
                                        Customer = False
                                if answer_4 == 'no':
                                    break
                        if answer_2 == 'no':
                            break
                if answer == 'no':
                    break
        if food == 'no':
            break
print("\nThis is your order with the price: ")
print("\n--Receipt--")
print(finished_list)

