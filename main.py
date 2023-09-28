from tkinter import *
#from tkinter import ttk
# PIL import Image, 

def update():
    global text
  #while True:
    a = text.get('1.0', END).strip().lower()
    if a == 'mo':
      canvas.itemconfig(contain, image=new_image1)
    elif a == 'katie':
      canvas.itemconfig(contain, image=new_image2)
    elif a == 'gerald':
      canvas.itemconfig(contain, image=new_image3)
    elif a == 'charlotte':
      canvas.itemconfig(contain, image=new_image4)
    else:
      print('Invalid name')
      pass
    #continue
  
window = Tk()
window.geometry('450x450')

text = Text(window, height=2, width=20)
text.pack()

button = Button(window, text='Find', command=lambda:update())
button.pack()

canvas = Canvas(window, height=200, width=200)
canvas.pack()

photo =PhotoImage(file='.tutorial/Guess Who/katie.png')
photo = photo.subsample(3)
  
new_image1 = PhotoImage(file='.tutorial/Guess Who/mo.png')
new_image1 = new_image1.subsample(3)
new_image2 = PhotoImage(file='.tutorial/Guess Who/katie.png')
new_image2 = new_image2.subsample(3)
new_image3 = PhotoImage(file='.tutorial/Guess Who/gerald.png')
new_image3 = new_image3.subsample(3)
new_image4 = PhotoImage(file='.tutorial/Guess Who/charlotte.png')
new_image4 = new_image4.subsample(3)

contain = canvas.create_image(100, 100, image=photo)
  
window.mainloop()