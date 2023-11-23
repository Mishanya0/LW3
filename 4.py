import json

firms = {}
with open('firms.txt', 'r') as f:
    total_profit = 0
    count_firms = 0
    lines = f.readlines()
    for line in lines:
        name, owner, revenue, costs = line.split()
        profit = int(revenue) - int(costs)
        firms[name] = profit
        if profit > 0:
            total_profit += profit
            count_firms += 1

average_profit = total_profit / count_firms

result = [firms, {"average_profit": average_profit}]
with open('firms.json', 'w') as f:
    json.dump(result, f, ensure_ascii=False, indent=4)
