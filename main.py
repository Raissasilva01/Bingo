import random
import tkinter as tk

class BingoApp:
    def __init__(self, root):
        self.root = root
        self.root.title('Bingo')

        #lista de numeros sorteados
        self.ls_num_sorteados = []

        #Label para exibir numeros sorteados
        self.lbl_result = tk.Label(root, text='', font=('Arial', 14))
        self.lbl_result.pack(pady=20)

        #botao para sortear numeros
        self.btn_sortear = tk.Button(root, text="Sortear", command=self.sortear_numeros, font=('Arial', 14))
        self.btn_sortear.pack(pady=10)

        #Botao para reiniciar o jogo
        self.btn_reset = tk.Button(root, text="Reiniciar o jogo", command=self.reset_jogo, font=('Arial', 14))
        self.btn_reset.pack(pady=10)

        #Funcao de sortear um numero de 1 a 75 e adiciona lista
    def sortear_numeros(self):
        if len(self.ls_num_sorteados) < 75:
            numeroSorteado = random.randint( 1, 75)
            while numeroSorteado in self.ls_num_sorteados:
                numeroSorteado = random.randint(1 , 75)
            self.ls_num_sorteados.append(numeroSorteado)
            self.lbl_result.config(text=', '.join(map(str, self.ls_num_sorteados)))
        else:
            self.lbl_result.config(text="bingo encerrado!")

    def reset_jogo(self):
        self.ls_num_sorteados.clear()
        self.lbl.result.config(text=' ')


if __name__ == "__main__":
    root = tk.Tk()
    app = BingoApp(root)
    root.mainloop()