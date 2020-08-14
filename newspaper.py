from tkinter import *
from PIL import ImageTk, Image

#TODO:change line after 100 characters

def newline(text):
    final_text=""
    for i in range(0, len(text)):
        final_text+=text[i]
        if i%100==0 and i!=0:
            final_text+="\n"
    return final_text



root=Tk()
root.title("Local Voice")
root.geometry("900x700")
root.minsize(900,700)
root.maxsize(900,700)

heading=Frame(root,height=100, width=800)
heading.pack()
Label(heading, text="Vocal for Local", font="lucida 33 bold", padx=10, pady=5).pack()
Label(heading, text="13 August 2020", font="lucida 12 bold").pack()



#list of texts
texts=[]
for i in range(1,4):
    with open(f"txt{i}.txt", encoding="utf8") as f:
        text = f.read()
        texts.append(newline(text))

photos=[]
for i in range(1,4):
    img=Image.open(f"img{i}.jpg")
    # TODO:resize image
    img = img.resize((150, 150), Image.ANTIALIAS)
    photo=ImageTk.PhotoImage(img)
    photos.append(photo)

frames=[]
for i in range(0,3):
    f=Frame(root, height=200, width=900, padx=10, pady=10)
    f.pack(anchor="w", fill=X)
    frames.append(f)


for i in range(0,3):
    Label(frames[i], text=texts[i]).pack(side="left")
    Label(frames[i], image=photos[i],anchor="e").pack()
root.mainloop()