import tkinter as tk
from konfiDict.konfiDict import KonfiDict

root = tk.Tk()

konfiDict = KonfiDict()

konfiDict.add_konfi_type("tkVar", {'set': str}, 'get', objekt_=tk.StringVar )
konfiDict.set_item('schoko', tk.StringVar(), 'tkVar')
konfiDict['schoko'] = 'schoko test'
konfiDict['samba'] = tk.StringVar()
konfiDict['samba'] = 'samba test'
print(konfiDict)
print(konfiDict['schoko'], '|', konfiDict['samba'])
konfiDict['samba'] = konfiDict['schoko']
print(konfiDict['schoko'], '|', konfiDict['samba'])