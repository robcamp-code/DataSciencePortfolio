# University Graduation Rates: A Data Driven Study on Race and Performance

When trying to a data set for the backbone of my first data science project, I took a lot of things into concideration. 
There were three criteria for a high quality dataset, many more observations than features (tall not wide),
multiple different feature types (categorical, numeric, ordinal, location), and some sort of meaningful real world application. Luckily, the Ipeds Data Center provided just what I needed, a rich data set of over 2000 4-year institutions and their characteristics. In my initial exploration of the data, one plot really stood out.
![MeanGraduationRates](https://user-images.githubusercontent.com/59036285/138110474-313de912-2a80-4935-8904-6b52366b9dc9.png) 

Given that these are completions within 150% of the time, the numbers are lower than expected. Additionally, two of the most marginalized communities in the United States, African Americans and Native Americans, have the lowest graduation rates by a large margin. These statistics gave me the motivation for this project and try to explain with data why these disparities exist and what contributes to graduation rates as a whole.

My target variable for this problem would be graduation rates, and the problem statement is as follows:

University X has very low graduation rates and even lower amongst students of color. They are facing immmence pressure from the community and board members and the leadership of the school needs to respond with a data backed explanation for their poor performance along with a data driven plan for improving their future graduation rates. The criteria for a successful project I defined as a prediction within 5% Mean Absolute Error. This felt like a reasonable margin for predicting graduation rates. With this goal in mind, I attempted to solve this problem with the data science process while giving data driven explanation for why African American students are less likely to graduate. I found that a University's performance in regards to graduation rates can be largely explained 5 features: sector of institution, residential level, price, revenue, SAT scores, and the interactions amongst them.

## Sector of Institution
As one might assume, some sectors perform much better than others when it comes to graduation rates. I found that  private non-profit institutions have the highest average graduation rate. Public schools are trailing not too far behind, and private for-profit institutions perform the worst
![sector](https://user-images.githubusercontent.com/59036285/138111617-9bbf9781-1353-4286-895b-3d55f014d767.png)

This was not what I expected. It is counter intuitive to think that private for-profit institutions would perform the worst out of all three sectors. These results also give us the first insight as to why a school might be performing as it is. Additionally, if we look at the distribution of race amongst these sectors we will find that African Americans have the highest representation at private for-profit institutions, the lowest performing of the three sectors.

![race_distribution](https://user-images.githubusercontent.com/59036285/138111623-d681c249-974c-4f38-a645-e747c267480e.png)

Just by looking at the sector of an institution, one can already start to see why their are major disparities between African American students and their majority counterparts. 

## Price
Another major influence on graduation rates is the price of the school. Schools with a higher price have higher graduation rates. Additionally, African American students attend cheaper schools. In the plot below small, the size and color of the plotted point are controlled by "The Percentage of Enrollment That Are Black" variable; therefore, smaller blue bubbles are schools where the percentage of african americans are lower while larger yellow bubbles are schools where the percentage of enrollment that are black is much higher.

![PricevsRace](https://user-images.githubusercontent.com/59036285/138111586-5e14aa55-bebe-4d1b-bc87-1064416b2594.png)


## Revenue
Revenue has a slightly less drastic impact on graduation rates than price, but generally schools with lower revenues have lower graduation rates. The same color coding was used to denote where African Americans are attending, and trend that was evident with price persisted with revenue.  

![RevVsRace](https://user-images.githubusercontent.com/59036285/138111556-bc070da6-cd22-4398-b8da-33f2c6c41e3a.png)

## SAT Scores
SAT scores did not show the same trends with graduation rates that Price and Revenue did in regards to race. Also, there was a very large amount of missing data for admissions scores. In the plot below, red points indicate the imputed data while blue points indicate reported values.
![SAT](https://user-images.githubusercontent.com/59036285/138111735-cdd264da-14a0-4e3e-aafb-aaa17acfea10.png)
As you can see, their is a clear trend if you look only at the blue points; however, due to the large amount of schools that failed to report their admissions scores, the correlation between SAT scores and graduation rates becomes less evident. Admissions scores contained thousands of missing data points that had to be imputed. If you want to check my imputation process, you can view the DataCleaning notebook. In short, if a school had ACT scores but not SAT scores, I did a ACT to SAT conversion and vice versa. If a school reported none of these, I used sklearn's KNNImputer() to estimate SAT and ACT scores that were still missing. The degree of missingness in the data had a large impact on model performance. As you can see, if I were to have the true scores for every school, then this variable would make for a very powerful explanatory variable

## Model Performance

![xgbAccuracy](https://user-images.githubusercontent.com/59036285/138111680-86a9d719-8a75-44dc-9c1c-7eb50f3e547d.png)


![XGBResiduals](https://user-images.githubusercontent.com/59036285/138111692-388d5efe-295a-41d0-a550-fdb96c179140.png)






