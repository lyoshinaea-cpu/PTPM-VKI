class Controller:
    def __init__(self, calculator, database, user_interface, external_service):
        self.calculator = calculator
        self.database = database
        self.user_interface = user_interface
        self.external_service = external_service

    def run(self):
        a, b, c = self.user_interface.get_data()

        record = self.database.get_record(a, b, c)

        if record is None:
            triangle_type, error_message = self.calculator.calculate(a, b, c)

            self.database.add_record(
                a, b, c, triangle_type, error_message
            )
        else:
            triangle_type, error_message = record

        if error_message:
            result = f"Ошибка: {error_message}"
        else:
            result = f"Тип треугольника: {triangle_type}"

        self.external_service.send_result(result)
        return result
