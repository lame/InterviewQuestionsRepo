from cqlengine import Model, columns


class VehicleBySerialNumber(Model):

    __table_name__ = 'vehicle_by_serial_number'

    prefix = columns.Text(primary_key=True, max_length=4)
    remainder = columns.Text(primary_key=True, max_length=8)
    vehicle_trim = columns.Integer(primary_key=True)
    serial_number = columns.Text(max_length=12)
    year = columns.Integer()
    make = columns.Text()
    model = columns.Text()
    trim_name = columns.Text()
