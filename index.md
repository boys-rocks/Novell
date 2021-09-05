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
* Waifu Commands -


#### Game Commands



#### Miscellaneous Commands



#### Utility Commands