#Question 1


class Validate:
    def password_validate(self,password):
        if len(password)<8:
            print("Invalid Password. Password must have atleast 8 characters. ")
        elif not any(char.isupper() for char in password):
            print("Invalid Password. Atleast one uppercase letter must be present. ")
        elif not any(char.islower() for char in password):
            print("Invalid Password. Atleast one lowercase letter must be present. ")
        elif not any(char.isdigit() for char in password):
            print("Invalid Password. Atleast one digit must be present. ")
        elif not any(char in "!@#$%^&*()-_=+[]{};:" "<>/?|" for char in password):
            print("Invalid Password. Atleast one special character  must be present. ")
        else:
            print("Valid Password")

password=input("Enter the password : ")
valid=Validate()
valid.password_validate(password)

#another method
class Password:
    def valid(text):
        upper=0
        lower=0
        digit=0
        special=0
        length=len(text)
        for i in text:
            if i.isupper():
                upper+=1
            elif i.islower():
                lower+=1
            elif i.isdigit():
                digit+=1
            else:
                special+=1
                
        if  upper>=1 and lower>=1 and digit>=1 and special>=1 and length>=8 and txt[0]==upper:
            print("Password is valid ")
        else:
            print("Invalid Password " )

txt=input("Enter string : ")
Password.valid(txt)

    


#Question 2

class TextProcessor:
    def __init__(self,text):
        self.text=text
        self.sentence=[]
    def split_into_sentences(self):
        special_char=['.','!','?']
        sentence=" "
        for word in self.text:
            sentence+=word
            if word in special_char:
                self.sentence.append(sentence.strip())
                sentence=" "
        if sentence.strip():
           self.sentence.append(sentence.strip())
        for i in self.sentence:
            print(i)
    def process_sentence(self):
        text=[]
        for sentence in self.sentence:
            word=len(sentence.split())
            text.append({"Sentence :" ,sentence,"Word count :",  word})
        return text     
            
text="Hello! How are you? Iam fine.Let's learn NLP."
tex=TextProcessor(text)
tex.split_into_sentences()
tex.process_sentence()








