#setting the counter for run number and the total for hours overall 
counter = 1 
hours_total = 0

#statement to enter time difference caclculator and accumulator
command_statement = input("Start time difference calculator? (Y/N) :")

while command_statement != 'N': #break statement

    #getting start and end time and splitting them 
    start_time = input("Enter start time in HH:MM:SS: ")
    end_time = input("Enter end time in HH:MM:SS: ")
    start_split = start_time.split(":")
    end_split = end_time.split(":")

    #converting string input into integers
    start_hr = int(start_split[0])
    start_min = int(start_split[1])
    start_sec = int(start_split[2])
    
    end_hr = int(end_split[0])
    end_min = int(end_split[1])
    end_sec = int(end_split[2])

    #accounting for borrowing 
    if end_sec < start_sec:
        end_sec += 60
        end_min -= 1 

    #difference in seconds converting to hours
    sec_in_hours = (end_sec - start_sec) / 3600
    
    if end_min < start_min:
        end_min += 60
        end_hr -= 1

    #difference in minutes converting to hours
    min_in_hours = (end_min - start_min) / 60
    
    hours = end_hr - start_hr

    #hours for this run
    run_hours = hours + min_in_hours + sec_in_hours

    #hours for all runs
    hours_total += run_hours

    #header if this is the first iteration, can probably be removed after tabulation.
    if counter == 0:
        print("Run\tStart Time\tEnd Time\t Hours\n")

    #printing run data 
    print(str(counter)+"\t"+start_time+"\t"+end_time+"\t"+str(run_hours))
    counter += 1

    #more times to enter?
    command_statement = input("Add Run? (Y/N): ")

#if break, print total run hours
print("Total run hours = "+str(hours_total))
