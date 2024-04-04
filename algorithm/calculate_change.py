def calculate_change(payment, cost):
    change = payment - cost
    five_mw = 0
    one_mw = 0
    five_cw = 0
    one_cw = 0
    if change % 50000 >= 0:
        five_mw = change // 50000
        change -= five_mw * 50000
    print("{}원 지폐: {}장".format(50000, five_mw))
    if change % 10000 >= 0:
        one_mw = change // 10000
        change -= one_mw * 10000
    print("{}원 지폐: {}장".format(10000, one_mw))
    if change % 5000 >= 0:
        five_cw = change // 5000
        change -= five_cw * 5000
    print("{}원 지폐: {}장".format(5000, five_cw))
    if change % 1000 >= 0:
        one_cw = change // 1000
        change -= one_cw * 1000
    print("{}원 지폐: {}장".format(1000, one_cw))

calculate_change(100000, 33000)

calculate_change(500000, 378000)