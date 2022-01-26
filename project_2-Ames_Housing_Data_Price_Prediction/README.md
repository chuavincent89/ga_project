# ![](https://ga-dash.s3.amazonaws.com/production/assets/logo-9f88ae6c9c3871690e33280fcf557f33.png) Project 2: Ames Housing Data and Kaggle Challenge

Author: Vincent Chua

### Table of Contents
* [Background](#Background)
* [Problem Statement](#Problem-Statement)
* [Executive Summary](#Executive-Summary)
* [Datasets](#Datasets)
* [Data Dictionary](#Data-Dictionary)
* [Conclusions and Recommendations](#Conclusions-and-Recommendations)

### Background

US Real estate is a dynamic industry where adapt and evolves quickly. However, there will always be handful of problems and challenges that investors facing in the real estate market. According to one of the member of Forbes Real Estate Council, *Richard Lackey, City Commercial Real Estate, Inc.*
> *A major challenge is the huge gap between the bid and ask. Generally speaking, commercial real estate buyers want a 30% discount where commercial real estate sellers are only prepared to offer a 5% discount. While property type and location sway discounts, a price decrease is generally more in support of the seller's position than the buyer's. Industrial and multifamily are doing the best while retail and hospitality are doing the worst. - source: [Forbes](https://www.forbes.com/sites/forbesrealestatecouncil/2021/01/11/16-challenges-for-real-estate-investors-and-how-to-deal-with-them/?sh=6fab694950e7)*

The huge gap between bid and ask housing price may not a good sign for a real estate investment firm as the housing price fluctuate too much may caused a lot of uncertainties for the investment return, we need to have a stable and predictable housing market so real estate investment firm able to find the location or the house type with good investment and potential value. We need to build a model that able to predict the housing price fairly and accurately, so the investment firm able to grab the investment opportunities on those houses sold undervalue or overvalue and maximize the investment return.

According to [Neighborhood Scout](https://www.neighborhoodscout.com/ia/ames) Ames city is a larger medium-sized city located in the state of Iowa and Ames is the eighth largest community in Iowa. Ames real estate is some of the most expensive in Iowa, hence We decided to take the datasets from Ames City, Iowa for our model building.

---
### Problem Statement

We are group of data scientists that working for a Real Estate Investment Firm. We are assigned to develop a model to predict the housing price of the property in Ames city, Iowa from the datasets given from year 2006 to 2010. We also need to provide insights and recommendation on which features that will affect positively and negatively to the selling price and how can the  property be further improved or modified to increase the housing price. Eventually the model can allow the firm to grab investment opportunities and maximize the investment return.

**Citations:**\
<sup>1</sup> https://www.e-rallc.com/ANSIstandards  
<sup>2</sup> https://www.opendoor.com/w/blog/factors-that-influence-home-value  
<sup>3</sup> https://home.howstuffworks.com/home-improvement/remodeling/measure-square-footage3.htm  
<sup>4</sup> https://data.census.gov/cedsci/profile?g=1600000US1901855  
<sup>5</sup> https://www.cityofames.org/government/departments-divisions-a-h/city-assessor  
<sup>6</sup> https://www.cityofames.org/government/departments-divisions-a-h/city-assessor/maps  
<sup>7</sup> https://www.statology.org/how-to-interpret-rmse/  
<sup>8</sup> https://www.mymove.com/buying-selling/guides/most-important-factors-for-buying-your-dream-home/  
<sup>9</sup> https://kenbenoit.net/assets/courses/ME104/logmodels2.pdf  
<sup>10</sup> https://stats.idre.ucla.edu/sas/faq/how-can-i-interpret-log-transformed-variables-in-terms-of-percent-change-in-linear-regression/    
<sup>11</sup> https://data.library.virginia.edu/interpreting-log-transformations-in-a-linear-model/  
<sup>12</sup> https://sites.google.com/site/curtiskephart/ta/econ113/interpreting-beta  
<sup>13</sup> https://www.forbes.com/sites/forbesrealestatecouncil/2021/01/11/16-challenges-for-real-estate-investors-and-how-to-deal-with-them/?sh=6fab694950e7

---

### Executive Summary

This Project mainly explore the 2016 to 2010 Ames housing datasets on different features and target sale price.

There are total of 80 possible features that may increase or decrease the Ames house sale price. We need to explore all these features and build a predictive model to better predict Ames sale price. All these information can help our Real Estate Investment Firm to made a better decision in decide where to invest their fund, and the type of modification can be made to add value on the house.

From our exploratory data analysis, the Ames housing sale price peak in Jan 2009 and start the drastic decreasing from mid 2010, this was mainly caused by the 2008 Financial Crisis. We also further explore on features *(Overall Quality, Garage Completion Level and Quality, Rooms and Living Size Area, Bathrooms, Year Remodified and Year Built and Neighborhood)* and these features have positive correlation against our target sale price. For neighborhoods, we found those neighborhoods with higher average sale price tend to be newly built and regardless of the year of house sold, these neighborhoods tend to have higher sale price. Hence these categories of neighborhoods tend to be the location with high desirability.

The top 6 features from our final model that have major impact (above 3%) on the average housing price are *Total Size, Quality Score, Age, Above Grade (Ground) Living Area, Overall Condition and Lot Area*. It will add the most value to the home.

---
### Datasets

* [`train.csv`](../datasets/train.csv): Ames Housing Price Train datasets 2006-2010
* [`test.csv`](../datasets/test.csv): Ames Housing Price Test datasets 2006-2010
* [`submit_pred.csv`](../datasets/submit_pred.csv): Predicted Ames Housing Price (for Kaggle challenge submission [here](https://www.kaggle.com/c/dsi-us-11-project-2-regression-challenge))


---
### Data Dictionary

**Ames Housing Data Dictionary** can refer to [here](https://web.archive.org/web/20201203235151/http://jse.amstat.org/v19n3/Decock/DataDocumentation.txt)

---

### Conclusions and Recommendations

**Findings:**

1) There are total 6 features that 1 unit change in the feature will lead to more than 3% changes in the average housing price:
- **Total Size:** Size has the highest impact to the housing price in Ames
- **Quality Score:** Quality of the house unit will determine the housing price as well
- **Age:** The newer the house unit will bring the housing price higher, on the other hand, the older the house unit will bring down the housing price
- **Above Grade (Ground) Living Area:** Living Area is crucial for a house as the buyer tend to prefer with bigger living area for staying, hence the housing price will be determined by the size of living area as well
- **Overall Condition:** Beside the overall quality score, the overall condition of the house unit also will impact the housing price
- **Lot Area:** The Lot Area may not be the fully utilized as livable area, however when comes to backyard size and potential building of additional facilities for the house, Lot Area will be important hence it have strong positive impact to the housing price in Ames.

2) Age has the most negative impact (reduce by 4.66%) on the average housing price, the firm should also avoid the **Commercial Zoning** area as the zone will have negative impact (reduce by 1.48%) on the average housing price. Besides that for **SubClass_30** which the type of dwelling is **1-STORY 1945 & OLDER** will also reduce 1.38% on the average housing price.

3) Pearson Correlation Coefficients shows that `garage_score` and `bsmt_score` have strong positive correlation against `saleprice` with 0.77 and 0.65 respectively, however `bsmt_score` have higher positive impact (increase 2.15%) on the average sale price as compared to `garage_score` with positive (increase 1.36%) on the average sale price.

4) RMSE score 19,795.80, it means our predictive model have average difference of $19,795.80 from the actual housing price which we find this is acceptable range to deploy our predictive model for generalization.



**Recommendations:**

1) In term of house characteristics, we will recommend the Real Estate Investment Firm can aim to focus on the **top 6 features** that have major impact (above 3%) on the average housing price - **Total Size, Quality Score, Age, Above Grade (Ground) Living Area, Overall Condition and Lot Area**. It will add the most value to the home.

2) We will not recommend the older house unit as the house age have negative impact on the average housing price. Besides that we will also suggest the firm to avoid invest to **Commercial Zoning** area and **SubClass_30** which the dwelling type is **1-STORY 1945 & OLDER**, both type of house will hurt the value of the home.

3) In term of house location, the firm can focus on zone with higher level as it will increase 1.96% of the average housing price for each level increase in the zone. We also recommend to invest in the Neighborhood of **Green Hills** and **Crawford** have the highest positive impact on the average housing price in Ames city and lead to better investment return.

4) We also recommend the firm to modify and complete the **Basement**, **Numbers and Quality of Fireplaces** and **Garage** in order to further improve the average housing price for better investment return.

5) We recommend the firm to deploy our predictive model which have average difference of **$19,795.80** from the actual housing price in Ames City, Iowa which means the firm can use the model to evaluate which house was sold undervalue or overvalue, and which house have great investment opportunities that can maximize the investment return.
