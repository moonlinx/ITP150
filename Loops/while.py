# Set the counter at 0 for initialization
i = 0

# While loops will continue to run as long as the condition is met
#WARNING: You must have a way to end the loop or the program will run forever
while i < 10:
    # Print the number and increment the counter
    # NOTE: This is the same as i = i + 1
    i += 1
    if i == 5:
        print("This is the number 5")
        # Instead of continuing the loop, skip to the next iteration
        continue
    print(i)
# The program will stop when i = 10
