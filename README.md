# What's a de Bruijn sequence ?
A de Bruijn sequence is a cyclic sequence of elements from a given alphabet (e.g., binary digits, letters) where every possible subsequence of a certain length occurs exactly once.
For example, the binary sequence "00011101" is a de Bruijn sequence of order 3 because it contains all possible binary sequences of length 3 (000, 001, 010, 011, 100, 101, 110, 111) exactly once.
NB : For those who do not see the '100' case it's beacause when you are emitting a signal, especially in ook encoding, not emiting represents a logical 0 so the last 1 of the sequence represents the start of the '100' case.

This algorythm will help you understand and generate de Bruijn sequences with the wanted alphabet and the lengh you want.

This algorithm is for experimental purposes only and is not meant for any illegal activity/purposes.
