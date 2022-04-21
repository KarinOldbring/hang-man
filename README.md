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

* Since the game continues such a vast majority of words the game can be quite complicated as of today. When developing the game features to set difficulty level could be implemented. One way this could be done is to limit the number of words that the computer picks it's random word from. The words could be divided into categories for example. Another way would be to set the length of the word to be guessed so that you could choose from shorter or longer words. 
* If you would like the game to be even more tricky, a timer could be used. The player then would have limited time, for example 20 seconds, to make their guess.  
* Since one round of playing is done pretty fast it would be a nice feature to be able to keep track of your previous games, a score count. This would work both when playing a number of rounds at once, to keep track if you or the computer are winning, but also when you visit the site again to check your track record from before. 
* Give the player the option to choose if they would like to have more turns each game, they could have the option of 9 turns instead of 6. 

## **Technologies Used**

This project was created using [Python](https://www.python.org/). Any other technologies present, such as JavaScript, are part of the Code Institue template used to create this project. 

## **Testing**

The game has been deployed using Heroku and runs in a command line Python Terminal. I've tested the site using Chrome, Edge and Firefox browser to make sure it runs as expected. I tried to cause the code to crash at various points using incorrect inputs, or no inputs, to try and make the code break it's loop. As there are numerous inputs for the player, I tested these during development. Below is the documentation of my testing: 


### **Enter Username**

* Expected Outcomes: When entering the game the player is asked to enter their name. A valid name contains only letters and is required for the player to continue. 

* Test: I tried entering names using letters, numbers, other signs and not entering anything at all. 

* Result: If entering a name and pressing enter the game would run and the name would display as intented. However if anything else was entered, number, signs or even left blank, the player could continue without a name by pressing enter. 

* Verdict: This test failed at this stage since the player was not forced to enter a valid name. 

* Solution: To resolve this issue, I added a **"while True"** statement, ensuring that game will not run without valid username. 

* Test 2: I tested incorrect inputs (digits, blanks, other signs) and correct inputs, to make sure the player can't get passed the name requirement. If input is invalid, the player should be encouraged to try again. 

* Result 2: With the **"while True"** statement, any invalid input printed the appropriate error message and requested correct input. 

* Verdict 2: This function now works, and the code loops through the game correctly. 

### **Play or not**

* Expected Outcomes: The player is asked if they want to play, player is supposed to answer by entering either Y, for yes, or No, for no. Any other inputs are expected to return an error message and request the player to choose 

* Test: I tried correct inputs (Y and N) as well as incorrect inputs, digits, blanks, other signsand letters. 

* Result: Correct inputs progressed the code correctly and incorrect inputs displayed a messeage prompting the player for the right input. 

* Verdict: Code functioned as intented and did not break at any stage. 

### **The Secret Word**

* Expected Outcomes: To run the game, the computer is supposed to select a random word from the words.py file. 

* Test: To ensure function was working as intended I made sure that different words were displayed each time a new game started. 

* Result: Since some words contains blanks or hyphens, I created a while loop to get the computer to choose another word if that was the case. New words got selected as intended but it was difficult to see how many letters the secret word contained since the underscores representing each letter was all in one line. 

* Verdict: The random word function worked as intented but the display of the secret word needed improvement. 

* Solution: To make it clear how many letters the secret word contains I added blanks between each underscore: " _ ". 

* Test 2: Ran game again to get computer to choose random word. 

* Result 2: The blanks make it easy to see how many letters are in the secret word. 

* Verdict 2: The secret word function runs as intented, presenting new random words, without blanks or hyphens, and the number of letters are also clearly displayed. 

### **Correct Letter**

* Expected Outcomes: Once the game is running, the player is presented with the secret word to guess. From start the player can see how many letters are in the secret word. If the guessed letter is in the secret word, the underscore in the word is supposed to be replaced by the correct letter. Each valid guess is to be displayed in a guessed letters list. 

* Test: Correct inputs; letters, and incorrect inputs; digits, blanks, other signs, were entered to test this function. 

* Result: Correct guesses reveal the letter in the secret word and is also added in the guessed letters list. 

* Verdict: The correct letter guesses works as intended. 

### **Wrong Letter**

* Expected Outcomes: If the guessed letter is not in the word, the player is encouraged to make another guess, if there are still turns to go. THe guessed letter is supposed to show in the guessed letters list and hanging stage display change, showing the player that they are one step closer to being hung. 

* Test: Correct inputs; letters, and incorrect inputs; digits, blanks, other signs, were entered to test this function. 

* Result: Wrong guesses are added in the guessed letters list, numbers of turns are decreasing and the display for hanging stage changes. 

* Verdict: The wrong letter guesses works as intended. 

### **Invalid Guess**

* Expected Outcomes: If the player inputs an invalid guess, i.e digits, blanks, other signs or a letter that has already been guessed, an error is supposed to be shown, encouraging the player to make another guess. 

* Test: Correct inputs; letters, and incorrect inputs; digits, blanks, other signs, were entered to test this function. 

* Result: If an invalid guess was entered an error is shown and the player is asked to choose one letter. As intented the number of turns reamain the same.  

* Verdict: The invalid guess works as intended. 

### **Player Loses**

* Expected Outcomes: If the player makes 6 valid guesses and still not manages to guess the secret word, the player loses. The secret word is displayed and the player is asked if they want to play again. 

* Test: Unsuccessful attempts at guessing the secret word were made. 

* Result: A message telling the player they lost appears, and the secret word is revealed. The player is asked if they wish to play again or not. 

* Verdict: The player loses function works as intented. 

### **Player wins**

* Expected Outcomes: If the player manages to guess the secret word using no more than 6 guesses, the player wins! The secret word is displayed and the player is asked if they want to play again. 

* Test: Successful attempts at guessing the secret word were made. 

* Result: A message telling the player they won apperars, and the secret word is displayed. The player is asked if they wish to play again or not. 

* Verdict: The player wins function works as intended. 

## **Validator**

![Pep8](/screenshots/pep8.png)

The python code was run through [Pep8 Online Check](http://pep8online.com/) to make sure there are no errors in the code. The known error, w292 no newline at end of file, is the only error showing. 

## **Bugs**

* When the player loses, the finas stage of hanging was not displayed but the secret word was revealed and the player asked if they want to play again. 
- Solution: Add print(stages_for_hanging(turns)) to the if-statement in the play_game function. 
* As explained in the testing section regarding the secret word, it was difficult for the player to determine how many letters the secret word contained. 
- Solution: Blanks were added before and after each underscore; " _ ". 

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