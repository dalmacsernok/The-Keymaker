# The Keymaker

## Story

Thousands of human refugees are living outside the Matrix, hiding from
Sentinels and the Agents of the machines. Keeping their systems safe and
intact from the powerful enemy is an enormous task. They cannot trust
any known algorithm for storing sensitive information such as names, access
codes, and passwords, because the machines with their superior computing
capacity would break the algorithms easily.

The access codes to the mainframe computers of the city of Zion are
stored as hashed values, with a secretly kept, custom hashing algorithm
created by a legendary figure known as the _Keymaker_. Even the user names
are stored in a hashed form. Your job is to implement the string
hashing algorithm described in the requirements.

The output of the hash function is always a 6 character long string.
During the transformations you have to use these numeric values for the
base lowercase English characters: `0` for `a`, `1` for `b`, `2` for
`c`, and so on until `25` for `z`.

**!!! WARNING !!!**
Never use custom hash algorithms in any real situation!
That is, never, ever after this project
**!!! DON'T TRY THIS AT HOME !!!**

## What are you going to learn?

- Practice string operations.
- Improve your algorithmic skills.

## Tasks

1. Implement `shift_characters(word, shift)` which returns the characters of the word, all shifted by `shift`. _Shifting a character_ means adding a number to the original character value. If the resulting character steps out of the `a-z` region, the count is continued from the other end. For example, shifting `'a'` by `5` yields `'f'`, shifting `'y'` by `5` yields `'d'`, shifting `'a'` by `-3` yields `'x'`. The function returns these shifted characters concatenated. Example: `shift_characters('abby', 5)` returns `'fggd'`. Example: `shift_characters('a', 27)` returns `'b'`. Example: `shift_characters('azcmx', 2)` returns `'cbeoz'`.
    - The length of the returned string is the same as length of `word`.
    - The returned string contains the shifted characters of `word`.
    - Shifting works for any integer value. Shifting by `n + 26` yields the same result as shifting by `n`.

2. Implement function `pad_up_to(word, shift, n)` which returns a string of `n` characters, starting with the lowercase version of `word`, continued by its shifted variants, as described above. A variant is the shifted version of the one before. Example: `pad_up_to('abb', 5, 11)` returns `'abbfggkllpq'` because the first couple of `5`-shifted variants of `'abb'` are `'fgg'`, `'kll'`, and `'pqq'`, and the first `11` characters of this series are returned. Example: `pad_up_to('aaa', 2, 100)` should return `"aaaccceeegggiiikkkmmmoooqqqsssuuuwwwyyyaaaccceeegggiiikkkmmmoooqqqsssuuuwwwyyyaaaccceeegggiiikkkmmmo"`.
    - The length of the returned string is `n`.
    - The returned string starts with the original `word` (or its first `n` characters when it is longer than `n`).
    - The returned string continues with the shifted variant of `word` (shifted by `shift`), and then further shifts until it reaches the length `n`.

3. Implement function `abc_mirror(word)` which returns a string where each character (all lowercase) is "mirrored" to the other side of 'abc'. A character is the mirror of another when its value distance from 'z' is the same as the value distance of the other character from 'a'. Examples for mirrored pairs: `'a' <-> 'z'`, `'b' <-> 'y'`, `'l' <->'o'`, `'m' <->'n'`, so for example `abc_mirror('abcd')` returns `'zyxw'`, and`abc_mirror('morpheus')` returns `'nliksvfh'`. Example: `abc_mirror('azbn')` returns `"zaym"`.
    - The length of the returned string is the same as the length of the input.
    - The returned string is character-by-character the mirrored version of the input.

4. Implement function `create_matrix(word1, word2)` which returns a list of strings where the nth row is `word1` shifted by the value of the nth character of `word2`. Example: `create_matrix('mamas', 'papas')` returns `['bpbph', 'mamas', 'bpbph', 'mamas', 'esesk']` (`'bpbph'` is `'mamas`' shifted by 15, the character value of `'p'`). Example: `create_matrix("az", "abz")` returns `['az', 'ba', 'zy']`.
    - The return value is a list of strings. The length of the strings is the length of `word1`, the length of the list is the length of `word2`.
    - Each row of the list is the shifted variant of `word1`, shifted by the corresponding character value of `word2`.

5. Implement function `zig_zag_concatenate(list_of_words)` which returns a single string
containing all the characters of the "matrix" in the following way.
```
   0  1  2
0  V  /--\
1  |  |  |
2  |  |  |
3  \--/  V
```
Start with the first "column" (that is, the first letters of the words) from the top,
then concatenate the letters of the second column from bottom to top, then turn again
and concatenate the third column starting from the top, and so on. For example,
for an input of `['abc', 'def', 'ghi', 'jkl']` it returns `'adgjkhebcfil'`.
The incoming list of strings are always of the same length.
Example: `zig_zag_concatenate(['aaa', 'bbb', 'ccc', 'ddd'])` returns `abcddcbaabcd`.
    - The returned string contains all the characters of the input once.
    - The characters are concatenated following the zig-zag direction described above.

6. Implement function `rotate_right(word, n)` which returns a string of the same length as `word`, only the characters are rotated by `n` positions rightwards. The character "falling out" on the right side come back from the left side. Example: `rotate_right('abcdefgh', 1)` returns `'habcdefg'`, `rotate_right('abcdefgh', 3)` returns `'fghabcde'`, `rotate_right('abcdefgh', 8)` returns `'abcdefgh'`. Rotating by the length of the string yields the input string unchanged. The value of `n` can be any integer. Example: `rotate_right('abcd', 1)` returns `dabc`. Example: `rotate_right('abcd', 4)` returns `abcd`. Example: `rotate_right('abcd', 100)` returns `abcd`. Example: `rotate_right('abcd', 5)` returns `dabc`. Example: `rotate_right('keymaker', -4)` returns `akerkeym`.
    - The returned string is the same length as `word`
    - The characters of `word` are rotated by `n` positions to the right, "falling out" characters appear on the left.
    - The returned value is identical for `n`-values differing by the length of the word. Example: `rotate_right('abcdefgh', 3)` yields the same result for other rotation values such as `n=11`, `n=-5`, and `n=-13` (as the length of the string is `8`).

7. Implement function `get_square_index_chars(word)` which returns all characters of `word` laying at square number indices. Example: `get_square_index_chars('abcdefghijklm')` returns `'abej'` because these letters are picked from positions `[0, 1, 4, 9]`, and the next square number position, `16` is not in the `13`-long input.
    - The returned string's length is the number of square numbers less than the length of `word` (including zero)
    - The characters of the returned string are taken from square number positions of the input.

8. Implement function `remove_odd_blocks(word, block_length)` which breaks the input into blocks of the given length, removes every second block (that is, keeping blocks number `0, 2, 4`, etc.), and returns the remaining blocks concatenated. Example: `remove_odd_blocks('abcdefghijklm', 3)` returns `'abcghim'` because removing every second from the blocks of length `3` (`['abc', 'def', 'ghi', 'jkl', 'm']`) yields to `['abc', 'ghi', 'm']`.
    - The returned string skips characters at positions `[3, 4, 5]`, `[9, 10, 11]`, etc. from the input as described above.

9. Implement function `reduce_to_fixed(word, n)` which cuts the first `n` characters of the input, and performs a left rotation of `n//3` and returns the result read backwards. Example: `reduce_to_fixed('abcdefghijklm', 6)` returns `'bafedc'` because left rotating `'abcdef'` (the first 6 characters) by 2 gives `'cdefab'` which is also reversed.
    - The returned string is `n` characters long.
    - The returned string is the rotated and flipped variant of the first `n` characters of the input.

10. Check your functions by using the prepared `hash_it` function. `hash_it('morpheus')` returns 'trowdo', `hash_it('trinity')` returns 'jotysy'. Check for the hashed name of 'neo' and share the surprise result.
    - The results are the same as the given examples, and Neo's true fate is revealed.

## General requirements

None

## Hints

None


## Background materials

- <i class="far fa-exclamation"></i> [Strings](project/curriculum/materials/competencies/python-basics/python-strings.md.html)

