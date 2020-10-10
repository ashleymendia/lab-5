## CS-UY 1114 — Lab 4
# Strings, Strings, Strings!
#### October 8th & 9th, 2020

**All lab work must be submitted within 24 hours of the start of your lab period on Gradescope** (we will be checking
this using the timestamps of your last submission on GradeScope). This, of course, also means that if you submit a
solution before your allotted lab time, you will get no credit. You must try each problem at least once (that is,
submitting at least one attempt to GradeScope, whether it is correct or not). You are welcome to continue to work on the
problems and continue submitting to Gradescope until you are satisfied with your results. It is your responsibility to
remember to submit your work.

Please note that your overall point value is awarded by the teaching assistants verifying that you attempted and
submitted each problem at least once! For every hour that your work is late on GradeScope, we will deduct 0.5 points
from the total 10-point value of the lab.

Please do not hesitate to check with your TAs if you are ever confused as to how to proceed! Strings are super important
and will come up again and again throughout the semester!

---

### Introducing: The Auto-Grader

From this lab forward, we will be leveraging GradeScope's auto-grader to help you check your work. Essentially, every
time you submit your work onto GradeScope, it will run all your functions through a few test cases that we have written
and let you know if it passed them or not. Remember, **labs are graded on completeness, not on correctness**, so don't
worry if your code doesn't pass all of the tests (you will still only be graded on whether you tried each problem or
not, in other words). This is just to help you check how well you are following the problem's directions. **THE LABS WILL STILL BE GRADED OUT OF 10, COMPLETELY BASED ON COMPLETENESS. THE POINTS THE AUTO-GRADER ON GRADESCOPE GIVES YOU WILL NOT BE COUNTED TOWARDS YOUR GRADE!**

For the auto-grader to work, **both your files and functions must be named the exact same way as they are written on
this `README`,** so don't change any function or file names!

### Problem 1: Student Information Generator

You already know how we start: simply. Your first task is to create a function, called
**`student_information_generator`**, that accepts two strings, **`full_name`** and **`major`**, and returns a nicely
formatted string as follows:

```python
def main():
    student_name = "Redding, Otis"
    student_major = "Computer Science"
    student_info = student_information_generator(student_name, student_major)

    print(student_info)

main()
```
Running this program should print _**exactly**_ the following on your console:
```text
Otis Redding is studying computer science.
```

A couple of things to note:

- The string **`full_name`** should always be in the format of `last_name, first_name`. If **`full_name`** does not
include a comma (**`,`**), you can assume the whole name is invalid and should instead have `[INVALID NAME]` as the
student's name. You may assume that there always is a space after a comma.
- The string **`major`** may **not** include any numeric values. If any are present, your program should include
`[INVALID MAJOR]` in its returned string instead of the major. The major must also be in all lowercase in the final
string that you are returning.

This function must be included in the file **[StudentInformationGenerator.py](StudentInformationGenerator.py)**.

### Problem 2: Song Information Generator

In a similar fashion to problem 1, imagine now that you are interning for your favorite streaming service, and your
first task is to convert a series of variables into a nicely formatted string. So write a function
**`create_song_string`** inside the file [**CreateSongString.py**](CreateSongString.py) that will take in the following
arguments:
- A song's title (can be any valid Python string)
- The song's artist (should always be in the format of `last_name, first_name`. If this string does not
include a comma (**`,`**), you can assume the whole name is invalid and should instead have `[INVALID NAME]` as the
artist's name. You may assume that there always is a space after a comma.)
- The song's album (can be any valid Python string)
- The song's BPM (must be a positive, non-zero integer, otherwise you may assume the BPM is `[INVALID BPM]`)
- The song's length, in seconds (must be a positive, non-zero float, otherwise you may assume the length is
`[INVALID LENGTH]`)

Using all these parameters, we want the following behavior:

```python
def main():
    title = "Groovy!"
    artist = "Hirose, Koumi"
    album = "Cardcaptor Sakura OST"
    bpm = 123
    length_in_seconds = 267.0

    formatted_song_string = create_song_string(title, artist, album, bpm, length_in_seconds)
    print(formatted_song_string)

main()
```

Which would print the following on your console:

```text
'Groovy!' by Koumi Hirose
From the album 'Cardcaptor Sakura OST'
BPM: 123, Length: 4:27
```

**HINT**: You may want to consider using the string method **`format`** to make your life easier. If you haven't seen
this method in lecture, it basically works like this:

When we're constructing a string from various parts (each which may be of different types), we're basically limited
to something like string concatenation, right?

```python
day = 15
month = "March"
year = 1993
isBirthDate = True

message = "This person was born on " + month + " " + str(day) + ", " + str(year) + ". Right? " + str(isBirthDate) + "."
# This is equivalent to "This person was born on March 15, 1993. Right? True."
```

Basically, anything that _isn't_ a string has to be _explicitly casted_ (or converted) to a string type in order to
be combined with other strings. This way works just fine, and some people even prefer it, but when working with very
long strings that have parts of lots of types involved, it's often easier to use Python's native `format` method.
Here's a basic example of how it works. While it's certainly not an exhaustive example, it should be enough to help
you in this problem:

```python
day = 15
month = "March"
year = 1993
isBirthDate = True

message = "This person was born on {} {}, {}. Right? {}.".format(month, day, year, isBirthDate)
# This is equivalent to "This person was born on March 15, 1993. Right? True."
```

This (at least to a lot of people) is much neater than the earlier version. You didn't have to cast any of the
non-string parameters into strings, for instance. Notice that the order of the arguments inside the parentheses
matters!

You can find detailed
documentation on `format` [**here**](https://pyformat.info/#simple) and
[**here**](https://docs.python.org/3/library/string.html#string.Formatter.format).

### Problem 3: Decoding A Message

Let's say you wanted to decode a message that used the following encryption: Starting from the last character of the
sentence, you must read every X-th letter. If the character that you land on is a number, you must skip it. For
instance:

```python
def main():
    encrypted_message = "!thnsdosdhdft7g68yyrop"
    key = 2
    decrypted_message = decode_by_skip(encrypted_message, key)

    print(decrypted_message)

main()
```

Which yields:

```text
python!
```

Above, we start at the last character, **`p`**, skip 2 (as denoted by the decryption key), and ignore the one numeric
character we landed on (**`6`**):

```text
!thnsdosdhdft7g68yyrop

! [th] n [sd] o [sd] h [df] t [7g 6 8y] y [ro] p

! n o h t y p

!nohtyp

python!
```

Do this in the function **`decode_by_skip`** (file: **[DecodeBySkip.py](DecodeBySkip.py)**), which accepts a string
argument **`encoded_message`** and the decryption "key", **`key`**, an integer. You may assume that both arguments will
always be valid ones. You may **not** use the **`reverse`** string method; you will **NOT** get credit for this problem if you use it.

### Problem 4: Password Checker

Write a function, **`password_checker`**, that checks whether the string parameter argument **`password`** is valid.
The rules for password validity are as follows:
1. Must include at least 8 characters.
2. Must include at least 2 lowercase letters.
3. Must include at least 2 uppercase letters.
4. Must include at least 1 number.
5. Must include at least 1  of the following non-alphanumeric characters: `!`, `@`, `#`, or `$`.

If the user's password is valid, your function will return **`True`**. Otherwise, it will return **`False`**. You can
find the starter code in the file **[PasswordChecker.py](PasswordChecker.py)**.

```python
def main():
    password = "this1IsAValidPassword!!"
    print(password_checker(password))

main()
```
Which displays the following in your console:
```text
True
```

### Problem 5: DNA Sequencing

Given two DNA sequences in the form of strings, write a function, **`get_fused_sequence_complement`**, that will:

1. Fuse the two sequences by adding a nucleotide from each in alternating order (i.e. `ACT` + `CA` = `ACCAT`). If any
invalid nucleotides (i.e., not A, C, T, or G) are found in either sequence, you should ignore them and not include them
in the fused sequence.
2. Create a complement sequence from the new, fused sequence. (i.e `ACCAT` complements to `TGGTA`)
3. Return that complement sequence.

Recall the DNA complements:

| **Nucleotide** | **Complement** |
|----------------|----------------|
| A              | T              |
| C              | G              |
| T              | A              |
| G              | C              |

_**Figure 1**: [Nucleotide Complements](https://en.wikipedia.org/wiki/Complementarity_(molecular_biology)#DNA_and_RNA_base_pair_complementarity)._

Here's another example to make it clearer:

```python
def main():
    sequence_a = "ACTGGGTA"
    sequence_b = "TTZAG"
    fused_sequence_complement = get_fused_sequence_complement(sequence_a, sequence_b)
    print(fused_sequence_complement)

main()
```

Which will print the following onto your console:

```text
TAGAACTCCCAT
```

You may assume that both DNA sequences will always be valid Python strings, and not and `int`, `float`, etc. You may
also find it useful to break this problem up into smaller functions (for instance, a function takes a single nucleotide
and returns its complement could be useful.) The starter code can be found in the file
**[GetFusedSequenceComplement.py](GetFusedSequenceComplement.py)**

### Problem 6: Goats Dream in Latin, Apparently

_**NOTE**: You may **NOT** use the string method `split` for this problem, as it creates a list, which we have not yet
covered in class; you will **NOT** get credit for this problem if you use it._

Write a function that accepts a single string, composed of words separated by spaces. Each word consists of lowercase
and uppercase letters only.

We would like to convert the sentence to "Goat Latin" (a made-up language similar to Pig Latin.)

The rules of Goat Latin are as follows:

- If a word begins with a vowel (`a`, `e`, `i`, `o`, or `u`), append `ma` to the end of the word.
For example, the word `apple` becomes `applema`.

- If a word begins with a consonant (i.e. not a vowel), remove the first letter and append it to the end, then add `ma`.
For example, the word `goat` becomes `oatgma`.

- Add one letter `a` to the end of each word per its word index in the sentence, starting with 1.
For example, the first word gets `a` added to the end, the second word gets `aa` added to the end and so on:

```python
def main():
    original_sentence = "I speak Goat Latin"
    goat_latin_translation = translate_sentence_to_goat_latin(original_sentence)
    print(goat_latin_translation)
```
Which results in:
```text
Imaa peaksmaaa oatGmaaaa atinLmaaaaa
```

Return the final sentence representing the conversion to Goat Latin. The function should be called
**`translate_sentence_to_goat_latin`**, inside the file **[TranslateToGoatLatin.py](TranslateToGoatLatin.py)**. You may
assume the original sentence will contain at least two words.

**HINT**: You may want to consider the use of the string method **`find`**. You may have learned in lecture that `find`
returns the index of a specified character in a string, or -1 if it doesn't exist:

```python
def main():
    some_string = "Bohemia has neither coasts nor a desert. Nice try, Shakespeare."
    period_index = some_string.find(".")
    exclamation_index = some_string.find("!")

    print(period_index)
    print(exclamation_index)

main()
```

This will display the following in your console:

```text
39
-1
```

That is, the index of the _first_ period (`.`) in the string `some_string` is 39, while the character `!` never shows
up.

However, we can add extra arguments to the `find` function that will make our search more specific. The format is:
`find(character_we_are_searching, starting_point, ending_point)`.

For instance:

```python
def main():
    some_string = "Bohemia has neither coasts nor a desert. Nice try, Shakespeare. You almost had me."
    period_index = some_string.find(".")

    # If we wanted to find the location of any periods AFTER the first period...
    second_period_index = some_string.find(".", period_index + 1)  # we add a 1 because it is non-inclusive

    # If we wanted to find the location of the first 's' in the second sentence...
    s_second_sentence_index = some_string.find("s", period_index + 1, second_period_index)

    print(second_period_index)
    print(s_second_sentence_index)

main()
```

Which will display the following on your console:
```text
62
56
```

We basically separated our original `some_string` by periods, `.`. So, keeping this in mind, by which character would
you separate each word in your sentence?

You can find more detailed documentation of the
`find` function [**here**](https://www.w3schools.com/python/ref_string_find.asp) and
[**here**](https://docs.python.org/2/library/string.html#string.find).
