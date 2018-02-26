import tkinter as tk
from tkinter import filedialog
from dbfread import DBF, FieldParser, InvalidValue

class MyFieldParser(FieldParser):
    def parseW(self, field, data):
        pass
    def parse(self, field, data):
        try:
            return FieldParser.parse(self, field, data)
        except ValueError:
            return InvalidValue(data)

root = tk.Tk()
root.withdraw()

filepath = filedialog .askopenfilename()
print ("otwierasz %s" %(filepath))
savepath=filepath[:-4]+"_import"+".txt"

table = DBF(filepath, parserclass=MyFieldParser)
file = open(savepath,"w")
for i, record in enumerate(table):
     for name, value in record.items():
                if name=="NAME":
                    nazwa=value
                    nazwa=''.join(nazwa.split())
                elif name=="NORTH":
                    north=value
                    try:
                        north=''.join(north.split())
                        north=north.replace("\x00","")
                    except:
                        pass
                elif name=="EAST":
                    east=value
                    try:
                        east=''.join(east.split())
                        east=east.replace("\x00","")
                    except:
                        pass
                elif name=="ELEVATION":
                    elevation=value
                    try:
                        elevation=''.join(elevation.split())
                        elevation=elevation.replace("\x00","")
                    except:
                        pass
                elif name=="CODE":
                    code=value
                    code=''.join(code.split())
                elif name=="NOTE":
                    note=value
                    note=''.join(note.split())
     file.write("%s\t%s\t%s\t%s\t%s\t%s\n" % (nazwa,north,east,elevation,code,note))
     print nazwa,"\t", north,"\t", east,"\t", elevation,"\t", code,"\t", note 
     #print('records[{}][{!r}] == {!r}'.format(i, name, value))
file.close()
print "press any key to continue"
raw_input()
