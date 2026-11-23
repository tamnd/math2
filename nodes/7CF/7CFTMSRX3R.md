---
tag: 7CFTMSRX3R
kind: example
name: The language of a proof that the square of an odd integer is odd
msc: ["00A35", "11A05"]
topics: [STSM6PR7TX]
audience: ug1
instance_of: [GKMRQCA8CW]
uses: [GKMRQCA8CW, 0NTF6DMVAP]
sources:
  - url: https://en.wikipedia.org/wiki/Glossary_of_mathematical_jargon
    locator: Proof terminology
  - book: isbn:9781108439534
    locator: Chapter 3
---

## Example

The statement is that for every integer $n$, if $n$ is odd, then $n^2$ is odd.
An integer $n$ is odd when $n = 2k + 1$ for some integer $k$.
Here is a short [[direct proof|0NTF6DMVAP]] with its lines numbered, so that we can read its [[proof words|GKMRQCA8CW]] one at a time.

> (1) Let $n$ be an integer.
> (2) Suppose that $n$ is odd.
> (3) By the definition of an odd integer, there is an integer $k$ with $n = 2k + 1$.
> (4) Then $n^2 = (2k + 1)^2 = 4k^2 + 4k + 1 = 2(2k^2 + 2k) + 1$.
> (5) Put $m = 2k^2 + 2k$.
> (6) Since $k$ is an integer, $m$ is an integer, and $n^2 = 2m + 1$.
> (7) Hence $n^2$ is odd, by the definition of an odd integer.
> $\square$

"Let" in line (1) brings in an arbitrary integer with no other property, so the conclusion holds for all integers.
"Suppose" in line (2) opens the hypothesis of the conditional, and the proof must close it with "$n^2$ is odd".
"There is" in line (3) brings in a new integer $k$, and its reason is the definition applied to line (2).
"Then" in line (4) marks a calculation that rests on expanding the square and taking out a factor $2$.
"Put" in line (5) names a known number, so it needs no reason.
"Since" in line (6) gives the reason first: sums and products of integers are integers.
"Hence" in line (7) draws the conclusion and closes the assumption of line (2).

## Remarks

Lines (3) and (7) both mention the definition of "odd", but they do opposite things.
Line (3) uses the definition on a given fact, and line (7) proves that a new number satisfies it.
Only the words "there is" and "hence" tell the two apart.

The same words appear in almost every direct proof of a conditional: "let", "suppose", a chain of "then", and a final "hence".
If the statement is changed to "if $n$ is even, then $n^2$ is even", the same frame works with $n = 2k$ and $n^2 = 2(2k^2)$.

Suppose line (3) said "let $n = 2k + 1$" instead.
That sentence would define $n$ again and cut the link with the arbitrary $n$ of line (1).
The words "there is" keep the link, because they say that $k$ comes from the given $n$.

## Explanations

### L1 human

The proof shows that the square of any odd number is odd.
For example, $7$ is odd, and $7^2 = 49 = 2 \cdot 24 + 1$ is odd.
The proof uses small words to show what each line does.
"Let" brings in a number, "suppose" says what we assume about it, and "hence" says what we have found.
A reader who knows these words can follow the proof line by line.

### L2 human

We test each line on the number $n = 7$.
Lines (1) and (2) hold, since $7$ is an odd integer.
Line (3) gives $k = 3$, because $7 = 2 \cdot 3 + 1$.
Line (4) gives $49 = 36 + 12 + 1 = 2(18 + 6) + 1$.
Lines (5) and (6) give $m = 24$ and $49 = 2 \cdot 24 + 1$, so line (7) says that $49$ is odd.

Reading a proof with one concrete value gives each proof word a visible meaning.
Watch out: the test with $n = 7$ checks the lines for one case only, and it does not prove the statement.
The proof is general because line (1) says "let $n$ be an integer", not "let $n = 7$".
