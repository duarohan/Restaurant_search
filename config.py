import os
import json

class Config:
    def __init__(self):
        self.config = {}
        current_dir = os.getcwd()
        with open(os.path.join(current_dir, 'config', 'base.json')) as base_file:
            base_json = json.load(base_file)
            self.config = base_json.copy()
    
    def getConfig(self):
        return self.config

def main():
    config = Config().getConfig()

if __name__ == "__main__":
    main()   