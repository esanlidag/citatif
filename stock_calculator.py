import tkinter as tk
from tkinter import ttk


PERCENTS = [5, 10, 15, 20, 25, 30, 35]


class PercentCalculator(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Stock Percent Calculator")
        self.resizable(False, False)

        self.price_var = tk.StringVar()
        self.custom_percent_var = tk.StringVar()
        self.results = {p: tk.StringVar() for p in PERCENTS}
        self.custom_result_var = tk.StringVar()

        self._build_ui()

    def _build_ui(self):
        main_frame = ttk.Frame(self, padding="10")
        main_frame.grid(row=0, column=0)

        ttk.Label(main_frame, text="Stock price:").grid(row=0, column=0, sticky="w")
        ttk.Entry(main_frame, textvariable=self.price_var).grid(row=0, column=1)
        ttk.Button(main_frame, text="Calculate", command=self.calculate).grid(row=0, column=2, padx=(5, 0))

        for i, p in enumerate(PERCENTS, start=1):
            ttk.Label(main_frame, text=f"Price -{p}%:").grid(row=i, column=0, sticky="w")
            ttk.Label(main_frame, textvariable=self.results[p]).grid(row=i, column=1, columnspan=2, sticky="w")

        # Custom percent entry
        row = len(PERCENTS) + 1
        ttk.Label(main_frame, text="Custom % drop:").grid(row=row, column=0, sticky="w")
        ttk.Entry(main_frame, textvariable=self.custom_percent_var, width=5).grid(row=row, column=1, sticky="w")
        ttk.Label(main_frame, textvariable=self.custom_result_var).grid(row=row, column=2, sticky="w")

    def calculate(self):
        try:
            price = float(self.price_var.get())
        except ValueError:
            for var in self.results.values():
                var.set("Invalid price")
            self.custom_result_var.set("")
            return

        for p in PERCENTS:
            result_price = price * (1 - p / 100)
            self.results[p].set(f"{result_price:.2f}")

        custom = self.custom_percent_var.get()
        if custom:
            try:
                custom_float = float(custom)
                result = price * (1 - custom_float / 100)
                self.custom_result_var.set(f"{result:.2f}")
            except ValueError:
                self.custom_result_var.set("Invalid %")
        else:
            self.custom_result_var.set("")


if __name__ == "__main__":
    app = PercentCalculator()
    app.mainloop()
