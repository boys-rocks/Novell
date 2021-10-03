# Imports
from typing import Union
from resources.metric_conversion_constants import (
    SYMBOLS,
    CONVERSION_TYPES,
    IMPERIAL_MASS_UNITS,
    METRIC_MASS_UNITS,
    IMPERIAL_VOLUME_UNITS,
    METRIC_VOLUME_UNITS,
    IMPERIAL_LENGTH_UNITS,
    METRIC_LENGTH_UNITS,
    TIME_UNITS,
    TEMPERATURE_UNITS,
)


# Function definitions


def _check_arg_validity(
    base_type: str, quantity: Union[int, float], start_unit: str, end_unit: str
) -> dict:

    """
    Checks user parameters to ensure they are valid for conversion.
    :param base_type: User provided base type for conversion, like length, mass, etc.
    :param quantity: Initial value to be converted.
    :param start_unit: Starting unit describing initial value provided by user.
    :param end_unit: target unit for initial value to be converted to from the starting unit.
    :return: A dictionary of flags indicating the validity of user arguments.
    """

    # Initialization
    type_flags = {
        "good_base": False,
        "good_quantity": False,
        "good_start_unit": False,
        "good_end_unit": False,
        "start_end_match": False,
    }

    # Checks / Decisioning
    if base_type in CONVERSION_TYPES:
        type_flags["good_base"] = True

    if isinstance(quantity, float):
        type_flags["good_quantity"] = True
    print(type_flags)
    if (
        start_unit in IMPERIAL_MASS_UNITS
        or start_unit in METRIC_MASS_UNITS
        or start_unit in IMPERIAL_LENGTH_UNITS
        or start_unit in METRIC_LENGTH_UNITS
        or start_unit in IMPERIAL_VOLUME_UNITS
        or start_unit in METRIC_VOLUME_UNITS
        or start_unit in TIME_UNITS
        or start_unit in TEMPERATURE_UNITS
    ):
        type_flags["good_start_unit"] = True

    if (
        end_unit in IMPERIAL_MASS_UNITS
        or end_unit in METRIC_MASS_UNITS
        or end_unit in IMPERIAL_LENGTH_UNITS
        or end_unit in METRIC_LENGTH_UNITS
        or end_unit in IMPERIAL_VOLUME_UNITS
        or end_unit in METRIC_VOLUME_UNITS
        or end_unit in TIME_UNITS
        or end_unit in TEMPERATURE_UNITS
    ):
        type_flags["good_end_unit"] = True

    if type_flags["good_start_unit"] and type_flags["good_end_unit"]:
        if (
            start_unit in IMPERIAL_MASS_UNITS or start_unit in METRIC_MASS_UNITS
        ) and base_type == "mass":
            if (
                end_unit in IMPERIAL_MASS_UNITS or end_unit in METRIC_MASS_UNITS
            ) and base_type == "mass":
                type_flags["start_end_match"] = True
        elif (
            start_unit in IMPERIAL_VOLUME_UNITS or start_unit in METRIC_VOLUME_UNITS
        ) and base_type == "volume":
            if (
                end_unit in IMPERIAL_MASS_UNITS or end_unit in METRIC_VOLUME_UNITS
            ) and base_type == "volume":
                type_flags["start_end_match"] = True
        elif (
            start_unit in IMPERIAL_LENGTH_UNITS or start_unit in METRIC_LENGTH_UNITS
        ) and base_type == "length":
            if (
                end_unit in IMPERIAL_LENGTH_UNITS or end_unit in METRIC_LENGTH_UNITS
            ) and base_type == "length":
                type_flags["start_end_match"] = True
        elif (
            start_unit in TIME_UNITS and end_unit in TIME_UNITS and base_type == "time"
        ):
            type_flags["start_end_match"] = True
        elif (
            start_unit in TEMPERATURE_UNITS
            and end_unit in TEMPERATURE_UNITS
            and base_type == "temperature"
        ):
            type_flags["start_end_match"] = True

    return type_flags


def _print_flag_errors(type_flags: dict) -> str:
    error = ""

    if not type_flags["good_base"]:
        error += "\nInvalid `base_type` value."
    if not type_flags["good_quantity"]:
        error += "\nInvalid `quantity` value."
    if not type_flags["good_start_unit"]:
        error += "\nInvalid `start_unit`."
    if not type_flags["good_end_unit"]:
        error += "\nInvalid `end_unit`."
    if not type_flags["start_end_match"]:
        error += "\n`start_unit` and `end_unit` values don't match `base_type`."

    return error


def _print_result(
    start_quantity: Union[int, float],
    start_unit: str,
    end_unit: str,
    end_quantity: Union[int, float],
) -> str:
    """
    Function to create final output string for conversion.

    :param start_quantity: Integer or float starting quantity which needed conversion.
    :param start_unit: Initial unit type of integer or float starting quantity.
    :param end_unit: Ending unit type of integer or float quantity.
    :param end_quantity: Integer or float of converted starting quantity from start unit to end unit.
    :return: String of values concatenated in user friendly message.
    """
    if end_quantity < 0.000001:
        output = "Value smaller than decimal precision 6. Cannot output."
    else:
        output = f"```{start_quantity} {start_unit} = {end_quantity} {end_unit}```"
    return output


def _check_symbols(start_unit: str, end_unit: str) -> tuple:
    """
    Checks if starting unit or ending unit are contained in the alias dictionary, SYMBOLS.
    :param start_unit: string indicating the starting unit type.
    :param end_unit: string indicating the ending unit type.
    :return: returns tuple of values post comparison/conversion with alias dictionary.
    """
    if start_unit in SYMBOLS:
        start_unit = SYMBOLS[start_unit]
    if end_unit in SYMBOLS:
        end_unit = SYMBOLS[end_unit]

    return start_unit, end_unit


def _intermediate_helper(
    start_unit: str,
    end_unit: str,
    quantity: Union[int, float],
    imperial: dict,
    metric: dict,
) -> Union[int, float]:

    """
    Function turns any input quantity into an intermediate value based on dictionary constants. Function
    then takes the intermediate form and converts it to the target form.

    :param start_unit: Starting unit type of value input.
    :param end_unit: ending unit type of value input.
    :param quantity: Starting value to be converted.
    :param imperial: Imperial dictionary for related type conversion (length, volume, etc.).
    :param metric: Metric dictionary for related type conversion (length, volume, etc.).
    :return: Converted integer or float value of quantity from starting unit to ending unit.
    """

    # Initialization
    final = 0
    intermediate_form = 0

    # Decisioning based on starting unit and ending unit.
    if start_unit in imperial:
        intermediate_form = quantity * imperial[start_unit]
        if end_unit in imperial:
            final = intermediate_form / imperial[end_unit]
        elif end_unit in metric:
            intermediate_form *= imperial["conversion"]
            final = intermediate_form / metric[end_unit]

    elif start_unit in metric:
        intermediate_form = quantity * metric[start_unit]
        if end_unit in metric:
            final = intermediate_form / metric[end_unit]
        elif end_unit in imperial:
            intermediate_form *= metric["conversion"]
            final = intermediate_form / imperial[end_unit]

    return final


def _convert_temp(
    start_unit: str, end_unit: str, quantity: Union[int, float]
) -> Union[int, float]:

    """
    Converts temperature between fahrenheit and celsius.
    :param start_unit: starting unit for conversion.
    :param end_unit: ending unit for quantity to be converted to.
    :param quantity: starting temperature to be converted.
    :return: quantity converted from starting unit to ending unit.
    """

    temperature = 0
    if start_unit == "fahrenheit" and end_unit == "celsius":
        temperature = (quantity - 32) * (5 / 9)  # (F - 32) * (5/9) = C
    elif start_unit == "celsius" and end_unit == "fahrenheit":
        temperature = (quantity * (9 / 5)) + 32  # (C * (9/5)) + 32 = F
    return temperature
