# coding: utf8
 #!/usr/bin/python
 # Simple comment generator
import sys,os
class Acsii_alphabet:
    def __init__(self, comment_sign, input_comment):
        self.list_letter_comment = list(input_comment.lower())
        self.comment_sign = comment_sign
        self.a=["░█████╗░","██╔══██╗","███████║","██╔══██║","██║░░██║","╚═╝░░╚═╝"]
        self.b=["██████╗░","██╔══██╗","██████╦╝","██╔══██╗","██████╦╝","╚═════╝░"]
        self.c=["██████╗░","██╔══██╗","██║░░╚═╝","██║░░██╗","╚█████╔╝","░╚════╝░"]
        self.d=["██████╗░","██╔══██╗","██║░░██║","██║░░██║","██████╔╝","╚═════╝░"]
        self.e=["███████╗","██╔════╝","█████╗░░","██╔══╝░░","███████╗","╚══════╝"]
        self.f=["███████╗","██╔════╝","█████╗░░","██╔══╝░░","██║░░░░░","╚═╝░░░░░"]
        self.g=["░██████╗░","██╔════╝░","██║░░██╗░","██║░░╚██╗","╚██████╔╝","░╚════╝░"]
        self.h=["██╗░░██╗","██║░░██║","███████║","██╔══██║","██║░░██║","░╚═╝░░╚═╝"]
        self.i=["██╗","██║","██║","██║","██║","╚═╝"]
        self.j=["░░░░░██╗","░░░░░██║","░░░░░██║","██╗░░██║","╚█████╔╝","░╚════╝░"]
        self.k=["██╗░░██╗","██║░██╔╝","█████═╝░","██╔═██╗░","██║░╚██╗","╚═╝░░╚═╝"]
        self.l=["██╗░░░░░","██║░░░░░","██║░░░░░","██║░░░░░","███████╗","╚══════╝"]
        self.m=["███╗░░░███╗","████╗░████║","██╔████╔██║","██║╚██╔╝██║","██║░╚═╝░██║","╚═╝░░░░░╚═╝"]
        self.n=["███╗░░██╗","████╗░██║","██╔██╗██║","██║╚████║","██║░╚███║","╚═╝░░╚══╝"]
        self.o=["░█████╗░","██╔══██╗","██║░░██║","██║░░██║","╚█████╔╝"," ╚════╝░"]
        self.p=["██████╗░","██╔══██╗","██████╔╝","██╔═══╝░","██║░░░░░","╚═╝░░░░░"]
        self.q=["░██████╗░","██╔═══██╗","██║██╗██║","╚██████╔╝","░╚═██╔═╝░"," ░░╚═╝░░░"]
        self.r=["██████╗░","██╔══██╗","██████╔╝","██╔══██╗","██║░░██║","╚═╝░░╚═╝"]
        self.s=["░██████╗","██╔════╝","╚█████╗░","░╚═══██╗","██████╔╝","╚═════╝░░"]
        self.t=["████████╗","╚══██╔══╝","░░░██║░░░","░░░██║░░░","░░░██║░░░","░░╚═╝░░░"]
        self.u=["██╗░░░██╗","██║░░░██║","██║░░░██║","██║░░░██║","╚██████╔╝","░╚═════╝░"]
        self.v=["██╗░░░██╗","██║░░░██║","╚██╗░██╔╝","░╚████╔╝░","░░╚██╔╝░░","░░░╚═╝░░░"]
        self.w=["░██╗░░░░░░░██╗","░██║░░██╗░░██║","░╚██╗████╗██╔╝","░░████╔═████║░","░░╚██╔╝░╚██╔╝░","░░░╚═╝░░░╚═╝░░"]
        self.x=["██╗░░██╗","╚██╗██╔╝","░╚███╔╝░","░██╔██╗░","██╔╝╚██╗","╚═╝░░╚═╝"]
        self.y=["██╗░░░██╗","╚██╗░██╔╝","░╚████╔╝░","░░╚██╔╝░░","░░░██║░░░","░░░╚═╝░░░"]
        self.z=["███████╗","╚════██║","░░███╔═╝","██╔══╝░░","███████╗","╚══════╝"]

    def make_comment(self):
        output_string =""
        #compter = []
        #print(self.list_letter_comment)
        #for letter in self.list_letter_comment:
            #for i in range(6):
                #try:
                    #list_letter = self.get_attribute(letter)[i]
                    #compter.append(len(list_letter))
                #except:
                    #pass
        #print(max(compter))
        for i in range(6):
            output_string += self.comment_sign + " "
            for letter in self.list_letter_comment:
                try:
                    output_string += self.get_attribute(letter)[i] + "  "
                except:
                    output_string += " "
                    pass
            output_string += "\n"
        return output_string

    def print_letter(self):
        for letter in self.list_letter_comment:
            return self.get_attribute(letter)

    def get_attribute(self, input_string):
        if input_string == 'a':
            return self.a
        if input_string == 'b':
            return self.b
        if input_string == 'c':
            return self.c
        if input_string == 'd':
            return self.d
        if input_string == 'e':
            return self.e
        if input_string == 'f':
            return self.f
        if input_string == 'g':
            return self.g
        if input_string == 'h':
            return self.h
        if input_string == 'i':
            return self.i
        if input_string == 'j':
            return self.j
        if input_string == 'k':
            return self.k
        if input_string == 'l':
            return self.l
        if input_string == 'm':
            return self.m
        if input_string == 'n':
            return self.n
        if input_string == 'o':
            return self.o
        if input_string == 'p':
            return self.p
        if input_string == 'q':
            return self.q
        if input_string == 'r':
            return self.r
        if input_string == 's':
            return self.s
        if input_string == 't':
            return self.t
        if input_string == 'u':
            return self.u
        if input_string == 'v':
            return self.v 
        if input_string == 'w':
            return self.w 
        if input_string == 'x':
            return self.x
        if input_string == 'y':
            return self.y
        if input_string == 'z':
            return self.z


def main(arg):
    le_comment = Acsii_alphabet(comment_sign = arg[0], input_comment = arg[1])
    print( le_comment.make_comment() )

if __name__ == "__main__":
    main(sys.argv[1:])
