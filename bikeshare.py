import time
import pandas as pd
import numpy as np

#description added
CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
#function
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
        city = input("Please enter the city you'd like to analyze (Chicago, New York City, Washington): ").lower()
        if city in CITY_DATA:
            break
        else:
            print("Invalid city name. Please enter a valid city.")
    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        month = input("Please enter the month to filter by (January, February, ..., June), or 'all' for no filter: ").lower()
        if month in ['all', 'january', 'february', 'march', 'april', 'may', 'june']:
            break
        else:
            print("Invalid month. Please enter a valid month or 'all'.")

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = input("Please enter the day of the week to filter by (Monday, Tuesday, ..., Sunday), or 'all' for no filter: ").lower()
        if day in ['all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']:
            break
        else:
            print("Invalid day of the week. Please enter a valid day or 'all'.")


    print('-'*40)
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
    # Load the data for the specified city
    if city == "chicago":
        data_file = "chicago.csv"
    elif city == "new york city":
        data_file = "new_york_city.csv"
    elif city == "washington":
        data_file = "washington.csv"
    else:
        return "Invalid city name"

    df = pd.read_csv(data_file)

    # Convert the 'Start Time' column to a datetime object for date-related filtering
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # Filter by month if applicable
    if month != "all":
        month_num = ["january", "february", "march", "april", "may", "june"].index(month) + 1
        df = df[df['Start Time'].dt.month == month_num]

    # Filter by day if applicable
    if day != "all":
        df = df[df['Start Time'].dt.day_name().str.lower() == day]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    common_month = df['Start Time'].dt.month.mode()[0]
    print(f"The most common month for travel is: {common_month}")

    # TO DO: display the most common day of week
    common_day = df['Start Time'].dt.day_name().mode()[0]
    print(f"The most common day of the week for travel is: {common_day}")

    # TO DO: display the most common start hour
    df['Start Hour'] = df['Start Time'].dt.hour
    common_start_hour = df['Start Hour'].mode()[0]
    print(f"The most common start hour for travel is: {common_start_hour}")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    common_start_station = df['Start Station'].mode()[0]
    print(f"The most commonly used start station is: {common_start_station}")

    # TO DO: display most commonly used end station
    common_end_station = df['End Station'].mode()[0]
    print(f"The most commonly used end station is: {common_end_station}")

    # TO DO: display most frequent combination of start station and end station trip
    most_frequent_combination = df.groupby(['Start Station', 'End Station']).size().idxmax()
    print(f"The most frequent combination of start station and end station for a trip is: {most_frequent_combination[0]} to {most_frequent_combination[1]}")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print(f"The total travel time is: {total_travel_time} seconds")

    # TO DO: display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print(f"The mean travel time is: {mean_travel_time} seconds")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_type_counts = df['User Type'].value_counts()
    print("Counts of User Types:")
    for user_type, count in user_type_counts.items():
        print(f"{user_type}: {count}")

    # TO DO: Display counts of gender
    if 'Gender' in df:
        gender_counts = df['Gender'].value_counts()
        print("\nCounts of Gender:")
        for gender, count in gender_counts.items():
            print(f"{gender}: {count}")
    else:
        print("\nGender data not available in this dataset.")

    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df:
        earliest_birth_year = int(df['Birth Year'].min())
        most_recent_birth_year = int(df['Birth Year'].max())
        most_common_birth_year = int(df['Birth Year'].mode()[0])

        print("\nBirth Year Statistics:")
        print(f"Earliest Birth Year: {earliest_birth_year}")
        print(f"Most Recent Birth Year: {most_recent_birth_year}")
        print(f"Most Common Birth Year: {most_common_birth_year}")
    else:
        print("\nBirth year data not available in this dataset.")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
def raw_data(df):
    """Display raw data to the user in chunks."""
    i = 0
    pd.set_option('display.max_columns', 200)
    while True:
        raw = input("Do you want to view raw data? (yes/no)\n").lower()
        if raw == 'no':
            break
        elif raw == 'yes':
            print(df.iloc[i:i+5])
            i += 5
        else:
            print("\nYour input is invalid. Please enter only 'yes' or 'no'.\n")

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        raw_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
