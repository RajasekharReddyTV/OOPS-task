import logging

#V1 = "this is My First Python programming class and i am learNING python string and its function"

"""Q1. Try to extract data from index one to index 300 with a jump of 3
Q2. Try to reverse a string without using reverse function
Q3. Try to split a string after conversion of entire string in uppercase
Q4.Try to convert the whole string into lower case
Q5. Try to capitalize the whole string
Q6. Write difference between isalnum() and isalpha()
Q7. Tru to give an example of expand tab
Q8. Give an example of strip, lstrip and rstrip
Q9. Replace a string charecter by another charector by taking your own example"""

class String:
    logging.basicConfig(filename='String_log.log', level=logging.DEBUG,
                        format='%(levelname)s: %(name)s: %(asctime)s: %(message)s')

    def data_extract(self, data):
        """ Trying to extract the data from index 1 to 300 with jump of 3"""
        extracted_data = ''
        try:
            logging.info("Trying to extract the data with jump 3")
            extracted_data = data[:300:3]
            return extracted_data
        except Exception as e:
            logging.exception(e)

    def reverse_data(self, data):
        """ Trying to reverse the data without using reverse function"""
        reversed_data = ""
        try:
            logging.info("Trying to reverse the given string data ")
            reversed_data = data[::-1]
            return reversed_data
        except Exception as e:
            logging.exception(e)

    def Up_split(self, data):
        """ Trying to covert the data into upper case and spliting with spces"""
        list1 = []
        try:
            logging.info("Trying to convert into upper cases of the given string and spliting with spaces ")
            list1 = data.upper().split(" ")
            return list1
        except Exception as e:
            logging.exception(e)

    def Lower(self, data):
        """ Trying to covert the data into lower case"""
        Lower_data = ""
        try:
            logging.info("Trying to convert into lower cases of the given string")
            Lower_data = data.lower()
            return Lower_data
        except Exception as e:
            logging.exception(e)

    def Capitalse(self, data):
        """ Trying to capitalize the data"""
        Captalised_Data = ""
        try:
            logging.info("Trying to capitalize the given data")
            Captalised_Data = data.capitalize()
            return Captalised_Data
        except Exception as e:
            logging.exception(e)

    def alnum_alpha(self, data):
        """ This function will say about the given data is alnum or alpha """
        try:
            if data.isalnum():
                logging.info("Trying to check the given data us alnum")
                print(" Given data is alnum")
            elif data.isalpha():
                logging.info("Trying to check the given data us alnum")
                print("Given data is alpha")
            else:
                print(" Given data is either alnum or alpha")
        except Exception as e:
            logging.exception(e)

    def Expand(self, data):
        """ This function will expand the data withh expand tab "\t" """
        expand_data = ""
        try:
            logging.info("Trying to expand the data with \t" )
            expand_data = "\t".join(data)
            return expand_data
        except Exception as e:
            logging.exception(e)

    def Strip(self, data):
        """ This function will perfrom strip , lstrip, rstrip of given data"""
        strip_data = ""
        lstrip_data = ""
        rstrip_data = ""
        try:
            logging.info("Trying to make strip the data")
            strip_data = data.strip()
            lstrip_data = data.lstrip()
            rstrip_data = data.rstrip()
            return  strip_data , lstrip_data , rstrip_data
        except Exception as e:
            logging.exception(e)
    def Replace(self, data, replace_data):
        """ This function will try to perform replece the given data with replace_data"""
        replaced_Data = ""
        try:
            logging.info("trying to replace the data with replace_data")
            replaced_Data = data.replace(data, replace_data)
            return  replaced_Data
        except Exception as e:
            logging.exception(e)

    def str_cen(self, data, cen, qty):
        """ This function wiil try to place the data in b/w """
        str_cen_data = ""
        try:
            logging.info("Trying to keep given data in b/w quantity of passed charecters")
            str_cen_data = data.center(qty, cen)
            return  str_cen_data
        except Exception as e:
            logging.exception(e)


V1 = "this is My First Python programming class and i am learNING python string and its function"

String_var = String()
print(String_var.data_extract(V1))
print(String_var.reverse_data(V1))
print(String_var.Up_split(V1))
print(String_var.Lower(V1))
print(String_var.Capitalse(V1))
String_var.alnum_alpha(V1)
print(String_var.Expand(V1))
print(String_var.Strip("       This is task for OOPS concept          "))
print(String_var.Replace(V1, "Try to rplace with data with this data"))
print(String_var.str_cen("iNeuron", "*", 20))

#=============================================== End Of String Class ==========================================



"""#Questions on date of 21.05.2022:
l = [3,4,5,6,7 , [23,456,67,8,78,78] , [345,56,87,8,98,9] , (234,6657,6) , {"key1" :"sudh" , 234:[23,45,656]}] 
1 . Try to reverse a list
2. try to access 234 out of this list
3 . try to access 456 
4 . Try to extract only a list collection form list l 
5 . Try to extract "sudh" 
6 . Try to list all the key in dict element avaible in list 
7 . Try to extract all the value element form dict available in list"""


class List:
    logging.basicConfig(filename="List_Log.log", level= logging.DEBUG,
                        format="%(levelname)s: %(name)s: %(asctime)s:%(message)s")

    def Reverse_List(self, data):
        """This function will keep index in reverse order"""
        l1 = []
        try:
            logging.info("Trying to reverse the index of given list ")
            l1 = data[::-1]
            return  l1
        except Exception as e:
            logging.exception(e)

    def  Accesss_234(self, data):
        """This function will try to fetch 234 value from given list"""
        try:
            logging.info("Trying to fetch the 234 value in given list")
            return data[7][0]
        except Exception as e:
            logging.exception(e)

    def  Accesss_456(self, data):
        """This function will try to fetch 456 value from given list"""
        try:
            logging.info("Trying to fetch the 456 value in given list")
            return data[5][1]
        except Exception as e:
            logging.exception(e)

    def Extract_List(self, data):
        """ This function will try ti access list in given data"""
        l1 = []
        try:
            logging.info("Trying to extract list in given data")
            for i in data:
                if type(i)== list:
                    l1.append(i)
            return l1
        except Exception as e:
            logging.exception(e)

    def Extract_sudh(self, data ):
        """ This function will try to extract sudh from given data"""
        try:
            logging.info("Trying to extract sudh from given data")
            for i in data:
                if type(i)==dict:
                    for j, k in i.items():
                        if i[j]=="sudh":
                            return i[j]
        except Exception as e:
            logging.exception(e)

    def Extract_keys(self, data ):
        """ This function will try to extract keys from given data"""
        try:
            logging.info("Trying to extract keys from given data")
            for i in data:
                if type(i)==dict:
                    return i.keys()
        except Exception as e:
            logging.exception(e)

    def Extract_values(self, data ):
        """ This function will try to extract values from given data if there is dictionary """
        try:
            logging.info("Trying to extract value  from given data")
            for i in data:
                if type(i)==dict:
                    return i.values()
        except Exception as e:
            logging.exception(e)





l = [3,4,5,6,7 , [23,456,67,8,78,78] , [345,56,87,8,98,9] , (234,6657,6) , {"key1" :"sudh" , 234:[23,45,656]}]

List_var = List()
print(List_var.Reverse_List(l))
print(List_var.Accesss_234(l))
print(List_var.Accesss_456(l))
print(List_var.Extract_List(l))
print(List_var.Extract_sudh(l))
print(List_var.Extract_keys(l))
print(List_var.Extract_values(l))




"""Questions on 28.05.2022
q1 :
ineruon 
ineruon ineruon 
ineruon ineruon ineruon
ineruon ineruon ineruon ineruon

q2 - 

          ineruon
    ineruon      ineruon
ineruon		ineruon 	ineruon
	ineruon		 ineruon
		  ineruon

l1 = [[1,2,3,4] , (2,3,4,5,6) , (3,4,5,6,7) , set([23,4,5,45,4,4,5,45,45,4,5]) , {'k1' :"sudh" , "k2" : "ineuron","k3":
            "kumar" , 3:6 , 7:8} , ["ineuron" , "data science "]]

q3 : Try to extract all the list entity 
q4 : Try to extract all the dict enteties
q5 : Try to extract all the tuples entities
q6 : Try to extract all the numerical data it may b a part of dict key and values 
q7 : Try to give summation of all the numeric data 
q8 : Try to filter out all the odd values out all numeric data which is a part of a list 
q9 : Try to extract "ineruon" out of this data
q10 :Try to find out a number of occurances of all the data 
q11 : Try to find out number of keys in dict element
q12 : Try to filter out all the string data 
q13 : Try to Find  out alphanum in data
q14 : Try to find out multiplication of all numeric value in  the individual collection inside dataset 
q15 : Try to unwrape all the collection inside collection and create a flat list """


class for_loop:
    def patren1(self, NR):
        """ This function will create patren like
        ineruon
        ineruon ineruon
        ineruon ineruon ineruon
        ineruon ineruon ineruon ineruon"""

        try:
            logging.info("Trying to create patren1")
            for i in range(NR + 1):
                print("iNeuron " * i, end=" \n")
        except Exception as e:
            logging.exception(e)

    def patren2(self, NR, data):
        """ This function will create patren like
                             ineruon
                     ineruon      ineruon
                ineruon		ineruon 	  ineruon
	                 ineruon		 ineruon
		                     ineruon  """


        FH = NR
        SH = NR-1
        A = B = 0

        try:
            logging.info("Trying to create patren2")
            for i in range(FH):
                A = FH-(i+1)
                for j in range(A):
                    print(" "*len(data), end = "")
                for k in range(i+1):
                    print(data, end = " "*len(data))
                print(end = "\n")
            for l in range(SH):
                for m in range(l+1):
                    print(" "*len(data), end = "")
                B = SH-l
                for n in range(B):
                    print(data, end = " "*len(data))
                print(end = "\n")
        except Exception as e:
            logging.exception(e)

    def extract_list(self, data):
        """This function will try to extract all list data type in a given data"""
        l = []
        try:
            logging.info("Trying to extract list from data")
            for i in data:
                if type(i) == list:
                    l.append(i)
            return l
        except Exception as e:
            logging.exception(e)

    def extract_dict(self, data):
        """This function will try to extract all dict data type in a given data"""
        try:
            logging.info("Trying to extract dict items in a given data")
            for i in data:
                if type(i)==dict:
                    print(i)
        except Exception as e:
            logging.exception(e)

    def extract_tuple(self, data):
        """This function will try to extract all tuple data type in a given data"""
        try:
            logging.info("Trying to extract tuple elements in a given data")
            for i in data:
                if type(i)==tuple:
                    print(i)
        except Exception as e:
            logging.exception(e)

    def extract_numerics(self, data):
        """This function will try to extract all numeric data from given input"""

        l = []
        sum = 0
        try:
            logging.info("Trying to extract all numeric values from given input ")
            for i in data:
                if type(i) == list or type(i) == tuple or type(i) == set:
                    for j in i:
                        if type(j)==int:
                            l.append(j)
                if type(i)==dict:
                    for k , m in i.items():
                        if type(k)==int:
                            l.append(k)
                        if type(m) == int:
                            l.append(m)
            for n in l:
                sum = sum+n
            print(l)
            print(sum)
        except Exception as e:
            logging.exception(e)

    def extract_odd(self, data):
        """ Tis function will try to extract all odd values in given set of dAta"""
        l = []
        try:
            logging.info("Trying to extract all odd values from given input ")
            for i in data:
                if type(i) == list or type(i) == tuple or type(i) == set:
                    for j in i:
                        if type(j) == int:
                            if j%2!=0:
                                l.append(j)
                if type(i) == dict:
                    for k, m in i.items():
                        if type(k) == int:
                            if k % 2 != 0:
                                l.append(k)
                        if type(m) == int:
                            if m % 2 != 0:
                                l.append(m)
            print(l)
        except Exception as e:
            logging.exception(e)

    def extract_iNeuron(self, data):
        """ Tis function will try to extract iNeuron in given set of data"""
        l = []
        try:
            logging.info("Trying to extract iNeuron from given input ")
            for i in data:
                if type(i) == list or type(i) == tuple or type(i) == set:
                    for j in i:
                        if type(j) == str:
                            if j=="ineuron":
                                l.append(j)
                if type(i) == dict:
                    for k, m in i.items():
                        if type(k) == str:
                            if k =="ineuron":
                                l.append(k)
                        if type(m) == str:
                            if m =="ineuron":
                                l.append(m)
            print(l)
        except Exception as e:
            logging.exception(e)

    def extract_occurence(self, data):
        """This function will try to extract number of occurrence  of each numeric value from given input"""

        l = []
        try:
            logging.info("Trying to extract number of occurrences of each numeric dat from given input ")
            for i in data:
                if type(i) == list or type(i) == tuple or type(i) == set:
                    for j in i:
                        if type(j)==int:
                            l.append(j)
                if type(i)==dict:
                    for k , m in i.items():
                        if type(k)==int:
                            l.append(k)
                        if type(m) == int:
                            l.append(m)
            for n in set(l):
                print(n, ":", l.count(n))
        except Exception as e:
            logging.exception(e)

    def extrac_number_Keys(self, data):
        """This function will try to count number of keys  from given input"""
        sum=0
        try:
            logging.info("Trying to find out number of keys  from given input ")
            for i in data:
                if type(i)==dict:
                    for k in i:
                        sum = sum+1
            print("Number of keys: ",  sum)
        except Exception as e:
            logging.exception(e)



l1 = [[1,2,3,4] , (2,3,4,5,6) , (3,4,5,6,7) , set([23,4,5,45,4,4,5,45,45,4,5]) , {'k1' :"sudh" , "k2" : "ineuron","k3":
            "kumar" , 3:6 , 7:8},{'k1' :"sudh" , "k2" : "ineuron","k3":
            "kumar" , 3:6 , 7:8} , ["ineuron" , "data science "]]

For_Loop_Var = for_loop()
For_Loop_Var.patren1(5)
For_Loop_Var.patren2(4,"iNeuron")
print(For_Loop_Var.extract_list(l1))
For_Loop_Var.extract_dict(l1)
For_Loop_Var.extract_tuple(l1)
For_Loop_Var.extract_numerics(l1)
For_Loop_Var.extract_odd(l1)
For_Loop_Var.extract_iNeuron(l1)
For_Loop_Var.extract_occurence(l1)
For_Loop_Var.extrac_number_Keys(l1)


class while_loop:

    def patren1(self):
        """ This function will try to print following patern
*
* *
* * *
* * * *
* * * * *
* * * * * *
* * * * * * *
* * * * * * * *
* * * * * * * * *
        """
        try:
            logging.info("trying to print patren 1")
            i=0
            while i <8:
                print("* "*(i+1), end = "\n")
                i = i+1
        except Exception as e:
            logging.exception(e)

    def patren2(self):
        """ This function will try to print following patren
A
B H
C I N
D J o S
E K p T W
F L Q U X z
G M R V Y
        """
        try:
            logging.info("Trying to print patren 2")
            i = 1
            while i<=7:
                asc = 65+(i-1)
                j = 0
                while (j+1)<=i and asc<=90:
                    ch = chr(asc)
                    print(ch, end = " ")
                    j = j + 1
                    asc = asc + (7-j)
                print(end = "\n")
                i = i+1
        except  Exception as e:
            logging.exception(e)

    def div_40_400(self):
        """This function will try to print all numbers which are divisbale by 3 b/w 40 - 400"""
        try:
            i = 40
            logging.info("trying to print numbers which are divisible by 3 b/w 40 - 400")
            while i<=400:
                if i%3 == 0:
                    print(i)
                i = i+1
        except Exception as e:
            print(e)

    def extract_vowels(self, data):
        """ This function will try to extract vowels from given string data"""
        try:
            logging.info("Trying to extract vowels from given string data")
            data1 = data.lower()
            l = []
            i = 0
            vowels = ("a","e","i","o","u")
            while i<len(data1):
                if data1[i] in vowels:
                    l.append(data1[i])
                i = i+1
            return l
        except Exception as e:
            logging.exception(e)
    def extract_even(self, data):
        """ This function will try to extract all even numbers in given data """
        try:
            logging.info(" trying to extract even numbers from given data")
            i = 1
            l = []
            while i <= data:
                if i%2==0:
                    l.append(i)
                i = i+1
            return l
        except Exception as e:
            logging.exception(e)

    def get_time(self):
        """This function will try to fetch system time"""
        try:
            logging.info("try to fetch system time")
            import time
            CU_TIME = time.strftime("%I:%M:%S:%p",time.localtime())
            print(CU_TIME)
        except Exception as e:
            logging.exception(e)

    def get_date(self):
        """This funtion will try to fetch date from your system"""
        try:
            logging.info("Try to fetch date from system")
            import  time
            To_Date = time.strftime("%d:%m:%Y", time.localtime())
            print(To_Date)
        except Exception as e:
            logging.exception(e)

    def send_mail(self):
        """ This function will try to send mail to mentioned mailid's"""
        try:
            logging.info("Trying to send mail to mailid")
            import smtplib
            server = smtplib.SMTP("smtp.gmail.com",587)
            server.starttls()
            server.login('raja.buildmate@gmail.com',"admrybuipdxzmloi")
            server.sendmail('raja.buildmate@gmail.com','raja.profi@gmail.com','Test email from python')
            print("mail sent")
        except Exception as e:
            logging.exception(e)

    def alarm(self, Time):
        """ This function will try to blow alarm """
        try:
            logging.info("trying blow alarm")
            import time
            from playsound import playsound
            import os
            alarm_time = Time
            if time.strftime("%H:%M", time.localtime()) == alarm_time:
                logging.info("Time matched")
                playsound(r"C:\Users\Thimmapur\Music\alarm.mp3")
        except Exception as e:
            logging.exception(e)

    def get_ip(self):
        """ This function will try to get IP address of the PC"""
        try:
            logging.info("Trying to fetch IP address of the PC")
            import socket
            host = socket.gethostname()
            ip = socket.gethostbyname(host)
            print(ip)

        except Exception as e:
            logging.exception(e)

    def get_insoft(self):
        """ This function will try to fetch all installed softwares"""
        try:
            import winapps
            for app in winapps.list_installed():
                print(app)
        except Exception as e:
            logging.exception(e)

    def tts(self,data):
        """ This function will try to convert data from text to speech"""
        try:
            logging.info("Trying to convert text to speech")
            from gtts import gTTS
            from playsound import  playsound
            gts = gTTS(data)
            gts.save(r'C:\Users\Thimmapur\Music\hello.mp3')
            playsound(r'C:\Users\Thimmapur\Music\hello.mp3')
        except Exception as e:
            logging.exception(e)

    def open_image(self):
        """ This function will try to open image and show"""
        try:
            logging.info("trying to open an image")
            from PIL import Image
            im = Image.open(r"C:\Users\Thimmapur\Downloads\Image2.jpg")
            im.show()
        except Exception as e:
            logging.exception(e)

    def file_fol(self):
        """ This fuction will list out all the files in a specified folder"""

        try:
            logging.info("trying to list out all the files in a specified path")
            import os
            print(os.listdir("F:\\"))
        except Exception as e:
            logging.exception(e)


    def append_pdf(self, path):
        """ This function will try to append two PDF's """
        try:
            logging.info("trying merge pdf files")
            from PyPDF2 import PdfFileMerger
            merge = PdfFileMerger()
            for pdf_file in path:
                merge.append(pdf_file)
            merge.write(r"F:\pdf files\merged.pdf")
            merge.close()
        except Exception as e:
            logging.exception(e)


    def sort_word(self, path):
        """ This function will filter only word files """
        try:
            logging.info("Try to filter word files from given path")
            import fnmatch
            import os
            file = fnmatch.filter(os.listdir(path), "*.docx")
            print(file)
        except Exception as e:
            logging.exception(e)








while_var = while_loop()

while_var.patren1()
while_var.patren2()
while_var.div_40_400()
S = "Python is a high-level, interpreted, general-purpose programming language. Its design philosophy emphasizes code readability with the use of significant indentation.[32]"
print(while_var.extract_vowels(S))
print(while_var.extract_even(1000))
while_var.get_time()
while_var.get_date()
#while_var.send_mail()
#while_var.alarm("20:02")
while_var.get_ip()
while_var.get_insoft()
#while_var.tts(S)
#while_var.open_image()
while_var.file_fol()
while_var.append_pdf([r"F:\pdf files\pdf1-pag1.pdf", r"F:\pdf files\pdf2-pag2.pdf"])
while_var.sort_word(r"F:\pdf files")








