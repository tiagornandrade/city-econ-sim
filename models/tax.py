class TaxesBusinessRules:
    def __init__(self):
        pass

    @staticmethod
    def increase_taxes(city_state):
        for i in range(len(city_state)):
            city_state[i][1] += 1
        return city_state
