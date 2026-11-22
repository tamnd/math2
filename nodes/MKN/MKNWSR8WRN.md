---
tag: MKNWSR8WRN
kind: example
name: If n^2 is even, then n is even
msc: ["00A35", "11A05"]
topics: [958EF46EYJ]
audience: school
instance_of: [0BB5TPGQ1N]
uses: [0BB5TPGQ1N, E330HD4J2D]
sources:
  - url: https://en.wikipedia.org/wiki/Contraposition
    locator: lead section
  - book: isbn:9781108439534
    locator: Section 3.2
---

## Example

Statement: for every integer $n$, if $n^2$ is even, then $n$ is even.
We give a [[proof by contrapositive|0BB5TPGQ1N]].

1. The contrapositive is: for every integer $n$, if $n$ is not even, then $n^2$ is not even.
2. Division by $2$ leaves remainder $0$ or $1$, so every integer is either even or odd, and not both.
   So "not even" means "odd" for integers.
3. The contrapositive therefore reads: if $n$ is odd, then $n^2$ is odd.
4. Let $n$ be odd, so $n = 2k + 1$ for an integer $k$.
5. Square:
   $$n^2 = 4k^2 + 4k + 1 = 2(2k^2 + 2k) + 1,$$
   and $2k^2 + 2k$ is an integer, so $n^2$ is odd.
   This is the [[direct proof that the square of an odd integer is odd|E330HD4J2D]].
6. Step 5 proves the contrapositive, and the contrapositive is equivalent to the statement, so the statement is proved.

Check: $n = 7$ is odd and $49$ is odd; $n = 6$ is even and $36$ is even.

## Remarks

Why not prove it directly?
A direct proof would start from $n^2 = 2m$ and would need a formula for $n$.
The candidate $n = \sqrt{2m}$ is not visibly an integer, and it says nothing about parity.
The contrapositive avoids the problem, because "$n$ is odd" gives the formula $n = 2k + 1$ to compute with.

The same statement holds with any prime $p$ in place of $2$, but the proof needs more than parity.
For $p = 3$, the contrapositive of "if $3 \mid n^2$, then $3 \mid n$" is "if $3 \nmid n$, then $3 \nmid n^2$".
"Not divisible by $3$" splits into $n = 3k + 1$ and $n = 3k + 2$, with squares $3(3k^2 + 2k) + 1$ and $3(3k^2 + 4k + 1) + 1$, so the proof becomes a [[proof by cases|0WCP0PVET6]].
For a general prime the standard proof uses [[Euclid's lemma|051VYKA1EX]].

The statement is the main lemma in the proof that $\sqrt{2}$ is [[irrational|0DZGSDHD92]].

## Explanations

### L1 human

We want to show: if a whole number times itself is even, then the number is even.
It is easier to look from the other side: if a number is odd, then its square is odd.
For example, $7 \times 7 = 49$ is odd, and $9 \times 9 = 81$ is odd.
The algebra shows that this happens for every odd number.
So an even square can never come from an odd number, and the number must be even.

### L2 human

Here is how the lemma is used.
Together with the direct fact that $n = 2k$ gives $n^2 = 2(2k^2)$, it shows that for every integer $n$, $n^2$ is even if and only if $n$ is even.
Now suppose $a^2 = 2b^2$ for integers $a$ and $b$.
Then $a^2$ is even, so $a$ is even by the lemma, and $a = 2c$ for an integer $c$.
Substituting gives
$$4c^2 = 2b^2, \qquad b^2 = 2c^2,$$
so $b$ is even as well.
This is the heart of the proof that $\sqrt{2}$ is irrational: a fact about a square tells you a fact about the number itself.
Watch out: the step "not even means odd" uses a fact about integers, and "if $x^2$ is an even integer, then $x$ is an even integer" is false for the real number $x = \sqrt{2}$.
