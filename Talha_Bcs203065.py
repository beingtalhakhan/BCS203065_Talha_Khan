import tkinter as tk
import requests


class CurrencyConverter:
    API_URL = "https://openexchangerates.org/api/latest.json"
    API_KEY = "8b7594e12be6491a8158d646add9834a"

    def __init__(self):
        self.currencies = self.fetch_currencies()

    def fetch_currencies(self):
        params = {"app_id": self.API_KEY}
        response = requests.get(self.API_URL, params=params)
        data = response.json()
        return data["rates"]

    def convert(self, from_currency, to_currency, amount):
        if from_currency != "USD":
            amount = amount / self.currencies[from_currency]

        amount = round(amount * self.currencies[to_currency], 4)
        return amount


class App:
    def __init__(self):
        self.converter = CurrencyConverter()
        self.app = tk.Tk()
        self.app.title("Currency Converter")
        self.from_currency_var = tk.StringVar()
        self.to_currency_var = tk.StringVar()
        self.amount_var = tk.StringVar()
        self.result_var = tk.StringVar()

        # Create currency dropdown menus
        self.from_currency_menu = tk.OptionMenu(
            self.app, self.from_currency_var, *self.converter.currencies.keys()
        )
        self.from_currency_menu.grid(row=0, column=0, padx=5, pady=5)
        self.from_currency_var.set("USD")

        self.to_currency_menu = tk.OptionMenu(
            self.app, self.to_currency_var, *self.converter.currencies.keys()
        )
        self.to_currency_menu.grid(row=0, column=1, padx=5, pady=5)
        self.to_currency_var.set("EUR")

        # Create amount input field
        self.amount_entry = tk.Entry(self.app, textvariable=self.amount_var)
        self.amount_entry.grid(row=1, column=0, padx=5, pady=5)

        # Create convert and reset buttons
        self.convert_btn = tk.Button(
            self.app, text="Convert", command=self.convert_currency
        )
        self.convert_btn.grid(row=2, column=0, padx=5, pady=5)

        self.reset_btn = tk.Button(
            self.app, text="Reset", command=self.reset
        )
        self.reset_btn.grid(row=2, column=1, padx=5, pady=5)

        # Create result label
        self.result_lbl = tk.Label(self.app, textvariable=self.result_var)
        self.result_lbl.grid(row=1, column=1, padx=5, pady=5)

    def convert_currency(self):
        from_currency = self.from_currency_var.get()
        to_currency = self.to_currency_var.get()
        amount = float(self.amount_var.get())

        result = self.converter.convert(from_currency, to_currency, amount)

        self.result_var.set(str(result))

    def reset(self):
        self.from_currency_var.set("USD")
        self.to_currency_var.set("EUR")
        self.amount_var.set("")
        self.result_var.set("")

    def run(self):
        self.app.mainloop()


if __name__ == "__main__":
    app = App()
    app.run()
