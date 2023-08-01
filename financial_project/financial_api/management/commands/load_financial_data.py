from django.core.management.base import BaseCommand
import pandas as pd
from financial_api.models import FinancialData
import json


class Command(BaseCommand):
    """Class to create a command to fill database with data"""
    help = "Load data from path"

    def add_arguments(self, parser):
        """This function takes arguments from command line"""
        parser.add_argument("data_path", type=str, help="Indicates path where you can find data")
        # Optional argument
        parser.add_argument("-rm", "--remove", action="store_true",
                            help="Remove previous Data")

    def handle(self, *args, **kwargs):
        """Use arguments from previous function and fill the database with the provided data"""
        data_path = kwargs["data_path"]
        is_replace_all = kwargs["remove"]
        if is_replace_all:
            FinancialData.objects.all().delete()
        with open(f"{data_path}") as f:
            data_json = json.load(f)

        currency = data_json["pnl"]["MXN"]["currency"]
        unit = data_json["pnl"]["MXN"]["unit"]

        data_df = pd.DataFrame(data_json["pnl"]["MXN"]["data"])
        financial_data_df = data_df.melt(value_vars=data_df.columns, ignore_index=False, var_name="financial_measure",
                                         value_name="amount").reset_index(names="date")
        financial_data = [
            FinancialData(
                date=financial_data_df.loc[ind, "date"],
                # company=data_df.loc[ind, "symbol"],
                financial_measure=financial_data_df.loc[ind, "financial_measure"],
                amount=financial_data_df.loc[ind, "amount"],
                currency=currency,
                unit=unit

            )
            for ind in financial_data_df.index
        ]

        FinancialData.objects.bulk_create(financial_data)
