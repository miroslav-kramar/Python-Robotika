# Programování v Pythonu (na souboru se stále pracuje)

## Proměnné

Proměnné slouží k uchovávání hodnot v rámci programu. Existuje mnoho datových typů proměnných pro uchovávání dat v různém formátu. Nejzákladnější datové typy, kterými se budeme pro začátek zabývat, jsou:
- celá čísla (integer),
- desetinná čísla (float),
- text (string),
- logické hodnoty (bool).

Proměnné se ve většině velkých programovacích jazycích deklarují. To znamená, že je zapotřebí "natvrdo" definovat datový typ proměnné, a to sice tak, že před název proměnné napíšeme definici datového typu. V Pythonu se proměnné **nedeklarují**, k zavedení proměnné stačí "pouze" napsat název proměnné a přiřadit k ní hodnotu příslušného datového typu. Python jí sám přiřadí datový typ vycházející z námi zadané hodnoty. Jako příklad můžeme uvést zavedení proměnné *x*:

Založení v jazyce Python
```python
x = 1
```

Založení v jazyce C
```c
int x = 1;
```

## Datové typy proměnných

Jak již bylo zmíněno, proměnné mohou být různých datových typů.

|**DATOVÝ TYP**|**PŘÍKLAD**|
|-|-|
|Integer (celé číslo)|x = 1|
|Float (desetinné číslo)|x = 0.5|
|String (text)|x = "text" (nezapomenout na uvozovky!)|
|Bool (logická hodnota; např.: pravda/nepravda, ano/ne, 0/1)|x = True (pravda) x = False (nepravda)|
