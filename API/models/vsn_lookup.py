from cqlengine import Model, columns


class VSNLookup(Model):

    __table_name__ = 'vsn_lookup'

    prefix = columns.Text(primary_key=True, max_length=4)
    remainder = columns.Text(primary_key=True, max_length=8)
    vehicle_trim = columns.Integer(primary_key=True)
    serial_number = columns.Text(max_length=12)
