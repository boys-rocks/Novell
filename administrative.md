---
title: Administrative Commands
parent: Novell
nav_order: 1
---
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
