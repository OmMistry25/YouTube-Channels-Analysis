# Goal: 
  We are interested in YouTube channel categories that obtain the most number of subscribers. In this report, we are going to use Python to explore the relationship between subscriber count and YouTube channel category.

# Programming Languages/plugins used:
Python, scipy, pandas, seaborn, and numpy. 

# Motivation: 
  Our analysis could be useful for people that are interested in starting a new YouTube channel to garner the most amount of subscribers. By finding which YouTube channel category has the most amount of subscribers on average, a user can choose to aim their content in that direction.

# Data collection:
The dataset was collected through web scraping from hypeauditor.com.

# Data cleaning:
Missing Values: Our data includes a total of 350 rows with missing values in the Category column. These values appear as NaN in our dataset and are automatically detected by Python. There are no other implicit missing values.

First, we decided to drop only one row which contained all missing values in all columns. Secondly, we replaced all missing values with 'Other' as dropping all missing values would cause almost 1/3 of our data to be removed. The advantages of treating the missing values in this way are keeping other relevant aspects of an observational unit and allowing for a greater number of units to perform analysis on. The drawbacks of treating the missing values in this manner would primarily be concerned with skewing the results since this new 'Other' category takes up a majority of the data.

Uncommon Values: In terms of uncommon values, the first row contained information that was not available. Because it did not contain anything of importance, that row was dropped. We decided to drop one observation because it only contained NaN values. We do not believe removing this observation will greatly impact future analysis.

# Research Question: 
  Is there a relationship between the Category of YouTube channels and the number of Subscribers that the YouTube channel has?

# Summarization: 
![image](https://github.com/OmMistry25/data-driven-approach-to-start-your-youtube-channel-/assets/157780551/af950748-8ae5-45a4-a09e-566b19c8cc07)

The dataset we chose to work around with and analyze was of the Top YouTubers worldwide (Top 1000) from Kaggle. This dataset is comprised of a diverse range of popular YouTube channels. Each channel has various variables, including the channel's name, subscribers, average view count, etc. Before analyzing, a few data cleaning measures were taken care of: first, we decided to drop the row that contained all missing values in all columns. Secondly, we replaced all missing values (NaN) in the ‘Category’ column with 'Other' as dropping all missing values would cause almost 1/3 of our data to be removed. Finally, we changed the subscribers column from an object type to a float type. These measures allow us to analyze and draw conclusions around our research question: Is there a relationship between the Category of YouTube channels and the number of Subscribers that the YouTube channel has?

# Limitations: 
While conducting analysis, the team faced some limitations with the number of missing values in the Category variable. These missing values can skew the results we obtain. Something else that we might want to look at is what year the YouTube channel was made, and the number of video content they created to reach their first 10,000 subscribers. This information can allow us to categorize channels more effectively for the viewers as certain channel categories might have been more popular at different points in time. This contextual information along with the results we obtained through our analysis can be used by an aspiring YouTube content creator to strategize and position their channel category to increase their odds of growing faster on YouTube.

# Future Work: 
For future research to be conducted on these analyses, a question worth investigating is whether the frequency with which each channel category influences the YouTube algorithms in a way that drives more engagement for that particular YouTube channel. This would require additional information on the channel’s frequency of uploading material every week/month for a particular set of periods, which could be compared with their respective channel matrics for that particular time frame. This future research can help aspiring YouTubers plan strategically and optimize their channel for the highest amount of engagement.


