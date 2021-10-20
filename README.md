# University Graduation Rates: A Data Driven Study on Race and Performance

When trying to a data set for the backbone of my first data science project, I took a lot of things into concideration. 
There were three criteria for a high quality dataset, many more observations than features (tall not wide),
multiple different feature types (categorical, numeric, ordinal, location), and some sort of meaningful real world application. Luckily, the Ipeds Data Center provided just what I needed, a rich data set of over 2000 4-year institutions and their characteristics. In my initial exploration of the data one plot really stood out: 
![MeanGraduationRates](https://user-images.githubusercontent.com/59036285/138110474-313de912-2a80-4935-8904-6b52366b9dc9.png) 

Given that these are completions within 150% of the time, the numbers are lower than expected. Additionally, two of the most marginalized communities in the United States, African Americans and Native Americans, have the lowest graduation rates by quite a margin. These statistics gave me the motivation to take this project and try to explain with data why these disparities exist and what contributes to graduation rates as a whole.

My target variable for this problem would be graduation rates, and the problem statement is as follows:

University X has very low graduation rates and even lower amongst students of color. They are facing immmence pressure from the community and board members and 
the leadership of the school needs to respond with a data backed explanation for their poor performance along with a data driven plan for improving their future 
graduation rates. The criteria for a successful project I defined as a prediction within 5% Mean Absolute Error. This felt like a reasonable metric for predicting 
graduation rates. With this goal in mind, I attempted to solve this problem with the data science process while giving data driven explanation for why African American students are less likely to graduate. I found that a University's performance in regards to graduation rates can be largely explained 5 features: sector of institution, residential level, price, revenue, SAT scores, and the interactions amongst them.

## Sector of Institution
As one might assume, some sectors perform much better than others when it comes to graduation rates. I found that  private non-profit institutions perform the best with public institutions trailing not far behind as depicted below.
![sector](https://user-images.githubusercontent.com/59036285/138111617-9bbf9781-1353-4286-895b-3d55f014d767.png)

This was not what I expected. It is counter intuitive to think that private for-profit institutions would perform the worst out of all three sectors. These results also give us the first insight as to why a school might be performing as it is. Additionally, if we look at the distribution of race amongst these sectors we will find that African Americans are represented the most at private for-profit institutions, the lowest performing of the three sectors.

![race_distribution](https://user-images.githubusercontent.com/59036285/138111623-d681c249-974c-4f38-a645-e747c267480e.png)



## Price

![PricevsRace](https://user-images.githubusercontent.com/59036285/138111586-5e14aa55-bebe-4d1b-bc87-1064416b2594.png)

## Revenue

![RevVsRace](https://user-images.githubusercontent.com/59036285/138111556-bc070da6-cd22-4398-b8da-33f2c6c41e3a.png)

## SAT Scores
![SAT](https://user-images.githubusercontent.com/59036285/138111735-cdd264da-14a0-4e3e-aafb-aaa17acfea10.png)


## Model Performance



![xgbAccuracy](https://user-images.githubusercontent.com/59036285/138111680-86a9d719-8a75-44dc-9c1c-7eb50f3e547d.png)

![XGBResiduals](https://user-images.githubusercontent.com/59036285/138111692-388d5efe-295a-41d0-a550-fdb96c179140.png)






