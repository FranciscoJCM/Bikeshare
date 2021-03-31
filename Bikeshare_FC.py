import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        city = input("Please choose which city you want to explore (chicago, new york city or washington): ").lower()
        if city in CITY_DATA:
            break
        else:
            print("Please input any of the 3 cities in lower case")

# TO DO: get user input for month (all, january, february, ... , june)
    while True:
        month = input("Please type in lower case the month you would like to explore (january, february, march, april, june) or type all to explore all of them: ").lower()
        months = ["january", "february", "march", "april", "may", "june", "all"]
        if month in months:
            break
        else:
            print("Please provide a valid option in lowercase")
        
# TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = input("Please type in lower case the day of the week you would like to explore: ").lower()
        days_of_week = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday", "all"]
        if day in days_of_week:
            break
        else:
            print ("Please provide a valipythond option un lowercase")
              
    print("-"*40)
    return city, month, day 


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    #load the data file into the df       
    df = pd.read_csv(CITY_DATA[city])
    #converts the Start Date column into datetime
    df["Start Time"] = pd.to_datetime(df["Start Time"])
    #Create new columns fot month, day and hour
    df["month"] = df["Start Time"].dt.month
    df["Day of Week"] = df["Start Time"].dt.day_name()
    df["hour"] = df["Start Time"].dt.hour

    # filter by month if applicable
    if month != "all":
        
    # use the index of the months list to get the corresponding int
        months = ["january", "february", "march", "april", "may", "june"]
        month = months.index(month) + 1
    # filter by month to create the new dataframe
        df = df[df["month"] == month]
            
    # filter by day of week if applicable
    if day != "all":
        # filter by day of week to create the new dataframe
        df = df[df["Day of Week"] == day.title()]
         
    return df
    

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    print ("The most common month was: {}".format(df.loc[:, "month"].mode()[0]))

    # TO DO: display the most common day of week
    print("The most common day of the week was: {}".format(df.loc[:, "Day of Week"].mode()[0]))

    # TO DO: display the most common start hour
    print ("The most common start hour was: {}".format(df.loc[:, "hour"].mode()[0]))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print("\nCalculating The Most Popular Stations and Trip...\n")
    start_time = time.time()

    # TO DO: display most commonly used start station
    print("The most commonly used start station was: {}".format(df.loc[:, "Start Station"].mode()[0]))

    # TO DO: display most commonly used end station
    print("The most commonly used end station was: {}".format(df.loc[:, "End Station"].mode()[0]))

    # TO DO: display most frequent combination of start station and end station trip
    #first I create a new column with combinations
    df["Start to End"] = df.loc[:, "Start Station"] + " - " + df.loc[:, "End Station"]
    print("The most frequent combination of start station and end station trip was: {}".format(df.loc[:, "Start to End"].mode()[0]))
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print("\nCalculating Trip Duration...\n")
    start_time = time.time()

    # TO DO: display total travel time
    print("The total travel time was: {}".format(df.loc[:, "Trip Duration"].sum()))

    # TO DO: display mean travel time
    print("The mean travel time was: {}".format(df.loc[:, "Trip Duration"].mean()))

    #print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
 
def user_stats(df, city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    print("We have the following types of users:\n{}".format(df.loc[:,"User Type"].value_counts(dropna=False)))

    # TO DO: Display counts of gender
    if city != "washington":
        print("The gender count is:\n{}".format(df.loc[:, "Gender"].value_counts(dropna=False)))
        
    # TO DO: Display earliest, most recent, and most common year of birth
        print("The earliest year of birth was: {}".format(int(df.loc[:, "Birth Year"].min())))
        print ("The most recent year of birth was: {}".format(int(df.loc[:, "Birth Year"].max())))
        print("The most common year of birth was: {}".format(int(df.loc[:, "Birth Year"].mode()[0])))
                   
    else:
        print("\nGender and Birth Date data is not included for Washington City.")
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)
    
def raw_data (df):
    """Displays the first 5 rows from the user´s selection"""
    print("Would you like to see the first 5 records from your selection?\n")
    i = 0
    five = input("Please type yes or no \n").lower()
    if five == "yes":
        print(df.head())
        i += 5
        while True:
            ten = input("Would you like to display 5 more rows?").lower()
            if ten == "yes":
                print(df.iloc[i:i+5,:])
                i += 5
                
            else:  
                break
    
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df, city)
        raw_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n').lower()
        if restart != 'yes':
            break


if __name__ == "__main__":
	main()