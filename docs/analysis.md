# **CLIENT PROJECT : EMOTION DETECTION AND ANALYSIS**

### **Epic**:

As an Admin, I want a system that is able to classify reviews regarding my AI courses, into different human emotions so that I can integrate the review summarization data as a feedback in the further improvement of the courses, without the need of manual data annotators.

### **User Story**:

- As a user, I want a system that takes my student review as its inputs so that the reviews reach the content creators.
- As an Admin, I want the system to classify the incoming student reviews into 5 different human emotions namely: anger, sadness, fear, happiness, excitement.
- As a user, I want the system to correctly identify the intent of my review so that the right feedback reaches the creators.
- As an admin, I want the system to output an easy visualization of the result rather than a probabilistic result so that all my teammates from various departments can interpret the results.
- As an Admin, I want the system to group the reviews according to the classified emotions so that it is convenient for me to check the review summarization according to my need.
- As an Admin, I want the system to be faster in terms of the time taken to classify a certain student review, compared to a human data annotator so that the feedback can be integrated early.


### **Problem and Solution Formation**:

#### What is the problem?
I need a system that tells me which kind of emotion is a given review depicting.


Formally,

|        |          |  |
| ------------- |:-------------:| -----:|
|Task (T)| Classify an unseen review in terms of the emotion it conveys: anger, sadness, fear, happiness, excitement and group those reviews for a better visualization|
| Experience (E) | A dataset consisting of 784,349 samples of informal short English messages  with one of the 5 emotion classes labelled in each of them: anger, sadness, fear, happiness, excitement. |
| Performance (P) | It would be considered a success if the accuracy or f1 score of the model is over 50% for test data|
#### Assumptions:

- The reviews are labeled.
- The reviews will be written in the English language.
- Each review is independent of the other.


#### Similar problems:
- Email spam detection
- Social media comments analysis
- Restaurant review analysis
- Clickbait title detection

#### Why does this problem need to be solved?
 Data Annotation is quite a tiresome manual task when you look at a bunch of reviews coming from the users. Moreover, not all reviews are meaningful for the improvement of the product. Automating the classification of reviews would save time and energy of data annotators and also make it easy for them to look into specific classes of reviews, rather than the whole bulk.
This solution could save the company time as well as money for hiring full time data annotators solely dedicated to go through the feedback alone.
The proposed solution can be used not just for a specific course, but for other similar problem scenarios where one needs to summarize and analyze student reviews.
The system however, needs to be updated timely, as the real-time data changes according to the course. The changes include model retraining, with new incoming training data.


 ### **Data Required for completing the project**:
- The data available to us is a dataset consisting of 784,349 samples of informal short English messages (i.e. a collection of English tweets), with 5 emotion classes: anger, sadness, fear, happiness, excitement where 60% is used for training, 20% for validation and 20% for testing.
- The available data are tweets and not any kind of review.
- Currently, the company is  storing their student review data in Google Sheets directly filled from the feedback coming from Google Form reviews from the students.
- The company does have data annotators who go through the reviews. Moreover, the company also has a separate team for Data and Analytics.
- Other sources of data that can be integrated into the training process include the reviews from the students taking the courses.


#### How would I solve the problem?
- Manually, we would hire data annotators who would go through each review and classify them according to the need basis.
For this, the data would be received directly from student online reviews and feedback.
This method would not be consistent, as each annotator would have their own way of interpreting reviews. Some reviews might also be skipped because of lack of understanding itself. Moreover, detecting sarcastic reviews would also be a potential barrier in correct interpretation and classification of reviews. Not all annotators would be familiar with all kinds of idioms used in the feedback. Hence, the diversity in the language used could also act as a barrier if we propose a manual solution.


- Using a **Machine Learning approach**, we would propose a solution in the following way:
1. Since it is an NLP task and specifically a classification problem, a baseline approach could be to use a simple Naive Bayes classifier for the emotion classification.
2. Other approaches could includea Random Forest Classifier or a Support Vector Classification.


### **Performance Metrics for the solution**:

The Perfomance metric that will be monitored for this system are:
- Accuracy Score
- F1 Score
