class StealFormatter:
    def __init__(self, result):
        self.result = result
        self.user = result.user
        self.metadata = result.metadata
        self.target_sfx = self.metadata["target_sfx"]
        self.victim = self.metadata["victim"]

    def format(self):
        return f"@{self.user} stole !{self.target_sfx} from @{self.victim}"
