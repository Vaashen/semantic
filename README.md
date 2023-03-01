># semantic

This is a simple python application that is based on "Semantic Similarity". It is using the modeule 
'en_core_web_md' to check the similarity between 2 or more words, and will return a float (decimal number)
showing how similar the words are, it uses a scale from 0 to 1, where 0 is the least similar and 1 being the most similar.

<br>

># How to run the app 
Download the files from the repo and create a folder for them on you device.
Open the command line and go into the directory that contains the files, you can use the command `cd` followed by the name of the folder.
Now in the command line, once you have navegated to the files, type in the command: `docker build -t semantic-app`.
It should take a few seconds to install everything, once that is done. Type in the command: `docker run -i semantic-app`. If everything installed correctly the code should work.
