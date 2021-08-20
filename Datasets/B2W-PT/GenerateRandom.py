import random
import os
import shutil
from tqdm import tqdm

# `B2W-Polarity`                -> build_polarity
# `B2W-Polarity-Balanced`       -> build_polarity_balanced
# `B2W-Rating`                  -> build_rating
# `B2W-Rating-Balanced`         -> build_rating_balanced
# `B2W-Recommend`               -> build_recommend
# `B2W-Recommend-Balanced`      -> build_recommend_balanced
# `B2W-Gender`                  -> build_gender
# `B2W-Gender-Balanced`         -> build_gender_balanced
B2W_SAVE_LOCATION ={
    "Polarity": "/mnt/d/Documentos/Doutorado/TextRepresentation/Datasets/B2W-PT/Raw/B2W-Polarity",
    "Polarity Balanced": "/mnt/d/Documentos/Doutorado/TextRepresentation/Datasets/B2W-PT/Raw/B2W-Polarity-Balanced",
    "Rating": "/mnt/d/Documentos/Doutorado/TextRepresentation/Datasets/B2W-PT/Raw/B2W-Rating",
    "Rating Balanced": "/mnt/d/Documentos/Doutorado/TextRepresentation/Datasets/B2W-PT/Raw/B2W-Rating-Balanced",
    "Recommend": "/mnt/d/Documentos/Doutorado/TextRepresentation/Datasets/B2W-PT/Raw/B2W-Recommend",
    "Recommend Balanced": "/mnt/d/Documentos/Doutorado/TextRepresentation/Datasets/B2W-PT/Raw/B2W-Recommend-Balanced",
    "Gender": "/mnt/d/Documentos/Doutorado/TextRepresentation/Datasets/B2W-PT/Raw/B2W-Gender",
    "Gender Balanced": "/mnt/d/Documentos/Doutorado/TextRepresentation/Datasets/B2W-PT/Raw/B2W-Gender-Balanced"
}

def random_numbers(numLow, numHigh, n=1000):
    return random.sample(range(numLow, numHigh), n)

def mount_name(category, items):
    name_list = []
    for i in items:
        name_list.append("%s_%s.txt" % (category, str(i)))
    return name_list

def move_files(files, location, message=""):
    print(message)

    if not(os.path.exists("%s/Test" % (location))):
        os.makedirs("%s/Test" % (location))

    for file_name in tqdm(files):
        shutil.move("%s/%s" % (location, file_name), "%s/Test/%s" % (location, file_name))

# ================================================================================

def build_polarity(location):
    selected_files_negative = random_numbers(0,35758,500)
    selected_files_positive = random_numbers(0,80300,500)
    selected_files_neutral = random_numbers(0,16315,500)

    file_negative = mount_name("0",selected_files_negative)
    file_positive = mount_name("1",selected_files_positive)
    file_neutral = mount_name("2",selected_files_neutral)

    all_files = file_negative + file_positive + file_neutral

    move_files(all_files, location, "\n>>> Processing Polarity Test Set")
    
def build_polarity_balanced(location):
    selected_files_negative = random_numbers(0,16315,500)
    selected_files_positive = random_numbers(0,16315,500)
    selected_files_neutral = random_numbers(0,16315,500)

    file_negative = mount_name("0",selected_files_negative)
    file_positive = mount_name("1",selected_files_positive)
    file_neutral = mount_name("2",selected_files_neutral)

    all_files = file_negative + file_positive + file_neutral

    move_files(all_files, location, "\n>>> Processing Polarity Balanced Test Set")

def build_rating(location):
    selected_files_rating1 = random_numbers(0,27369,500)
    selected_files_rating2 = random_numbers(0,8389,500)
    selected_files_rating3 = random_numbers(0,16315,500)
    selected_files_rating4 = random_numbers(0,32345,500)
    selected_files_rating5 = random_numbers(0,47955,500)


    files_rating1 = mount_name("1",selected_files_rating1)
    files_rating2 = mount_name("2",selected_files_rating2)
    files_rating3 = mount_name("3",selected_files_rating3)
    files_rating4 = mount_name("4",selected_files_rating4)
    files_rating5 = mount_name("5",selected_files_rating5)
    
    all_files = files_rating1 + files_rating2 + files_rating3 + files_rating4 + files_rating5

    move_files(all_files, location, "\n>>> Processing Rating Test Set")

def build_rating_balanced(location):
    selected_files_rating1 = random_numbers(0,8389,500)
    selected_files_rating2 = random_numbers(0,8389,500)
    selected_files_rating3 = random_numbers(0,8389,500)
    selected_files_rating4 = random_numbers(0,8389,500)
    selected_files_rating5 = random_numbers(0,8389,500)


    files_rating1 = mount_name("1",selected_files_rating1)
    files_rating2 = mount_name("2",selected_files_rating2)
    files_rating3 = mount_name("3",selected_files_rating3)
    files_rating4 = mount_name("4",selected_files_rating4)
    files_rating5 = mount_name("5",selected_files_rating5)
    
    all_files = files_rating1 + files_rating2 + files_rating3 + files_rating4 + files_rating5

    move_files(all_files, location, "\n>>> Processing Rating Balanced Test Set")

def build_recommend(location):
    selected_files_yes = random_numbers(0,96368,500)
    selected_files_no = random_numbers(0,35987,500)

    files_rating_yes = mount_name("1",selected_files_yes)
    files_rating_no = mount_name("0",selected_files_no)
    
    all_files = files_rating_yes + files_rating_no

    move_files(all_files, location, "\n>>> Processing Recommend Test Set")

def build_recommend_balanced(location):
    selected_files_yes = random_numbers(0,35987,500)
    selected_files_no = random_numbers(0,35987,500)

    files_rating_yes = mount_name("1",selected_files_yes)
    files_rating_no = mount_name("0",selected_files_no)
    
    all_files = files_rating_yes + files_rating_no

    move_files(all_files, location, "\n>>> Processing Recommend Balanced Test Set")

def build_gender(location):
    selected_files_f = random_numbers(0,62071,500)
    selected_files_m = random_numbers(0,66166,500)

    files_rating_f = mount_name("0",selected_files_f)
    files_rating_m = mount_name("1",selected_files_m)
    
    all_files = files_rating_f + files_rating_m

    move_files(all_files, location, "\n>>> Processing Gender Test Set")

def build_gender_balanced(location):
    selected_files_f = random_numbers(0,62071,500)
    selected_files_m = random_numbers(0,62071,500)

    files_rating_f = mount_name("0",selected_files_f)
    files_rating_m = mount_name("1",selected_files_m)
    
    all_files = files_rating_f + files_rating_m

    move_files(all_files, location, "\n>>> Processing Gender Balanced Test Set")


build_polarity(B2W_SAVE_LOCATION["Polarity"])
build_polarity_balanced(B2W_SAVE_LOCATION["Polarity Balanced"])

build_rating(B2W_SAVE_LOCATION["Rating"])
build_rating_balanced(B2W_SAVE_LOCATION["Rating Balanced"])

build_recommend(B2W_SAVE_LOCATION["Recommend"])
build_recommend_balanced(B2W_SAVE_LOCATION["Recommend Balanced"])

build_gender(B2W_SAVE_LOCATION["Gender"])
build_gender_balanced(B2W_SAVE_LOCATION["Gender Balanced"])