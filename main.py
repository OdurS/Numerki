import tkinter as tk
import aufrufe as a

def main():
    """bei starten des Programms wird eine Benutzeroberfläche mit 3 Knöpfen erstellt
    """
    root = tk.Tk()
    root.title("Matrix Auswahl - Gauss Jordan")
    root.geometry("300x200")

    label = tk.Label(root, text="Bitte Auswahl treffen:", font=("Arial", 12))
    label.pack(pady=10)

    button_A1 = tk.Button(root, text="A1", width=15, command=a.Beispiel_1)
    button_A1.pack(pady=5)

    button_A2 = tk.Button(root, text="A2", width=15, command=a.Beispiel_2 )
    button_A2.pack(pady=5)

    button_manual = tk.Button(root, text="Manuelle Eingabe", width=15,command=a.manual_auswahl)
    button_manual.pack(pady=5)

    root.mainloop()

if __name__ == "__main__":
    main()
