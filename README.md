# CircuitPython Implementation of Conway's Game of Life



This repo contains code for CircuitPython implementation of the famous '[Conway's Game of Life](https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life)'. It uses Adafruit's *adafruit_st7735r* library to draw the game on a  128x160 pixel color TFT LCD. This has been tested on Raspberry Pi Pico, here is a  video of the game in action:




The code assumes you are using Raspberry Pi Pico and ST7735 based 120*160 pixel TFT LCD. The connections between the board and LCD are as follows:

| Display Pin Number |   Display Pin Name | Pi pico Pins |
|--------------------|--------------------|--------------|
| 2                  | VCC                | 5V           |
| 1                  | GND                | GND          |
| 10                 | CS                 | GP18         |
| 6                  | RESET              | GP17         |
| 7                  | A0                 | GP16         |
| 8                  | SDA                | GP11         |
| 9                  | SCK                | GP10         |
| 15                 | LED                | 3.3V         |



For a different board, you will have to update code to use PINs which were used for connecting the LCD


### Things to try

* Add a reset button to re-start the game.
* Play around with '*scale*' variable, try different value (recommended values are 2,4,8)

A CircuitPython implementation of Conway's Game of Life, that shows the game over TFT LCD
