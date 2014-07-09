# I2C
TP1 = SCL = "183"
TP2 = SDA = "168"
TP8 = NCS = "161"
TP9 = PWREN = "162"

# ONLY OUTPUT
TP11 = NINT = "157"
TP12 = SOMI = "159"
TP13 = SIMO = "158"
TP14 = CLK = "156"

# GPIO
TP15 = "132"
TP16 = "133"
TP17 = "134"
TP18 = "135"
# DIRECTION
MODE1516 = "137"
MODE1718 = "136"

# BIDIRECTIONAL GPIO
TP19 = "139"
TP20 = "138"
TP21 = "131"
TP22 = "130"
# DIRECTION
MODE1920 = "140"
MODE2122 = "141"

# UART
UART2_TX = "142"
UART2_RX = "143"

PWM0 = "144"
PWM1 = "145"
PWM2 = "146"

LED0 = "/beagleboard::usr0"
LED1 = "/beagleboard::usr1"

BIPINS = [TP15, TP16, TP17, TP18, TP19, TP20, TP21, TP22]
MODEPINS = [MODE1516, MODE1718, MODE1920, MODE2122]
LEDPINS = [LED0, LED1]

GPIO = "/sys/class/gpio/gpio"
LEDS = "/sys/class/leds"
IN = "in\n"
OUT = "out\n"
HIGH = "1\n"
LOW = "0\n"

def GET(filename):
	with open(filename, "r") as f:
		output = f.read()
	return output

def SET(filename, value):
	with open(filename, "w") as f:
		f.write(value)

def pinMode(pin, mode):
	direction = GPIO + pin + "/" + "direction"
	if pin in BIPINS:
		if mode == OUT:
			dirvalue = HIGH
		else:
			dirvalue = LOW
		digitalWrite(MODEPINS[BIPINS.index(pin) / 2], dirvalue)
	SET(direction, mode)

def digitalWrite(pin, value):
	if pin in LEDPINS:
		ledWrite(pin, value)
	else:
		pinval = GPIO + pin + "/" + "value"
		pinMode(pin, OUT)
		SET(pinval, value)

def digitalRead(pin):
	pinval = GPIO + pin + "/" + "value"
	pinMode(pin, IN)
	return GET(pinval)

def ledWrite(led, value):
	ledpin = LEDS + led + "/" + "brightness"
	SET(ledpin, value)

def clearMode():
	for pin in MODEPINS:
		pinMode(pin, IN)
