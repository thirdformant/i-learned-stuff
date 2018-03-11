import jsonpickle

class LearnObject:

    def __init__(self, logtime, message, tags):
        self.log_time = logtime.strftime("%Y-%m-%d %H:%M:%S")
        self.message = message
        self.tags = list(tags)

    def write_learnobject(self, logtime):
        frozen = jsonpickle.encode(self)
        with open("output/" + logtime.strftime("%Y-%m-%d_%H:%M:%S") + "_" + "learnlog.txt", "w") as outfile:
            outfile.write(frozen)
