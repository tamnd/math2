---
tag: 017DH8WXTE
kind: statement
role: theorem
name: Riemann's criterion for integrability
msc: [26A42]
uses: [0QRQVH0CRW, 021XJAQVDC]
sources:
  - url: https://en.wikipedia.org/wiki/Darboux_integral
    locator: Refinement of a partition and relation to Riemann integration
---

## Statement

Let $a < b$ and let $f \colon [a, b] \to \mathbb{R}$ be bounded.
Then $f$ is Riemann integrable on $[a, b]$ if and only if the following holds.
For each $\varepsilon > 0$ there is a partition $P$ of $[a, b]$ with $U(f, P) - L(f, P) < \varepsilon$.

## Remarks

Here $U$ and $L$ are the upper and lower [[Darboux sums|0QRQVH0CRW]].
The condition says that the upper and lower Darboux integrals are equal. So it follows from the [[equality of Darboux and Riemann integrability|021XJAQVDC]].
This is the usual tool to prove that [[continuous|06SESV7GQY]] and [[monotone|04YKAYDQPW]] functions are integrable.

## Explanations

### L1 human

A function is integrable when we can trap its graph between step functions whose areas differ by as little as we like.
