---
tag: 0VEKNG02W0
kind: statement
role: proposition
name: Volume of a box
aliases: [volume-of-a-rectangular-box]
msc: [28A75]
uses: [0565DC8RMK, 0GTBGMZXV8, 0R0T1VWH5X]
sources:
  - url: https://en.wikipedia.org/wiki/Volume
    locator: Basic shapes
  - url: https://en.wikipedia.org/wiki/Volume
    locator: Integral calculus
---

## Statement

Let $a_i < b_i$ for $i = 1, \dots, n$, and let $Q = [a_1, b_1] \times \dots \times [a_n, b_n] \subseteq \mathbb{R}^n$.
Then $Q$ is Jordan measurable, and its volume is
$$\operatorname{vol}(Q) = \int_Q 1 \, dV = (b_1 - a_1)(b_2 - a_2) \cdots (b_n - a_n).$$

## Remarks

For a box, the [[Jordan measure|0565DC8RMK]] and the Riemann integral of the constant function $1$ give the same value.
The integral can be computed with [[Fubini's theorem|0R0T1VWH5X]] as an iterated integral of $1$, one factor $b_i - a_i$ at a time.
Open and half-open boxes with the same edges have the same volume, because the faces of $Q$ have volume zero.
For $n = 3$ this is the formula length times width times height, a case of base area times height. The volume of a general solid $E$ is the [[triple integral|0GTBGMZXV8]] $\iiint_E 1 \, dV$.

## Explanations

### L1 human

The volume of a box is the product of its side lengths.
In the theory of multiple integrals this is the starting point: Riemann sums and Jordan measure are both built from volumes of small boxes.
