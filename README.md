# **Hangman Game!**

![Am I Responsive](/screenshots/am-i-responsive.png)

## **Aim of the site**

The site is for users who want to play a fun game of Hangman. There are a great number of random words, 2466 to be precise, so the game can be quite tricky even without any difficulty levels present. The player has 6 guesses before the game is over and the number of turns left will be displayed using the classic hangman images (a man being hung). 

[The deployed site can be seen here](https://hang-or-not.herokuapp.com/)

## **Game Features**
### **Title Screen**

![Welcome screen](/screenshots/welcome.png)

The welcome screen welcomes the player to the site and provides the player with the rules of the game. The welcome screen also asks the player to enter their name. 

### **Enter username to continue**

![Username to start](/screenshots/playername.png)
![Invalid option](/screenshots/invalid-option.png)

Once the player has entered their name, they are asked if they want to play. If they choose yes (Y) the game starts, if they choose no (N) then they are being thanked for their participation and the game ends. If anything else is entered they get an invalid option message. 

### **Play Game**

**The secret word**

![Start game](/screenshots/start-game.png)

The secret word is randomly picked by the computer and the game can now begin. A number of underscores are displayed to show the player the number of letters present in the secret word. The player is now asked to pick a letter. Number of turns are displayed, which are 6 from the start. 

**Correct Letter**

![Correct letter](/screenshots/correct-letter.png)

If the letter chosen by the player is in the secret word the underscore where the letter goes will be replaced with it. All guessed letters are also displayed for the player to be able to keep track. The number of turns are not decreased since the guess was correct. 

**Wrong Letter**

![Wrong letter](/screenshots/wrong-letter.png)

If the letter chosen by the player is incorrect the number of turns will decrease by one and the visual will change showing that the hanging is approaching... The incorrect letter is added to the list of guessed letters. 

**Invalid guess**

![Invalid guess](/screenshots/invalid-guess.png)

If the player makes an invalid choice, i.e a digit, multiple letters, a previously guessed letter or any other sign that is not a letter, an error will occur telling the player to make another guess. The number of turns left will not be decreased but the player is encouraged to keep guessing. 

**Player loses**

![Player loses](/screenshots/gameover.png)

If 6 incorrect guesses are made the player will lose, hang. The secret word is revealed and so is a visual of the poor player being hung. The player is asked if they wish to play again. If so, they do not need to enter name again but the game just runs from the start. 

**Player wins**

![Player wins](/screenshots/win.png)

If the player manages to guess the correct word the player wins and hence does not need to hang! Also here the player gets to choose whether or not they wish to play again. 

## **Possible Future Features**

* Set difficulty level; limit numbers of words or the lenght of the word to be guessed. 
* Add timer to force the player to guess within a given timelimit. 

## **Technologies Used**

This project was created using [Python](https://www.python.org/). Any other technologies present, such as JavaScript, are part of the Code Institue template used to create this project. 

## **Testing**

The game has been deployed using Heroku and runs in a command line Python Terminal. I've tested the site using Chrome, Edge and Firefox browser. To make sure the game runs as expected I tried entering invalid inputs as mentioned in the features section. To my knowledge the game runs as it is supposed to and no known bugs are found. 

## **Validator**

![Pep8](/screenshots/pep8.png)

The python code was run through [Pep8 Online Check](http://pep8online.com/) to make sure there are no errors in the code. The known error, w292 no newline at end of file, is the only error showing. 

## **Deployment**

The page was deployed using Heroku. The procedure to do this was:
1. Use [GitHub](https://github.com) to build project.
2. Push built project code to GitHub.
3. Navigate to [Heroku](https://heroku.com)
4. Login or signup to the site.
5. Select create a new app, select a unique name and region.
6. Click settings, then reveal config vars.
7. Add PORT to the KEY field and 8000 to the VALUE field.
8. Select Buildpack, select Python and save.
9. Select Buildpacks again and select Nodejs and save again.
10. Ensure order of Buildpacks is Python then Nodejs.
11. Navigate to the deploy tab, choose GitHub as deployment method and connect to you GitHub account.
12. Enter your repository and connect.
13. Select either automatic deploys which automatically deploys whenever you push to GitHub, or manual deploys to deploy manually.
14. Since Heroku made updates the procedure to deploy required additional steps in Gitpod. To deploy the following commands were forced to be run in the terminal:
- heroku login -i (enter username and password)
- heroku git:remote -a your_app_name_here
- git push heroku main
15. Once deployment is finished, click view to be taken to the deployed app.
16. [Live site here](https://hang-or-not.herokuapp.com/)

## **Credits**

**Content**

To create this game I watched a number of tutorials for inspiration and ideas;
(https://www.youtube.com/watch?v=cJJTnI22IF8)
(https://www.youtube.com/watch?v=m4nEnsavl6w)
(https://www.youtube.com/watch?v=JNXmCOumNw0)
Whilst I've tried to deviate as much as possible there may be similarities in the code. The visual of the hanging stages was taken from (https://www.youtube.com/watch?v=m4nEnsavl6w&t=3s)
The list of random words is from (https://www.randomlists.com/data/words.json)

**Thanks**

I would like to thank my mentor [Richard Wells](https://github.com/D0nni387) for great support and encouragement! 