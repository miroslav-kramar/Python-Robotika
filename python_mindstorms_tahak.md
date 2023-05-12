# Python EV3 Micropython Tahák (na souboru se stále pracuje)

## Obsah

bude doplněn

## Tlačítka a práce s nimi

Tlačítka, jako fyzické zařízení, jsou součástí třídy ```EV3Brick```, kterou je třeba
importovat na začátku souboru.

```python
from pybricks.hubs import EV3Brick
```

Tlačítka, jako parametr, jsou potom ze třídy ```Button```, kterou je taktéž třeba importovat.

```python
from pybricks.parameters import Button
```

Práce s tlačítky je poměrně přímočará, jelikož o tlačítka se "stará" jediná funkce,
a to funkce ```buttons.pressed()``` z třídy EV3Brick. Tato funkce nám při každém zavolání
vrátí pole (list) právě zmačknutých tlačítek. Příklad použití:

```python
from pybricks.hubs import EV3Brick
from pybricks.parameters import Button

ev3 = EV3Brick()

while True:
	if (Button.CENTER in ev3.buttons.pressed()):
		ev3.speaker.beep()
``` 

## Ultrasonic Sensor a práce s ním
