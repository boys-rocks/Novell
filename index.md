## NUUB-BOT Command Documentation - V0.02

#### Administrative Commands
* Analytics Commands -
  * Frequency: 
    * Usage: ```nb.freq <any NUUB-BOT command>```
    * Description: Input a NUUB-BOT command as the argument and receive an output of the number of times it has been used since NUUB-BOT was added to the server
  * Top Commands:
      * Usage: ```nb.topcommands <n>```
      * Description: Input a number less than the total number of NUUB-BOT commands and receive a chronological list of the NUUB-BOT command's usage. The list starts with the highest used command and outputs the frequency of commands until the nth command is reached.
* Decision / Polling Commands -
  * Choose:
      * Usage: ``` nb.choose <option-one> <option-two> ... <option-n> ```
      * Description: Input a list of choices for NUUB-BOT to make a selection from. Options must be one word.
  * Multiple Choice Poll:
      * Usage: ``` nb.multi_choice <option-one> <option-two> ... <option-n>```
      * Description: Input a list of choices to NUUB-BOT to generate a multiple choice poll. Users interact with the poll by selecting the preset reactions on the poll message NUUB-BOT outputs on command run.
  * Poll (Yes / No Question):
      * Usage: ``` nb.poll <yes / no question> ```
      * Description: Input a yes or no question to NUUB-BOT to generate a poll for. Users interact with the poll by selecting the preset reactions on the poll message NUUB-BOT outputs on command run.
  * Toss:
      * Usage: ``` nb.toss ```
      * Description: Input this command and NUUB-BOT will output a heads or tails response randomly.
* Moderation Commands -
  * Ban User From Server:
      * Usage: ``` nb.ban <user name> <reason> ```
      * Description: Bans user from server for a provided reason.
      * Permission: ban_members = True
  * Kick User From Server:
      * Usage: ``` nb.kick <user name> <reason> ```
      * Description: Kicks user from server for a provided reason.
      * Permission: kick_members = True
  * Purge Chat Messages:
      * Usage: ``` nb.purge <n> ```
      * Description: Permanently deletes chat messages in the channel it is ran in, starting with the most reason message and going until the nth message (so long as n is less than 1000).
      * Permission: manage_messages = True



#### Boredom / Fun Commands
* Boredom Commands -
  * Activity:
      * Usage: ``` nb.activity ```
      * Description: On running this command, NUUB-BOT will output a suggested activity.
  * Cat:
      * Usage: ``` nb.cat ```
      * Description: On running this command, NUUB-BOT will output an image of a cute cat.
  * Country:
      * Usage: ``` nb.country <country name>```
      * Description: Input a country to NUUB-BOT with this command and it will output information on the country provided.
  * Meme:
      * Usage: ``` nb.meme ```
      * Description: On running this command, NUUB-BOT will output a hilarious meme image.
  * Name(Country guesser):
      * Usage: ``` nb.name <name> ```
      * Description: Input a name to NUUB-BOT with this command and it will guess the country of origin of the provided name.
  * Trivia: 
      * Usage: ``` nb.trivia ```
      * Description: On running this command, NUUB-BOT will output a fun trivia fact to enhance your noodle.
* Joke Commands -
  * Affirmation: 
      * Usage: ``` nb.affirm ```
      * Description: On running this command, NUUB-BOT will output a positive affirmation message to stroke your fragile ego.
  * Chuck Norris: 
      * Usage: ``` nb.chuckjokes ```
      * Description: On running this command, NUUB-BOT will output a totally not tired Chuck Norris joke for your pleasure.
  * Insult: 
      * Usage: ``` nb.insult ```
      * Description: On running this command, NUUB-BOT will output a sick burn against you.
  * Jokes: 
      * Usage: ``` nb.joke ```
      * Description: On running this command, NUUB-BOT will output a joke that is sure to put you in stitches.
  * Programmer jokes: 
      * Usage: ``` nb.projoke ```
      * Description: On running this command, NUUB-BOT will output a joke to satisfy your corny programmer humor itch.
* Quote Commands -
  * Quote:
      * Usage: ``` nb.quote ```
      * Description: On running this command, NUUB-BOT will output a sick and totally not edgy anime character quote, along with name of the quoted character and the anime they are from
* Waifu Commands -
  * Get Waifu:
      * Usage: ``` nb.waifu <search criteria>```
      * Description: On running this command, NUUB-BOT will search the web for the best waifu to match your search criteria.

#### Game Commands



#### Miscellaneous Commands



#### Utility Commands
* Away From Keyboard (AFK) Command - 
  * Usage: ``` nb.afk ```
  * Description: On running this command, NUUB-BOT toggles your AFK status. If it is your first time running it, you are set to AFK status. If it is a second run of the command, you will be removed from AFK status. If you send messages after setting your status to AFK, you will be removed from AFK status without having to toggle your status again.
* Calculation Commands - 
  * Calculator:
      * Usage: ``` nb.clc <expression> ```
      * Description: Input an arithmetic expression to NUUB-BOT via this command and it will evaluate the arithmetic.
  * Convert binary to decimal:
      * Usage: ``` nb.convert_from_bin <binary-number> ```
      * Description: Input a binary number to NUUB-BOT via this command and it will output the decimal equivelent. 
  * Convert decimal to binary: 
      * Usage: ``` nb.convert_to_bin <decimal-number> ```
      * Description: Input a decimal number to NUUB-BOT via this command and it will output the binary equivelent.
  * Convert decimal to hexadecimal
      * Usage: ``` nb.convert_to_hex <decimal-number> ```
      * Description: Input a decimal number to NUUB-BOT via this command and it will output the hexadecimal equivelent.
  * Convert hexadecimal to decimal
      * Usage: ``` nb.convert_from_hex <hexadecimal-number> ```
      * Description: Input a hexadecimal number to NUUB-BOT via this command and it will output the decimal equivelent.
* Dictionary -
  * Usage: ``` nb.dictionary <word> ```
  * Description: Input a word to NUUB-BOT via this command and it will output its definition.
* Listening Commands -
  * Bot Join Voice Chat:
      * Usage: ``` nb.join ```
      * Description: Pulls NUUB-BOT into your current voice channel. 
  * Bot Leave Voice Chat:
      * Usage ``` nb.leave ```
      * Description: Kicks NUUB-BOT out of your current voice channel.
* Search Commands - 
  * Github Repository Search:
      * Usage: ``` nb.ghrepo <user> <repository> ```
      * Description: Input a GitHub user name and a GitHub repository name to NUUB-BOT via this command and it will output information on the specified repository.
  * Github User Search:
      * Usage: ``` nb.ghuser <user> ```
      * Description: Input a GitHub user name to NUUB-BOT via this command and it will output information on the specified user.
  * Pypi search:
      * Usage: ``` nb.pypi <package> ```
      * Description: Input a PyPi package name to NUUB-BOT via this command and it will output information on the specified package.
  * Wikipedia search:
      * Usage: ``` nb.search <search criteria> ```
      * Description: Input a search phrase to NUUB-BOT via this command and it will check Wikipedia for information on the search phrase.
* Security Commands (NOT INTENDED FOR REAL SECURITY PURPOSES!) -
  * Create Hash:
      * Usage: ``` nb.make_hash <hashing-algorithm> <text> ```
      * Description: Input a hashing algorithm and text to be hashed to NUUB-BOT via this command and it will output the hash of the input text using the specified algorithm.
      * Parameter <hashing-algorithm> potential values: md5, sha1, sha256, sha512
  * Create Password:
      * Usage: ``` nb.getpassword <n> ```
      * Description: Input a length and NUUB-BOT will generate a password of the specified length. If no length is provided, a default password of length 15 will be output.
* URL Shortener -
  * Usage: ``` nb.shrink <URL> ```
  * Description: Input a URL to NUUB-BOT via this command and it will output a shortened version of it.
* Weather Search - 
  * Usage: ``` nb.weather <location> ```
  * Description: Input a location to NUUB-BOT via this command and it will output the temperature for that location in fahrenheit and celsius. For best result, use the format of City, State, Country.
