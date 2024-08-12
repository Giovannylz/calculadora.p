import tkinter as tk

class CalculatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculadora")

        # Tela de entrada
        self.display = tk.Entry(root, font=("Arial", 16), borderwidth=2, relief="solid")
        self.display.grid(row=0, column=0, columnspan=4, pady=10, padx=10)

        # Botões da calculadora
        self.create_buttons()

    def create_buttons(self):
        # Definir os botões e suas posições
        buttons = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
            ('0', 4, 0), ('.', 4, 1), ('+', 4, 2), ('=', 4, 3),
            ('C', 5, 0, 4)
        ]

        for button in buttons:
            text, row, col = button[0], button[1], button[2]
            colspan = button[3] if len(button) > 3 else 1
            button_widget = tk.Button(self.root, text=text, padx=20, pady=20, font=("Arial", 16),
                                     command=lambda t=text: self.on_button_click(t))
            button_widget.grid(row=row, column=col, columnspan=colspan)

    def on_button_click(self, button_text):
        if button_text == 'C':
            self.display.delete(0, tk.END)
        elif button_text == '=':
            expression = self.display.get()
            try:
                result = self.evaluate_expression(expression)
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, str(result))
            except Exception:
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, "Erro")
        else:
            self.display.insert(tk.END, button_text)

    def evaluate_expression(self, expression):
        # Avalia a expressão matemática com segurança
        try:
            # Remover espaços e validar a expressão
            expression = expression.replace('^', '**')
            return eval(expression, {"__builtins__": None}, {})
        except:
            raise ValueError("Expressão inválida")

if __name__ == "__main__":
    root = tk.Tk()
    app = CalculatorApp(root)
    root.mainloop()
