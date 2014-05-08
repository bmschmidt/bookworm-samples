bookworm-samples
================

Extension to Bookworm that splits it up into a bunch of (roughly) equal-sized chunks for testing.


Purpose
=======


This is an easy drop in to a Bookworm to get some sense whether effects are driven by random sample noise or by real factors.

Install it according to the [instructions for Bookworm Extensions](http://bmschmidt.github.io/Presidio/Extensions.html) in the extensions folder; switch into the folder, and run `make`

You'll now have two new variables in your metadata; `randomA` and `randomB`. By default, randomA has 5 levels and randomB has 24. This means that you can:

1. Split any query up by the random variables to see if (for instance) five separate random samples of Canadian writers differ from five separate random samples of American writers*
2. Pull a random subset of data in really processor intensive queries (like getting wordcounts). You can compare a 20% sample of American writers to a 20% sample of Canadian writers, say.


*Although nb: most error won't come from this sort of random variation.

Why two random variables?
--------------------------

There are two random variables so you can interact with each other. That's why one is five, and the other two is 24 (so the multiple of a bunch of threes and twos). It should be possible to create most reasonable samples you might want.

To get a 10% sample, for example, you could put in `"search_limits":{"randomA":[1],"randomB":{"$lte":12}`; all of the first set, and half of the second set.

To get one in twelve, put in "search_limits":{"randomB":[1,2]}.

And so forth.