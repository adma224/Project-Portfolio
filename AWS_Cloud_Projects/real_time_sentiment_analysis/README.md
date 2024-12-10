# Sentiment Analysis deployed in AWS - Using SVM, Logistic Regression, and Bert for on-demand predictions

The goal of this project is to compare the power of **SVM**, **Logistic Regression**, and **BERT** in a text classification task as simple as Tweet Sentiment Analysis Classification. 

### What we know about the data

The data was extracted from a . It contains the following features

- target: the polarity of the tweet (0 = negative, 2 = neutral, 4 = positive)
- ids: The id of the tweet ( 2087)
- date: the date of the tweet (Sat May 16 23:58:44 UTC 2009)
- flag: The query (lyx). If there is no query, then this value is NO_QUERY.
- user: the user that tweeted (robotickilldozr)
- text: the text of the tweet (Lyx is cool)

To keep it simple we will only focus on 'target' and 'text' features for text classification.

### Data Pre-processing

In this notebook we will process and transform Tweet text data by using the following data transformation techniques:

- Tokenization
- Lemmatization
- Stop Words Removal
- Contractions conversion

### Feature Engineering

For this project we will initially use Tf-Idf vectorization for feature engineering. Once we have the Tf-Idf matrix ready, we will apply an SVDTransformer for dimentionality reduction.

### Validation and Evaluation

I will use gridsearch and k-fold cross-validation to perform multiple trainings and use AUC as an evaluation metric for hyperparameyter tuning. In our grid search we will test multiple hyperparameters as well as regularization algorithms.

### Deployment into production with AWS Sagemaker Hosting and Visualization with AWS QuickSight

The following AWS services will be used to deploy an API endpoint on-demand predictions and Data Visualizations:

AWS Sagemaker Hosting will deploy my ML models. For this, I will be using Docker to containerize my built inference models and deploy them in Sagemaker. I will be using A/B release strategy to load balance the traffic to different hosted inferences.

**AWS API Gateway** will be used to create an API endpoing where the request will return the respopnse of the inference model. 

**AWS Lambda** will take care of data transformation and preprocessing as well as evoking the Sagemaker inference. 

Requests will be stored in **AWS Aurora Servelress SQL** Database. 

**AWS QuickSight** will be used for data vizualization.
