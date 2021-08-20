def solution(array: list):
    buy, sell = array[0], array[1]
    global_profit = sell - buy 
    current_profit = -999

    for i in range(1, len(array)):
        current_profit = array[i] - buy 

        if current_profit > global_profit:
            global_profit =  current_profit
            sell = array[i]
        if array[i] < buy:
            buy = array[i]
        
    result = sell - global_profit, sell

    return result


def find_buy_sell_stock_prices(array):
  current_buy, global_sell = array[0], array[1]
  global_profit = global_sell - current_buy
  current_profit = -999

  for i in range(1, len(array)):
    current_profit = array[i] - current_buy

    if current_profit > global_profit:
      global_profit = current_profit
      global_sell = array[i]

    if current_buy > array[i]:
      current_buy = array[i];

  result = global_sell - global_profit, global_sell                 
   
  return result


if __name__ == "__main__":
    array = [8, 5, 12, 9, 19, 1]
    print(solution(array))
