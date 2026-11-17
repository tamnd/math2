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

*Statement.* For every integer $n$, if $n$ is odd, then $n^2$ is odd.
An integer $n$ is odd when $n = 2k + 1$ for some integer $k$.

*Proof.*

1. Let $n$ be an integer.
2. Suppose that $n$ is odd.
3. By the definition of an odd integer, there is an integer $k$ with $n = 2k + 1$.
4. Then $n^2 = (2k + 1)^2 = 4k^2 + 4k + 1 = 2(2k^2 + 2k) + 1$.
5. Put $m = 2k^2 + 2k$.
6. Since $k$ is an integer, $m$ is an integer, and $n^2 = 2m + 1$.
7. Hence $n^2$ is odd, by the definition of an odd integer. $\square$

We check the role of each proof word, line by line.

1. "Let" introduces an arbitrary integer $n$. Because $n$ has no other property, the conclusion holds for all integers. This matches the "for every" of the statement.
2. "Suppose" opens the hypothesis "$n$ is odd" of the conditional. The proof must close it with the conclusion "$n^2$ is odd".
3. "There is" introduces a new integer $k$. The reason for its existence is the definition of an odd integer, applied to the assumption of line 2.
4. "Then" marks a calculation. The equalities hold by the expansion $(2k+1)^2 = 4k^2 + 4k + 1$ and by taking out the factor $2$.
5. "Put" defines a symbol $m$ for a known number. Nothing is assumed, so this line needs no reason.
6. "Since" gives the reason first: integers are closed under multiplication and addition. The rest of the line restates line 4 with the new name.
7. "Hence" draws the conclusion from line 6 and the definition. It closes the assumption of line 2, so the proof has shown the conditional for the arbitrary $n$ of line 1.

## Remarks

1. The example shows that the proof words fix the logical role of each line. Without them, lines 3 and 7 would look alike, although line 3 uses the definition of "odd" and line 7 proves it.
2. The proof is a [[direct proof|0NTF6DMVAP]] of a conditional. The same words appear in every direct proof: "let", "suppose", a chain of "then", and a final "hence".
3. If the statement changes to "if $n$ is even, then $n^2$ is even", the same words work with $n = 2k$ and $n^2 = 2(2k^2)$.
4. If line 3 said "let $n = 2k + 1$", the line would define $n$ again, and it would lose the link to the arbitrary $n$ of line 1. The words "there is" keep the link.

## Explanations

### L1 human

The proof shows that the square of any odd number is odd.
For example, $7$ is odd, and $7^2 = 49 = 2 \cdot 24 + 1$ is odd.
The proof uses words to show what each line does.
"Let" brings in a number, "suppose" says what we assume about it, and "hence" says what we have found.
A reader who knows these words can follow the proof line by line.

### L2 human

We test each line on the number $n = 7$.

1. Line 1 and line 2: $n = 7$ is an integer, and it is odd.
2. Line 3: $k = 3$, because $7 = 2 \cdot 3 + 1$.
3. Line 4: $49 = 4 \cdot 9 + 4 \cdot 3 + 1 = 36 + 12 + 1$, and $36 + 12 + 1 = 2(18 + 6) + 1$.
4. Line 5 and line 6: $m = 2 \cdot 9 + 2 \cdot 3 = 24$, and $49 = 2 \cdot 24 + 1$.
5. Line 7: $49$ is odd.

The typical use of this check is to read a proof with one concrete value, so that each proof word has a visible meaning.
A trap is to think that the test with $n = 7$ proves the statement.
It only checks the lines for one case, and the proof is general because line 1 says "let $n$ be an integer", not "let $n = 7$".
