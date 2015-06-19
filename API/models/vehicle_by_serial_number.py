from cqlengine import Model, columns


class VehicleBySerialNumber(Model):

    __table_name__ = 'vehicle_by_serial_number'

    serial_number = columns.Text(primary_key=True, max_length=12)
    vehicle_trim = columns.Integer(primary_key=True)
    year = columns.Integer()
    make = columns.Text()
    model = columns.Text()
    trim_name = columns.Text()
