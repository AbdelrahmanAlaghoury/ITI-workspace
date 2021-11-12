def DPknapSack(items, knap_weight):
    """
    fill the knapsack using Dynamic Progamming(I/0)

    Parameters
    ----------
    items : List
        It's a List that contains items to be filled and each item has profit and weight:
        [item, itme profit and item weight].
    knap_weight : Integer
        Max weight of the knapsack.

    Returns
    -------
    optimal_value : Integer
        Optimal value of the items that can the knapsack hold.

    """
    n_items = len(items)
    # create a table (number of items x max knap weight)
    table = [[0 for x in range(knap_weight + 1)] for x in range(n_items + 1)]
        
    for item in range(n_items + 1):
        for weight in range(knap_weight + 1):
            if item == 0 or weight == 0:
                table[item][weight] = 0
            elif items[item-1][2] <= weight:
                table[item][weight] = max(items[item-1][1]+ table[item-1][weight-items[item-1][2]], table[item-1][weight])
            else:
                table[item][weight] = table[item-1][weight] 

    return table[n_items][knap_weight]


def main():
    item_list = [(1,8,1),(2,10,3),(3,15,5),(4,7,4),(5,8,2),(6,9,3),(7,4,2)] 
    print(DPknapSack(item_list, 50))
    
if __name__ == "__main__":
    main()