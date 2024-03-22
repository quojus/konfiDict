import re
class KonfiDict(dict):
    """
        Ein spezialisiertes Dictionary zur Verwaltung von Konfigurationselementen mit Typ- und Schlüsselspezifikation.
        Methoden:
            add_konfi_type, __getitem__, __setitem__, set_item, get_item, copy_konfi
        """
    _key_2_type_pattern = re.compile(r'(?<=^_)[^_]+(?=__)')
    _None_funktion = lambda: None

    def __init__(self):

        super().__init__()
        self._koniDict_items: dict[str,] = {}
        self._roh_keys: dict = {}

    def _key_pattern(self, typeName: str, key:str) -> str:
        return f'_{typeName}__{key}'

    def add_konfi_type(self, typeName: str, *args, objekt_=None,  **kwargs) -> None:
        """
       Fügt einen neuen Konfigurationstyp hinzu, der durch `typeName` spezifiziert ist. Dieser Typ
       kann dann zur Definition von Set- und Get-Verhalten für Konfigurationselemente verwendet werden.

       Die Definition von Set- und Get-Verhalten ermöglicht die Verwendung von magischen Methoden zur
       Manipulation der Konfigurationselemente, sowie das Setzen von Standardwerten oder das Ausführen
       spezifischer Funktionen bei der Interaktion mit den Konfigurationselementen.

       Parameter:
           typeName (str): Der Name des Konfigurationstyps. Dieser Name ist erforderlich und dient
                           als Identifikator für den Konfigurationstyp.
           objekt_ (objekt): wenn mit gegeben wird sucht sich später die andern funktion die type mit den typeName
           *args: Optionale Objekte, die dem Konfigurationstyp hinzugefügt werden sollen. Diese Objekte
                  können verwendet werden, um direkt Konfigurationselemente hinzuzufügen, die über
                  magische Methoden verfügen.
           **kwargs: Schlüsselwortargumente, die spezifisches Set- und Get-Verhalten definieren.
                     - `set`: Ein Dictionary, das als Schlüssel den Namen der Funktion, die ausgeführt
                              werden soll, und als Wert den Typ des Wertes, der den Aufruf der Funktion
                              auslöst, enthält. Diese Funktionen werden bei der Zuweisung von Werten zu
                              Konfigurationselementen des entsprechenden Typs aufgerufen.
                     - `get`: Eine Funktion oder ein Standardwert, der ausgegeben wird, wenn ein
                              Konfigurationselement abgefragt wird. Dieser Parameter ist optional.

       Beispiel:
           # Hinzufügen eines neuen Konfigurationstyps mit spezifischen Set- und Get-Verhalten.
           konfiDict.add_konfi_type('meinTyp',
                                    set={'setFunktion': int, 'anderesSet': str},
                                    get='standardWert')

           # Optional: Hinzufügen eines Elements über magische Methoden.
           konfiDict.add_konfi_type('andererTyp', meinObjekt)

       Hinweis:
           Die Verwendung der `set`- und `get`-Parameter ist optional, ermöglicht jedoch eine
           feingranulare Kontrolle darüber, wie Werte gesetzt und abgerufen werden. Die Konfiguration
           für `set` kann direkt über die `kwargs` erfolgen, indem Funktionen und zugehörige Typen
           als Schlüssel-Wert-Paare angegeben werden.
           """
        itemData = [[], '', objekt_]
        def ceck_arg(arg):
            if isinstance(arg, dict):
                for k, v in arg.items():
                    itemData[0].append((v, k))
            else:
                itemData[1] = arg
        if 'set' in kwargs.keys() and isinstance(kwargs['set'], dict):
            for k, v in kwargs.pop('set').items():
                itemData[0].append((v, k))
        if 'get' in kwargs.keys():
            itemData[1] = kwargs.pop('get')
        for arg in args:
            ceck_arg(arg)
        for k, v in kwargs.items():
            itemData[0].append((v, k))
        self._koniDict_items[typeName] = itemData

    def __getitem__(self, key):
        if not re.search(self._key_2_type_pattern, key):
            if key in self._roh_keys.keys():
                key = self._roh_keys[key]
                typeName = re.search(self._key_2_type_pattern, key).group(0)
                method = getattr(super().__getitem__(key), self._koniDict_items[typeName][1], None)
                if callable(method):
                    return method()
                return super().__getitem__(key)
        try:
            return super().__getitem__(key)
        except KeyError:
            return None

    def __setitem__(self, key: str, value) -> None:
        """
        Setzt einen Wert für einen gegebenen Schlüssel im Konfigurationsdictionary.
        Wenn der Schlüssel bereits existiert und der Werttyp mit einem der für diesen Typ definierten
        set-Methodennamen übereinstimmt, wird die entsprechende Methode aufgerufen, um den Wert zu setzen.
        Ist der Schlüssel noch nicht vorhanden, wird er hinzugefügt, vorausgesetzt, der Konfigurationstyp
        wurde zuvor mit add_konfi_type registriert.

        Parameter:
            key (str): Der Schlüssel des Konfigurationselements. Wenn der Schlüssel bereits existiert,
                       identifiziert dieser die Konfiguration und die spezifische set-Methode für den
                       übergebenen Werttyp. Ist der Schlüssel noch nicht vorhanden, muss der Typ zuvor
                       mit der Methode add_konfi_type hinzugefügt worden sein.
            value: Der Wert, der für das Konfigurationselement gesetzt werden soll. Der Datentyp des Wertes
                   wird verwendet, um die entsprechende set-Methode aus den für den Konfigurationstyp
                   definierten Methoden zu ermitteln.

        Wirft:
            ValueError: Wenn der Schlüssel existiert, aber kein entsprechender Methodenname für den Werttyp
                        gefunden werden kann.
            KeyError: Wenn der Schlüssel nicht vorhanden ist und der zugehörige Konfigurationstyp nicht
                      zuvor mit add_konfi_type registriert wurde.

        Beispiel:
            konfiDict.add_konfi_type('myType', set={'setMethode1': int, 'setMethode2': str}, get='getMethode')
            konfiDict['myType__configKey'] = 10  # Ruft setMethode1(10) auf, wenn int der Werttyp ist.
        """
        if not re.search(self._key_2_type_pattern, key):

            if key in self._roh_keys.keys():
                key = self._roh_keys[key]
                typeName = re.search(self._key_2_type_pattern, key).group(0)
                for objTupel in self._koniDict_items[typeName][0]:
                    if type(value) == objTupel[0] or objTupel[0] == None:
                        method = getattr(super().__getitem__(key), objTupel[1], None)
                        if method is None:
                            raise ValueError(f'{key} hat kein method names {objTupel[1]}')
                        method(value)
                return None
            else:
                for typeName in self._koniDict_items.keys():

                    if self._koniDict_items[typeName][2] is not None:
                        print(self._koniDict_items[typeName][2])
                        if isinstance(value, self._koniDict_items[typeName][2]):
                            self.set_item(key, value, typeName)
                            return None
        try:
            super().__getitem__(key)
        except KeyError:
            return None


    def set_item(self,key: str, item: object, typeName: str=None) -> None:
        """
        Setzt ein Konfigurationselement eines bestimmten Typs.

        Parameter:

            key (str): Der spezifische Schlüssel des Konfigurationselements.
            item (object): Das zu setzende Konfigurationselement.
            typeName (str): Der Typ des Konfigurationselements.
        """
        if typeName is None:
            for k in self._koniDict_items.keys():
                if type(item) == type(self._koniDict_items[k][2]):
                    typeName = k
        if typeName in self._koniDict_items.keys():
            super().__setitem__(self._key_pattern(typeName, key), item)
            self._roh_keys[key] = self._key_pattern(typeName, key)
            return
        raise KeyError(f'{typeName} is not exist')

    def get_item(self,  key: str,typeName: str =None) -> object | None:
        """
       der weg um das objekt im dict zu bekommen

       Parameter:
            key (str): Der spezifische Schlüssel des Konfigurationselements.
            typeName (str): (obzonal) Der Typ des abzurufenden Konfigurationselements.

        """
        if typeName is None:
            return super().__getitem__(self._roh_keys[key])
        return super().__getitem__(self._key_pattern(typeName, key))

    def copy_konfi(self):
        """
        copy der Konfigurationselement ohne die items in dict
        :return:
        """
        konfi = KonfiDict()
        konfi._koniDict_items = self._koniDict_items
        konfi._roh_keys = self._roh_keys
        return konfi
