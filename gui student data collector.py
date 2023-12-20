from tkinter import *
root = Tk()
root.geometry("500x500")
def calculation():
    
    na = sn_en.get()
    roll = sroll_en.get()
    seme1 = se1_en.get()
    seme2 = se2_en.get()
    seme3 = se3_en.get()
    seme4 = se4_en.get()
    seme5 = se5_en.get()
    seme6 = se6_en.get()
    seme7 = se7_en.get()
    seme8 = se8_en.get()

    total_semester_mark = eval(seme1)+eval(seme2)+eval(seme3)+eval(seme4)+eval(seme5)+eval(seme6)+eval(seme7)+eval(seme8)
    average = total_semester_mark/8
    if average >= 20.0:
        student_report = "Pass" 
    else:
        student_report = "Fail"
    
    

    #DROPOUT STUDENT COUNT
    if student_report == "Pass":
        student_dropout = 0
    else:
        student_dropout = 1

    


sn = Label(root,text = "StudentName :")
sn.pack()
sn_en = Entry(root,width = 30)
sn_en.pack()

sroll = Label(text ="RollNo :")
sroll.pack()
sroll_en = Entry(root, width=30)
sroll_en.pack()

se_1 = Label(root,text = "Semester 1 :")
se_1.pack()
se1_en = Entry(root,width = 30)
se1_en.pack()

se_2= Label(root,text = "Semester 2 :")
se_2.pack()
se2_en = Entry(root,width = 30)
se2_en.pack()

se_3= Label(root,text = "Semester 3 :")
se_3.pack()
se3_en = Entry(root,width = 30)
se3_en.pack()

se_4= Label(root,text = "Semester 4 :")
se_4.pack()
se4_en = Entry(root,width = 30)
se4_en.pack()

se_5= Label(root,text = "Semester 5 :")
se_5.pack()
se5_en = Entry(root,width = 30)
se5_en.pack()

se_6= Label(root,text = "Semester 6 :")
se_6.pack()
se6_en = Entry(root,width = 30)
se6_en.pack()

se_7= Label(root,text = "Semester 7 :")
se_7.pack()
se7_en = Entry(root,width = 30)
se7_en.pack()

se_8= Label(root,text = "Semester 8 :")
se_8.pack()
se8_en = Entry(root,width = 30)
se8_en.pack()











bu_1 = Button(root, text = 'Save', command=calculation)
bu_1.pack()


root.mainloop()