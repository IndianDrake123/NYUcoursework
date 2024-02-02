def organize_into_profits_losses(lst):
    organized_list = []
    current_streak = []

    for num in lst:
        if not current_streak or (current_streak[-1] < 0 and num < 0) or (current_streak[-1] >= 0 and num >= 0):
            current_streak.append(num)
        else:
            organized_list.append(current_streak)
            current_streak = [num]

    organized_list.append(current_streak)

    return organized_list

def spending_statistics(lst):
    prof = 0
    loss = 0 
    prof_or_loss = None
    balance = 0
    for ls in lst:
        for ls1 in ls:
            if ls1 > 0:
                prof_or_loss = True
            else:
                prof_or_loss = False
            
            balance += ls1
        
        if prof_or_loss:
            prof += 1 
        else:
            loss += 1
    
    print(f'You have had {prof} periods of subsequent profit.')
    print(f'You have had {loss} periods of subsequent losses.')
    print(f'Total balance: {balance}')

    if balance > 0:
        print("You're doing great! Keep it up!")
    elif balance == 0:
        print("You are doing just fine!")
    else:
        print("You could be doing better with your finances...")

def main():
    weeks_lst = [1, 4, 5, 4, -2, -5, 3, -3, -5, 3]
    organized_weeks_lst = organize_into_profits_losses(weeks_lst)
    print("Here are your spending habits over the last few weeks:",
    organized_weeks_lst)
    spending_statistics(organized_weeks_lst)

main()