---
tag: 6G5GATCE78
kind: example
name: An empirical proof scheme for the sum of two odd numbers
msc: ["97E50", "97C30"]
topics: [VHGA6J4NZK]
audience: research
instance_of: [YVNRVXJR68]
uses: [YVNRVXJR68, 5V35SGEN1T]
sources:
  - url: https://doi.org/10.1090/cbmath/007/07
    locator: pages 234-283
---

## Example

A student must decide whether "the sum of two odd integers is even" is true, and must convince a classmate.
The student writes this answer.

> $1 + 3 = 4$, $5 + 7 = 12$, $11 + 13 = 24$, $25 + 49 = 74$.
> All the sums are even, so the claim is true.

We check that the answer shows an inductive empirical [[proof scheme|YVNRVXJR68]] in the sense of Harel and Sowder.

1. Ascertaining: the student became sure of the claim after the four computations, so the source of conviction is the examples.
2. Persuading: the student offers the same four computations to the classmate, so the student expects examples to convince another person.
3. The arithmetic is correct:
   $$1 + 3 = 2 \cdot 2, \quad 5 + 7 = 2 \cdot 6, \quad 11 + 13 = 2 \cdot 12, \quad 25 + 49 = 2 \cdot 37.$$
4. No step refers to a property of all odd numbers.
   The examples are not used to show a general structure, so the answer is not a [[generic proof|SG9XA69J64]].
5. Conviction that rests on particular cases is the defining condition of an inductive empirical scheme, so the answer is an instance of it.

## Remarks

The claim is true, and the student's belief is correct.
What the example shows is a standard of conviction, not a wrong conclusion.
The danger appears with other claims.
The same standard would accept "$n^2 + n + 41$ is prime for every natural number $n$" after the cases $n = 0$ to $5$, and the claim is false at $n = 40$:
$$40^2 + 40 + 41 = 1681 = 41^2.$$

One sentence would change the picture.
If the student wrote "$7$ is three pairs and one, $9$ is four pairs and one, and the two ones make a pair", the example $7 + 9$ would carry a structure that every odd sum shares.
That answer moves from the empirical scheme toward a generic argument, and the [[transformational example|GA27MSTQQD]] completes the move with letters.

## Explanations

### L1 human

The student tries a few pairs of odd numbers and sees that each sum is even.
The student then believes that this always happens.
That is how many people become sure of a pattern.
Here the belief is right, but the reason is weak, because a pattern can hold for the first numbers and fail later.

### L2 human

A teacher who wants to identify the scheme asks three questions.
What convinced you?
The student answers "it worked every time".
What would change your mind?
The student answers "an odd sum", which is a search for a counterexample among more cases.
Would a reason that works for all odd numbers add anything?
A student with an empirical scheme often says no, and that answer, more than the written text, marks the scheme.
Watch out: the claim is true, so judging the scheme by the conclusion would miss the point.
