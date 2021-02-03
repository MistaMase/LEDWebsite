import board
import neopixel

pixels = neopixel.NeoPixel(board.D18, 12, brightness=0.5, auto_write=False, pixel_order=neopixel.GRB)

pixels.fill((0, 0, 0))
pixels.show()
