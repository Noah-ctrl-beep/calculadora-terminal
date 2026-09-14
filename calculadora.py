from textual.app import App, ComposeResult
from textual.widgets import Header, Footer, Button, Input
from textual.containers import Grid

class CalcAplicativo(App):
    CSS = """
    Grid {
        grid-size: 4 4;
        grid-gutter: 1;
        padding: 1;
    }
    Input {
        column-span: 4;
        margin-bottom: 1;
    }
    """
    BINDINGS = [("q", "quit", "Sair")]

    def compose(self) -> ComposeResult:
        yield Header(show_clock=True)
        yield Input(placeholder="0", id="tela")
        with Grid():
            botoes = ["7", "8", "9", "/", "4", "5", "6", "*", "1", "2", "3", "-", "C", "0", "=", "+"]
            for label in botoes:
                if label == "/": id_seguro = "div"
                elif label == "*": id_seguro = "mult"
                elif label == "-": id_seguro = "sub"
                elif label == "+": id_seguro = "soma"
                elif label == "=": id_seguro = "resultado"
                else: id_seguro = label

                # O ID agora guarda o caractere original de forma limpa
                yield Button(label, id=f"char_{id_seguro}")
        yield Footer()

    def on_button_pressed(self, event: Button.Pressed) -> None:
        tela = self.query_one("#tela", Input)

        # SOLUÇÃO DEFINITIVA: Lemos o ID que definimos acima, sem mexer no objeto 'Content'
        botao_id = event.button.id.replace("char_", "")

        # Mapeamos os IDs de volta para os operadores matemáticos
        if botao_id == "div": texto = "/"
        elif botao_id == "mult": texto = "*"
        elif botao_id == "sub": texto = "-"
        elif botao_id == "soma": texto = "+"
        else: texto = botao_id

        if texto == "C":
            tela.value = ""
        elif texto == "resultado":
            try:
                tela.value = str(eval(tela.value))
