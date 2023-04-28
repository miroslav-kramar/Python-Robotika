# Python Programování Tahák

## Obsah


- [Proměnné](#proměnné)
  - [Deklarace](#deklarace)
  - [Datové typy proměnných](#datové-typy-proměnných)
  - [Přetypování proměnných](#přetypování-proměnných)
  - [Pole](#pole)
- [Řídící struktury jazyka](#řídící-struktury-jazyka)
  - [Cykly](#cykly)
    - [Cyklus for](#cyklus-for)
    - [Cyklus while](#cyklus-while)
  - [Podmínky](#podmínky)
    - [If/Else](#ifelse)  
- [Funkce](#funkce)

## Proměnné

#### Deklarace

Proměnné se v Pythonu deklarují tak, že napíšeme jméno proměnné a pomocí operátoru přiřazení ```=``` do ní přiřadíme její hodnotu.

Příklad:

```python
x = 1
```

#### Datové typy proměnných

Proměnné mohou mít různé datové typy. Typ nemusíme předem specifikovat, Python to udělá za nás. Typ určí podle přiřazené hodnoty.

```python
i = 1       # integer (cele cislo)
f = 0.5     # float (desetinne cislo)
s = "text"  # string (text)
b = True    # bool (logicka hodnota)
```

#### Přetypování proměnných

Typy proměnnýc můžeme mezi sebou měnit. Slouží k tomu funkce pojmenované podle cílového datového typu:

- ```int()```
- ```float()```
- ```str()```
- ```bool()```

Užití:

```python
x = "123"   # x je v tomto pripade typu string a obsahuje retezec "123"
x = int(x)  # hodnotu x pomoci funkce int() zmenime z textu "123" na cele cislo 123
            # datovy typ promenne x se po prirazeni zmeni na integer
```

U přetypování je dobré se zamyslet, zda dává smysl:

```python
x = "ahoj"  # x je v tomto pripade typu string a obsahuje retezec "ahoj"
x = int(x)  # konverze v tomto pripade selze, ponevadz string "ahoj" nelze smysluplne prevest na cele cislo
            # program v tomto pripade spadne
```

#### Pole

Pole je ve své podstatě proměnnou, která dokáže držet více hodnot. Každá hodnota má svůj index (pozici v poli). Pole se indexuje od 0. Počet pozic pole je teoreticky neomezený.

```python
pole = [1,2,3,4]  # deklarace a definice pole se 4 prvky
len(pole)         # funkce len() vrati delku pole (v nasem pripade 4)
pole[1] = 10      # nahradi cislo na pozici 1 cislem 10
pole.append(5)    # prida na konec pole cislo 5
pole.insert(0, 0) # na prvni pozici vlozi cislo 0, zbytek pole se posune o index dal
pole.pop(0)       # odstrani prvni pozici
pole.sort()       # seradi prvky v poli vzestupne
```

## Řídící struktury jazyka

### Cykly

#### Cyklus ```for```

```python
for i in range(10):
  print("Ahoj")
  print(i)
```

Cyklus ```for``` provádí příkazy v něm napsané tolikrát, kolikrát jsme specifikovali ve funkci ```range()```. V tomto případě 10x vypíše slovo "Ahoj" a pokaždé vrátí hodnotu iterační proměnné ```i```. 

Funkce ```range(10)``` v tomto případě vrátí čísla od 0 do 9 (celkem 10 čísel).

#### Cyklus ```while```

```python
while True:
    print("Ahoj")
```

Cyklus ```while``` provádí příkazy v něm napsané tolikrát, dokud bude platit podmínka uvedená jeho "hlavičce". V tomto případě bude vypisovat slovo "Ahoj" do nekonečna (nebo dokud program ručně neukončíme). 

```python
x = 0

while x < 10:
    print(x)
    x += 1
```

V tomto případě bude vypisovat hodnotu proměnné *x*, dokud hodnota *x* nebude větší, než 10. 

### Podmínky

#### If/Else

```python
x = 1

if x == 1:
    print("x je 1")
elif x == 2:
    print("x je 2")
elif x == 3:
    print("x je 3")    
else:
    print("x je neco jineho")
```

## Funkce

Funkce je blok kódu, který lze volat tolikrát, kolikrát potřebujeme. Funkci definujeme pomocí klíčového slova ```def```. Funkci můžeme také předávat jeden a více argumentů (vstupních hodnot), se kterými bude pracovat a lze z ní také vracet zpracované hodnoty.

Příklad funkce s jedním argumentem, která vrátí číslo o 1 větší, než jsme zadali:

```python
def funkce(arg):
  return arg + 1
  
print(funkce(1)) # funkce v tomto pripade vrati cislo 2
print(funkce(2)) # funkce v tomto pripade vrati cislo 3
print(funkce(3)) # funkce v tomto pripade vrati cislo 4
```

Příklad funkce s více argumenty, která vrátí jejich součin

```python
def funkce(arg1, arg2):
  vystup = arg1 * arg2
  return vystup
  
print(funkce(2, 3)) # funkce v tomto pripade vrati cislo 6
print(funkce(3, 4)) # funkce v tomto pripade vrati cislo 12
```
