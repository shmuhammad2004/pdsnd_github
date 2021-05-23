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
    print('Hello! Let us explore some US bikeshare data!')
    print('Enter the city which you want to analyze the data for:')
    print('Chicago: 1')
    print('New York: 2')
    print('Washington: 3')
    print(' ')
    city = input('Please choose the city which you would like to see the Statistics: ')
    city = city.lower()
    
    while True:     
            if city == '1' or city == 'chicago':
                print("\nChicago City!\n")
                return 'chicago'
            if city == '2' or city == 'new york':
                print("\nNew York City!\n")
                return 'new york city'
            elif city == '3' or city == 'washington':
                print("\nWashington!\n")
                return 'washington'
           
            else:
                print('\nPlease enter 1, 2 or 3 or the names of the cities\n')
                city = input('Please choose the city which you would like to see the Statistics: ')
                city = city.lower()
    return city
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs

def get_time():
    
    #the code below asks the user to choose between month and day of month,day of the week or no filters
    
    period = input('\nDo you wish to filter the data by month and day of the month, day of the week, or you do not want to filter at all? Type "no" for no period filter.\n')
    period = period.lower()

    while True: 
        if period == "month":
            while True:
                day_month = input("\nDo you want to filter the data by day of the month? Type 'YES' or 'NO'\n").lower()
                if day_month == "no":
                    print('\n The data filtered by month\n')
                    return 'month'
                elif day_month == "yes":
                   print ('\n The data filtered by month and day of the month\n')
                   return 'day_of_month'
                
        if period == "day":
            print('\n The data filtered by the day of the week\n')
            return 'day_of_week'
        elif period == "no":
            print('\n No period filter is being applied to the data\n')
            return "none"
        period = input("\n Please choose a period filter option between 'month', 'day' of the week, or none (no) \n").lower()

    # TO DO: get user input for month (all, january, february, ... , june)

def month_info(m):
    if m == 'month':
        month = input('\nChoose the month! January, February, March, April, May, or June? Please type the full month name.\n')
        while month.strip().lower() not in ['january', 'february', 'march', 'april', 'may', 'june']:
            month = input('\nPlease choose between January, February, March, April, May, or June? Please type the full month name.\n')
        return month.strip().lower()
    else:
        return 'none'

    def month_day_info(df, day_m):     # Asks the user for a month and a day of month,
    month_day = []
    if day_m == "day_of_month":
        month = month_info("month")
        month_day.append(month)
        maximum_day_month = max_day_month(df, month)

        while (True):
            ask = """ \n Which day of the month? \n
            Please type your response as an integer between 1 and 7 """                 
            ask  = ask + str(maximum_day_month) + "\n" 
            day_m = input(ask)

            try: 
                day_m = int(day_m)
                if 1 <= day_m <= maximum_day_month:
                    month_day.append(day_m)
                    return month_day
            except ValueError:
                print("That's not a numeric value")
    else:
        return 'none'

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)

def day_info(d):
    if d == 'day_of_week':
        day = input('\nWhich day? Please type a day M, Tu, W, Th, F, Sa, Su. \n')
        while day.lower().strip() not in ['m', 'tu', 'w', 'th', 'f', 'sa', 'su']:
            day = input('\nPlease type a day as a choice from M, Tu, W, Th, F, Sa, Su. \n')
        return day.lower().strip()
    else:
        return 'none'
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
df = pd.read_csv(CITY_DATA[city])

    #extracting from Start Time
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    df['month'] = df['Start Time'].dt.month
    df["day_of_month"] = df["Start Time"].dt.day
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    
    print('Data loaded. Now computing statistics... \n')
    #Filter by Month
    if time == 'month':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        df = df[df['month'] == month]

    #Filter by day of week
    if time == 'day_of_week':
        days = ['Monday', 'Tuesday', 
        'Wednesday', 'Thursday', 
        'Friday', 'Saturday', 'Sunday']
        for d in days:
            if week_day.capitalize() in d:
                day_of_week = d
        df = df[df['day_of_week'] == day_of_week]

    if time == "day_of_month":
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = md[0]
        month = months.index(month) + 1
        df = df[df['month']==month]
        day = md[1]
        df = df[df['day_of_month'] == day]

    return df

    
    # TO DO: display the most common month

def month_freq(df):
    '''What is the most popular month for start time?
    '''
    # df - dataframe returned from time_filters
    print('\n What is the most popular month for bike traveling?')
    m = df.month.mode()[0]
    months = ['january', 'february', 'march', 'april', 'may', 'june']
    popular_month = months[m - 1].capitalize()
    return popular_month

    # TO DO: display the most common day of week

def day_freq(df):
    print('\n What is the most popular day of the week for bike rides?')
    return df['day_of_week'].value_counts().reset_index()['index'][0]

    # TO DO: display the most common start hour
def hour_freq(df):
   
    print('\n What is the most popular hour of the day for bike rides?')
    df['hour'] = df['Start Time'].dt.hour
    return df.hour.mode()[0]

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station


    # TO DO: display most commonly used end station


    # TO DO: display most frequent combination of start station and end station trip

def stations_freq(df):
    '''What is the most popular start station and most popular end station?
    '''
 
    print("\nWhat is the most popular start station?\n")
    start_station = df['Start Station'].value_counts().reset_index()['index'][0]
    print (start_station)
    print("\n* Q6. What is the most popular end station?\n")
    end_station = df['End Station'].value_counts().reset_index()['index'][0]
    print(end_station)
    return start_station, end_station

def common_trip(df):
    '''What is the most popular trip?
    '''
    result = df[['Start Station', 'End Station']].groupby(['Start Station', 'End Station']).size().nlargest(1)
    print('\nWhat was the most popular trip from start to end?')
    return result


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time


    # TO DO: display mean travel time


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
def bike_users(df):
    '''What are the counts for each user type?
    '''
    
    print('\nTypes of users: subscribers, customers, others\n')
    return df['User Type'].value_counts()


    # TO DO: Display counts of gender

def gender_data(df):
    
    try:
        print('\nWhat is the count of gender among users?\n')
        return df['Gender'].value_counts()
    except:
        print('There is no gender data in the source.')
        
    # TO DO: Display earliest, most recent, and most common year of birth
def birth_years(df):
    
    try:
        print('\n*What is the earliest, latest, and most common year of birth, respectively?')
        earliest = np.min(df['Birth Year'])
        print ("\nThe earliest year of birth is " + str(earliest) + "\n")
        latest = np.max(df['Birth Year'])
        print ("The latest year of birth is " + str(latest) + "\n")
        most_frequent= df['Birth Year'].mode()[0]
        print ("The most frequent year of birth is " + str(most_frequent) + "\n")
        return earliest, latest, most_frequent
    except:
        print('No available birth date data for this period.')

def process(f, df):
    start_time = time.time()
    statToCompute = f(df)
    print(statToCompute)
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def disp_raw_data(df):
    
    #omit irrelevant columns
    df = df.drop(['month', 'day_of_month'], axis = 1)
    row_index = 0

    see_data = input("\nwould you like to see rows of the data used to compute the stats? Kindly write 'yes' or 'no' \n").lower()
    while True:
        if see_data == 'no':
            return
        if see_data == 'yes':
            print(df[row_index: row_index + 5])
            row_index = row_index + 5
        see_data = input("\n Would you like to see five more rows of the data used to compute the stats? Kindly write 'yes' or 'no' \n").lower()

    

def main():
    
# calling all the functions
    city = city_input()
    df = load_data(city)
    period = get_time()
    month = month_info(period)
    day = day_info(period)
    month_day = month_day_info(df, period)

    df = time_filters(df, period, month, day, month_day)
    disp_raw_data(df)
    
    # all the conclusions
    stats_funcs_list = [month_freq,
     day_freq, hour_freq, 
     ride_duration, common_trip, 
     stations_freq, bike_users, birth_years, gender_data]
	
    for x in stats_funcs_list:	# displays processing time for each function block
        process(x, df)

    # Restarting option
    restart = input("\n * Would you like to restart again? Enter yes or no.\n")
    if restart.upper() == 'YES' or restart.upper() == "Y":
        main()

if __name__ == "__main__":
	main()
