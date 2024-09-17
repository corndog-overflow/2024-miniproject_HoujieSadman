# SADMAN KABIR, HOUJIE XIONG MINI PROJECT
# THIS README IS A COPY OF Report.md IN THE REPO
*** API KEYS are obfuscated via environment variable, running this project will not work without the actual API keys which are not included in this repo.

# EXERCISE 1

I found max_bright = 50000, min_bright = 13000 to work well.
Video: https://drive.google.com/file/d/1poDTyKDpKiJNFNspiosgc4Bz6xrph9xx/view?usp=sharing


# EXERCISE 2:

Code found in exercise_sound.py, it plays the intro to toccata and fugue in d minor.
Video: https://drive.google.com/file/d/19Zg6qp6rDTfPMSJX8wQfVWdqUt--pyr8/view?usp=sharing


# EXERCISE 3; HOW IT WORKS:

Video: https://drive.google.com/file/d/11qYbl1SCVdqrzu1bXacUKSWjNf5vF1U7/view?usp=sharing

1. N = 10 LED BLinks and reaction time measured, then sorted into min, max and avg;
   This data is then sent to our ThingSpeak database via **HTTPS REST API call.**

   ![image](https://github.com/user-attachments/assets/2f12d983-8ed9-4581-a465-0a1d51161aa7)


   We push the data to our database:
   ![image](https://github.com/user-attachments/assets/4a33befa-2534-47be-85bd-41dadd4cd1bb)


   Our data, visualized in our database.
   ![image](https://github.com/user-attachments/assets/c78d1bde-5969-4155-a153-a998cdf23cc3)


2. In our REACT Web app, we then fetch that data and do so every 5 seconds to update constantly:

   ![image](https://github.com/user-attachments/assets/6964ea49-5252-487a-93af-e1f1d1f28f1a)

3. Resulting in the following web app, pulling data from the cloud, from our hardware:

   ![image](https://github.com/user-attachments/assets/14049065-a8e2-4179-9988-0c7ac7969855)


