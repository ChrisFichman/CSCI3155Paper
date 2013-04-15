
Introduction
============

This should be a fun assignment.

Take your group project and distill it down to something to present to the class. You can combine your papers into one talk, or select just one. It's up to you. Just make it fit into the five minute slot.

With that in mind, uou have the following requirements:

* 20 unique slides, spaced *exactly* 15 seconds apart, for a total of 5 minutes.
* This is a class on programming languages, so show and talk about code! You want to find a good balance between describing a concept abstractly and demonstrating specific code usage in the language you're writing about in your paper.
* Slides must be written in Markdown, however, they can embed other media or use embedded Latex, much like the lecture notes do.
* Presentation is a PDF file generated via Beamer and pandoc; see the below section.

This style we are requiring for this presentation is actually closest to the Ignite format, vs a typical conference lightning talk. I recommend this [blog post][presenting-for-ignite] as a good start: it walks you through the process of going from a storyboard to a finished product. You may also find that a short presentation can sometimes require more work than a longer presentation: that's the essence of getting your content distilled down.


Grading rubric
==============

* 70% content of the talk itself
* 20% from the evidence in GitHub around your slide preparation
* 10% constructive peer assessments on worksheets we will distribute during class on *other* talks

Lastly:

* Be creative.
* Remember to have fun!


Presentation times
==================

The instructors will generate a presentation schedule using a undisclosed algorithm ;) such that groups will present in class on either April 25 or April 30. If you cannot make your time slot, at prior request and instructor permission, we can show a video that you have made following the same standard format.


Extra credit opportunities
==========================

Some possibilities for extra credit:

* Modify generation mechanism such that generated PDFs will autoplay on a 15 second interval. This likely requires modifying the provided beamer template and/or generate script.

* Modifications to the generate script and/or templates that can better support creative usage. 


Generating your presentation
============================

Included in this directory is `generate`, a simple script that wraps pandoc with some standard options. To build a presentation PDF:

    $ ./generate presentation.md
	
You will need to install the dependencies for pandoc. For Ubuntu, these are:

    sudo apt-get install pandoc
	sudo apt-get install latex-beamer



[presenting-for-ignite]: http://www.speakingaboutpresenting.com/content/fast-ignite-presentation/
