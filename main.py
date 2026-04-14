# main.py
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.core.window import Window
from kivy.utils import get_color_from_hex

# Définir une couleur de fond pour la fenêtre (optionnel)
Window.clearcolor = get_color_from_hex("#2E2E2E")

class CalculatorApp(App):
    def build(self):
        self.title = "Calculatrice Kivy"
        self.expression = ""
        self.result_displayed = False  # Indique si le résultat vient d'être affiché

        # Layout principal vertical
        main_layout = BoxLayout(orientation='vertical', spacing=5, padding=10)

        # Affichage (Label non éditable, aligné à droite)
        self.display = Label(
            text="0",
            font_size="40sp",
            halign="right",
            valign="middle",
            size_hint=(1, 0.25),
            color=get_color_from_hex("#FFFFFF"),
            text_size=(None, None)  # sera ajusté automatiquement
        )
        # Lier la taille du texte à celle du label pour un bon alignement
        self.display.bind(size=self.display.setter('text_size'))
        main_layout.add_widget(self.display)

        # Grille des boutons
        button_grid = GridLayout(cols=4, spacing=5, size_hint=(1, 0.75))
        
        # Liste des boutons : (texte, couleur de fond)
        buttons = [
            ("C", "#FF6B6B"), ("⌫", "#FFB347"), ("%", "#FFB347"), ("/", "#FFB347"),
            ("7", "#4A4A4A"), ("8", "#4A4A4A"), ("9", "#4A4A4A"), ("*", "#FFB347"),
            ("4", "#4A4A4A"), ("5", "#4A4A4A"), ("6", "#4A4A4A"), ("-", "#FFB347"),
            ("1", "#4A4A4A"), ("2", "#4A4A4A"), ("3", "#4A4A4A"), ("+", "#FFB347"),
            ("+/-", "#4A4A4A"), ("0", "#4A4A4A"), (".", "#4A4A4A"), ("=", "#4CAF50")
        ]

        for text, bg_color in buttons:
            btn = Button(
                text=text,
                font_size="24sp",
                background_normal='',
                background_color=get_color_from_hex(bg_color),
                color=get_color_from_hex("#FFFFFF"),
                bold=True
            )
            btn.bind(on_press=self.on_button_press)
            button_grid.add_widget(btn)

        main_layout.add_widget(button_grid)
        return main_layout

    def on_button_press(self, instance):
        text = instance.text

        if text == "C":
            self.expression = ""
            self.display.text = "0"
            self.result_displayed = False

        elif text == "⌫":
            if self.result_displayed:
                self.expression = ""
                self.display.text = "0"
                self.result_displayed = False
            else:
                self.expression = self.expression[:-1]
                self.display.text = self.expression if self.expression else "0"

        elif text == "=":
            try:
                # Remplacer les symboles pour l'évaluation
                expr = self.expression.replace("×", "*").replace("÷", "/").replace("%", "/100")
                # Évaluation sécurisée (uniquement nombres, opérateurs et parenthèses)
                # On restreint l'espace de noms pour éviter les abus
                result = eval(expr, {"__builtins__": None}, {})
                # Formater le résultat
                if isinstance(result, float):
                    # Éviter les décimales inutiles
                    if result.is_integer():
                        result = int(result)
                    else:
                        result = round(result, 10)
                self.display.text = str(result)
                self.expression = str(result)
                self.result_displayed = True
            except Exception:
                self.display.text = "Erreur"
                self.expression = ""
                self.result_displayed = False

        elif text == "+/-":
            if self.expression and not self.result_displayed:
                # Inverser le signe du dernier nombre
                # Méthode simple : on ajoute "*(-1)" à la fin
                self.expression = f"({self.expression})*(-1)"
                self.display.text = self.expression
            elif self.result_displayed:
                # Si un résultat est affiché, on le négative directement
                try:
                    val = float(self.display.text)
                    val = -val
                    self.display.text = str(val)
                    self.expression = str(val)
                except:
                    pass

        else:
            # Chiffre, opérateur ou point
            if self.result_displayed:
                # Si on vient de faire "=", on recommence une nouvelle saisie
                if text in "0123456789.":
                    self.expression = text
                else:
                    self.expression = self.display.text + text
                self.result_displayed = False
            else:
                # Empêcher plusieurs points dans un même nombre (optionnel)
                if text == ".":
                    # Vérifier si le dernier nombre contient déjà un point
                    parts = self.expression.replace("+", " ").replace("-", " ").replace("*", " ").replace("/", " ").split()
                    if parts and "." in parts[-1]:
                        return  # Ne pas ajouter un deuxième point
                self.expression += text

            # Remplacer les symboles pour l'affichage
            display_expr = self.expression.replace("*", "×").replace("/", "÷")
            self.display.text = display_expr

if __name__ == "__main__":
    CalculatorApp().run()