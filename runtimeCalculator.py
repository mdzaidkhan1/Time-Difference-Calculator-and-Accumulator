counter = 1
hours_total = 0
command_statement = input("Start time difference calculator? (Y/N) :")

while command_statement != 'N':
    start_time = input("Enter start time in HH:MM:SS: ")
    end_time = input("Enter end time in HH:MM:SS: ")
    start_split = start_time.split(":")
    end_split = end_time.split(":")
    
    start_hr = int(start_split[0])
    start_min = int(start_split[1])
    start_sec = int(start_split[2])
    
    end_hr = int(end_split[0])
    end_min = int(end_split[1])
    end_sec = int(end_split[2])
    
    if end_sec < start_sec:
        end_sec += 60
        end_min -= 1 
    
    sec_in_hours = (end_sec - start_sec) / 3600
    
    if end_min < start_min:
        end_min += 60
        end_hr -= 1
    
    min_in_hours = (end_min - start_min) / 60
    
    hours = end_hr - start_hr
    
    run_hours = hours + min_in_hours + sec_in_hours
    hours_total += run_hours
    
    if counter == 0:
        print("Run\tStart Time\tEnd Time\t Hours\n")
    
    print(str(counter)+"\t"+start_time+"\t"+end_time+"\t"+str(run_hours))
    counter += 1
    
    command_statement = input("Add Run? (Y/N): ")

print("Total run hours = "+str(hours_total))
