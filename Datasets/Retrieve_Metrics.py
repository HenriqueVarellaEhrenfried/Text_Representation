from datetime import datetime
import multiprocessing as mp
import statistics
import glob
import os

FILES_IN = {
    "10kGNAD-DE" : "./10kGNAD-DE/Parsed/",
    "B2W-PT": "./B2W-PT/Raw/B2W-Rating-Balanced/",
    "MR": "./MR/Parsed/",
    "Ohsumed": "./Ohsumed/Output-dataset/"
}

class Metrics():
    def __init__(self, dataset_name, files_dir):
        self.input = files_dir
        self.files = self.read_files()
        self.tokens = []
        self.cores = 8
        self.final_data = []
        self.dataset_name = dataset_name

        self.calculate_metrics()

    def timestamp(self):
        now = datetime.now()
        return now.strftime("[%d/%m/%Y %H:%M:%S] ")

    def read_files(self):
        print(">> Reading files from:", self.input)
        f = glob.glob(self.input + "*.txt")
        return f

    def get_ranges(self, array, number):
        ranges = []
        print(">> There are", len(array), "itens to process")
        for _ in range(0, number):
            step = len(array)/number
            if ranges:
                a = int(ranges[-1])
                b = int(a + step)
                ranges.append(a)
                ranges.append(b)
            else:
                a = int(0)
                b = int(a + step)
                ranges.append(a)
                ranges.append(b) 
        # Observe that the last range is bigger to acoomodate missing jobs
        ranges[-1] = ranges[-1] + (len(array) - ranges[-1]) 
        return ranges

    def separe_sentences(self, doc):
        document_tokens = doc.split(" ")

        return len(document_tokens)

    def calculate_statistics(self):
        mean = statistics.mean(self.final_data)
        std_dev = statistics.pstdev(self.final_data)
        max_val = max(self.final_data)
        min_val = min(self.final_data)
        with open(self.dataset_name+'.txt', 'w') as fi:
            fi.write(">>> Dataset " + str(self.dataset_name) + " statistics <<<\n")
            fi.write("-- Total files: " + str(len(self.final_data)) + "\n") 
            fi.write("-- Mean: " + str(mean) + "\n")
            fi.write("-- Std Dev: " + str(std_dev) + "\n")
            fi.write("-- Max: " + str(max_val) + "\n")
            fi.write("-- Min: " + str(min_val) + "\n")

    def worker(self, id, files_in, return_dict):
        print(self.timestamp(), ">> Starting worker:", id)
        print(self.timestamp(), ">> Worker:", id, "has to process", len(files_in), "file(s)")
        num_tokens = []
        for file_in in files_in:
            f = open(file_in, "r")
            file_content = f.read()
            f.close()

            num_tokens.append(int(self.separe_sentences(file_content)))

        return_dict[id] = num_tokens
        print(self.timestamp(), "!! >> Worker [", id, "] finished its job")

    def calculate_metrics(self):        
        number_of_threads = self.cores

        array = self.files
        processes = []
        ranges = self.get_ranges(array,number_of_threads)
        y = 0
        
        manager = mp.Manager()
        return_dict = manager.dict()

        for i in range(0,number_of_threads):            
            processes.append(mp.Process(target=self.worker, args=(str(i), array[ranges[y]:ranges[y+1]], return_dict)))
            y = y + 2 

        for p in processes:
            p.start()

        for p in processes:
            p.join()        
    
        for rd in return_dict:
            for item in return_dict[rd]: 
                self.final_data.append(int(item))
        self.calculate_statistics()

b2w = Metrics("B2W-Rating", FILES_IN["B2W-PT"])
mr = Metrics("MR", FILES_IN["MR"])
_10kgnad = Metrics("10kGNAD", FILES_IN["10kGNAD-DE"])
ohsumed = Metrics("Ohsumed", FILES_IN["Ohsumed"])