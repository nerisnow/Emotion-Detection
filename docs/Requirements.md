## ISEAR Sentiment and Emotion Analysis

### Requirement Gathering:

#### 1. About the Company?

Since we have the details of the project but not the company, we can arbitrarily choose a company that can benefit from an emotion detection system. We are thinking of implementing an emotion detection system to categorise the emotions in provided feedback that are collected from students studying the courses through Fusemachines.

Fusemachines’ goal is to “Democratize AI” i.e. to empower local communities by giving them opportunities  to build the next generation of AI products. One of the key ways to do so, is to provide AI education that can be easily accessible to people of every race, gender and background. Fusemachines operate in three levels of services: Fuse Classroom, Fuse Education and Fuse Talents.


#### 2. Context of Product:

With that aim of “Democratizing AI”, the company is coming up with a number of courses that students can take. There will always be the constant pressure to improve the courses materials like reading materials, slides, pedagogy, classes durations & effectiveness and assignments. One of the primary ways to improve such course materials is via working on the feedback from students who take the courses.


**2.1. Why do you need this new system?**

With the monotonic increment in the number of students along with the number of courses, the feedback for each will start piling up. It is crucial to understand the needs of the students and the needs of the market. To attend to all the feedback with different moods and emotions at once is a very gruesome task. If the feedback could be categorised on the basis of the emotions like happiness, sadness or anger, the person who analyzes the feedback will have the proper mindset and the idea regarding the particular course. If the feedback for a course specifically a reading material is consistently sadness or anger frequently, it is paramount to understand that the reading material needs changes to be made.
Similarly, for the contents that generate feedback with emotions like happiness or surprise is bound to have met the needs of the students. That particular content can be analysed and the style, formatting, description could be imitated in other reading materials.

**2.2. What is the business need?**

The system can bring efficiency in feedback management and will help to improve the course contents based on students needs.

**2.3. Is there a system in place to do it right now (even if manual)? If so, how is it done right now? Is the process documented?**

The process of collecting feedback from students regarding different aspects of teaching and learning are documented using Google forms and analyzed manually.
- After the end of any session, course, completing of assignments or anything related to content, students are asked to fill the feedback form which queries how students felt about the session.
- The collected feedbacks are looked up one by one for any that indicate a need for change  or modification in the contents and summarised in a report
- The specified feedback is then passed on to the respect teams for reiteration of the materials along with the HOSs and senior managers for evaluations.


#### 3. About the new system/project

**3.1. What is the main aim of this project?**

- Sentiment Analysis aims to detect positive, neutral, or negative feelings from text, whereas
- Emotion Analysis aims to detect and recognize types of feelings through the expression of texts, such as anger, disgust, fear, happiness, sadness, and surprise.
- Using emotion detection we intend to automate the process of filtering out feedback

**3.2. Where can this project be used?**

The project can be used to analyse the feedback from students. The feedbak with positive sentiment or emotions indicating happiness, suprise will semantically mean that the contents are good. That motivation can promt the changes in contents that are categorised with negative sentiments or emtions like sadness or anger. The analyser doesnt have to go through each feedback to categorise and dispatch to respective team. Based on the emotions of the feedback we would be able to distinguish contents that meet the students need. These contents will be a baseline for developing other materials.


**3.3. Out of the list of emotions available, which ones will be used for this project?**

anger, fear, happiness, sadness and excitement.

**3.4. What features don't you like about the current system?**
The manual needs to go through each and every feedback particularly not knowing its abstract nature. When the quantity of feedback increases (which is bound to increase with increasing courses and enrolling students), the process of analysing and categorising feedback manually in sheets will be very time consuming and gruesome.


**3.5. Given only text data without facial expressions and voice recordings, how do we approach this problem?**

This task can be tackled using lexicon-based methods, machine learning, or a concept-level approach. Here, we are exploring how we can achieve this task via a machine learning approach, specifically using the deep learning technique.

#### 4. About the data

**4.1. What are the different difficulties one would face while handling text data?**

Context-dependence of emotions within text, word-sense disambiguation, coreference resolution, lack of labelled emotion database.’
Word Sense disambiguation: One word can have multiple senses like:
Bass: fish
Bass: tone of frequency
Bass : Type of instrument
A phrase can have an element of anger without using the word anger like “Shut Up!”.

Special Characters and Stop Words


**4.2. How much data is available out there for such a task?**

- ISEAR, which contains 2500 sentences, with 5 categories of emotions (it lacks “Surprise”).
- Affective Text database consists of 250 sentences annotated with 6 categories of emotions, with another 1000 sentences as test data.

These data will be used to train and test the model

**4.3. How was the labelling process conducted for the dataset?**

Crowd sourced to perform labelling using Mechanical Turk
A process, inspired by a DARPA translation project, which is also crowd-sourced, is put in place to validate the accuracy of labelling.

**4.4. Where does this data come from?**

TO train and test the system:

- Product reviews, personal blogs/journals, social network websites, forums, fiction excerpts, analysis, critiques, and more.
- anywhere that people discuss and share their opinion freely could be a source.

Implementation will be on feedback from studetns reagarding the course contents.

**4.5. Is the data already preprocessed in any way?**

Since it is highly possible the proportion of “neutral” sentences outweigh those with emotional elements. To understand the impact of this, sentences are passed into a sentiment analyzer to provide basic labels of “positive”, “neutral” or “negative”. This allows us to filter the set if necessary, and gives us a rough idea of the mix of sentences.

**4.6. What steps have been taken to ensure the quality of the produced label?**

- Option to reject by the Requester.
- Redundancy: Allow each Human Intelligence Task (HIT) to be completed by several different Turkers, and only select higher quality ones.
- Ensure a minimum standard by putting in place a small test, before allowing actual labelling.

**4.7. How much data will be used for this task?**

The dataset used in this experiment consists of 784,349 samples of informal short English messages (i.e. a collection of English tweets), with 5 emotion classes: anger, sadness, fear, happiness, excitement where 60% is used for training, 20% for validation and 20% for testing.

#### 5. Caveats


#### 6. Performance Metrics

**6.1. What evaluation metrics will be used for the model?**
- Precision
- Accuracy unweighted
- Recall
- Confusion Matrix


#### 7. What is the deadline for this project?

Jan 9, 2021


#### 8. What is the acceptance criteria? Any bar that we need to meet?


**Is there any immediate platform that will be using this model?**

**If yes, any integration pre-information that we should be aware of?**

**Is there any platforms performing the similar objectives?**
- [Parallel Dots](https://www.paralleldots.com/emotion-analysis)
- [Twinword (2020): Emotion Analysis](https://www.twinword.com/api/emotion-analysis.php)



### Related Papers
- [EMOTION DETECTION FROM TEXT](https://www.airccj.org/CSCP/vol2/csit2237.pdf)
- [Towards Text-based Emotion Detection](https://sci-hub.do/10.1109/icime.2009.113)

### Reference
- [Results: Emotion Detection and Recognition from Text Using Deep Learning | CSE Developer Blog. (2020, March 15).](https://github.com/ryubidragonfire/Emotion)
- [Emotion Detection and Recognition from Text Using Deep Learning](https://devblogs.microsoft.com/cse/2015/11/29/emotion-detection-and-recognition-from-text-using-deep-learning/)
- [Dataset: ISEAR.csv](https://drive.google.com/file/d/12jwlbgKEASZ8kKLZ1Q7mAkxuhHM_AKB0/view)
