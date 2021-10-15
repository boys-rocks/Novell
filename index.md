---
title: Novell
has_children: true
nav_order: 1
---
# Novell Bot commands


#### Administrative Commands
* Analytics Commands -
  * Frequency: 
    * Usage: ```nv.freq <any Novell command>```
    * Description: Input a Novell command as the argument and receive an output of the number of times it has been used since Novell was added to the server
  * Top Commands:
      * Usage: ```nv.topcommands <n>```
      * Description: Input a number less than the total number of Novell commands and receive a chronological list of the Novell command's usage. The list starts with the highest used command and outputs the frequency of commands until the nth command is reached.
* Decision / Polling Commands -
  * Choose:
      * Usage: ``` nv.choose <option-one> <option-two> ... <option-n> ```
      * Description: Input a list of choices for Novell to make a selection from. Options must be one word.
  * Multiple Choice Poll:
      * Usage: ``` nv.multi_choice <option-one> <option-two> ... <option-n>```
      * Description: Input a list of choices to Novell to generate a multiple choice poll. Users interact with the poll by selecting the preset reactions on the poll message Novell outputs on command run.
  * Poll (Yes / No Question):
      * Usage: ``` nv.poll <yes / no question> ```
      * Description: Input a yes or no question to Novell to generate a poll for. Users interact with the poll by selecting the preset reactions on the poll message Novell outputs on command run.
  * Toss:
      * Usage: ``` nv.toss ```
      * Description: Input this command and Novell will output a heads or tails response randomly.
* Moderation Commands -
  * Ban User From Server:
      * Usage: ``` nv.ban <user name> <reason> ```
      * Description: Bans user from server for a provided reason.
      * Permission: ban_members = True
  * Kick User From Server:
      * Usage: ``` nv.kick <user name> <reason> ```
      * Description: Kicks user from server for a provided reason.
      * Permission: kick_members = True
  * Purge Chat Messages:
      * Usage: ``` nv.purge <n> ```
      * Description: Permanently deletes chat messages in the channel it is ran in, starting with the most reason message and going until the nth message (so long as n is less than 1000).
      * Permission: manage_messages = True



#### Boredom / Fun Commands
* Boredom Commands -
  * Activity:
      * Usage: ``` nv.activity ```
      * Description: On running this command, Novell will output a suggested activity.
  * Cat:
      * Usage: ``` nv.cat ```
      * Description: On running this command, Novell will output an image of a cute cat.
  * Country:
      * Usage: ``` nv.country <country name>```
      * Description: Input a country to Novell with this command and it will output information on the country provided.
  * Meme:
      * Usage: ``` nv.meme ```
      * Description: On running this command, Novell will output a hilarious meme image.
  * Name(Country guesser):
      * Usage: ``` nv.name <name> ```
      * Description: Input a name to Novell with this command and it will guess the country of origin of the provided name.
  * Trivia: 
      * Usage: ``` nv.trivia ```
      * Description: On running this command, Novell will output a fun trivia fact to enhance your noodle.
* Joke Commands -
  * Affirmation: 
      * Usage: ``` nv.affirm ```
      * Description: On running this command, Novell will output a positive affirmation message to stroke your fragile ego.
  * Chuck Norris: 
      * Usage: ``` nv.chuckjokes ```
      * Description: On running this command, Novell will output a totally not tired Chuck Norris joke for your pleasure.
  * Insult: 
      * Usage: ``` nv.insult ```
      * Description: On running this command, Novell will output a sick burn against you.
  * Jokes: 
      * Usage: ``` nv.joke ```
      * Description: On running this command, Novell will output a joke that is sure to put you in stitches.
  * Programmer jokes: 
      * Usage: ``` nv.projoke ```
      * Description: On running this command, Novell will output a joke to satisfy your corny programmer humor itch.
* Quote Commands -
  * Quote:
      * Usage: ``` nv.quote ```
      * Description: On running this command, Novell will output a sick and totally not edgy anime character quote, along with name of the quoted character and the anime they are from
* Waifu Commands -
  * Get Waifu:
      * Usage: ``` nv.waifu <search criteria>```
      * Description: On running this command, Novell will search the web for the best waifu to match your search criteria.

#### Game Commands
* Hangman -
  * Usage: ``` nv.hangman ```
  * Description: Play hangman with Novell. Run the command to start the game. After that, guess letters (no commands necessary for guesses) and try to complete the word.
* Higher / Lower Guessing -
  * Usage: ``` nv.higherlower```
  * Description: Play a higher lower guessing game with Novell. Guess between randomized options from Novell for which quantity is greater. Input your guesses in the chat (no commands necessary for guesses)
* Paper Trading -
  * Balance:
      * Usage: ``` nv.balance ```
      * Description: On command run, Novell outputs the cash value of your paper trading account.
  * Buy:
      * Usage: ``` nv.buy <symbol> <amount> ```
      * Description: On command run, buys the coins specified in the amount specified.
      * Parameter ```<symbol>``` potential values: See Binance.com for coin list.
  * Coins:
      * Usage: ``` nv.coins ```
      * Description: On command run, Novell outputs a list of the coins you have.
  * New Account:
      * Usage: ``` nv.newacc ```
      * Description: On command run, creates a new account for the user running the command.
  * Portfolio:
      * Usage: ``` nv.portfolio ```
      * Description: On command run, Novell outputs your portfolio value.
  * Price:
      * Usage: ``` nv.price <symbol> ```
      * Description: On command run, Novell outputs the value of the coins specified.
      * Parameter ```<symbol>``` potential values: See Binance.com for coin list.
  * Sell:
      * Usage: ``` nv.sell <symbol> <amount> ```
      * Description: On command run, sells the coins specified in the amount specified.
      * Parameter ```<symbol>``` potential values: See Binance.com for coin list.
* Rock Paper Scissors -
  * Usage: ``` nv.rps ```
  * Description: Play rock paper scissors with Novell. Running the command toggles the game. Make your selection between rock, paper, or scissors in the chat (no command needed for the selection).
* Tic Tac Toe -
  * Multiplayer: 
      * Usage: ``` nv.play_tic_tac_toe_multiplayer <player> ```
      * Description: Play tic-tac-toe with another player, hosted by NUUB-HOT. Input another player's name when running the command to play against them. The command initiates the game. Once started, you will input numbers 1-9 to indicate position to placement on the board (no command needed after game initiated).
  * Singleplayer: 
      * Usage: ``` nv.play_tic_tac_toe <difficulty> ```
      * Description: Play tic-tac-toe with Novell. Input a difficulty for Novell to play against you. The command initiates the game. Once started, you will input numbers 1-9 to indicate position to placement on the board (no command needed after game initiated).
      * Parameter <difficulty> potential values: easy, difficult, impossible


#### Miscellaneous Commands
* Sound Commands -
  * Nyan Cat:
      * Usage: ``` nv.nyan ```
      * Description: Plays the Nyan Cat song in the voice chat.
  * Pause:
      * Usage: ``` nv.pause ```
      * Description: Pauses the current playing audio in the voice chat.
  * Play:
      * Usage: ``` nv.play <URL> ```
      * Description: Plays sound in the voice channel from the specified URL.
  * Pog:
      * Usage: ``` nv.pog <directory> ```
      * Description: Plays a random sound in the voice chat from specified directory.
      * Parameter ```<directory>``` potential values: animesounds, starwars
  * Rap:
      * Usage: ``` nv.rap <directory> ```
      * Description: Plays text to speech from song lyrics or text files in the voice channel.
      * Parameter ```<directory>``` potential values: asap, eazye, juicewrld, lilpeep, trump
  * Resume:
      * Usage: ``` nv.resume ```
      * Description: Resumes the current playing audio in the voice chat.
  * Song:
      * Usage: ``` nv.song ```
      * Description: Creates a song from a sound clip.
  * Stop:
      * Usage: ``` nv.stop ```
      * Description: Stops current playing audio in the voice chat.
  * Text to Speech:
      * Usage: ``` nv.tts <text> ```
      * Description: Input a message to Novell via this command and it will read it in the voice chat.



#### Utility Commands
* Away From Keyboard (AFK) Command - 
  * Usage: ``` nv.afk ```
  * Description: On running this command, Novell toggles your AFK status. If it is your first time running it, you are set to AFK status. If it is a second run of the command, you will be removed from AFK status. If you send messages after setting your status to AFK, you will be removed from AFK status without having to toggle your status again.
* Calculation Commands - 
  * Calculator:
      * Usage: ``` nv.clc <expression> ```
      * Description: Input an arithmetic expression to Novell via this command and it will evaluate the arithmetic.
  * Convert binary to decimal:
      * Usage: ``` nv.convert_from_bin <binary-number> ```
      * Description: Input a binary number to Novell via this command and it will output the decimal equivelent. 
  * Convert decimal to binary: 
      * Usage: ``` nv.convert_to_bin <decimal-number> ```
      * Description: Input a decimal number to Novell via this command and it will output the binary equivelent.
  * Convert decimal to hexadecimal
      * Usage: ``` nv.convert_to_hex <decimal-number> ```
      * Description: Input a decimal number to Novell via this command and it will output the hexadecimal equivelent.
  * Convert hexadecimal to decimal
      * Usage: ``` nv.convert_from_hex <hexadecimal-number> ```
      * Description: Input a hexadecimal number to Novell via this command and it will output the decimal equivelent.
* Dictionary -
  * Usage: ``` nv.dictionary <word> ```
  * Description: Input a word to Novell via this command and it will output its definition.
* Listening Commands -
  * Bot Join Voice Chat:
      * Usage: ``` nv.join ```
      * Description: Pulls Novell into your current voice channel. 
  * Bot Leave Voice Chat:
      * Usage ``` nv.leave ```
      * Description: Kicks Novell out of your current voice channel.
* Search Commands - 
  * Github Repository Search:
      * Usage: ``` nv.ghrepo <user> <repository> ```
      * Description: Input a GitHub user name and a GitHub repository name to Novell via this command and it will output information on the specified repository.
  * Github User Search:
      * Usage: ``` nv.ghuser <user> ```
      * Description: Input a GitHub user name to Novell via this command and it will output information on the specified user.
  * Pypi search:
      * Usage: ``` nv.pypi <package> ```
      * Description: Input a PyPi package name to Novell via this command and it will output information on the specified package.
  * Wikipedia search:
      * Usage: ``` nv.search <search criteria> ```
      * Description: Input a search phrase to Novell via this command and it will check Wikipedia for information on the search phrase.
* Security Commands (NOT INTENDED FOR REAL SECURITY PURPOSES!) -
  * Create Hash:
      * Usage: ``` nv.make_hash <hashing-algorithm> <text> ```
      * Description: Input a hashing algorithm and text to be hashed to Novell via this command and it will output the hash of the input text using the specified algorithm.
      * Parameter ```<hashing-algorithm>``` potential values: md5, sha1, sha256, sha512
  * Create Password:
      * Usage: ``` nv.getpassword <n> ```
      * Description: Input a length and Novell will generate a password of the specified length. If no length is provided, a default password of length 15 will be output.
* URL Shortener -
  * Usage: ``` nv.shrink <URL> ```
  * Description: Input a URL to Novell via this command and it will output a shortened version of it.
* Weather Search - 
  * Usage: ``` nv.weather <location> ```
  * Description: Input a location to Novell via this command and it will output the temperature for that location in fahrenheit and celsius. For best result, use the format of City, State, Country.
