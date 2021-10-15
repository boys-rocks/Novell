---
title: Utility Commands
parent: index
nav_order: 1
---


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
