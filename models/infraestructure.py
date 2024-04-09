class InfraestructureBusinessRules:
    def __init__(self):
        pass

    @staticmethod
    def invest_in_infrastructure(city_state):
        starting_amount = 10000000
        increment_amount = 1000000
        tax_increase = 500000

        if city_state[0][0] == 0:
            city_state[0][0] = starting_amount
            infrastructure_value = starting_amount
        else:
            city_state[0][0] += increment_amount
            infrastructure_value = city_state[0][0]

        for i in range(len(city_state)):
            city_state[i][1] += tax_increase

        return city_state, starting_amount, increment_amount, infrastructure_value, tax_increase
