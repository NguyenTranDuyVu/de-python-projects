class Validator:
    @classmethod
    def get_from_a_list(cls, message, values):
        while True:
            content = input(message)
            for v in values:
                if v == content:
                    return v
