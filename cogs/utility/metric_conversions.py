import discord
from discord.ext import commands
from resources.metric_conversion_constants import (
    IMPERIAL_LENGTH_UNITS,
    METRIC_LENGTH_UNITS,
    IMPERIAL_VOLUME_UNITS,
    METRIC_VOLUME_UNITS,
    IMPERIAL_MASS_UNITS,
    METRIC_MASS_UNITS,
    TIME_UNITS,
    PLACEHOLDER,
    SYMBOLS,
)

from helpers.metric_conversion_helpers import (
    _check_arg_validity,
    _check_symbols,
    _print_flag_errors,
    _intermediate_helper,
    _print_result,
    _convert_temp,
)


class MetricConverter(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def do_convert(
        self, ctx, base_type: str, quantity: str, start_unit: str, end_unit: str
    ) -> None:

        """
        Command converts a starting quantity of one unit to and ending quantity of another user specified unit.
        User cannot cross base types (length unit to volume unit) because this kind of conversion obviously does
        not make sense.

        :param ctx: The discord context the command is used in.
        :param base_type: The type of conversion being done (length, mass, etc.).
        :param quantity: The starting quantity to be converted.
        :param start_unit: The starting unit to be converted from.
        :param end_unit: The ending unit to be converted to.
        :return: None. This function generates only text output to discord context.
        """
        # Initialize input for processing.
        base_type = base_type.lower()
        start_unit = start_unit.lower()
        end_unit = end_unit.lower()
        start_unit, end_unit = _check_symbols(start_unit, end_unit)
        if quantity.isnumeric():
            quantity = float(quantity)
        ctx.send("intial processing done")

        # Check user arguments.
        input_flags = _check_arg_validity(base_type, quantity, start_unit, end_unit)
        print(input_flags)
        if False in input_flags.values():
            await ctx.send(_print_flag_errors(input_flags))
            await ctx.send(
                "Usage: `<command_prefix>do_convert <base_type> "
                + "<starting_quantity> <starting_unit> <ending_unit>`"
            )
        else:

            # Decisioning based on conversion type.
            if base_type == "length":
                length = _intermediate_helper(
                    start_unit,
                    end_unit,
                    quantity,
                    IMPERIAL_LENGTH_UNITS,
                    METRIC_LENGTH_UNITS,
                )
                await ctx.reply(
                    _print_result(quantity, start_unit, end_unit, round(length, 6))
                )

            elif base_type == "volume":
                volume = _intermediate_helper(
                    start_unit,
                    end_unit,
                    quantity,
                    IMPERIAL_VOLUME_UNITS,
                    METRIC_VOLUME_UNITS,
                )
                await ctx.reply(
                    _print_result(quantity, start_unit, end_unit, round(volume, 6))
                )

            elif base_type == "mass":
                mass = _intermediate_helper(
                    start_unit,
                    end_unit,
                    quantity,
                    IMPERIAL_MASS_UNITS,
                    METRIC_MASS_UNITS,
                )
                await ctx.reply(
                    _print_result(quantity, start_unit, end_unit, round(mass, 6))
                )

            elif base_type == "time":
                the_time = _intermediate_helper(
                    start_unit, end_unit, quantity, TIME_UNITS, PLACEHOLDER
                )
                await ctx.reply(
                    _print_result(quantity, start_unit, end_unit, round(the_time, 6))
                )

            elif base_type == "temperature":
                temperature = _convert_temp(start_unit, end_unit, quantity)
                await ctx.reply(
                    _print_result(quantity, start_unit, end_unit, round(temperature, 6))
                )

    @do_convert.error
    async def on_unit_convert_error(self, ctx, error):

        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send("Not enough arguments provided.")
            await ctx.send(
                "Usage: `<command_prefix>do_convert <base_type> "
                + "<starting_quantity> <starting_unit> <ending_unit>`"
            )


def setup(client):
    client.add_cog(MetricConverter(client))
