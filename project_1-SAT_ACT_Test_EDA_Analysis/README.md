# ![](https://ga-dash.s3.amazonaws.com/production/assets/logo-9f88ae6c9c3871690e33280fcf557f33.png) Project 1: US Standardized Test Analysis

### Table of Contents
* [Background](#Background)
* [Problem Statement](#Problem-Statement)
* [Executive Summary](#Executive-Summary)
* [Datasets](#Datasets)
* [Data Dictionary](#Data-Dictionary)
* [Conclusions and Recommendations](#Conclusions-and-Recommendations)

### Background

The SAT and ACT are standardized tests that many colleges and universities in the United States require for their admissions process. This score is used along with other materials such as grade point average (GPA) and essay responses to determine whether or not a potential student will be accepted to the university.

The SAT has two sections of the test: Evidence-Based Reading and Writing and Math ([*source*](https://www.princetonreview.com/college/sat-sections)). The ACT has 4 sections: English, Mathematics, Reading, and Science, with an additional optional writing section ([*source*](https://www.act.org/content/act/en/products-and-services/the-act/scores/understanding-your-scores.html)). They have different score ranges, which you can read more about on their websites or additional outside sources (a quick Google search will help you understand the scores for each test):
* [SAT](https://collegereadiness.collegeboard.org/sat)
* [ACT](https://www.act.org/content/act/en.html)

Standardized tests have long been a controversial topic for students, administrators, and legislators. Since the 1940's, an increasing number of colleges have been using scores from students' performances on tests like the SAT and the ACT as a measure for college readiness and aptitude ([*source*](https://www.minotdailynews.com/news/local-news/2017/04/a-brief-history-of-the-sat-and-act/)). Supporters of these tests argue that these scores can be used as an objective measure to determine college admittance. Opponents of these tests claim that these tests are not accurate measures of students potential or ability and serve as an inequitable barrier to entry.

---
### Problem Statement

College-going culture has increasingly important to the US States, standardize test are required in order to enroll into the desired college. This project aim to provide insights to Oregon State Board of Education. To find out ACT and SAT participation rate of Oregon and the indicators may caused state have lower participation rate as compared to other states. How to further improve the participation rate in order to increase the High School Graduates college-going rate from current 55.6% to Oregon education goal of 80% by 2025.

**Citations:**\
<sup>1</sup> https://www.oregon.gov/highered/research/Pages/educational-attainment.aspx \
<sup>2</sup> http://www.higheredinfo.org/dbrowser/?year=2018&level=nation&mode=data&state=&submeasure=63

---

### Executive Summary

This project mainly explore the 2017, 2018 and 2019 both ACT and SAT datasets which contains the US states average participation rate and score from ACT and SAT.

Exploratory data analysis shows in 2017, 2017 and 2019 Maine have the lowest participation rate on ACT test and North Dakota have the lowest participation rate in SAT test. However data shows that Maine have average 97.67% in SAT participation rate and North Dakota have average 97.33% in ACT participation rate. This is due to the respective state have the test mandate for the high school students to participate in standardized test. Hence this is bias to categorize either Maine and North Dakota as low participation rate in standardized test. Iowa and Oregon are both without test mandate requirements, however Iowa have preference on ACT test, and the average participation rate in ACT is 67%. While Oregon is the only state consistently fall below 52% of participation rate on both test in 2017, 2018 and 2019.

Besides the score from the datasets, this project also added in additional datasets to analyze the correlations of participation rate with these variables *(Median Household Income, Number of universities, K12 spending per student, Postsecondary spending per student, Federal funding per student and State and local funding per student)*. Based on the findings from the data analysis and provide *Oregon State Board of Education* with recommendations to increase the participation rate in standardized test.

---
### Datasets

* [`act_2017.csv`](../data/act_2017.csv): 2017 ACT Scores by States
* [`act_2018.csv`](../data/act_2018.csv): 2018 ACT Scores by States
* [`act_2019.csv`](../data/act_2019.csv): 2019 ACT Scores by States
* [`sat_2017.csv`](../data/sat_2017.csv): 2017 SAT Scores by States
* [`sat_2018.csv`](../data/sat_2018.csv): 2018 SAT Scores by States
* [`sat_2019.csv`](../data/sat_2019.csv): 2019 SAT Scores by States
* [`spending_funding_states.csv`](../data/spending_funding_states.csv): U.S. Public Education Spending Statistics by states
* [`Median-Household-Income-by-State.csv`](../data/Median-Household-Income-by-State.csv): U.S. Census Bureau Median Income By State 2015-2019
* [`act_sat_mandate.csv`](../data/act_sat_mandate.csv): U.S. States with standardized test mandate 2018-2019
* [`state_abbreviations.csv`](../data/state_abbreviations.csv): US states, abbreviations and code table
* [`Most-Recent-Cohorts-All-Data-Elements.csv`](../data/Most-Recent-Cohorts-All-Data-Elements.csv)<span style="color:red">**(Data set is large, readers will have to unzip)**</span>: Institution-level data files for 1996-97 through 2019-20, field of study-level data files for the pooled 2014-15, 2015-16 award years through the pooled 2016-17, 2017-18 award years and crosswalk files for 2000-01 through 2018-19 that link the Department’s OPEID with an IPEDS UNITID for each institution

---
### Data Dictionary

|Feature|Type|Dataset|Description|
|---|---|---|---|
|state|object|df_act_sat_long / df_act_sat_wide / df_combine|Names of all US states and District of Columbia|
|participation|float|df_act_sat_long|The percentage of participation rate who took the ACT or SAT (0.9810 means 98.1%)|
|score|float|df_act_sat_long|The total score of of the test on ACT or SAT|
|score_percent|float|df_act_sat_long|The percentage of score out of full mark (ACT full mark is 36, SAT full mark is 1600)|
|test|object|df_act_sat_long|The test type (ACT or SAT)|
|year|object|df_act_sat_long|The year of attending the ACT or SAT|
|participation_act|float|df_act_sat_wide|Average percentage of participation rate who took the ACT from 2017 - 2019(0.9810 means 98.1%)|
|participation_sat|float|df_act_sat_wide|Average percentage of participation rate who took the SAT from 2017 - 2019(0.9810 means 98.1%)|
|score_percent_act|float|df_act_sat_wide|Average percentage of score out of full mark for ACT from 2017 - 2019(ACT full mark is 36)|
|score_percent_sat|float|df_act_sat_wide|Average percentage of score out of full mark for SAT from 2017 - 2019(SAT full mark is 1600)|
|code|object|df_act_sat_wide|Postal abbreviations of all US states and District of Columbia|
|income|float|df_act_sat_wide|US States Average median household income (2015 - 2019)|
|total_uni|int|df_act_sat_wide|The total numbers of university / college institution in each US state|
|k12_spending|int|df_act_sat_wide|US States K12 spending per student|
|postsec_spending|int|df_act_sat_wide|US States Postsecondary spending per student|
|fed_funding|int|df_act_sat_wide|US States Federal funding per student|
|state_funding|int|df_act_sat_wide|US statas and local funding per student|
|fed_fund_per_mincome|float|df_act_sat_wide|US States Federal funding per student per Median Household Income|
|state_fund_per_mincome|float|df_act_sat_wide|US States State and Local funding per student per Median Household Income|
|test_mandate|object|df_act_sat_wide|US States with ACT or SAT mandate requirement 2018 - 2019|
|participation_act_2017|float|df_combine|The percentage of participation rate who took the ACT in 2017(0.9810 means 98.1%)|
|participation_act_2018|float|df_combine|The percentage of participation rate who took the ACT in 2018(0.9810 means 98.1%)|
|participation_act_2019|float|df_combine|The percentage of participation rate who took the ACT in 2019(0.9810 means 98.1%)|
|participation_sat_2017|float|df_combine|The percentage of participation rate who took the SAT in 2017(0.9810 means 98.1%)|
|participation_sat_2018|float|df_combine|The percentage of participation rate who took the SAT in 2018(0.9810 means 98.1%)|
|participation_sat_2019|float|df_combine|The percentage of participation rate who took the SAT in 2019(0.9810 means 98.1%)|
|score_percent_act_2017|float|df_combine|The percentage of score out of full mark for ACT in 2017(ACT full mark is 36)|
|score_percent_act_2018|float|df_combine|The percentage of score out of full mark for ACT in 2018(ACT full mark is 36)|
|score_percent_act_2019|float|df_combine|The percentage of score out of full mark for ACT in 2019(ACT full mark is 36)|
|score_percent_sat_2017|float|df_combine|The percentage of score out of full mark for SAT in 2017(SAT full mark is 1600)|
|score_percent_sat_2018|float|df_combine|The percentage of score out of full mark for SAT in 2018(SAT full mark is 1600)|
|score_percent_sat_2019|float|df_combine|The percentage of score out of full mark for SAT in 2019(SAT full mark is 1600)|

---

### Conclusions and Recommendations

**Findings:**

1) Participation rate in ACT and SAT tend to be negative correlated (mirror) to each other, it means that the higher the SAT participation rate tend to have lower ACT participation rate. State with test mandate requirements tend to have higher participation rate than the states without any test mandate requirements. 35.29% of US States with no test mandate only have average 51.8% in ACT participation rate and 44.13% in SAT participation rate.

2) Either of the test also tend to be negative correlated with the score percent, it means that the higher the test participation rate tend to have lower test score percent. It is mainly because of the average may be lower and the more students taking the test probably rank relatively low in their class are applying to the selective institution of higher education.

3) Oregon rank 21st nationwide in median household income, rank 24th nationwide in state funding per student and rank 30th nationwide in K12 spending per student. It rank bottom out of the states with bottom 10 college-going rate and without test mandate for K12 spending per student and State and Local funding per student. However, all 3 variables of Oregon shows fall below national averages. Pearson's Correlation Coefficient shows there is 0.49 in Median Household Income correlated to SAT participation rate, 0.48 in K12 Spending per student to SAT participation rate and 0.5 in State and Local funding per student to SAT participation rate.

**Recommendations:**

1) Oregon can decide to mandate either one of the standardized test and focus the efforts to increase participation rate of chosen test. By negotiating the term with SAT and ACT to bring the more benefits or financial aid to the high school of Oregon and test participants, example School Day and Test Fee Waiver.

2) Oregon state can aim to provide more budget to fund the students for having free to participate in standardized test or minimally can subsidize the test to further support the low income family as well as cultivating a college-going culture in the state.

3) The state can also provide more resources to support the test participants, example free online test preparation materials or  high school to provide additional resources for students to prepare standardize test.

4) The state can launch some marketing campaigns or organize University and college readiness fair for the high school, to share more about the enrollment requirements and supports example, college scholarships, financial aid and student loan for the college tuition fee, so the students from low income family have the more opportunities to enroll and it also create stronger awareness to the students and public for the importance and support for college-going.
