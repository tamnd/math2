---
tag: N3FERWCTTJ
kind: example
name: The implicit universal quantifier in an algebraic identity
msc: ["97E40", "97H20"]
topics: [WMY13MXY3W]
audience: school
instance_of: [EGTZPA6QH3]
uses: [EGTZPA6QH3, 0GHS47PDAQ, 0ED72CTBNP]
sources:
  - url: https://en.wikipedia.org/wiki/Quantifier_(logic)
    locator: lead section
  - url: https://en.wikipedia.org/wiki/Identity_(mathematics)
    locator: lead section
  - book: isbn:9781108439534
    locator: Section 2.1
---

## Example

A textbook writes the identity $(a + b)^2 = a^2 + 2ab + b^2$.
No quantifier is written, but the identity is a claim about all real numbers $a$ and $b$.
We make the hidden [[quantifiers|EGTZPA6QH3]] explicit and check the statement.

1. The letters $a$ and $b$ are not given values, and the text does not ask for a solution. So each letter carries a hidden [[universal quantifier|0GHS47PDAQ]].
2. The full statement is: for every real number $a$ and for every real number $b$, $(a + b)^2 = a^2 + 2ab + b^2$.
3. Proof: let $a$ and $b$ be arbitrary real numbers. Then $(a + b)^2 = (a + b)(a + b) = a^2 + ab + ba + b^2$.
4. Since $ab = ba$, the sum is $a^2 + 2ab + b^2$.
5. The numbers $a$ and $b$ were arbitrary, so the identity holds for all real $a$ and $b$.

## Remarks

The same shape of formula can carry a different claim.
The equation $(a + b)^2 = a^2 + b^2$ is not an identity.
Read with the hidden "for all $a$ and $b$", it is false, and $a = b = 1$ is a [[counterexample|0ED72CTBNP]]: $(1 + 1)^2 = 4$, but $1^2 + 1^2 = 2$.
Read as a condition on $a$ and $b$, it holds exactly when $2ab = 0$, that is, when $a = 0$ or $b = 0$.
So a reader must decide from the context whether a formula is an identity, which hides "for all", or an equation to solve, which asks for the set of solutions.

Some books write $\equiv$ for an identity, as in $(a + b)^2 \equiv a^2 + 2ab + b^2$, to mark the universal reading.
The identity also holds in every commutative ring, and the proof above uses only the ring laws and $ab = ba$.
For square matrices $A$ and $B$, the product $AB$ need not equal $BA$, and $(A + B)^2 = A^2 + AB + BA + B^2$ is the correct form.

## Explanations

### L1 human

The rule $(a + b)^2 = a^2 + 2ab + b^2$ is meant to work for every pair of numbers.
For $a = 3$ and $b = 2$, the left side is $5^2 = 25$, and the right side is $9 + 12 + 4 = 25$.
For $a = 10$ and $b = 1$, the left side is $121$, and the right side is $100 + 20 + 1 = 121$.
The rule does not say "every" in words, but every pair of numbers fits it.

### L2 human

We decide which of two formulas hides "for all": $\sin^2 x + \cos^2 x = 1$ and $\sin x = \cos x$.

1. The first formula is true for every real $x$, because the point $(\cos x, \sin x)$ lies on the unit circle. So it is an identity, and it means "for all real $x$".
2. The second formula is false for $x = 0$, since $\sin 0 = 0$ and $\cos 0 = 1$. So it cannot mean "for all $x$".
3. The second formula is true for $x = \pi/4$. So it is an equation, and "solve $\sin x = \cos x$" asks for the set $\{\pi/4 + k\pi : k \in \mathbb{Z}\}$.

The typical use of this test is in reading a formula: the context or one checked value tells whether it is an identity or an equation.

A trap: a single value that satisfies a formula does not make it an identity.
The formula $x^2 = 2x$ holds for $x = 2$, but not for $x = 1$.
