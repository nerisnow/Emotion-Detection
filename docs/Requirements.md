# Requirements

<center>ISEAR Sentiment and Emotion Analysis</center>

Requirement Gathering:

About the Company?
Since we have the details of the project but not the company, we can arbitrarily choose a company that can benefit from an emotion detection system. We are thinking about representing the needs of an Online Shopping Company like Daraz who can benefit from the analysis of comments and reviews on their products.
Suppose Youtube decides to add a metric of measuring the video in the analytics page. This metric represents the overall sentiment of the audience, especially commenters based on emotion detection systems.

What is the main aim of this project?
Sentiment Analysis aims to detect positive, neutral, or negative feelings from text, whereas
Emotion Analysis aims to detect and recognize types of feelings through the expression of texts, such as anger, disgust, fear, happiness, sadness, and surprise.

Where can this project be used?
Gauging how happy our citizens are - Evaluating The Happy Planet Index (HPI) and societal wellbeing metrics
Pervasive computing, to serve the individual better.
Understanding the consumer.
To improve brand reputation and sales
Tone of an email before sending it out

Out of the list of emotions available, which ones will be used for this project?


anger, fear, happiness, sadness and excitement.

Given only text data without facial expressions and voice recordings, how do we approach this problem?
This task can be tackled using lexicon-based methods, machine learning, or a concept-level approach. Here, we are exploring how we can achieve this task via a machine learning approach, specifically using the deep learning technique.

What are the different difficulties one would face while handling text data?
Context-dependence of emotions within text, word-sense disambiguation, coreference resolution, lack of labelled emotion database.’
Word Sense disambiguation: One word can have multiple senses like
Bass: fish
Bass: tone of frequency
Bass : Type of instrument
A phrase can have an element of anger without using the word anger like “Shut Up!”.

How much data is available out there for such a task?
 ISEAR, which contains 2500 sentences, with 5 categories of emotions (it lacks “Surprise”).
Affective Text database consists of 250 sentences annotated with 6 categories of emotions, with another 1000 sentences as test data.

How was the labelling process conducted for the dataset?
crowd sourced to perform labelling using Mechanical Turk
A process, inspired by a DARPA translation project, which is also crowd-sourced, is put in place to validate the accuracy of labelling.

Where does this data come from?
product reviews, personal blogs/journals, social network websites, forums, fiction excerpts, analysis, critiques, and more.
anywhere that people discuss and share their opinion freely could be a source.

Is the data already preprocessed in any way?
Since it is highly possible the proportion of “neutral” sentences outweigh those with emotional elements. To understand the impact of this, sentences are passed into a sentiment analyzer to provide basic labels of “positive”, “neutral” or “negative”. This allows us to filter the set if necessary, and gives us a rough idea of the mix of sentences.

What steps have been taken to ensure the quality of the produced label?
Option to reject by the Requester.
Redundancy. Allow each Human Intelligence Task (HIT) to be completed by several different Turkers, and only select higher quality ones.
Ensure a minimum standard by putting in place a small test, before allowing actual labelling.
What evaluation metrics will be used for the model?
Precision
Accuracy unweighted
Recall
Confusion Matrix

How much data will be used for this task?
The dataset used in this experiment consists of 784,349 samples of informal short English messages (i.e. a collection of English tweets), with 5 emotion classes: anger, sadness, fear, happiness, excitement where 60% is used for training, 20% for validation and 20% for testing.


What is the deadline for this project?
Jan 9, 2021


What is the acceptance criteria? Any bar that we need to meet?

Is there any immediate platform that will be using this model?

If yes, any integration pre-information that we should be aware of?
