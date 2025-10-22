import tkinter as tk
from tkinter import messagebox

# ====== Funções auxiliares ======
def parse_number(value):
    try:
        value = value.replace(',', '.')
        return float(value)
    except:
        return None

def calcular():
    dmax_str = entry_dmax.get()
    dmin_str = entry_dmin.get()
    dmax = parse_number(dmax_str)
    dmin = parse_number(dmin_str)

    if dmax is None or dmin is None:
        messagebox.showerror('Erro', 'Informe valores numéricos válidos para ambos os diâmetros.')
        return
    
    if dmax < dmin:
        messagebox.showerror('Erro', 'O diâmetro maior não pode ser menor que o diâmetro menor.')
        return

    tipo = tipo_tubo.get()
    ovalizacao = (dmax - dmin) / ((dmax + dmin) / 2) * 100
    label_ovalizacao_valor.config(text=f"{ovalizacao:.1f}%")

    # ====== Lógica conforme o tipo selecionado ======
    if tipo == "geleado":
        limite = 10
        if ovalizacao < limite:
            status_label.config(text="Tubo Geleado (OK)", fg="#16a34a")  # Verde
        else:
            status_label.config(text="Tubo GELEADO REPROVADO!", fg="#dc2626")
            messagebox.showwarning(
                "Reprovado",
                "⚠️ Tubo GELEADO REPROVADO!\n\nOvalização acima de 10%.\n"
                "Abra uma FOLHA ROSA e coloque o tubo na área NÃO CONFORME."
            )

    elif tipo == "seco":
        limite = 15
        if ovalizacao < limite:
            status_label.config(text="Tubo Seco (OK)", fg="#0ea5a4")  # Azul esverdeado
        else:
            status_label.config(text="Tubo SECO REPROVADO!", fg="#dc2626")
            messagebox.showwarning(
                "Reprovado",
                "⚠️ Tubo SECO REPROVADO!\n\nOvalização acima de 15%.\n"
                "Abra uma FOLHA ROSA e coloque o tubo na área NÃO CONFORME."
            )
    
    else:
            status_label.config(text="TIPO DE TUBO NÃO SELECIONADO", fg="#dc2626")
            messagebox.showerror(
                "TIPO DE TUBO NÃO SELECIONADO",
                "⚠️ O TIPO DE TUBO NÃO FOI SELECIONADO.\n"
                "Por favor, selecione um tipo de tubo para realizar a verificação."
            )
        

# ====== Função para adicionar placeholder ======
def add_placeholder(entry, text):
    entry.insert(0, text)
    entry.config(fg="#94a3b8")  # cinza claro

    def on_focus_in(event):
        if entry.get() == text:
            entry.delete(0, tk.END)
            entry.config(fg="#0f172a")  # cor normal

    def on_focus_out(event):
        if not entry.get():
            entry.insert(0, text)
            entry.config(fg="#94a3b8")

    entry.bind("<FocusIn>", on_focus_in)
    entry.bind("<FocusOut>", on_focus_out)
    
    
# ====== Função para limpar ======
def limpar():
    entry_dmax.delete(0, tk.END)
    entry_dmin.delete(0, tk.END)
    label_ovalizacao_valor.config(text='--')
    status_label.config(text='', fg="#0f172a")
    tipo_tubo.set("null")
    add_placeholder(entry_dmax, "Ex.: 2.5")
    add_placeholder(entry_dmin, "Ex.: 2.4")

# ====== JANELA PRINCIPAL ======
root = tk.Tk()
root.title('Ovalização do Tubo Loose')
root.geometry('780x420')
root.config(bg='#eef6f9')
root.resizable(False, False)

# ====== FRAME PRINCIPAL ======
main_frame = tk.Frame(root, bg='#eef6f9')
main_frame.pack(expand=True, fill='both', padx=20, pady=20)

# ====== CARD ESQUERDO ======
card = tk.Frame(main_frame, bg='white', bd=0, relief='solid')
card.pack(side='left', padx=(0,20), fill='y', ipadx=10, ipady=10)

titulo = tk.Label(card, text='Ovalização do Tubo Loose', bg='white', fg='#0f172a', font=('Inter', 14, 'bold'))
titulo.pack(pady=(10, 5))

# ====== OPÇÃO DE TIPO DE TUBO ======
tipo_tubo = tk.StringVar(value="null")

tipo_frame = tk.Frame(card, bg='white')
tipo_frame.pack(padx=20, pady=(5, 0), anchor='w')

tk.Label(tipo_frame, text="Tipo de Tubo:", bg='white', fg='#334155', font=('Inter', 10, 'bold')).pack(anchor='w')

tk.Radiobutton(
    tipo_frame, text="Tubo Geleado", variable=tipo_tubo, value="geleado",
    bg='white', fg='#0f172a', font=('Inter', 10), activebackground='white',
    selectcolor='#e2e8f0'
).pack(side='left', padx=(0,10))

tk.Radiobutton(
    tipo_frame, text="Tubo Seco", variable=tipo_tubo, value="seco",
    bg='white', fg='#0f172a', font=('Inter', 10), activebackground='white',
    selectcolor='#e2e8f0'
).pack(side='left')

# ====== CAMPOS DE ENTRADA ======
label_dmax = tk.Label(card, text='Diâmetro Maior', bg='white', fg='#334155', font=('Inter', 10))
label_dmax.pack(anchor='w', padx=20, pady=(10, 0))
entry_dmax = tk.Entry(card, font=('Inter', 11), bg='#f8fafc', relief='flat', highlightbackground='#e6eef6', highlightthickness=1)
entry_dmax.pack(fill='x', padx=20, pady=(4, 0))

label_dmin = tk.Label(card, text='Diâmetro Menor', bg='white', fg='#334155', font=('Inter', 10))
label_dmin.pack(anchor='w', padx=20, pady=(10, 0))
entry_dmin = tk.Entry(card, font=('Inter', 11), bg='#f8fafc', relief='flat', highlightbackground='#e6eef6', highlightthickness=1)
entry_dmin.pack(fill='x', padx=20, pady=(4, 0))


# ====== Adicionar placeholders ======
add_placeholder(entry_dmax, "Ex.: 2.5")
add_placeholder(entry_dmin, "Ex.: 2.4")


# ====== BOTÕES ======
btn_frame = tk.Frame(card, bg='white')
btn_frame.pack(padx=20, pady=(15, 5), fill='x')

btn_calc = tk.Button(btn_frame, text='Calcular', bg='#0ea5a4', fg='white', relief='flat', font=('Inter', 10, 'bold'), command=calcular)
btn_calc.pack(side='left', expand=True, fill='x', padx=(0,5))

btn_limpar = tk.Button(btn_frame, text='Limpar', bg='#e2e8f0', fg='#0f172a', relief='flat', font=('Inter', 10, 'bold'), command=limpar)
btn_limpar.pack(side='left', expand=True, fill='x', padx=(5,0))

# ====== RESULTADOS ======
result_frame = tk.Frame(card, bg='#f8fafc', bd=0, relief='solid')
result_frame.pack(fill='x', padx=20, pady=(10, 0))

label_ovalizacao = tk.Label(result_frame, text='Ovalização:', bg='#f8fafc', fg='#0f172a', font=('Inter', 10, 'bold'))
label_ovalizacao.grid(row=0, column=0, sticky='w', padx=5, pady=4)
label_ovalizacao_valor = tk.Label(result_frame, text='--', bg='#f8fafc', font=('Inter', 10))
label_ovalizacao_valor.grid(row=0, column=1, sticky='e', padx=5, pady=4)

status_label = tk.Label(card, text='', bg='white', fg='#0f172a', font=('Inter', 11, 'bold'))
status_label.pack(pady=(10, 0))

rodape = tk.Label(card, text='Insira valores em mm.', bg='white', fg='#94a3b8', font=('Inter', 9))
rodape.pack(side='bottom', pady=(10,5))

# ====== PAINEL DIREITO ======
info_frame = tk.Frame(main_frame, bg='white', bd=0, relief='solid')
info_frame.pack(side='right', fill='both', expand=True)

info_title = tk.Label(info_frame, text='Critérios de Aprovação', bg='white', fg='#0f172a', font=('Inter', 13, 'bold'))
info_title.pack(pady=(10,5))

info_text = (
    "Tubo Geleado: Ovalização < 10% (OK)\n"
    "Tubo Seco: Ovalização < 15% (OK)\n\n"
    "Caso o tubo esteja REPROVADO, deve ser aberta uma\n"
    "folha rosa e o tubo deve ser colocado na área\n"
    "NÃO CONFORME."
)

info_label = tk.Label(info_frame, text=info_text, bg='white', fg='#334155', font=('Inter', 10), justify='left')
info_label.pack(padx=20, pady=10, anchor='w')

root.mainloop()
