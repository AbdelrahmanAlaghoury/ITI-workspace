from operator import itemgetter

def greedy_knapsack(items, knap_weight, cost_code = 1, knap_type = 1):
    """
    fill a knapsack with items according to the greedy algorithm rules

    Parameters
    ----------
    items : List
        It's a List that contains items to be filled and each item has profit and weight:
            [item, itme profit and item weight].
    knap_weight : Integer
        Max weight of the knapsack.
    cost_code : Integer, optional
        How the Greedy algorithm will fill the knapsack 
        1-> max profit
        2-> min weight.
        3-> max profit per weight
        4-> All of the above as sorting levels
        The default is 1.
    knap_type : Integer, optional
        0-> Fractional.(Item is divisible)
        1-> (I/0)Pick the item or not.(Item isn't divisible)
        The default is 1.

    Returns
    -------
    knapsack_items : Dict
        Picked items for the knapsack based on the Greedy algorithm rules.
        Ex:
            "Max Profit" : [List of items]
            and the keys will be added based on the user selection
    """    
    knapsack_items = {}
    Cost_Map = ["Max Profit", "Min Weight", "Max profit per weight"]
    
    if cost_code == 1 or cost_code == 4:
        # To sort the items based on max profit
        items.sort(key = itemgetter(1), reverse=True)
        knapsack_items[Cost_Map[0]] = fill_knapsack(items, knap_weight, knap_type)
        
    if cost_code == 2 or cost_code == 4:
        # To sort the items based on min weight
        items.sort(key = itemgetter(2))
        knapsack_items[Cost_Map[1]] = fill_knapsack(items, knap_weight, knap_type)
        
    if cost_code == 3 or cost_code == 4:
        # To sort the items based on the max profit per weight
        items.sort(key = lambda item: item[1]/item[2], reverse=True)
        knapsack_items[Cost_Map[2]] = fill_knapsack(items, knap_weight, knap_type)

    if cost_code < 1 and cost_code > 4:
        # Set to the default value of cost_code(profit)
        cost_code = 1                     
        items.sort(key = itemgetter(1), reverse=True) 
        knapsack_items[Cost_Map[0]] = fill_knapsack(items, knap_weight, knap_type)

    return knapsack_items 

def fill_knapsack(items, knap_weight, knap_type = 1):
    """
    Fill a knapsack with sorted items up to a certain weight

    Parameters
    ----------
    items : List
        It's a List that contains items to be filled and each item has profit and weight:
        [item, itme profit and item weight].
    knap_weight : Integer
        Max weight of the knapsack.
    knap_type : Integer
        0-> Fractional.(Item is divisible)
        1-> (I/0)Pick the item or not.(Item isn't divisible)

    Returns
    -------
    knapsack_items : List
        Picked items for the knapsack based on the Greedy algorithm rules.

    """
    knapsack_items = []
    for item in items:
        item_weight = item[2]
        if knap_weight > item_weight:
            knapsack_items.append(item)
            knap_weight -= item_weight
        elif knap_weight == item_weight:
            break
        else:
            if knap_type:
                knap_weight = 0
                break
            else:
                fraction = knap_weight / item_weight
                knapsack_items.append((item[0], item[1]*fraction, item[2]*fraction))
                knap_weight = 0
                break
    return knapsack_items

def main():
    #(item, Profit, Weight)
    item_list = [(1,8,1),(2,10,3),(3,15,5),(4,7,4),(5,8,2),(6,9,3),(7,4,2)] 
    current_configurations = ["I/0", "Max profit", None]
    knap_type = 1
    cost_code = 1
    user_input = 0
    knapsack_items = None
    while user_input != 4:
        user_input = int(input(f"""
        # Configurations:
        [knapType, cost, weight]
        {current_configurations}
        =======================
        1- To configure the type of Knapsack ( Fractional - I/0) 
            # Default value I/0
        2- To configure The cost function based on:
            # Maximum Profit(Default) 
            # Minimum Weight 
            # Maximum Profit/Weight 
            # All
        3- To Configure the maximum weight of the knapsack and fill it
        4- To Close the program
        =======================  
        Knapsack:{knapsack_items}     
        =======================              
        Enter a valid Choice: 
        """))
        if user_input > 0 and user_input <= 4:
            # Fractional or I/0
            if user_input == 1:
                knap_type = int(input("""
                # 0-> Fractional
                # 1-> I/0
                =======================
                Enter a valid Choice: 
                """))
                knapTypes = ['Fractional', 'I/0']
                if knap_type == 0 or knap_type == 1:
                    current_configurations[0] = knapTypes[knap_type]
                else:
                    # Default value (I/0)
                    knap_type = 1
                    print("Invalid Input!!!!")
            elif user_input == 2:
                cost_code = int(input("""
                # 1-> Maximum Profit(Default) 
                # 2-> Minimum Weight 
                # 3-> Maximum Profit/Weight 
                # 4-> All
                =======================
                Enter a valid Choice: 
                """))
                cost_codes = ['Maximum Profit', 'Minimum Weight', 'Maximum Profit/Weight', 'All'] 
                if cost_code > 0 and cost_code <= 4:
                    current_configurations[1] = cost_codes[cost_code - 1]
                else:
                    # Default value (Max Profit)
                    cost_code = 1
                    print("Invalid Input!!!!")              
            elif user_input == 3: 
                user_input = int(input("""
                # 1-> To configure the weight
                # 2-> To fill the knapsack with the previous weight
                =======================
                Enter a valid valid Choice:                         
                """))
                if user_input == 1:
                    knap_weight = int(input("""
                    Enter a valid weight
                    """))
                    if knap_weight != None and knap_weight > 0:
                        current_configurations[2] = knap_weight
                elif current_configurations[2] != None:
                    knap_weight = current_configurations[2]
                    knapsack_items = greedy_knapsack(item_list, knap_weight, cost_code, knap_type)
                else:
                    print("Invalid Input!!!!")    
            else:
                print("Closing the program....")
                break
    print("Program close")
            
if __name__ == "__main__":
    main()