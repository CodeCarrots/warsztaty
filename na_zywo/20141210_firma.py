class Pracownik:
    ilu = 0
    def __init__(self, name, job):
        self.name = name
        self.job = job
        Pracownik.ilu += 1
    
    def get_name(self):
        print(self.name)
    
    def get_count(self):
        print(Pracownik.ilu)

    def change_job(self, new_job):
        self.job = new_job

class Komputer:
    
    def __init__(self, name, type):
        self.name = name
        self.type = type
        self.worker = None
        
    def get_name(self):
        print(self.get_name)
    
    def give_to(self, worker):
        self.worker = worker
	
    def	whose(self):
        print(self.worker.get_name())
	
	