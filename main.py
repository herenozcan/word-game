import tkinter as tk
from data import words
from random import choice

root = tk.Tk()
root.title("Kelime Oyunu")
root.geometry("600x600")
#"root.configure(background="white")"(bu pencerenin arkaplanını değiştirir.)

point = 0
turn = 4

question = tk.Label(
    root, text=words[turn]["soru"], font=("Arial", 20), pady=10, wraplength=400)
question.pack()

opens = [False for i in range(turn)]
show = " ".join(["_" for i in range(turn)])
label = tk.Label(root, text=show, font = ("Arial", 40), pady = 20)
label.pack()

def letter():
    global turn
    global words
    answer = words[turn]["cevap"]
    falses = [index for index, value in enumerate(opens) if value == False]
    will_open = choice(falses)
    opens[will_open] = True
    show = " ".join([answer[index] if opens[index] else "_" for index in range(len(answer))])
    label.config(text=show)

    if "_" not in show:
        label.config(text=answer + "\nPuanınız: {}".format(point))
        if turn == len(words) + 3:
            harf_al.config(state = tk.DISABLED)
            guess_button.config(state = tk.DISABLED)
            next_word_button.destroy()
        next_word_button.config(state=tk.ACTIVE)

harf_al = tk.Button(root, text="Harf Alim", command=lambda: letter(), activebackground="gray", font=("Arial", 20))
harf_al.pack(pady=20)

guess = tk.Entry(root, font=("Arial", 20))
guess.pack()

def guess_func():
    global turn
    global point
    global opens
    guess_word = guess.get()
    answer = words[turn]["cevap"]
    if guess_word == answer:
        falses = [index for index, value in enumerate(opens) if value == False]
        point += 100 * len(falses)
        label.config(text = "Tebrikler!\nPuanınız: {}".format(point))
        guess_button.config(state=tk.DISABLED)
        harf_al.config(state=tk.DISABLED)
        if not turn >= len(words) + 3:
            next_word_button.config(state=tk.ACTIVE)
        else:
            next_word_button.destroy()
    else:
        harf_al.config(state=tk.DISABLED)
        next_word_button.config(state=tk.ACTIVE)
        guess.delete(0, tk.END)
    
guess_button = tk.Button(root, text="Tahmin Et", command=lambda: guess_func(), font=("Arial", 20))
guess_button.pack()

def next_word_func():
    global turn
    global point
    global opens
    global show

    turn += 1
    question.config(text=words[turn]["soru"])
    opens = [False for i in range(turn)]
    show = " ".join(["_" for i in range(turn)])
    label.config(text=show)
    guess.delete(0, tk.END)
    next_word_button.config(state=tk.DISABLED)
    harf_al.config(state=tk.ACTIVE)
    guess_button.config(state=tk.ACTIVE)

next_word_button = tk.Button(
    root, text="Sonraki Kelime", command = lambda : next_word_func(), state= tk.DISABLED, font=("Arial", 20))
next_word_button.pack()

root.mainloop()