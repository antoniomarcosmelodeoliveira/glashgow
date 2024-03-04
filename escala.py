# importar as bibliotecas de uso para parte grafica e uso de imagem.
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

# FUNÇÃO PARA CALCULAR OS VALORES OBTIDOS APOS ENVIAR PELO BOTAO.
def calcular_ecg():
    abertura_ocular = int(abertura_ocular_var.get())
    resposta_motora = int(resposta_motora_var.get())
    resposta_verbal = int(resposta_verbal_var.get())
    
    pontuacao_total = abertura_ocular + resposta_motora + resposta_verbal
    
    resultado_label.config(text="Pontuação Obtida: " + str(pontuacao_total), foreground="green")

    interpretacao_label.config(text="Diagnostico/Conduta: " + interpretar_pontuacao(pontuacao_total), foreground="red")

# FUNÇÃO PARA INTERPRETAR O RESULTADO OBTIDO.
def interpretar_pontuacao(pontuacao_total):
    if pontuacao_total == 3:
        return "Coma profundo sem qualquer resposta"
    elif pontuacao_total == 4:
        return "Coma profundo com provável comprometimento do diencéfalo (postura em extensão ou de descerebração)"
    elif pontuacao_total == 7:
        return "Coma moderado"
    elif pontuacao_total == 11:
        return "Coma superficial"
    elif pontuacao_total == 15:
        return "Normalidade"
    elif 3 <= pontuacao_total <= 8:
        return "Trauma cranioencefálico grave, com necessidade de intubação imediata"
    elif 9 <= pontuacao_total <= 12:
        return "Trauma cranioencefálico moderado"
    elif 13 <= pontuacao_total <= 15:
        return "Trauma cranioencefálico leve"


# Criar a janela principal da aplicação
root = tk.Tk()
root.title("Calculadora da Escala de Coma de Glasgow") #TITULO DA APLICAÇÃO

# Carregar a imagem
image = Image.open("1.png") #carrega a imagem do cerebro.
image = image.resize((230, 230), Image.ANTIALIAS) #define uma altura e largura para imagem 
photo = ImageTk.PhotoImage(image) #empacota a imagem 
image_label = tk.Label(root, image=photo) #exibe a imagem na label definida.
image_label.grid(row=0, column=0, columnspan=3, padx=5, pady=(0, 1)) #define um padding para a imagem 

# Variáveis para armazenar as pontuações selecionadas pelos radio buttons.
abertura_ocular_var = tk.StringVar()
resposta_motora_var = tk.StringVar()
resposta_verbal_var = tk.StringVar()

# Criar e posiciona os widgets da aplicação.

#resposta OCULAR.
abertura_ocular_label = ttk.Label(root, text="Abertura Ocular:", foreground="blue")
abertura_ocular_label.grid(row=0, column=0, padx=5, pady=(250, 0))
abertura_ocular_radio1 = ttk.Radiobutton(root, text="Espontânea", variable=abertura_ocular_var, value=4)
abertura_ocular_radio1.grid(row=1, column=0, sticky="w", padx=5, pady=2)
abertura_ocular_radio2 = ttk.Radiobutton(root, text="À voz", variable=abertura_ocular_var, value=3)
abertura_ocular_radio2.grid(row=2, column=0, sticky="w", padx=5, pady=2)
abertura_ocular_radio3 = ttk.Radiobutton(root, text="À dor", variable=abertura_ocular_var, value=2)
abertura_ocular_radio3.grid(row=3, column=0, sticky="w", padx=5, pady=2)
abertura_ocular_radio4 = ttk.Radiobutton(root, text="Ausente", variable=abertura_ocular_var, value=1)
abertura_ocular_radio4.grid(row=4, column=0, sticky="w", padx=5, pady=2)

#resposta VERBAL.
resposta_verbal_label = ttk.Label(root, text="Resposta Verbal:", foreground="blue")
resposta_verbal_label.grid(row=0, column=1, padx=5, pady=(250, 0))
resposta_verbal_radio1 = ttk.Radiobutton(root, text="Orientado", variable=resposta_verbal_var, value=5)
resposta_verbal_radio1.grid(row=1, column=1, sticky="w", padx=5, pady=2)
resposta_verbal_radio2 = ttk.Radiobutton(root, text="Confuso", variable=resposta_verbal_var, value=4)
resposta_verbal_radio2.grid(row=2, column=1, sticky="w", padx=5, pady=2)
resposta_verbal_radio3 = ttk.Radiobutton(root, text="Palavras inapropriadas", variable=resposta_verbal_var, value=3)
resposta_verbal_radio3.grid(row=3, column=1, sticky="w", padx=5, pady=2)
resposta_verbal_radio4 = ttk.Radiobutton(root, text="Sons ininteligíveis", variable=resposta_verbal_var, value=2)
resposta_verbal_radio4.grid(row=4, column=1, sticky="w", padx=5, pady=2)
resposta_verbal_radio5 = ttk.Radiobutton(root, text="Ausente", variable=resposta_verbal_var, value=1)
resposta_verbal_radio5.grid(row=5, column=1, sticky="w", padx=5, pady=2)

#resposta MOTORA.
resposta_motora_label = ttk.Label(root, text="Resposta Motora:", foreground="blue")
resposta_motora_label.grid(row=0, column=2, padx=5, pady=(250, 0))
resposta_motora_radio1 = ttk.Radiobutton(root, text="Obedece comando", variable=resposta_motora_var, value=6)
resposta_motora_radio1.grid(row=1, column=2, sticky="w", padx=5, pady=2)
resposta_motora_radio2 = ttk.Radiobutton(root, text="Localiza dor", variable=resposta_motora_var, value=5)
resposta_motora_radio2.grid(row=2, column=2, sticky="w", padx=5, pady=2)
resposta_motora_radio3 = ttk.Radiobutton(root, text="Retira à dor", variable=resposta_motora_var, value=4)
resposta_motora_radio3.grid(row=3, column=2, sticky="w", padx=5, pady=2)
resposta_motora_radio4 = ttk.Radiobutton(root, text="Flexão anormal", variable=resposta_motora_var, value=3)
resposta_motora_radio4.grid(row=4, column=2, sticky="w", padx=5, pady=2)
resposta_motora_radio5 = ttk.Radiobutton(root, text="Extensão anormal", variable=resposta_motora_var, value=2)
resposta_motora_radio5.grid(row=5, column=2, sticky="w", padx=5, pady=2)
resposta_motora_radio6 = ttk.Radiobutton(root, text="Ausente", variable=resposta_motora_var, value=1)
resposta_motora_radio6.grid(row=6, column=2, sticky="w", padx=5, pady=2)

#BOTAO DE CALCULAR
calcular_button = ttk.Button(root, text="Calcular", command=calcular_ecg)
calcular_button.grid(row=7, column=0, columnspan=3, padx=5, pady=5)

#CAMPO ONDE MOSTRA O VALOR OBTIDO, DEFINIDO INICIALMENTE COMO VAZIO
resultado_label = ttk.Label(root, text="")
resultado_label.grid(row=8, column=0, columnspan=3, padx=5, pady=5)

#CAMPO ONDE MOSTRA  A CONDUTA E DIAGNOSTICO OBTIDO APOS A TRATATIVA DO VALOR, DEFINIDO INICIALMENTE COMO VAZIO
interpretacao_label = ttk.Label(root, text="")
interpretacao_label.grid(row=9, column=0, columnspan=3, padx=5, pady=5)

# Iniciar o loop da aplicação 
#para que na precise sempre esta limpando o campo quando quiser realizar uma nova operação
#basta selecionar uma nova opçao e clicar em calcular.
root.mainloop()