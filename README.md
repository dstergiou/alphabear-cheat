# Alphabear-cheat

Quick and dirty hack to cheat on the [AlphaBear](https://spryfox.com/our-games/alphabear2/) game

Program runs in a loop, expects 1 or 2 inputs:

* With 1 input: letters, e.g: `hjreuis` (letters on the board)
* With 2 inputs: `hjreuis jre` (letters on the board, require the word to contain the letters `j` `r` and `e`)
  * If the second input is prefixed with `+`, only words that contain the input in order will be returned (to facilitate boards with prefix/suffix words like `Non`, `Port`, etc.)
