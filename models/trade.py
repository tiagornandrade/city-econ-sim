class TradeBusinessRules:
    def __init__(self):
        pass

    @staticmethod
    def encourage_trade(city_state):
        for i in range(len(city_state)):
            city_state[i][2] += 1
        return city_state
