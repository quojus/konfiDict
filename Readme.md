# KonfiDict - Dynamische Konfigurationsverwaltung

KonfiDict ist eine spezialisierte Klasse in Python, die darauf abzielt, die Verwaltung und Manipulation von Konfigurationseinstellungen in einer Anwendung zu vereinfachen und flexibler zu gestalten. Durch die Erweiterung der Standard-dict-Funktionalität ermöglicht KonfiDict das Definieren von Konfigurationstypen mit zugehörigen Set- und Get-Methoden, die automatisch aufgerufen werden, wenn Konfigurationselemente manipuliert werden.
## Features

- Typbasierte Konfigurationselemente: Definieren Sie Konfigurationselemente basierend auf Typnamen, um ihre Verwendung und Verwaltung zu vereinfachen.
- Automatische Set- und Get-Methoden: Legen Sie spezifische Methoden fest, die beim Setzen oder Abrufen von Konfigurationselementen eines bestimmten Typs aufgerufen werden.
- Unterstützung für magische Methoden: Integrieren Sie Objekte, die über magische Methoden verfügen, um deren Verhalten direkt in die Konfigurationslogik einzubinden.
- Flexible Konfiguration: Verwenden Sie args und kwargs, um Set- und Get-Verhalten dynamisch zu definieren und anzupassen.

Verwendung
Einrichtung

Um eine neue Instanz von KonfiDict zu erstellen, importieren Sie zunächst die Klasse und instanziieren Sie sie:

```python
from konfiDict.konfiDict import KonfiDict

konfiDict = KonfiDict()
```

## Konfigurationstypen hinzufügen

Verwenden Sie die add_konfi_type-Methode, um einen neuen Konfigurationstyp mit optionalen Set- und Get-Methoden hinzuzufügen:
```python

konfiDict.add_konfi_type('meinTyp',
                         set={'setFunktion': int, 'anderesSet': str},
                         get='standardWert')

```
oder 

```python

class Kuh:
    ... # mit den funktionen die in add_konfi_type angegeben werden 
konfiDict.add_konfi_type("Kuh", {'razepatuf': str, 'multi': tuple}, 'weide', multi=int, print_text=bool)
# mit type
konfiDict.add_konfi_type("Kuh2", {'razepatuf': str, 'multi': tuple}, 'weide', multi=int, objekt_=Kuh)

```

## Erstellen eins item im dict 
```python

konfiDict.set_item( 'Elfi', Kuh(), 'Kuh')

```
alternative dafür muss aber bei add_konfi_type das objekt_ mit gegeben werden 
```python
class Kuh:
    ... # mit den funktionen die in add_konfi_type angegeben werden 
konfiDict.add_konfi_type("Kuh", {'funk1': str, 'funk2': tuple}, 'returnFunk', funk3=int,objekt_=Kuh)

konfiDict.set_item('Kuh', 'Elfi', Kuh())
# oder 



```
## Verwendung 
Hab ich mir gebaut für die Verwendung von TKinter elementen, Da ich so entspannt mit den dazugehörigen variablen und Daten arbeiten kann.
