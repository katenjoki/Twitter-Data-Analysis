tweet_blob = [TextBlob(tweet) for tweet in df['text']]
df['polarity'] = [b.sentiment.polarity for b in tweet_blob]

tweet_blob = [TextBlob(tweet) for tweet in df['text']]
df['subjectivity'] = [b.sentiment.subjectivity for b in tweet_blob]

df['followers_count'] = [x.get('followers_count') for x in df['user']]
df['friends_count'] = [x.get('friends_count') for x in df['user']]
df['favourites_count'] = [x.get('favourites_count') for x in df['user']]

class Clean_Tweets:
    """
    The PEP8 Standard AMAZING!!!
    """
    def __init__(self, df:pd.DataFrame):
        self.df = df
        print('Automation in Action...!!!')
        
    def drop_unwanted_column(self, df:pd.DataFrame)->pd.DataFrame:
        """
        remove rows that has column names. This error originated from
        the data collection stage.  
        """
        unwanted_rows = df[df['retweet_count'] == 'retweet_count' ].index
        df.drop(unwanted_rows , inplace=True)
        df = df[df['polarity'] != 'polarity']
        
        return df
    def drop_duplicate(self, df:pd.DataFrame)->pd.DataFrame:
        """
        drop duplicate rows
        """
        
        df = df.drop_duplicates(subset=None,keep=False,inplace=True)
        
        return df
    def convert_to_datetime(self, df:pd.DataFrame)->pd.DataFrame:
        """
        convert column to datetime
        """
        df['created_at'] = pd.to_datetime(df['created_at'])
        
        df = df[df['created_at'] >= '2020-12-31' ]
        
        return df
    
    def convert_to_numbers(self, df:pd.DataFrame)->pd.DataFrame:
        """
        convert columns like polarity, subjectivity, retweet_count
        favorite_count etc to numbers
        """
        df['polarity'] = pd.to_numeric(df['polarity'])
        df['subjectivity'] = pd.to_numeric(df['subjectivity'])
        df['retweet_count'] = pd.to_numeric(df['retweet_count'])
        df['favourite_count'] = pd.to_numeric(df['favourite_count'])
        
        return df
    
    def remove_non_english_tweets(self, df:pd.DataFrame)->pd.DataFrame:
        """
        remove non english tweets from lang
        """
        df = df['lang'].map(lambda x:x.isascii())
        
        return df
