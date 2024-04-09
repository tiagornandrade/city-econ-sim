import os
import sys
import time

from models.exit import ExitBusinessRules
from models.infraestructure import InfraestructureBusinessRules
from models.tax import TaxesBusinessRules
from models.trade import TradeBusinessRules


class InitGame:
    def __init__(self):
        pass

    @staticmethod
    def clear_screen():
        os.system("cls" if os.name == "nt" else "clear")

    @staticmethod
    def start():
        InitGame.clear_screen()
        print("Game started")
        input("Pressione Enter para continuar...")
        InitGame.clear_screen()
        print("🤗 Bem-vindo ao Jogo de Simulação Econômica!")
        time.sleep(2)
        print(
            "🔊 Você é o governante de uma cidade e precisa tomar decisões econômicas."
        )
        time.sleep(2)

        city_state = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        infrastructure_values = []

        while True:
            InitGame.clear_screen()
            print("Escolha uma ação:")
            print("1. Investir em infraestrutura 🏗️")
            print("2. Aumentar impostos 💰")
            print("3. Incentivar o comércio 🏪")
            print("4. Sair do jogo 👋")

            escolha = input("Digite o número da sua escolha: ")

            if escolha == "1":
                InitGame.clear_screen()
                print("Você decidiu investir em infraestrutura.")

                (
                    city_state,
                    initial_amount,
                    increment_amount,
                    current_amount,
                    tax_increase,
                ) = InfraestructureBusinessRules.invest_in_infrastructure(city_state)

                formatted_initial_amount = "{:,.2f}".format(initial_amount)
                formatted_increment_amount = "{:,.2f}".format(increment_amount)
                formatted_tax_increase = "{:,.2f}".format(tax_increase)

                time.sleep(2)
                InitGame.clear_screen()
                print(f"A cidade possui em caixa $ {formatted_initial_amount}.")

                print(
                    f"Nesse momento a cidade está recebendo um incremento de $ {formatted_increment_amount}."
                )

                time.sleep(5)
                InitGame.clear_screen()
                print("Investindo... ")
                time.sleep(5)
                print("Investimento realizado com sucesso! ✅")
                time.sleep(3)

                current_amount = initial_amount + increment_amount
                formatted_current_amount = "{:,.2f}".format(current_amount)
                infrastructure_values.append(current_amount)
                InitGame.clear_screen()
                print(f"A cidade agora possui $ {formatted_current_amount}.")

                print(f"O imposto atual é de $ {formatted_tax_increase}.")
                time.sleep(5)

            elif escolha == "2":
                print("Você decidiu aumentar impostos.")
                time.sleep(2)
            elif escolha == "3":
                print("Você decidiu incentivar o comércio.")
                time.sleep(2)
            elif escolha == "4":
                InitGame.clear_screen()
                ExitBusinessRules.exit_game()
                break
            else:
                print("Escolha inválida. Tente novamente.")
                time.sleep(2)


if __name__ == "__main__":
    InitGame.start()
