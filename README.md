# Time-Difference-Calculator-and-Accumulator
Python script to calculate difference in times that can be accumulated per execution of the code

This code is use case specific for a simple hand calculation that I wanted to avoid at work.

I needed to hand-calculate the run times for a device, where I had the times for when it turned on and off, and I had multiple of these devices to verify against logic I had already deployed on the system to determine accuracy. Instead of calculating the difference between the times by hand and adding them up, I created this simple script on an online Python compiler to do the calculations for me.

The code asks for permission to start and asks for the start time and end time for the run
After you input it, it returns the run number, the inputted values, and the difference.
It then asks if you want to add more runs for this particular "device".
If yes, you repeat the steps above and receive the "Add run" question again.
If no, the total runtime for this iteration/device is output as "Total runtime"

FUTURE WORK:
-Add tabular approach to the data storage
-Add I/O exception catches
-Create non-volatile data, where you can delete an entry if there was a typo
-Create differenet device objects?
