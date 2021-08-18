from tqdm import tqdm
import importlib
import shutil
import glob
import os

class ProcessDataset():
    def __init__(self, dataset):
        # Constants
        self.INPUT_PATH = "./Dataset/" + dataset + "/Raw/"
        self.OUPUT_PATH = "./Dataset/" + dataset + "/"

        # Parameters passed
        self.dataset = dataset

        # Call Method
        method = getattr(self, dataset)   
        method()


    def read_files(self, input):
        return glob.glob(input+"/*")

    def process_mr(self, set): 
        print(">> Processing", set, "set")
        with open(self.INPUT_PATH + "label_"+set.lower()+".txt", "r") as f:
            label_content = [line.rstrip() for line in f]

        with open(self.INPUT_PATH + "text_"+set.lower()+".txt", "r") as f:
            text_content = [line.rstrip() for line in f]

        SIZE = len(label_content) 
        
        print(">> Processing dataset [", set, "]")
        for i in tqdm(range(0, SIZE)):
            # File name must be class_id.txt
            name = label_content[i] + "_" + str(i) + ".txt"
            path = self.OUPUT_PATH + set + "/" + name
            with open(path, "w") as file_out:
                file_out.write(text_content[i])

    def process_ohsumed(self, set):
        print(">> Processing", set, "set")
        if set == "Train":
            set_name = "training"
        elif set == "Test":
            set_name = 'test'

        PATH_IN = self.INPUT_PATH + "ohsumed_single_23/" + set_name + "/"
        OUTPUT = self.OUPUT_PATH + set + "/"
        for i in range(1,24):
            print(">> Working on class", i)
            path_in = PATH_IN    
            directory = 'C' + str(format(i, '02d')) + "/"
            path_in += directory
            files = self.read_files(path_in)
            for f in tqdm(files):
                file_name = f.split("/")[-1]
                shutil.copyfile(f, OUTPUT + str(i) + "_" + file_name + ".txt")

    def process_irony_pt(self, set):
        # Dataset from https://github.com/fabio-ricardo/deteccao-ironia
        #  1 = Ironic | 0 = Non Ironic

        # file[0] = username;date;retweets;favorites;text;geo;mentions;hashtags;id;permalink
        #              0    ; 1  ;    2   ;   3     ;  4 ; 5 ;     6  ;   7    ; 8;   9 
        print(">> Processing", set, "set")
        OUTPUT = self.OUPUT_PATH + set + "/"

        with open(self.INPUT_PATH + "/ironia.csv", "r") as f:
            ironia_raw = [line.rstrip() for line in f]

        with open(self.INPUT_PATH + "/nao-ironico.csv", "r") as f:
            nao_ironico_raw = [line.rstrip() for line in f]

        print(ironia_raw[0].split(";")[8])
        size_irony = len(ironia_raw)
        size_not_irony = len(nao_ironico_raw)
        print("Irony Length:", size_irony, "\nNon Irony Length:", size_not_irony)

        print(">> Processing Irony dataset [", set, "]")
        for i in tqdm(range(1, size_irony)):
            irony = ironia_raw[i].split(";")
            name = "1" + "_" + str(irony[8][1:-1]) + ".txt"
            path = OUTPUT + name

            with open(path, "w") as file_out:
                file_out.write(irony[4][1:-1])

        print(">> Processing Non Irony dataset [", set, "]")
        for i in tqdm(range(1, size_not_irony)):
            not_irony = nao_ironico_raw[i].split(";")
            name = "0" + "_" + str(not_irony[8][1:-1]) + ".txt"
            path = OUTPUT + name

            with open(path, "w") as file_out:
                file_out.write(not_irony[4][1:-1])

    def process_semeval2018_task3A(self, set):
        print(">> Processing", set, "set")
        Files = {
            "Train": ["SemEval2018-T3-train-taskA.txt"],
            "Test": ["SemEval2018-T3_input_test_taskA.txt"]
        }
        OUTPUT = self.OUPUT_PATH + set + "/"

        for f in Files[set]:
            tweets = []
            with open(self.INPUT_PATH + f, "r") as fo:
                tweets = [line.rstrip() for line in fo]

        length_task_A = len(tweets)

        print(">> Processing SemEval 2018 Task 3A dataset [", set, "]")
        for i in tqdm(range(1, length_task_A)):
            splitted = tweets[i].split("\t")

            assigned_id = splitted[0]
            assigned_class = splitted[1]
            tweet = splitted[2]

            name = str(assigned_class) + "_" + str(assigned_id) + ".txt"
            path = OUTPUT + name

            with open(path, "w") as file_out:
                file_out.write(tweet)

    def process_semeval2018_task3B(self, set):
        print(">> Processing", set, "set")
        Files = {
            "Train": ["SemEval2018-T3-train-taskB.txt"],
            "Test": ["SemEval2018-T3_input_test_taskB.txt"]
        }
        OUTPUT = self.OUPUT_PATH + set + "/"

        for f in Files[set]:
            tweets = []
            with open(self.INPUT_PATH + f, "r") as fo:
                tweets = [line.rstrip() for line in fo]

        length_task_B = len(tweets)

        print(">> Processing SemEval 2018 Task 3B dataset [", set, "]")
        for i in tqdm(range(1, length_task_B)):
            splitted = tweets[i].split("\t")

            assigned_id = splitted[0]
            assigned_class = splitted[1]
            tweet = splitted[2]

            name = str(assigned_class) + "_" + str(assigned_id) + ".txt"
            path = OUTPUT + name

            with open(path, "w") as file_out:
                file_out.write(tweet)

    def process_IDPT2021(self, set):

        print(">> Processing", set, "set")
        OUTPUT = self.OUPUT_PATH + set + "/"

        with open(self.INPUT_PATH + "Training/training_news.csv", "r") as f:
            news_raw = [line.rstrip() for line in f]

        with open(self.INPUT_PATH + "Training/training_tweets.csv", "r") as f:
            tweets_raw = [line.rstrip() for line in f]

        raw_text = [news_raw, tweets_raw]
        dataset = "News"
        for rt in raw_text:
            print("\n>> Processing IDPT 2021", dataset, "dataset [", set, "]")
            size = len(rt)
            print("SIZE:", size)
            for i in tqdm(range(1, size)):
                item = rt[i].split("\t")
                if dataset == "News":
                    class_ = str(item[1][1:-1])
                else:
                    class_ = str(item[1])
                text = str(item[0][1:-1])
                
                name = class_ + "_" + dataset + "_" + str(i) + ".txt"
                path = OUTPUT + name

                with open(path, "w") as file_out:
                    file_out.write(text)

            dataset = "Tweets"


    def MR(self):
        self.process_mr("Test")
        self.process_mr("Train")

    def Ohsumed(self):
        self.process_ohsumed("Train")
        self.process_ohsumed("Test")

    def Irony_pt(self):
        self.process_irony_pt("Train")
        # self.process_irony_pt("Test")

    def SemEval2018_Task3A(self):
        self.process_semeval2018_task3A("Train")
        self.process_semeval2018_task3A("Test")

    def SemEval2018_Task3B(self):
        self.process_semeval2018_task3B("Train")
        self.process_semeval2018_task3B("Test")
    
    def IDPT_2021(self):
        self.process_IDPT2021("Train")

ProcessDataset("IDPT_2021")
