class InstantiateCSVError(Exception):
    """
    Самодельный класс ошибки
    """

    def __init__(self, *args):
        if len(args) > 0:
            self.massage = args[0]
