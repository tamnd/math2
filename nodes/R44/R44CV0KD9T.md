---
tag: R44CV0KD9T
kind: statement
role: theorem
name: Sturm's theorem
msc: ["12D10", 26C10]
uses: [0Q9EZS90GY, 00EHX6FWC0, 0F1WR9C83K, D6D0SR1FK3, Q75YRG25JK, 00KAFBR32E]
about: [019MA1VTR2]
sources:
  - url: https://en.wikipedia.org/wiki/Sturm%27s_theorem
same_as:
  wikidata: Q1632301
  wikipedia: Sturm's theorem
---

## Statement

Let $p \in \R[x]$ be a nonconstant polynomial without multiple roots.
Define the *Sturm sequence* by $p_0 = p$, $p_1 = p'$ (the [[derivative|0F1WR9C83K]]), and $p_{i+1} = -\operatorname{rem}(p_{i-1}, p_i)$.
Here $\operatorname{rem}$ is the remainder of [[polynomial division|D6D0SR1FK3]], and the sequence stops at the last nonzero term $p_m$.
For $\xi \in \R$, let $V(\xi)$ be the number of sign changes in the sequence $p_0(\xi), p_1(\xi), \dots, p_m(\xi)$, with zeros ignored.
Let $a < b$ be real numbers that are not [[roots|00EHX6FWC0]] of $p$.
Then the number of distinct real roots of $p$ in the interval $(a, b)$ is $V(a) - V(b)$.

## Remarks

The sequence is the Euclidean algorithm for $p$ and $p'$ with sign changes, so $p_m$ is a [[greatest common divisor|Q75YRG25JK]] of $p$ and $p'$, a nonzero constant here.
As $\xi$ increases, $V(\xi)$ can only change when $\xi$ passes a root of some $p_i$.
At a root of $p_i$ with $0 < i < m$, the relation $p_{i-1} = q_i p_i - p_{i+1}$ forces $p_{i-1}$ and $p_{i+1}$ to have opposite signs, so $V$ does not change.
At a root of $p$, the signs of $p$ and $p'$ go from opposite to equal, so $V$ drops by exactly one.
Example: for $p = x^2 - 2$, the sequence is $x^2 - 2$, $2x$, $2$; then $V(0) = 1$ and $V(2) = 0$, so there is one root in $(0, 2)$, namely $\sqrt 2$.
The theorem also holds without the hypothesis on multiple roots, still counting distinct roots, but the proof then divides the sequence by $p_m$.

## Explanations

### L1 human

Sturm's theorem counts the real roots of a polynomial in an interval exactly, with no guessing.
One builds a short chain of polynomials by repeated division, evaluates the chain at the two ends of the interval, and counts sign changes.
The difference of the two counts is the number of roots in between.

### L2 human

Unlike [[Descartes' rule of signs|T6DQQ36JZ5]], which only gives an upper bound, Sturm's theorem gives the exact number of distinct roots.
By bisection, it isolates every real root in an interval as small as one likes, which is the basis of exact real root isolation in computer algebra.
Taking $a$ below and $b$ above all roots, it counts all real roots of $p$, using the signs of leading coefficients only.
The same argument works over any real closed field, where the [[intermediate value theorem|00KAFBR32E]] holds for polynomials.
