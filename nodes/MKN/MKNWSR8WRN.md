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
2. Each integer is either even or odd, and not both, by division by $2$ with remainder $0$ or $1$. So "not even" means "odd".
3. The contrapositive therefore reads: if $n$ is odd, then $n^2$ is odd.
4. Let $n$ be odd. Then $n = 2k + 1$ for an integer $k$.
5. So $n^2 = 4k^2 + 4k + 1 = 2(2k^2 + 2k) + 1$, which is odd. This is the [[direct proof that the square of an odd integer is odd|E330HD4J2D]].
6. Step 5 proves the contrapositive. The contrapositive is equivalent to the statement, so the statement is proved.

## Remarks

A direct proof would start from $n^2 = 2m$ and would need a formula for $n$.
The natural candidate $n = \sqrt{2m}$ is not visibly an integer, and it says nothing about parity.
The contrapositive avoids this problem, because "$n$ is odd" gives the formula $n = 2k + 1$.

The same proof works with any prime $p$ in place of $2$, but it needs more than parity.
For $p = 3$, the claim "if $3 \mid n^2$, then $3 \mid n$" has the contrapositive "if $3 \nmid n$, then $3 \nmid n^2$".
Here "not divisible by $3$" splits into the two cases $n = 3k + 1$ and $n = 3k + 2$, so the proof becomes a [[proof by cases|0WCP0PVET6]].
For a general prime $p$ the standard proof uses [[Euclid's lemma|051VYKA1EX]].

The statement is a step in the proof that $\sqrt{2}$ is [[irrational|0DZGSDHD92]].

## Explanations

### L1 human

We want to show: if a whole number times itself is even, then the number itself is even.
It is easier to show the same fact from the other side: if a number is odd, then its square is odd.
For example, $7 \times 7 = 49$ is odd, and $9 \times 9 = 81$ is odd.
The algebra shows that this happens for every odd number.
So an even square can never come from an odd number, and the number must be even.

### L2 human

We use the result to prove that $n^2$ even and $n$ even are equivalent, and then apply it.

1. If $n$ is even, then $n = 2k$ and $n^2 = 2(2k^2)$ is even. This is a direct proof.
2. If $n^2$ is even, then $n$ is even, by the example above.
3. So for every integer $n$, $n^2$ is even if and only if $n$ is even.
4. Application: if $a^2 = 2b^2$ for integers $a$ and $b$, then $a^2$ is even, so $a$ is even by step 2.

The typical use is step 4: a statement about a square tells something about the number itself.

A trap: the step "not even means odd" uses a fact about integers.
For real numbers there is no such split, and "if $x^2$ is an even integer, then $x$ is an even integer" is false for $x = \sqrt{2}$.
