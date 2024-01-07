from tkinter import *

def info():
    infobut.grid_forget()
    def close():
        infobut.grid(row=0,column=3)
        labelinfo.grid_forget()
        closebut.grid_forget()
        entry0.grid(row=0,column=0)
        entry1.grid(row=1,column=0)
        entry2.grid(row=2,column=0)
        entry3.grid(row=3,column=0)
        submit_button.grid(row = 4,columnspan=1)
    labelinfo = Label(wn,text='Welcome to Units converter. Units converter offers many units to convert.\n Below is a list of them. Be careful bc all the\n units NEED to be written in a singular form and in\n all lowercase. Here is the list:\n fahrenheit \n celsius \n kilometer \n centimeter \n meter \n dollar \n pound sterling \n great british pound \n czech crown \n euro \n Keep in mind that all of these that are listed above are written correctly...',font=('consolas',20))
    entry0.grid_forget()
    entry1.grid_forget()
    entry2.grid_forget()
    entry3.grid_forget()
    submit_button.grid_forget()
    labelinfo.grid(row=0,columnspan=1)
    closebut = Button(text='CLOSE',font=('Arial',20),command=close)
    closebut.grid(columnspan=1)

def FtoC(F):
    equation = (F-32)*5/9
    entry3.delete(0,END)
    entry3.insert(True,f'{equation} degrees F')

def CtoF(C):
    equation = C/ 5/9 + 32
    entry3.delete(0,END)
    entry3.insert(True,f'{equation} degrees C')

def kmTocm(KM):
    equation = KM * 100000
    entry3.delete(0,END)
    entry3.insert(True,f'{equation} cm')


def kmTom(KM):
    equation = KM * 1000
    entry3.delete(0,END)
    entry3.insert(True,f'{equation} m')

def mToKm(M):
    equation = M / 1000
    entry3.delete(0,END)
    entry3.insert(True,f'{equation} KM')

def mTocm(M):
    equation = M * 100
    entry3.delete(0,END)
    entry3.insert(True,f'{equation} cm')

def cmTom(CM):
    equation = CM / 100
    entry3.delete(0,END)
    entry3.insert(True,f'{equation} m')

def cmTokm(CM):
    equation = CM / 100000
    entry3.delete(0,END)
    entry3.insert(True,f'{equation} KM')

def BPSToCZK(PS):
    equation = PS * 28.64
    entry3.delete(0,END)
    entry3.insert(True,f'{equation} CZK')

    
def BPSToUSD(PS):
    equation = PS * 1.27
    entry3.delete(0,END)
    entry3.insert(True,f'{equation} USD')
def BPSToEUR(PS):
    equation = PS * 1.16
    entry3.delete(0,END)
    entry3.insert(True,f'{equation} EUR')

def EUROToUSD(EUR):
    equation = EUR * 1.10
    entry3.delete(0,END)
    entry3.insert(True,f'{equation} USD')

def EUR0ToGBPS(EUR):
    equation = EUR * 0.86
    entry3.delete(0,END)
    entry3.insert(True,f'{equation} british pounds')

def EURToCZK(EUR):
    equation = EUR * 24.66
    entry3.delete(0,END)
    entry3.insert(True,f'{equation} CZK')


def USDToEUR(USD):
    equation = USD / 1.10
    entry3.delete(0,END)
    entry3.insert(True,f'{equation} USD')

def USDToCZK(USD):
    equation = USD * 22.51
    print(equation)
    entry3.delete(0,END)
    entry3.insert(True,f'{equation} CZK')

def USDToBPS(USD):
    equation = USD / 1.27
    entry3.delete(0,END)
    entry3.insert(True,f'{equation} USD')

def CZKToUSD(CZK):
    equation = CZK / 22.51
    entry3.delete(0,END)
    entry3.insert(True,f'{equation} USD')

def CZKToEUR(CZK):
    equation = CZK / 24.66
    entry3.delete(0,END)
    entry3.insert(True,f'{equation} EUR')

def CZKToBSP(CZK):
    equation = CZK / 28.64
    entry3.delete(0,END)
    entry3.insert(True,f'{equation} CZK')

def convert():
    try:
        textV = int(entry0.get())
        textV1 = str(entry1.get())
        textV2 = str(entry2.get())
        
        if textV and textV1 and textV2:
            print('Gotta')

        if textV1.lower() == 'fahrenheit' and textV2.lower() == 'celsius':
            FtoC(textV)
        elif textV1.lower() == 'celsius' and textV2.lower() == 'fahrenheit':
            CtoF(textV)
        elif textV1.lower() == 'kilometer' and textV2.lower() == 'meter':
            kmTom(textV)
        elif textV1.lower() == 'kilometer' and textV2.lower() == 'centimeter':
            kmTocm(textV)
        elif textV1.lower() == 'meter' and textV2.lower() == 'kilometer':
            mToKm(textV)
        elif textV1.lower() == 'meter' and textV2.lower() == 'centimeter':
            mTocm(textV)
        elif textV1.lower() == 'centimeter' and textV2.lower() == 'kilometer':
            cmTokm(textV)
        elif textV1.lower() == 'centimeter' and textV2.lower() == 'meter':
            cmTom(textV)


        elif textV1.lower() == 'great british pound' or textV1.lower() == 'pound sterling' and textV2.lower() == 'dollar':
            BPSToUSD(textV)
        elif textV1.lower() == 'great british pound' or textV1.lower() == 'pound sterling' and textV2.lower() == 'czech crown':
            BPSToCZK(textV)
        elif textV1.lower() == 'great british pound' or textV1.lower() == 'pound sterling' and textV2.lower() == 'euro':
            BPSToEUR(textV)

        elif textV1.lower() == 'dollar' and textV2.lower() == 'pound sterling' or textV1.lower() == 'great british pound':
            USDToBPS(textV)
        elif textV1.lower() == 'dollar' and  textV2.lower() =='czech crown':
            USDToCZK(textV)
        elif textV1.lower() == 'dollar' and textV2.lower() == 'euro':
            USDToEUR(textV)

        
        elif textV1.lower() == 'czech crown' and textV2.lower() == 'pound sterling' or textV1.lower() == 'great british pound':
            CZKToBSP(textV)
        elif textV1.lower() == 'czech crown' and  textV2.lower() =='czech crown':
            CZKToUSD(textV)
        elif textV1.lower() == 'czech crown' and textV2.lower() == 'euro':
            CZKToEUR(textV)

        else:
            entry3.delete(0,END)
            entry3.insert(True,'Im afraid I cant help you with that.')


        

    except ValueError:
        entry2.insert(True,'SYNTAX ERROR')
        entry1.insert(True,'SYNTAX ERROR')
        entry0.insert(True,'SYNTAX ERROR')



wn = Tk()

entry0 = Entry(width=40,font=('Arial',20))
entry0.grid(row=0,column=0)
entry0.insert(True,'### Enter the value to convert ###')

entry1 = Entry(width=40,font=('Arial',20))
entry1.grid(row=1,column=0)
entry1.insert(True,'### Enter the unit you are converting ###')

entry2 = Entry(width=40,font=('Arial',20))
entry2.grid(row=2,column=0)
entry2.insert(True,'### Enter the unit it should be converted in ###')

entry3 = Entry(width=40,font=('Arial',20),state=NORMAL)
entry3.grid(row=3,column=0)
entry3.insert(True,'### DONT WRITE ANYTHING IN HERE!!! ###')

submit_button = Button(text='Convert',font=('Arial',20),command=convert)
submit_button.grid(row = 4,columnspan=1)

infobut = Button(text='INFO',font=('Arial',20),command=info)
infobut.grid(row = 0,column=3)

wn.mainloop()