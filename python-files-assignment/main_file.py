###         Question: File-Based Data Processing and Logging System        ###

with open('numbers.txt', 'r') as file:
    numbers = []

    for line in file:
        line = line.strip()
        if line != "":
            numbers.append(int(line))

total_value = len(numbers)
total_sum = sum(numbers)

if total_value > 0:
    avg = total_sum / total_value
else:
    avg = 0

with open('results.log', 'a') as log:
    log.write('File opened successfully\n')
    log.write('Data loaded successfully\n')
    log.write('Read '+str(total_value)+' numbers\n')
    log.write('Sum:'+str(total_sum)+"\n")
    log.write('Average:'+str(avg)+'\n')
    log.write('Processing completed\n')