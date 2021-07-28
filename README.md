# Read me for Battleship Game

## Introduction
The sole purpose for this python project was following a brief layout for my third milestone project, building a battleship game using python was suggested as an idea within the brief therefore I decided to give it a go.<br>
Using a game, I feel is a fun and interactive way to display my knowledge in python.

## Features
My battleship game, will be displayed in a 10x10 grid. It is a one player game. There will be 8 ships of variable lengths, randomly placed around the grid by the computer. The user will start with 50 bullets to take down the ships. The user must choose a row and column of where they would like to shot, the row must be picked by a letter from the range A-J and the column is picked using a number from the range 0-9, they must be typed into the terminal together such as A3. This will indicate exactly where the user would like to shot on the grid.<br>
For every shot that shots or misses, it will be shown on the grid using a symbol from a legend explained below and outlined in a comment in the code for this game.<br>
A ship cannot be placed diagonally in this battleships game. Therefore when a shot hits, the rest of that ship can only be in one of four directions, left, right, up, or down.<br>
To win this battleship game, all 8 ships must be fully unearthed before running out of bullets. If you have used all 50 bullets and have not found all eight ships, you lose.<br>
The legend in this game is as follows:<br>
"." = empty space<br>
"O" = part of the ship (unhit)<br>
"X" = part of the ship hit with a bullet<br>
"#" = empty space hit with a bullet (a miss because it hit no ship)<br>
## Testing
To test that this python battleships game was working correctly, I first added a function to my code called debug_mode. This debug_mode is equal to false when the game is being played but to test that all functions in my code were working correctly I set this equal to true (debug_mode = True). What this did is aloud me to see where the computer had placed the ships using the symbol from the above legend of "O", when these symbol were visible I could hit and miss while playing the game to ensure the correct message was being displayed in these situations.<br>
I also tested the python using
## Technology
* Python was the main language used in this battleships game. An extension of python had to be installed for it to be used correctly.
* I used GitHub to store my code
* I used GitPod to write my code
* I used [heroku](https://dashboard.heroku.com/apps) to deploy my python project
## Deployment
## Credits
As always I relied heavily on my code institute [course notes.](https://discuss.codecademy.com/t/excellent-battleship-game-written-in-python/430605)<br>I also used a number of websites and Youtube videos when building this battleships game in python these include:<br>
### Youtube Video
* [freeCodeCamp.org](https://www.youtube.com/watch?v=rfscVS0vtbw&t=222s)
* [Programming with Mosh](https://www.youtube.com/watch?v=_uQrJ0TkZlc)
* [freeCodeCamp.org](https://www.youtube.com/watch?v=8ext9G7xspg&t=2134s)
* [Learn Python with CodeCademy: Battleship!](https://www.youtube.com/watch?v=7Ki_2gr0rsE&t=883s)
* [Robert Heaton](https://www.youtube.com/channel/UCOp0YjvVlwp-GfdpgX0V3sA)
* [CS Students](https://www.youtube.com/watch?v=MgJBgnsDcF0)
### Websites
* [w3school](https://www.w3schools.com/python/default.asp)
* [stackoverflow](https://stackoverflow.com/questions/tagged/python)
* [CodeCademy](https://discuss.codecademy.com/t/excellent-battleship-game-written-in-python/430605)

