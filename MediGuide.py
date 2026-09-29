import tkinter  as tk
from tkinter import ttk, messagebox

root=tk.Tk()
root.title("MEDIGUIDE")
root.geometry("600x700")


page1=tk.Frame(root)
page2=tk.Frame(root)

label_page1=tk.Label(page1,text="MEDIGUIDE\nPersonal Health Information Assistant",font="Arial")
label_page1.grid(row=0 ,column=2)
label_log=tk.Label(page1,text="LOGIN",font=7).grid(row=2,column=2,pady=10)
page1.place(relwidth=1,relheight=1)
labe=tk.Label(page1,text="Name:")
labe.grid(row=4,column=1,padx=10)
labe1=tk.Label(page1,text="Contact Number:")
labe1.grid(row=5 ,column=1,padx=10)
labe2=tk.Label(page1, text="EMail Address:").grid(row=6,column=1,padx=10)
entr=tk.Entry(page1,width=50)
entr.grid(row=4 ,column=2)
entr1=tk.Entry(page1,width=50)
entr1.grid(row=5 ,column=2)
ent2=tk.Entry(page1,width=50)
ent2.grid(row=6,column=2)

def submit():
        name=entr.get()
        num=entr1.get()
        add=ent2.get()
        if name=="" :
           messagebox.showwarning("Missing Information", "Please Enter Your Name")
           return
        if num=="":
           messagebox.showwarning("Missing Information", "Please Enter Your Contact Number")
           return
        if add=="":
           messagebox.showwarning("Missing Information", "Please Enter Your Email Address")
           return
        if not num.isdigit():
           messagebox.showwarning("Missing Information", "Please Enter Only Numbers")
           return
        if len(num)!=10:
           messagebox.showwarning("Missing Information", "Please Enter 10 digit number.")
           return
        page2.tkraise()
tk.Button(page1,text="Continue",command=submit).grid(row=7,column=2,padx=20,pady=10)

page2.place(relwidth=1,relheight=1)
label_page2=tk.Label(page2,text="WELCOME TO MEDIGUIDE\nHOME PAGE",font=("Arial",28))
label_page2.pack(pady=16)


page3=tk.Frame(root)
page4=tk.Frame(root)
page5=tk.Frame(root)
page6=tk.Frame(root)
page7=tk.Frame(root)
page8=tk.Frame(root)
page9=tk.Frame(root)
symp_button = tk.Button(page2,text="Symptom Analysis",command=page3.tkraise,font=16)
symp_button.pack(pady=10,padx=10)
app_button = tk.Button(page2,text="Appointment", command=page4.tkraise,font=16)
app_button.pack(pady=10,padx=10)
health_button = tk.Button(page2,text="Health Information",command=page5.tkraise,font=16)
health_button.pack(pady=10,padx=10)
about_button=tk.Button(page2,text="About Us", command=page6.tkraise,font=16)
about_button.pack(pady=10,padx=10)

page4.place(relwidth=1,relheight=1)
page4_label=tk.Label(page4,text="APPOINTMENT",font=("Arial",26))
page4_label.pack()
page4_fram=tk.Frame(page4)
page4_fram.pack()
doc_nam=tk.Label(page4_fram,text="Doctor:").grid(row=0,column=0,pady=10)
doctor=ttk.Combobox(page4_fram,values=["Pulmonologist","Gastroenlogist","Dermatologist"],state="readonly")
doctor.grid(row=0,column=1,pady=10)
tk.Label(page4_fram,text="Date:").grid(row=1,column=0,pady=10)
entry=tk.Entry(page4_fram)
entry.grid(row=1,column=1,pady=10)
tk.Label(page4_fram,text="Time:").grid(row=2,column=0,pady=10)
time=ttk.Combobox(page4_fram,values=["08:00am","10:00am","02:00pm","04:00pm"])
time.grid(row=2,column=1,pady=10)
def mistake():
        tim=time.get()
        doc=doctor.get()
        date=entry.get()
        if date=="":
         messagebox.showwarning("Missing Information","Please Enter the Date") 
         return
        
        if doc=="":
         messagebox.showwarning("Missing Information","Please Select according to the disease.") 
         return
        if tim=="":
         messagebox.showwarning("Missing Information","Please Select Appoinment.") 
         return
        messagebox.showinfo("APPOINTMENT",f"The request have been recorded.\n"
                            f"Doctor:{doc}\n"f"Date:{date}.\n"f"Time:{tim}.\n"
                            f"Till the appointment take care of your Health.\n"
                            f"Thank You")
        
tk.Button(page4,text="Book Appointment",command=mistake).pack(pady=10)
tk.Button(page4,text="Back to Home",command=page2.tkraise).pack(pady=10)

page5.place(relwidth=1,relheight=1)
tk.Label(page5,text="HEALTH INFORMATION",font="Arial").pack()


health_text = """
General Health Information

1. Maintain a balanced diet.

2. Drink adequate water according to
   your individual needs.

3. Maintain regular physical activity.

4. Get adequate sleep.

5. Maintain good personal hygiene.

6. Avoid smoking and exposure to
   harmful substances.

7. Seek professional medical advice
   when symptoms are severe, persistent,
   or concerning.

Emergency symptoms such as severe
difficulty breathing, severe chest pain,
loss of consciousness, or other serious
conditions require prompt medical attention.
"""


tk.Label(page5,text=health_text,font="Arial",justify="left").pack()
tk.Button(page5,text="Back to Home",command=page2.tkraise).pack()

page6.place(relwidth=1,relheight=1)
tk.Label(page6,text="About MediGuide",font="Arial").pack()
about_text = """
MEDIGUIDE

Personal Health Information Assistant

MEDIGUIDE is a Python Tkinter educational
project designed to demonstrate:

• GUI design
• Patient information collection
• Input validation
• Checkbuttons
• Radiobuttons
• Comboboxes
• Scales
• Dictionaries
• Functions
• Page navigation
• Basic symptom matching

The symptom analysis feature uses a simple
rule-based matching approach.

It is intended only as a demonstration
project and should not be used for
medical diagnosis.
"""
tk.Label(page6,text=about_text,font=("Arial", 12)).pack(padx=50)


tk.Button(page6,text="Back to Home",command=page2.tkraise).pack()
diseases = {
    "Respiratory": {"Common Cold": ["Cough","Runny Nose","Sneezing","Sore Throat"]
        ,"Influenza": ["Fever","Cough","Headache","Muscle Pain","Fatigue"]
        ,"Asthma": ["Wheezing","Shortness of Breath","Chest Tightness","Cough"]
        ,"Bronchitis": ["Cough","Mucus","Fatigue","Chest discomfort"]
        ,"Pneumonia": ["Cough","Fever","Chest Pain","Shortness of Breath"]}

    ,"Digestive": {
        "Indigestion": ["Stomach discomfort","Heartburn","Bloating"]
        ,"Food Poisoning": ["Stomach Pain","Nausea","Diarrhea","Vomiting"]
        ,"Gastritis":["Stomach Pain","Nausea","Bloating","Indigestion"]}

    ,"Skin": {"Acne": ["Pimples","Blackheads","Oily Skin"]
        ,"Eczema": ["Itchy Skin","Dry Skin","Red Skin","Rash"]
        ,"Ringworm": ["Itchy Skin","Circular Rash","Red Skin"]}}


page3.place(relwidth=1,relheight=1)
pag3_lab=tk.Label(page3,text="SYMPTOM ANALYSIS",font=("Arial",26))
pag3_lab.pack(pady=10)
page3_lab=tk.Label(page3,text="Select The Category Related To Your Symptoms",font="bold")
page3_lab.pack(pady=10)
respi=tk.Button(page3,text="RESPIRATORY",command=page7.tkraise)
respi.pack(pady=10)
diges=tk.Button(page3,text="DIGESTIVE",command=page8.tkraise)
diges.pack(pady=10)
skin=tk.Button(page3,text="Skin",command=page9.tkraise)
skin.pack(pady=10)
back=tk.Button(page3,text="Back to Home",command=page2.tkraise)
back.pack(pady=10)
#respiratory Section

page7.place(relwidth=1, relheight=1)

page7_lab=tk.Label(page7,text="Respiratory Health Questionnaire",font=("Arial",20)).pack(pady=10)

page7_=tk.Label(page7,text="How long have you had these symptoms?",font="bold").pack(pady=10)

duration = ttk.Combobox(page7,values=["1 day","2-3 days","4-7 days",
                                      "More than 1 week"],state="readonly")
duration.pack()

tk.Label(page7,text="What type of cough do you have?").pack(pady=10)

cough_type = tk.StringVar()

tk.Radiobutton(page7,text="Dry",variable=cough_type,value="Dry").pack()

tk.Radiobutton(page7,text="With mucus",variable=cough_type,value="With mucus").pack()

cough=tk.BooleanVar()
run=tk.BooleanVar()
snee=tk.BooleanVar()
sour=tk.BooleanVar()
fev=tk.BooleanVar()
hea=tk.BooleanVar()
mus=tk.BooleanVar()
fat=tk.BooleanVar()
wheez=tk.BooleanVar()
shor=tk.BooleanVar()
ch=tk.BooleanVar()
muc=tk.BooleanVar()
ch_dis=tk.BooleanVar()
ch_pain=tk.BooleanVar()


tk.Label(page7,text="What Symptoms You Have Observed.").pack(pady=8)
tk.Checkbutton(page7,text="Cough",variable=cough).pack()
tk.Checkbutton(page7,text="Runny Nose",variable=run).pack()
tk.Checkbutton(page7,text="Sneezing",variable=snee).pack()
tk.Checkbutton(page7,text="Sore Throat",variable=sour).pack()
tk.Checkbutton(page7,text="Headache",variable=hea).pack()
tk.Checkbutton(page7,text="Muscle Pain",variable=mus).pack()
tk.Checkbutton(page7,text="Fatigue",variable=fat).pack()
tk.Checkbutton(page7,text="Mucus",variable=muc).pack()
tk.Checkbutton(page7,text="Chest Pain",variable=ch_pain).pack()
tk.Checkbutton(page7,text="Chest discomfort",variable=ch_dis).pack()
tk.Checkbutton(page7,text="Fever",variable=fev).pack()
tk.Checkbutton(page7,text="Wheezing",variable=wheez).pack()
tk.Checkbutton(page7,text="Shortness of Breath",variable=shor).pack()
tk.Checkbutton(page7,text="Chest Tightness",variable=ch).pack()

def analyse1():
        user=[]
        if cough.get():
            user.append("Cough")
        if run.get():
            user.append("Runny Nose")
        if snee.get():
            user.append("Sneezing")
        if fat.get():
            user.append("Fatigue")
        if muc.get():
            user.append("Mucus")
        if sour.get():
            user.append("Sore Throat")
        if hea.get():
            user.append("Headache")
        if mus.get():
            user.append("Muscle Pain")
        if ch_pain.get():
            user.append("Chest Pain")
        if ch_dis.get():
            user.append("Chest discomfort")
        if fev.get():
            user.append("Fever")
        if wheez.get():
            user.append("Wheezing")
        if shor.get():
            user.append("Shortness of Breath")
        if ch.get():
            user.append("Chest Tightness")
        if len(user)==0:
          messagebox.showwarning("No Symptoms", "Feel free to express from what you are suffering,\n so we can help you")
          return
        duration_value = duration.get()
        cough_value = cough_type.get()

        if duration_value == "":
         messagebox.showwarning("Missing Information","Please select the duration.")
         return


        if cough.get() and cough_value == "":
         messagebox.showwarning("Missing Information","Please select the cough type.")
         return
        name=entr.get()
        num=entr1.get()
        

        result=""
       
        for disease, disease_symp in diseases["Respiratory"].items():

    
          common=set(user)&set(disease_symp)
          per=(len(common)/len(disease_symp))*100
          result=result+f"{disease}: {per:.1f}%\n"

        messagebox.showinfo("RESULT",f"Name of Patient: {name}\nContact Number: {num}\nDuration: {duration_value}\nCough Type: {cough_value}\nSelected Symptoms: {",".join(user)}\nPossible Symtom Matches: {result}\nPlease take Precautions as mentined in Medical Information Section.")

tk.Button(page7,text="Analyse",command=analyse1).pack(padx=10,pady=5)
tk.Button(page7,text="Back",command=page3.tkraise).pack(padx=10,pady=5)
#Digestive Section

page8.place(relwidth=1, relheight=1)

page8_lab=tk.Label(page8,text="Digestive Health Questionnaire",font=("Arial",26)).pack(pady=10)


page8_=tk.Label(page8,text="How long have you had these symptoms?",font="bold").pack(pady=10)

duration_1 = ttk.Combobox(page8,values=["2-3 days","4-7 days",
                                      "More than 1 week","You have digetion problem from earlier"],state="readonly")
duration_1.pack()

bloat=tk.BooleanVar()
heartb=tk.BooleanVar()
stom_dis=tk.BooleanVar()
vomit=tk.BooleanVar()
diarr=tk.BooleanVar()
stom_pain=tk.BooleanVar()
naus=tk.BooleanVar()
indiges=tk.BooleanVar()


tk.Label(page8,text="What Symptoms You Have Observed.").pack(pady=8)
tk.Checkbutton(page8,text="Bloating",variable=bloat).pack()
tk.Checkbutton(page8,text="Heartburn",variable=heartb).pack()
tk.Checkbutton(page8,text="Stomach discomfort",variable=stom_dis).pack()
tk.Checkbutton(page8,text="Vomiting",variable=vomit).pack()
tk.Checkbutton(page8,text="Diarrhea",variable=diarr).pack()
tk.Checkbutton(page8,text="Stomach Pain",variable=stom_pain).pack()
tk.Checkbutton(page8,text="Nausea",variable=naus).pack()
tk.Checkbutton(page8,text="Indigestion",variable=indiges).pack()

def analyse2():
        user=[]
        if bloat.get():
            user.append("Bloating")
        if heartb.get():
            user.append("Heartburn")
        if stom_dis.get():
            user.append("Stomach discomfort")
        if vomit.get():
            user.append("Vomiting")
        if diarr.get():
            user.append("Diarrhea")
        if stom_pain.get():
            user.append("Stomach Pain")
        if naus.get():
            user.append("Nausea")
        if indiges.get():
            user.append("Indigestion")
        
        if len(user)==0:
          messagebox.showwarning("No Symptoms", "Feel free to express from what you are suffering,\n so we can help you")
          return
        duration_value = duration_1.get()

        if duration_value == "":
         messagebox.showwarning("Missing Information","Please select the duration.")
         return

        name=entr.get()
        num=entr1.get()
        

        result=""
       
        for disease, disease_symp in diseases["Digestive"].items():

    
          common=set(user)&set(disease_symp)
          per=(len(common)/len(disease_symp))*100
          result=result+f"{disease}: {per:.1f}%\n"

        messagebox.showinfo("RESULT",f"Name of Patient: {name}\nContact Number: {num}\nDuration: {duration_value}\nSelected Symptoms: {",".join(user)}\nPossible Symtom Matches: {result}\nPlease take Precautions as mentined in Medical Information Section.")

tk.Button(page8,text="Analyse",command=analyse2).pack(padx=10,pady=5)
tk.Button(page8,text="Back",command=page3.tkraise).pack(padx=10,pady=5)
#Skin Section

page9.place(relwidth=1, relheight=1)

page9_lab=tk.Label(page9,text="Skin Questionnaire",font=("Arial",26)).pack(pady=10)


page9_=tk.Label(page9,text="How long have you had these symptoms?",font="bold").pack(pady=10)

duration_2 = ttk.Combobox(page9,values=["since Childhood","1 week", "More than 1 week"],state="readonly")
duration_2.pack()

pimp=tk.BooleanVar()
black=tk.BooleanVar()
oily=tk.BooleanVar()
itchy=tk.BooleanVar()
dry=tk.BooleanVar()
red=tk.BooleanVar()
rash=tk.BooleanVar()
cir_rash=tk.BooleanVar()


tk.Label(page9,text="What Symptoms You Have Observed.").pack(pady=8)
tk.Checkbutton(page9,text="Pimples",variable=pimp).pack()
tk.Checkbutton(page9,text="Blackheads",variable=black).pack()
tk.Checkbutton(page9,text="Oily Skin",variable=oily).pack()
tk.Checkbutton(page9,text="Itchy Skin",variable=itchy).pack()
tk.Checkbutton(page9,text="Dry Skin",variable=dry).pack()
tk.Checkbutton(page9,text="Red Skin",variable=red).pack()
tk.Checkbutton(page9,text="Rash",variable=rash).pack()
tk.Checkbutton(page9,text="Circular Rash",variable=cir_rash).pack()

def analyse3():
        user=[]
        if pimp.get():
            user.append("Pimples")
        if black.get():
            user.append("Blackheads")
        if oily.get():
            user.append("Oily Skin")
        if itchy.get():
            user.append("Itchy Skin")
        if dry.get():
            user.append("Dry Skin")
        if red.get():
            user.append("Red Skin")
        if rash.get():
            user.append("Rash")
        if cir_rash.get():
            user.append("Circular Rash")
        
        if len(user)==0:
          messagebox.showwarning("No Symptoms", "Feel free to express from what you are suffering,\n so we can help you")
          return
        duration_value = duration_2.get()

        if duration_value == "":
         messagebox.showwarning("Missing Information","Please select the duration.")
         return

        name=entr.get()
        num=entr1.get()
        result=""
       
        for disease, disease_symp in diseases["Skin"].items():

    
          common=set(user)&set(disease_symp)
          per=(len(common)/len(disease_symp))*100
          result=result+f"{disease}: {per:.1f}%\n"

        messagebox.showinfo("RESULT",f"Name of Patient: {name}\nContact Number: {num}\nDuration: {duration_value}\nSelected Symptoms: {",".join(user)}\nPossible Symtom Matches: {result}\nPlease take Precautions as mentined in Medical Information Section.")

tk.Button(page9,text="Analyse",command=analyse3).pack(padx=10,pady=5)
tk.Button(page9,text="Back",command=page3.tkraise).pack(padx=10,pady=5)
        


page1.tkraise()
root.mainloop()
