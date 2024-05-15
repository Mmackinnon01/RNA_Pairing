import pandas as pd

count = 0
#Side A is the start point
#Side B is the End Point on the other side of the bridge.
#Trip to Side B
#Code should work for any amount of people

#Modelling a general trip across for any 2 people
def two_across(A, B, df):
    A_to_B(A[0], A[1], A, B, df)

#Modelling a return trip required for additional person
#1st trip to side B takes person with max crossing time
#2nd trip takes person with min. crossing time to return torch
def three_across(A, B, df):
    A_to_B(df.loc[A, :][df.loc[A, :] == df.loc[A, :].max(axis=0)].dropna().index[0], df.loc[A, :][df.loc[A, :] == df.loc[A, :].min(axis=0)].dropna().index[0], A, B, df)
    B_to_A(df.loc[B, :][df.loc[B, :] == df.loc[B, :].min(axis=0)].dropna().index[0], A, B, df)
   # print(" %s minutes back to A for %s" % (str(df.loc[B, :].min(axis=0)[0]), df.loc[B, :][df.loc[B, :] == df.loc[B, :].min(axis=0)].dropna().index[0]))

#For any situation with 4+ people
#Person with max crossing time counted as time across
#Person with min crossing time counted as return time

def four_plus_across(A, B, df):
    A_to_B(df.loc[A, :][df.loc[A, :] == df.loc[A, :].min(axis=0)].dropna().index[0], df.loc[A, :].sort_values(by = df.columns[0], ascending=True).index[1], A, B, df)
    B_to_A(df.loc[B, :][df.loc[B, :] == df.loc[B, :].min(axis=0)].dropna().index[0], A, B, df)
    A_to_B(df.loc[A, :][df.loc[A, :] == df.loc[A, :].max(axis=0)].dropna().index[0], df.loc[A, :].sort_values(by = df.columns[0], ascending=True).index[-2], A, B, df)
    B_to_A(df.loc[B, :][df.loc[B, :] == df.loc[B, :].min(axis=0)].dropna().index[0], A, B, df)

#Defining the function taking max time across the birdge for each trip
def A_to_B(first_Name, second_Name, A, B, df):
    global count
    A.remove(first_Name)
    A.remove(second_Name)
    count += max(df.loc[first_Name, :][0], df.loc[second_Name, :][0])
    print(" Trip across takes %s & %s minutes for %s & %s." % (str(df.loc[first_Name, :][0]), str(df.loc[second_Name, :][0]), first_Name, second_Name))
    df.loc[first_Name, :][0] = fatigue(df.loc[first_Name, :][0], first_Name)
    df.loc[second_Name, :][0] = fatigue(df.loc[second_Name, :][0], second_Name)
    B.append(first_Name)
    B.append(second_Name)

#Defining the function taking min time of return trip
def B_to_A(name, A, B, df):
    global count
    B.remove(name)
    count += df.loc[name, :][0]
    print(" Return Trip takes %s minutes for %s." % (str(df.loc[name, :][0]), name))
    df.loc[name, :][0] = fatigue(df.loc[name,:][0], name)
    A.append(name)

def fatigue(time, name, style = 'Flat', value = 2):
    if style == 'Flat':
        print(' %s Time: %s --> %s minutes.' % (name, str(time), str(time+value)))
        return time+value
    else:
        print(' %s Time: %s --> %s minutes.' % (name, str(time), str(time*value)))
        return time*value
    
def getTravellers():
    A = [int(x) for x in input("Enter time of each person: ").split()]
    A_Names = [x for x in input("Enter name of each person: ").split()]
    df = pd.DataFrame(A).set_index([A_Names])
    df.columns = ['Names']
    return df, A_Names

#Enter N times for N people needing to cross
#This will loop until it counts all N people
#Counts and outputs the total time for all trips
if __name__ == '__main__':
    df, A = getTravellers()
    B = []
    
    print(df)
    
    while len(A) != 0:
        if len(A) == 1:
            print("Bring Time to B")
        if len(A) == 2:
            two_across(A, B, df)
            print("Total Time: %s" % str(count))
            break
        elif len(A) == 3:
            three_across(A, B, df)
        else:
            four_plus_across(A, B, df)