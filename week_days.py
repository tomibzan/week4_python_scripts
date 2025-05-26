day = input("Enter a day of the week (Monday-Sunday): ").lower()

match day:
    case "monday":
       print ("Wow!, day of calmness")
    case "tuesday":
       print("Get Up, go out for exercise")
    case "wednsday":
       print("Rest, make coffee")
    case "thursday":
       print("You need to run")
    case "friday":
       print("Conserve energy eat well")
    case "saturday" | "sunday":
       print("Productive weekend!")
    case _:
       print("Invalid")