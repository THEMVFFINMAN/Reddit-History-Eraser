# Reddit-History-Eraser

Using Praw and Python this will erase up to 100 billion posts and comments in
one run through. Or however many comments or posts the user has. The user can
also specify how many comments and/or posts they would like deleted.
Additionally the user can keep his more recent history by specifying how many
days to keep.

This script relies on only one library, Praw:
https://praw.readthedocs.org/en/v2.1.21/ the Python Reddit Api Wrapper. My
recommended way of installing any python library is through pip. 

On most Linux machines, you open up a terminal and can just run "sudo apt-get
install pip" and then "pip install praw" and then you're all set up. 

On Mac, you open a terminal and type "sudo easy_install pip" and then "pip
install praw" and then you're all set up. I recommend pip to easy_install mainly
due to easy_install now not being updated and relatively deprecated. 

Windows is a little more tricky but not too tricky. Basically you will download
the easy setup pip script from here: https://bootstrap.pypa.io/get-pip.py. Once
downloaded you will find the file in command line and run "python get-pip.py"
after which it should install pip. Now while you're still in the command line
type "pip install praw" and it should install it.

To finalize setup, you need to generate the configuration file to be use by
running "python createtoken.py". Follow its instructions. This will generate a
configuration file named "RedEraser-Token" that must be in the same directory as
RedEraser.py when you run it. It contains the script's id, secret key, and
refresh token. Be sure to add any subreddits you want to exclude from being
erased as well as how many days you want to keep in the top of RedEraser.py.

Now whenever you want to run the script, simply open up a terminal, go into the
directory it's in, and type "python RedEraser.py" or whatever you called the
file. It should give you some output. 

This was written in python 3.

This is still a working progress so any pulls, pushes, commits, or any other
interested contributors are more than welcome to contribute. 
