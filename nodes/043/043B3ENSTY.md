---
tag: 043B3ENSTY
kind: statement
role: theorem
name: Fermat's theorem on sums of two squares
aliases: [fermat-christmas-theorem]
msc: ["11E25"]
uses: [0SN0MAEKYX, 00DW862T78]
sources:
  - url: https://en.wikipedia.org/wiki/Fermat%27s_theorem_on_sums_of_two_squares
    locator: History
  - url: https://en.wikipedia.org/wiki/Fermat%27s_theorem_on_sums_of_two_squares
    locator: Euler's proof by infinite descent
same_as:
  wikidata: Q914517
  wikipedia: Fermat's theorem on sums of two squares
---

## Statement

Let $p$ be an odd [[prime number|0SN0MAEKYX]].
Then there are integers $x$ and $y$ with $p = x^2 + y^2$ if and only if $p \equiv 1 \pmod 4$.

## Remarks

The prime $2 = 1^2 + 1^2$ is also a sum of two squares. So a prime $p$ is a sum of two squares if and only if $p \not\equiv 3 \pmod 4$.
For example, $5 = 1 + 4$, $13 = 4 + 9$ and $29 = 4 + 25$. For $p \equiv 1 \pmod 4$, the representation is unique up to order and signs.
The "only if" part is easy: a square is $0$ or $1$ modulo $4$, so $x^2 + y^2 \not\equiv 3 \pmod 4$.
One proof of the other part starts from a [[square root of $-1$ modulo $p$|00DW862T78]] and uses [[Gaussian integers|0B268GVX95]] or [[Minkowski's theorem|0K387S2PKQ]].

## History

Albert Girard stated the result in a book published in 1625.
Fermat stated it in a letter to Mersenne of 25 December 1640, so it is also called Fermat's Christmas theorem.
Euler gave the first proof, by infinite descent, in 1749.

## Explanations

### L1 human

The primes $5, 13, 17, 29$ leave remainder $1$ on division by $4$, and each of them is a sum of two squares.
The primes $3, 7, 11, 19$ leave remainder $3$, and none of them is a sum of two squares.
