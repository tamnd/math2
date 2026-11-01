---
tag: RN58Z2NWAC
kind: statement
role: theorem
name: Gelfond–Schneider theorem
msc: [11J81]
uses: [0MNF0BYFQC, 0VTQXTCR2G, 0DZXAXEJQ9, 02QGGD5G87]
about: [0VTQXTCR2G]
sources:
  - url: https://en.wikipedia.org/wiki/Gelfond%E2%80%93Schneider_theorem
same_as:
  wikidata: Q976033
  wikipedia: Gelfond–Schneider theorem
---

## Statement

Let $a$ and $b$ be complex [[algebraic numbers|0MNF0BYFQC]] with $a \ne 0$, $a \ne 1$, and $b \notin \Q$.
Let $\log a$ be any value of the [[complex logarithm|02QGGD5G87]] of $a$.
Then the number $a^b = e^{b \log a}$ is [[transcendental|0VTQXTCR2G]].

## Remarks

The proof builds an auxiliary function $F(z) = \sum_{i,j} c_{ij} e^{(i + j b) z \log a}$ with integer coefficients $c_{ij}$, not all zero, chosen so that $F$ vanishes at many integer points.
If $a^b$ were algebraic, the values of $F$ and its derivatives at integers would be algebraic numbers of controlled size.
An analytic estimate and a lower bound for nonzero algebraic numbers then force too many zeros, which is a contradiction.
Examples: $2^{\sqrt{2}}$ is transcendental, and so is $e^{\pi}$, since $e^{\pi} = (-1)^{-i}$ with $\log(-1) = i\pi$.
Another consequence: $\log 3 / \log 2$ is transcendental, since it is irrational and $2^{\log 3 / \log 2} = 3$.
The hypothesis $b \notin \Q$ is necessary: $2^{1/2} = \sqrt{2}$ is algebraic.
The theorem answers Hilbert's seventh problem.
[[Baker's theorem|WMBJSNG57F]] generalizes it to linear forms in several logarithms.

## Explanations

### L1 human

Raise an algebraic number to an irrational algebraic power, for example $2^{\sqrt{2}}$.
The theorem says that the result is never a root of a polynomial with integer coefficients.
So numbers such as $2^{\sqrt{2}}$ and $e^{\pi}$ are transcendental, like $\pi$ and $e$.

### L2 human

An equivalent form: if $\alpha$ and $\beta$ are nonzero algebraic numbers and $\log \alpha$ and $\log \beta$ are linearly independent over $\Q$, then they are linearly independent over the algebraic numbers.
This is the case of two logarithms in Baker's theorem.
Together with the [[Lindemann–Weierstrass theorem|0JNCBFMPXR]], it is one of the classical results of transcendence theory.
The question whether $e + \pi$ or $e \pi$ is transcendental is still open.
