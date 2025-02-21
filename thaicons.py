import tkinter as tk
import random

# List of all Thai consonants with their names
thai_consonants = [
    ("ก", "Gor Gai"), ("ข", "Kho Khai"), ("ฃ", "Kho Khuat"),
    ("ค", "Kho Khwai"), ("ฅ", "Kho Khon"), ("ฆ", "Kho Rakhang"),
    ("ง", "Ngo Ngu"), ("จ", "Jo Jan"), ("ฉ", "Cho Ching"),
    ("ช", "Cho Chang"), ("ซ", "So So"), ("ฌ", "Cho Cho"),
    ("ญ", "Yo Ying"), ("ฎ", "Do Chada"), ("ฏ", "To Patak"),
    ("ฐ", "Tho Than"), ("ฑ", "Tho Montho"), ("ฒ", "Tho Phu Thao"),
    ("ณ", "No Nen"), ("ด", "Do Dek"), ("ต", "To Tao"),
    ("ถ", "Tho Thung"), ("ท", "Tho Thahan"), ("ธ", "Tho Thong"),
    ("น", "No Nu"), ("บ", "Bo Baimai"), ("ป", "Po Pla"),
    ("ผ", "Pho Phung"), ("ฝ", "Fo Fa"), ("พ", "Pho Phan"),
    ("ฟ", "Fo Fan"), ("ภ", "Pho Samphao"), ("ม", "Mo Ma"),
    ("ย", "Yo Yak"), ("ร", "Ro Rua"), ("ฤ", "Rue"),
    ("ล", "Lo Ling"), ("ฦ", "Lue"), ("ว", "Wo Waen"),
    ("ศ", "So Sala"), ("ษ", "So Rusi"), ("ส", "So Sua"),
    ("ห", "Ho Hip"), ("ฬ", "Lo Chula"), ("อ", "O Ang"),
    ("ฮ", "Ho Nokhuk")
]

class FlashcardApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Thai Consonant Flashcards")
        
        self.card_frame = tk.Frame(root, padx=20, pady=20, bg="white", relief=tk.RAISED, bd=3)
        self.card_frame.pack(pady=50)
        
        self.label = tk.Label(self.card_frame, text="", font=("Arial", 50), bg="white")
        self.label.pack()
        
        self.flip_button = tk.Button(root, text="Flip", command=self.flip_card, font=("Arial", 14))
        self.flip_button.pack(pady=10)
        
        self.next_button = tk.Button(root, text="Next", command=self.next_card, font=("Arial", 14))
        self.next_button.pack(pady=10)
        
        self.is_flipped = False
        self.current_card = None
        self.next_card()
    
    def next_card(self):
        self.current_card = random.choice(thai_consonants)
        self.label.config(text=self.current_card[0])
        self.is_flipped = False
    
    def flip_card(self):
        if self.is_flipped:
            self.label.config(text=self.current_card[0])
        else:
            self.label.config(text=self.current_card[1])
        self.is_flipped = not self.is_flipped

if __name__ == "__main__":
    root = tk.Tk()
    app = FlashcardApp(root)
    root.mainloop()