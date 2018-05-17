class TestCaseInfo(object):
    """description of class"""
    def __init__(self, id="", name="", author="", result="Failed", start_time="", end_time="", seconds_duration="", error_info=""):
        self.id = id
        self.name = name
        self.author = author
        self.result = result
        self.start_time = start_time
        self.end_time = end_time
        self.seconds_duration = seconds_duration
        self.error_info = error_info

