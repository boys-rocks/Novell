# -----------------------LENGTH CONSTANTS----------------------- #
IMPERIAL_LENGTH_UNITS = {
    "inches": 1,  # Base imperial length unit.
    "feet": 12,  # 12 inches in one foot.
    "yards": 36,  # 36 inches in one yard.
    "miles": 63_360,  # 63,360 inches in one mile.
    "conversion": 25.4,  # 25.4 millimeters in one inch.
}

METRIC_LENGTH_UNITS = {
    "millimeters": 1,  # Base metric length unit.
    "centimeters": 10,  # 10 millimeters in one centimeter.
    "decimeters": 100,  # 100 millimeters in one decimeter.
    "meters": 1_000,  # 1,000 millimeters in one meter.
    "kilometers": 1_000_000,  # 1,000,000 millimeters in one kilometer.
    "conversion": 0.0393701,  # 0.0393701 inches in one millimeter.
}

# -----------------------VOLUME CONSTANTS----------------------- #
IMPERIAL_VOLUME_UNITS = {
    "ounces": 1,  # Base imperial volume unit.
    "cups": 8,  # 8 ounces in one cup.
    "pints": 16,  # 16 ounces in one pint.
    "quarts": 32,  # 32 ounces in one quart.
    "gallons": 128,  # 128 ounces in one gallon.
    "conversion": 29.5735,  # 29.5735 millimeters in one ounce.
}

METRIC_VOLUME_UNITS = {
    "milliliters": 1,  # Base metric volume unit.
    "liters": 1_000,  # 1,000 millimeters in one liter.
    "conversion": 0.033814,  # 0.033814 ounces in one millimeter.
}

# -----------------------TIME CONSTANTS----------------------- #
TIME_UNITS = {
    "milliseconds": 1,  # Base time unit (no metric / imperial difference here).
    "seconds": 1_000,  # 1,000 milliseconds in one second.
    "minutes": 60_000,  # 60,000 milliseconds in one minute.
    "hours": 3_600_000,  # 3,600,000 milliseconds in one hour.
    "days": 86_400_000,  # 86,400,000 milliseconds in one day.
}

PLACEHOLDER = (
    {}
)  # Required placeholder dictionary for time conversions since function requires two.

# -----------------------TEMPERATURE CONSTANTS----------------------- #
TEMPERATURE_UNITS = [
    "celsius",
    "fahrenheit",
]

# -----------------------MASS CONSTANTS----------------------- #
IMPERIAL_MASS_UNITS = {
    "ounces": 1,  # Base imperial mass unit.
    "pounds": 16,  # 16 ounces in one pound.
    "tons": 35_840,  # 35,840 ounces in a ton.
    "conversion": 28_349.5,  # 28,349.5 milligrams in one ounce.
}
METRIC_MASS_UNITS = {
    "milligrams": 1,  # Base metric mass unit.
    "grams": 1_000,  # 1,000 milligrams in one gram.
    "kilograms": 1_000_000,  # 1,000,000 milligrams in one kilogram.
    "conversion": 0.00003527400004546,  # 0.00003527400004546 ounces in one milligram.
}

# -----------------------COMMAND ALIASES----------------------- #
SYMBOLS = {
    "f": "fahrenheit",
    "c": "celsius",
    "oz": "ounces",
    "g": "grams",
    "kg": "kilograms",
    "lb": "pounds",
    "ft": "feet",
    "foot": "feet",
    "yd": "yards",
    "min": "minutes",
    "in": "inches",
    "km": "kilometers",
    "cm": "centimeters",
    "day": "days",
    "sec": "seconds",
    "ms": "milliseconds",
    "milligram": "milligrams",
    "gram": "grams",
    "kilogram": "kilograms",
    "ounce": "ounces",
    "pound": "pounds",
    "ton": "tons",
    "tonnes": "tons",
    "millisecond": "milliseconds",
    "second": "seconds",
    "minute": "minutes",
    "hour": "hours",
    "milliliter": "milliliters",
    "liter": "liters",
    "cup": "cups",
    "pint": "pints",
    "quart": "quarts",
    "gallon": "gallons",
    "millimeter": "millimeters",
    "centimeter": "centimeters",
    "decimeter": "decimeters",
    "meter": "meters",
    "kilometer": "kilometers",
    "inch": "inches",
    "yard": "yards",
    "mile": "miles",
}

#  ----------------------- AVAILABLE CONVERSION TYPES ----------------------- #
CONVERSION_TYPES = [
    "length",
    "volume",
    "temperature",
    "mass",
    "time",
]
