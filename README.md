# Anki-Parser
Parser from txt file -> anki importable deck
So. I wanted to digitalize my textbook originally written in english.

First page I've done by hand, and thought that i could optimize this
Second one I used ctrl+c alt+tab ctrl+v to copy from digital copy of the book to anki add cards by hand
And then I thought that there must be a way of using a script here.

When i copied it by hand it looked like this
adoptive parents
/əˈdɒptɪv peərənts/
rodzice adopcyjni	
ancestor
/ˈænsestə/
przodek	

It goes like this:
english word
pronunciation 
polish word

I went to anki dock and saw that I needed such format 
adoptive parents	rodzice adopcyjni
rodzice adopcyjni	adoptive parents
ancestor	przodek
przodek	ancestor

just as an example. Rest was a simple python script that may help somebody
If you want to import from txt file in anki,
you have to enter into a deck you want to put data into, 
then click file -> import and select the output file

Hope it will be usefull to somebody!