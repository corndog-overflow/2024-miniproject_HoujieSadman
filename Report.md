# SADMAN KABIR, HOUJIE XIONG MINI PROJECT

# EXERCISE 1

I found max_bright = 50000, min_bright = 13000 to work well.


# EXERCISE 2:

Code found in exercise_sound.py, it plays the intro to toccata and fugue in d minor.

# EXERCISE 3; HOW IT WORKS:

![image](https://github.com/user-attachments/assets/4a33befa-2534-47be-85bd-41dadd4cd1bb)


1. N = 10 LED BLinks and reaction time measured, then sorted into min, max and avg;
   This data is then sent to our ThingSpeak database via HTTPS REST API call.

2. In our REACT Web app, we then fetch that data and do so every 5 seconds to update constantly:

![image](https://github.com/user-attachments/assets/6964ea49-5252-487a-93af-e1f1d1f28f1a)

3. Resulting in the following web app, pulling data from the cloud, from our hardware:

![image](https://github.com/user-attachments/assets/16a4e3be-0798-4fc9-97be-abdc6e8ba091)


