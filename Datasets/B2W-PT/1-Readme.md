# B2W Reviews

This dataset was published in the STIL 2019:
http://comissoes.sbc.org.br/ce-pln/stil2019/accepted.html

B2W-Reviews01: An open product reviews corpus - Livy Real (B2W Digital); Marcio Oshiro (B2W Digital); Alexandre Mafra (B2W Digital);

Real, L., Oshiro, M., Mafra, A.: B2w-reviews01: An open product reviews corpus. Proceedings of STIL - Symposium in Information and Human Language Technology (2019)

[GitHub Link](https://github.com/b2w-digital/b2w-reviews01)

The file `Metrics.ipynb` presents some metrics about the dataset.

Using the provided dataset eight datasets were created. They are `B2W-Polarity`, `B2W-Polarity-Balanced`, `B2W-Rating`, `B2W-Rating-Balanced`, `B2W-Recommend`, `B2W-Recommend-Balanced`, `B2W-Gender` and `B2W-Gender-Balanced`.

## The eight datasets

In this Section the creation process of each of the datasets is described.


### B2W-Polarity

In this dataset, the categories 1 and 2 were grouped into the class Negative (0), the categories 4 and 5 were grouped int othe class Positive (1) and the category 3 was renamed to class Neutral (2).

| Rating | Count |
| ------ | ----- |
| 1      | 27369 |
| 2      | 8389  |
| 3      | 16315 |
| 4      | 32345 |
| 5      | 47955 |

Therefore, the number of reviews by class is shown in the following table:

| Class    | Count |
| -------- | ----- |
| Negative | 35758 |
| Neutral  | 16315 |
| Positive | 80300 |
|----------|-------|
| **TOTAL**|132373 |

The test dataset is composes of 500 documents from each class.

### B2W-Polarity-Balanced

In this dataset, the categories 1 and 2 were grouped into the class Negative (0), the categories 4 and 5 were grouped int othe class Positive (1) and the category 3 was renamed to class Neutral (2).

| Rating | Count |
| ------ | ----- |
| 1      | 27369 |
| 2      | 8389  |
| 3      | 16315 |
| 4      | 32345 |
| 5      | 47955 |

As showed by the B2W-Polarity dataset, the number of reviews are unbalanced across classes, as the following table shows:

| Class    | Count |
| -------- | ----- |
| Negative | 35758 |
| Neutral  | 16315 |
| Positive | 80300 |
|----------|-------|
| **TOTAL**|132373 |

In this dataset, classes Negative and Positive are reduced to be contain the same ammount of reviews as the Neutral class. The selection of the reviews are made randomly. Resulting in the dataset described by the following table:

| Class    | Count |
| -------- | ----- |
| Negative | 16315 |
| Neutral  | 16315 |
| Positive | 16315 |
|----------|-------|
| **TOTAL**| 48945 |


The test dataset is composes of 500 documents from each class.

### B2W-Rating

In this dataset the rating of the reviews are the classes. The Rating 1 is the lowest rate while 5 is the best rate.

| Rating    | Count   |
| --------- | ------- |
| 1         | 27369   |
| 2         | 8389    |
| 3         | 16315   |
| 4         | 32345   |
| 5         | 47955   |
| --------  | ------- |
| **TOTAL** | 132373  |

The test dataset is composes of 500 documents from each class.

### B2W-Rating-Balanced

In this dataset the rating of the reviews are the classes. The Rating 1 is the lowest rate while 5 is the best rate. Differently from the B2W-Rating dataset, in this dataset all classes contain the same number of reviews. The removal of reviews in the ratings 1, 3, 4 and 5 were made randomly.

| Rating    | Count   |
| --------- | ------- |
| 1         | 8389    |
| 2         | 8389    |
| 3         | 8389    |
| 4         | 8389    |
| 5         | 8389    |
| --------  | ------- |
| **TOTAL** | 41945   |

The test dataset is composes of 500 documents from each class.

### B2W-Recommend

In this dataset there is 2 classes, the No (0) and Yes (1). The null values are removed from the dataset since it can't be set neither "Yes" nor "No". The original numbers are showed in the table below

| Recommend to a friend | Count |
| --------------------- | ----- |
| No                    | 35987 |
| Yes                   | 96368 |
| null                  | 18    |

Therefore, the final dataset has the following shape:

| Recommend to a friend | Count |
| --------------------- | ----- |
| No                    | 35987 |
| Yes                   | 96368 |
|-----------------------|-------|
| **TOTAL**             | 132355|

The test dataset is composes of 500 documents from each class.


### B2W-Recommend-Balanced

In this dataset there is 2 classes, the No (0) and Yes (1). The null values are removed from the dataset since it can't be set neither "Yes" nor "No". The original numbers are showed in the table below

| Recommend to a friend | Count |
| --------------------- | ----- |
| No                    | 35987 |
| Yes                   | 96368 |
| null                  | 18    |

Additionaly, the classes were balanced to contain the same number of reviews. Therefore, The "Yes" class lost some reviews randomly, leading to the following final dataset:

| Recommend to a friend | Count |
| --------------------- | ----- |
| No                    | 35987 |
| Yes                   | 35987 |
|-----------------------|-------|
| **TOTAL**             | 71974 |

The test dataset is composes of 500 documents from each class.


### B2W-Gender

In this dataset there is 2 classes, the F (Female,, represented by 0) and M (Male, represented by 1). The null values are removed from the dataset since it can't be set neither "F" nor "M". The original numbers are showed in the table below

| Gender | Count |
| ------ | ----- |
| F      | 62071 |
| M      | 66166 |
| null   | 4136  |

Therefore, the final dataset has the following shape:


| Gender    | Count   |
| --------- | ------- |
| F         | 62071   |
| M         | 66166   |
| --------  | ------- |
| **TOTAL** | 128237  |

The test dataset is composes of 500 documents from each class.


### B2W-Gender-Balanced

In this dataset there is 2 classes, the F (Female,, represented by 0) and M (Male, represented by 1). The null values are removed from the dataset since it can't be set neither "F" nor "M". The original numbers are showed in the table below

| Gender | Count |
| ------ | ----- |
| F      | 62071 |
| M      | 66166 |
| null   | 4136  |

Additionaly, the classes were balanced to contain the same number of reviews. Therefore, The "M" class lost some reviews randomly, leading to the following final dataset:


| Gender    | Count   |
| --------- | ------- |
| F         | 62071   |
| M         | 62071   |
| --------  | ------- |
| **TOTAL** | 124142  |

The test dataset is composes of 500 documents from each class.

## Objectives

The following table specifies all datasets objectives and sizes

| Dataset                | Objective                                                   | Balanced | Dataset size | Number of classes | Train dataset size | Test dataset size |
| ---------------------- | ----------------------------------------------------------- | -------- | ------------ | ----------------- | ------------------ | ----------------- |
| B2W-Polarity           | Classify polarity of the review                             | NO       | 132373       | 3                 | 132223             | 1500              |
| B2W-Polarity-Balanced  | Classify polarity of the review                             | YES      | 48945        | 3                 | 47445              | 1500              |
| B2W-Rating             | Classify rating of the review                               | NO       | 132373       | 5                 | 129873             | 2500              |
| B2W-Rating-Balanced    | Classify rating of the review                               | YES      | 41945        | 5                 | 39445              | 2500              |
| B2W-Recommend          | Predict if a product is recommended or not                  | NO       | 132355       | 2                 | 131355             | 1000              |
| B2W-Recommend-Balanced | Predict if a product is recommended or not                  | YES      | 71974        | 2                 | 70974              | 1000              |
| B2W-Gender             | Identify if the text was written by a male or female person | NO       | 128237       | 2                 | 127237             | 1000              |
| B2W-Gender-Balanced    | Identify if the text was written by a male or female person | YES      | 124142       | 2                 | 123142             | 1000              |