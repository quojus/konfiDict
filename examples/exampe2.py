from konfiDict.konfiDict import KonfiDict



class Kuh:
    def __init__(self):
        self.ton = 'Muh '
        self.text2 = "(oo)\\_______\\n"
    def razepatuf(self, text):
        self.ton = text


    def weide(self):
        return self.ton

    def print_text(self, b:bool):
        if b:
            print(self.ton)

    def multi(self, data):
        if type(data) is tuple:
            print(' '*11,*data)
        if type(data) is int:
            print(' '*data, self.ton, "----w |\\n")

konfiDict = KonfiDict()

konfiDict.add_konfi_type("Kuh", {'razepatuf': str, 'multi': tuple}, 'weide', multi=int, print_text=bool)
konfiDict.set_item('Elfi', Kuh(),'Kuh')

print(konfiDict['Elfi'])
konfiDict['Elfi'] = '        ^__^\\n'
konfiDict['Elfi'] = True
konfiDict['Elfi'] = '(__)\\\\       )\\\\/\\\\n"'
print('       ', konfiDict.get_item('Elfi').text2)
print(' '*7, konfiDict['Elfi'])
konfiDict['Elfi'] = '||'
konfiDict['Elfi'] = 11
konfiDict.add_konfi_type("Kuh2", {'razepatuf': str, 'multi': tuple}, 'weide', multi=int, objekt_=Kuh)
konfiDict['Ella'] = Kuh()
konfiDict['Ella'] = ('||', ' '*4, '||\\n')
print(konfiDict['Ella'])
