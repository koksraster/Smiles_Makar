from tkinter import *
root= Tk()
root.title("Прекрасная_улыбка_Макара")

class App(Frame):
	def __init__(self,master):
		super().__init__(master)
		self.grid()
		self.create_widgets()

	def create_widgets(self):
		Label(self, text = "Введи значение,сынок:").grid(row = 0, column = 0, columnspan = 2, sticky = W)
		self.user_text = Entry(self)
		self.user_text.grid(row = 1, column = 0, sticky = W )

		Button(self, text = "Получить результат:", command = self.result).grid(row = 2,column = 0,sticky = W)
		self.txt = Text(self, width = 75, height = 10, wrap = WORD)
		self.txt.grid(row = 3, column = 0, columnspan = 4)

	def result(self):
		user_text = self.user_text.get()
		answer = ""

		for i in user_text[::-1]:
			answer+=i

		answer = answer.capitalize()
		self.txt.delete(0.0, END)
		self.txt.insert(0.0, answer)

app = App(root)
root.mainloop()
