import os
from src.data_tables.BaseDataTable import BaseDataTable
import logging
import csv
import json
import pandas
import copy

pandas.set_option("display.width", 132)
pandas.set_option("display.max_columns", 12)

logger = logging.getLogger()


class CSVDataTable(BaseDataTable):
    """
    Implements the BaseDataTable abstraction on top of CSV files.
    """

    def __init__(self, table_name, connect_info, entity_type_name="CSV",
                 key_columns=None, columns=None, rows=None, context=None):
        """

        :param table_name: The logical name you want to use for your table.
        :param connect_info: A dictionary of the form {"directory": path to folder, "file_name": xxx.csv}
        :param entity_type_name: Always CSV for CSV data tables.
        :param key_columns: List of columns from the CSV file you want for key fields.
        :param rows: This may be a derived table and we are loading from rows.
        :param context: Ignore for now.
        :param columns: List of columns from CSV file you want in your table.
        """
        self._table_name = table_name
        self._connect_info = connect_info
        self._entity_type = entity_type_name
        self._key_columns = key_columns
        self._columns = columns
        self._context = context

        if entity_type_name != "CSV":
            raise ValueError("entity_type_name must be CSV")

    def __str__(self):

        return "Cool"

    def find_by_primary_key(self, key_fields, field_list=None, context=None):
        """

        :param key_fields: The values for the key_columns, in order, to use to find a record. For example,
            for Appearances this could be ['willite01', 'BOS', '1960']
        :param field_list: A subset of the fields of the record to return. The CSV file or RDB table may have many
            additional columns, but the caller only requests this subset.
        :param context: Ignore for now.
        :return: None, or a dictionary containing the columns/values for the row.
        """
        pass

    def find_by_template(self, template, field_list=None, limit=None, offset=None, order_by=None, context=None):
        """

        :param template: A dictionary of the form { "field1" : value1, "field2": value2, ...}. The function will return
            a derived table containing the rows that match the template.
        :param field_list: A list of requested fields of the form, ['fielda', 'fieldb', ...]
        :param limit: Do not worry about this for now.
        :param offset: Do not worry about this for now.
        :param order_by: Do not worry about this for now.
        :param context: Ignore for now.
        :return: A derived table containing the computed rows.
        """
        pass

    def insert(self, new_entity, context=None):
        """

        :param new_record: A dictionary representing a row to add to the set of records. Raises an exception if this
            creates a duplicate primary key.
        :return: None
        """
        pass

    def delete_by_template(self, template, context=None):
        """

        Deletes all records that match the template.

        :param template: A template.
        :return: A count of the rows deleted.
        """
        pass

    def delete_by_key(self, key_fields, Context=None):
        """

        Delete record with corresponding key.

        :param key_fields: List containing the values for the key columns
        :return: A count of the rows deleted.
        """
        pass

    def update_by_template(self, template, new_values, context=None):
        """

        :param template: A template that defines which matching rows to update.
        :param new_values: A dictionary containing fields and the values to set for the corresponding fields
            in the records. This returns an error if the update would create a duplicate primary key. NO ROWS are
            update on this error.
        :return: The number of rows updates.
        """
        pass

    def update_by_key(self, key_fields, new_values, context=None):
        """

        :param key_fields: List of values for primary key fields
        :param new_values: A dictionary containing fields and the values to set for the corresponding fields
            in the records. This returns an error if the update would create a duplicate primary key. NO ROWS are
            update on this error.
        :return: The number of rows updates.
        """
        pass

    def query(self, query_statement, args, context=None):
        """
        Passed through/executes a raw query in the native implementation language of the backend.
        :param query_statement: Query statement as a string.
        :param args: Args to insert into query if it is a template
        :param context:
        :return: A JSON object containing the result of the operation.
        """
        pass

    def load(self, rows=None):
        """
        Loads data into the data table.
        :param rows:
        :return: Number of rows loaded.
        """
        pass

    def save(self, context):
        """
        Writes any cached data to a backing store.
        :param context:
        :return:
        """

