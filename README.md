# talon-cheat-sheet
printable well formatted cheat sheet for all available contexts

copied and modded from https://gist.github.com/A/c538b7ae8e1f21db9a794c2c0f5becf4

Talon Voice Commands Cheatsheet


1. Have talon installed and running on your computer following the instructions at [talonvoice.com](https://talonvoice.com/docs/index.html#getting-started)
2. Have this repo cloned  into the user directory of ~/talon.  This makes these scripts available to talon.
3. Say "print cheatsheet" or Open the talon repl and type

```
actions.user.cheatsheet()
```

Then open the cheatsheet.html file  which is generating in the lib directory of this project in your browser ( google chrome works, firefox doesn't).
You can then print it to have a hard copy, or save it as a PDF.

The HTML includes page breaks,  as well as breaks within the tables describing the commands of each context, so it should come out fairly nicely.

The within table logic breaks every five lines,  unless each command is starting roughly the same in which case it defers the page break until a suitable endpoint

An example of how this looks  in pdf format is in the example output folder.

The page break logic doesn't quite work if you try and edit it in word or or libre office, 
Everything's works fine with  google chrome,  firefox gives me some kind of security error,  I've not tested elsewhere.

I apologize for the ugly code, I just wanted to make it work so I can print the commands out so I could have them on my wall

The algorithms for  counting the number of lines to calculate page breaks page breaks are assuming A4,
and were derived from multiple runs until it seemed to work for me with the contexts that I have!
It may be that if you're using US letter format that the page breaks are not appropriate.

 I was unable to find a way to programmatically pass the formatters and show the results so I hardcoded them.
 if new ones are added etc they will not be reflected in this until somebody updates them,  or tells me about them.



In order not to waste paper,  I simply deleted all of the folders from the talent community apps folder  that had applications I knew I would never use.

Also for readability,  I  skipped identifying which OS the commands were for on the basis that  I'd be able to work it out anyway.
I do use mac windows and Linux for my operations but I rarely touch anything other than Linux so I can't say for sure that  this logic is sound.

I hope you find this useful and I love talon!!



Suggested Future features:

Add a way to print a  cheat sheet from a single user context to cater for new user repositories and applications.
It might just be easier to generate individual HTML files per context so that no configuration is required  by users who don't know how to use PHP.
Alternatively you can just choose to print the page you want in the browser when you're printing there's only one thing  that has changed.

The advantage of printing one file per context,  is that when the contexts are updated upstream with things like say for instance the Community repo,
 you will be able to see the diff of those and know which ones need reprinting.

Someday I will probably implement this but don't hold your breath :-)

Feel free to contribute to this repo.  I will be happy to accept pull requests.

/Paul
