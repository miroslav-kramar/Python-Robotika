# Python Turtle Tahák

## Zavedení modulu a založení želvy

Funkce Python Turtle nejsou výchozí součástí Pythonu, musíme je proto zavést. To provedeme klíčovým slovem ***import*** hned na začátku souboru.

```python
import turtle # zavedeni modulu turtle
```

Želvu (šipku, se kterou pohybujeme) založíme tak, že zavoláme konstruktor objektu želvy a objekt připřadíme do proměnné. Název podle vlastního výběru.

```python
tr = turtle.Turtle()
```

Želv můžeme zakládat, kolik chceme, pouze se každá musí jmenovat jinak.

```python
tr1 = turtle.Turtle()
tr2 = turtle.Turtle()
```

Ke každé poté přistupujeme zvlášť podle jejího jména.

```python
tr1.fd(100) # posuneme zelvu tr1 o 100 kroku
tr2.fd(-50) # posuneme zelvu tr2 o -50 kroku
```
## Zápis kódu při práci s modulem *turtle*

Syntaxe (zápis) se může na první pohled zdát nezvyklá, a to hlavně kvůli spoustě teček spojujících různá "slovíčka". Tečky zde jsou proto, že naše želva, kterou chceme ovládat, se zakládá jako objekt. Objekty jsou "základním stavebním kamenem" Objektově Orientovaného Programování (OOP).

V OOP se ke všem proměnným a funkcím objektů přistupuje právě přes tečku ```.```.

```python
objekt.funkce() # provedeni funkce objektu
```

## Nepleťte si objekty!

Trocha zmatení může nastat kvůli faktu, že se nám tu "míchají" dva zdánlivě totožné objekty:
- "naše" želva, jenž je objektem třídy *Turtle*,
- objekt turtle, který je nadřazen "naší" želvě a zodpovídá za práci s oknem. Jeho nejčastěji volaná funkce je ```turtle.done()```.

# Důležité funkce

## Funkce pro pohyb želvou (voláme z želvy)

|Funkce|Další zápis|Popis|
|-|-|-|
|```forward(x)```|```fd(x)```|Posune želvu dopředu o *x* kroků.|
|```backward(x)```|```bk(x)```|Posune želvu dozadu o *x* kroků.|
|```left(x)```|```lt(x)```|Otočí želvu o *x* stupňů doleva.|
|```right(x)```|```rt(x)```|Otočí želvu o *x* stupňů doprava.|
|```goto(x,y)```|```setpos(x,y)```|Přemístí želvu na souřadnice *x*, *y*.|
|```setx(x)```||Přemístí želvu po ose X na souřadnici *x*.|
|```sety(y)```||Přemístí želvu po ose Y na souřadnici *y*.|
|```setheading(x)```|```seth(x)```|Nastaví směr, kam se želva "kouká".|
|```home()```||Přesune želvu na počáteční souřadnice (0,0).|

## Funkce pro získání stavu želvy (voláme z želvy)

|Funkce|Další zápis|Popis|
|-|-|-|
|```xcor()```||Vrátí hodnotu souřadnice *x*, na které se želva nachází.|
|```ycor()```||Vrátí hodnotu souřadnice *y*, na které se želva nachází.|
|```heading()```||Vrátí směr, kterým se želva "kouká".|
|```isdown()```||Zjistí, jestli je pero želvy dole nebo nahoře. Vrací logickou hodnotu.|

## Funkce pro kreslení želvou

|Funkce|Další zápis|Popis|
|-|-|-|
|```penup()```||Želva nebude kreslit.|
|```pendown()```||Želva bude kreslit.|

## Funkce pro práci s oknem (voláme z *turtle*)

|Funkce|Další zápis|Popis|
|-|-|-|
|```done()```||Funkce zajistí, že okno po konci programu zůstane otevřené.|
|```resetscreen()```||Resetuje okno do počátečního stavu.|
