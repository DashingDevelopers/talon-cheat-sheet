# talon-cheat-sheet
printable well formatted cheat sheet for all available contexts

copied and modded from https://gist.github.com/tararoys/c538b7ae8e1f21db9a794c2c0f5becf4

#Talon Voice Commands Cheatsheet


1. Have talon installed and running on your computer following the instructions at [talonvoice.com](https://talonvoice.com/docs/index.html#getting-started)
2. Have this repo cloned  into the user directory of ~/talon.  This makes these scripts available to talon.
3. Say "print cheatsheet" or Open the talon repl and type

```
actions.user.cheatsheet()
```

Then open the cheatsheet.html file in your browser.  You can also print it to have a hard copy.
The HTML includes page breaks, so it should come out fairly nicely.


I apologize for the ugly code, I just wanted to make it work so I can print the commands out so I could have them on my wall

The algorithms for  counting the number of lines to calculate page breaks page breaks are assuming A4,
and were derived from multiple ones until it seemed to work for me with the contexts that I have!

In order not to waste paper,  I simply deleted all of the folders from the talent community apps folder  that had applications I knew I would never use.

Also for readability,  I  skipped identifying which OS the commands were for on the basis that  I'd be able to work it out anyway.
 do use mac windows and Linux for my operations but I rarely touch anything other than Linux so I can't say for sure that  this logic is sound.





Suggested Future features:

Add a way to print a  cheat sheet from a single user context to cater for new user repositories and applications.
It might just be easier to generate individual HTML files per context so that no configuration is required  by users who don't know how to use PHP.
Alternatively you can  just let the page you want in the browser when you're printing there's only one thing  that has changed

Feel free to contribute to this repo.  I will be happy to accept pull requests.

/Paul
