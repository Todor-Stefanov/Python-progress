On the first line, you will receive the starting quantity of water (integer) in a dispenser. Then, on the following lines, you will be given the names of some people who want to get water (each on a separate line) until you receive the command **"Start"**. Add those people in a queue. Finally, you will receive some commands until the command **"End"**:
-	**"{liters}"** - litters (integer) that the current person in the queue wants to get. Check if there is enough water in the dispenser for that person.
    - If there is enough water, print **"{person_name} got water"** and remove him/her from the queue.
    - Otherwise, print **"{person_name} must wait"** and remove the person from the queue without reducing the water in the dispenser.
-	**"refill {liters}"** - add the given litters in the dispenser.  

In the end, print how many liters of water have left in the format: **"{left_liters} liters left"**.
