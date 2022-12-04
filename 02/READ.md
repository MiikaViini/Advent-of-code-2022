# Day 3

For first part i looped through file with "with"
and seems you dont have to initialise that variable
you are reading in to. Found another useful function
called readLine(), which finds first newline and takes
everything before that to variable.

Then i had to use strip() to remove newline from the
end, because my if statement crashed due that. Index got
messed.

Then i had to figure out the point system and found out
when character is upcase, i will use ord() and minus 38
and i got proper answer. Same went with lower case, except
minus 96.
