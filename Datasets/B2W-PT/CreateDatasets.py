import sqlite3
import pandas as pd
from tqdm import tqdm

dat = sqlite3.connect('B2W_Reviews01.db')
df = pd.read_sql_query("SELECT * FROM B2W_Reviews01", dat)

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
    "Gender-Balanced": "/mnt/d/Documentos/Doutorado/TextRepresentation/Datasets/B2W-PT/Raw/B2W-Gender-Balanced"
}

def build_file(groupClass, entries, save_location, message=""):
    index = 0
    print(message)

    for entry in tqdm(entries):
        file_name = "%s/%s_%s.txt" % (save_location, groupClass, index)
        with open(file_name, 'w') as writer:
            writer.write(entry["review_text"])
        index += 1


def build_polarity(df, save_location):
    """
    Create all files of the B2W-Polarity dataset
    Negative class is 0
    Positive class is 1
    Neutral class is 2
    """
    df_negative = df.loc[(df['overall_rating'] == 1) | (df['overall_rating'] == 2)]
    df_positive = df.loc[(df['overall_rating'] == 4) | (df['overall_rating'] == 5)]
    df_neutral = df.loc[(df['overall_rating'] == 3)]

    negative = df_negative[['overall_rating', 'review_text']].to_dict('records')
    positive = df_positive[['overall_rating', 'review_text']].to_dict('records')
    neutral = df_neutral[['overall_rating', 'review_text']].to_dict('records')

    build_file("0", negative, save_location, "\n>>> Processing Polarity - Negative")
    build_file("1", positive, save_location, "\n>>> Processing Polarity - Positive")
    build_file("2", neutral, save_location, "\n>>> Processing Polarity - Neutral")

def build_polarity_balanced(df, save_location, random_state = 1):
    """
    Create all files of the B2W-Polarity-Balanced dataset
    Negative class is 0
    Positive class is 1
    Neutral class is 2
    """
    RANDOM_STATE = random_state

    df_negative = df.loc[(df['overall_rating'] == 1) | (df['overall_rating'] == 2)]
    df_positive = df.loc[(df['overall_rating'] == 4) | (df['overall_rating'] == 5)]
    df_neutral = df.loc[(df['overall_rating'] == 3)]

    lowest_number = min([   
            int(df_negative['overall_rating'].size),
            int(df_positive['overall_rating'].size),
            int(df_neutral['overall_rating'].size)
    ])

    negative = df_negative[['overall_rating', 'review_text']].sample(n=lowest_number, random_state = RANDOM_STATE).to_dict('records')
    positive = df_positive[['overall_rating', 'review_text']].sample(n=lowest_number, random_state = RANDOM_STATE).to_dict('records')
    neutral = df_neutral[['overall_rating', 'review_text']].sample(n=lowest_number, random_state = RANDOM_STATE).to_dict('records')

    build_file("0", negative, save_location, "\n>>> Processing Polarity Balanced - Negative")
    build_file("1", positive, save_location, "\n>>> Processing Polarity Balanced - Positive")
    build_file("2", neutral, save_location, "\n>>> Processing Polarity Balanced - Neutral")


def build_rating(df, save_location):
    """
    Create all files of the B2W-Rating dataset
    The available classes are the rating (1-5)
    """
    df_1 = df.loc[(df['overall_rating'] == 1)]
    df_2 = df.loc[(df['overall_rating'] == 2)]
    df_3 = df.loc[(df['overall_rating'] == 3)]
    df_4 = df.loc[(df['overall_rating'] == 4)]
    df_5 = df.loc[(df['overall_rating'] == 5)]

    rating_1 = df_1[['overall_rating', 'review_text']].to_dict('records')
    rating_2 = df_2[['overall_rating', 'review_text']].to_dict('records')
    rating_3 = df_3[['overall_rating', 'review_text']].to_dict('records')
    rating_4 = df_4[['overall_rating', 'review_text']].to_dict('records')
    rating_5 = df_5[['overall_rating', 'review_text']].to_dict('records')

    build_file("1", rating_1, save_location, "\n>>> Processing Rating 1")
    build_file("2", rating_2, save_location, "\n>>> Processing Rating 2")
    build_file("3", rating_3, save_location, "\n>>> Processing Rating 3")
    build_file("4", rating_4, save_location, "\n>>> Processing Rating 4")
    build_file("5", rating_5, save_location, "\n>>> Processing Rating 5")

def build_rating_balanced(df, save_location, random_state = 1):
    """
    Create all files of the B2W-Rating-Balanced dataset
    The available classes are the rating (1-5)
    """
    RANDOM_STATE = random_state

    df_1 = df.loc[(df['overall_rating'] == 1)]
    df_2 = df.loc[(df['overall_rating'] == 2)]
    df_3 = df.loc[(df['overall_rating'] == 3)]
    df_4 = df.loc[(df['overall_rating'] == 4)]
    df_5 = df.loc[(df['overall_rating'] == 5)]

    lowest_number = min([   
            int(df_1['overall_rating'].size),
            int(df_2['overall_rating'].size),
            int(df_3['overall_rating'].size),
            int(df_4['overall_rating'].size),
            int(df_5['overall_rating'].size)      
    ])

    rating_1 = df_1[['overall_rating', 'review_text']].sample(n=lowest_number, random_state = RANDOM_STATE).to_dict('records')
    rating_2 = df_2[['overall_rating', 'review_text']].sample(n=lowest_number, random_state = RANDOM_STATE).to_dict('records')
    rating_3 = df_3[['overall_rating', 'review_text']].sample(n=lowest_number, random_state = RANDOM_STATE).to_dict('records')
    rating_4 = df_4[['overall_rating', 'review_text']].sample(n=lowest_number, random_state = RANDOM_STATE).to_dict('records')
    rating_5 = df_5[['overall_rating', 'review_text']].sample(n=lowest_number, random_state = RANDOM_STATE).to_dict('records')

    build_file("1", rating_1, save_location, "\n>>> Processing Rating Balanced 1")
    build_file("2", rating_2, save_location, "\n>>> Processing Rating Balanced 2")
    build_file("3", rating_3, save_location, "\n>>> Processing Rating Balanced 3")
    build_file("4", rating_4, save_location, "\n>>> Processing Rating Balanced 4")
    build_file("5", rating_5, save_location, "\n>>> Processing Rating Balanced 5")


def build_recommend(df, save_location):
    """
    Create all files of the B2W-Rercommend dataset
    No is 0
    Yes is 1
    """
    df_no = df.loc[(df['recommend_to_a_friend'] == 'No')]
    df_yes = df.loc[(df['recommend_to_a_friend'] == 'Yes')]

    no = df_no[['recommend_to_a_friend', 'review_text']].to_dict('records')
    yes = df_yes[['recommend_to_a_friend', 'review_text']].to_dict('records')

    build_file("0", no, save_location, "\n>>> Processing Recommend - No")
    build_file("1", yes, save_location, "\n>>> Processing Recommend - Yes")

def build_recommend_balanced(df, save_location, random_state = 1):
    """
    Create all files of the B2W-Rercommend-Balanced dataset
    No is 0
    Yes is 1
    """
    RANDOM_STATE = random_state

    df_no = df.loc[(df['recommend_to_a_friend'] == 'No')]
    df_yes = df.loc[(df['recommend_to_a_friend'] == 'Yes')]

    lowest_number = min([   
            int(df_no['recommend_to_a_friend'].size),
            int(df_yes['recommend_to_a_friend'].size)  
    ])

    no = df_no[['recommend_to_a_friend', 'review_text']].sample(n=lowest_number, random_state = RANDOM_STATE).to_dict('records')
    yes = df_yes[['recommend_to_a_friend', 'review_text']].sample(n=lowest_number, random_state = RANDOM_STATE).to_dict('records')

    build_file("0", no, save_location, "\n>>> Processing Recommend - No")
    build_file("1", yes, save_location, "\n>>> Processing Recommend - Yes")


def build_gender(df, save_location):
    """
    Create all files of the B2W-Gender dataset
    F is 0
    M is 1
    """
    df_f = df.loc[(df['reviewer_gender'] == 'F')]
    df_m = df.loc[(df['reviewer_gender'] == 'M')]

    f = df_f[['reviewer_gender', 'review_text']].to_dict('records')
    m = df_m[['reviewer_gender', 'review_text']].to_dict('records')

    build_file("0", f, save_location, "\n>>> Processing Gender - F")
    build_file("1", m, save_location, "\n>>> Processing Gender - M")

def build_gender_balanced(df, save_location, random_state = 1):
    """
    Create all files of the B2W-Gender-Balanced dataset
    F is 0
    M is 1
    """
    RANDOM_STATE = random_state

    df_f = df.loc[(df['reviewer_gender'] == 'F')]
    df_m = df.loc[(df['reviewer_gender'] == 'M')]

    lowest_number = min([   
            int(df_f['reviewer_gender'].size),
            int(df_m['reviewer_gender'].size)  
    ])

    f = df_f[['reviewer_gender', 'review_text']].sample(n=lowest_number, random_state = RANDOM_STATE).to_dict('records')
    m = df_m[['reviewer_gender', 'review_text']].sample(n=lowest_number, random_state = RANDOM_STATE).to_dict('records')

    build_file("0", f, save_location, "\n>>> Processing Gender Balanced - F")
    build_file("1", m, save_location, "\n>>> Processing Gender Balanced - M")



build_polarity(df, B2W_SAVE_LOCATION["Polarity"])
build_polarity_balanced(df, B2W_SAVE_LOCATION["Polarity Balanced"])

build_rating(df, B2W_SAVE_LOCATION["Rating"])
build_rating_balanced(df, B2W_SAVE_LOCATION["Rating Balanced"])

build_recommend(df, B2W_SAVE_LOCATION["Recommend"])
build_recommend_balanced(df, B2W_SAVE_LOCATION["Recommend Balanced"])

build_gender(df, B2W_SAVE_LOCATION["Gender"])
build_gender_balanced(df, B2W_SAVE_LOCATION["Gender Balanced"])