---
tag: 5D5SC7NNJ2
kind: definition
name: Pettis integral
msc: [28B05, 46G10]
defines: 9A5F3JGTC0
uses: [P15VQS5DJ9, X7GTF3D98F, DWJF7ABPR1, 0BDTTM24DP, 0M856Q1AMZ]
sources:
  - url: https://en.wikipedia.org/wiki/Pettis_integral
---

## Definition

Let $(X, \Sigma, \mu)$ be a [[measure space|P15VQS5DJ9]].
Let $E$ be a [[Banach space|0BDTTM24DP]] over $\R$ or $\C$ with [[dual space|0M856Q1AMZ]] $E^*$.
Let $f \colon X \to E$ be a function such that $\varphi \circ f$ is [[integrable|X7GTF3D98F]] for every $\varphi \in E^*$.
The function $f$ is *Pettis integrable* if for every $A \in \Sigma$ there is a vector $x_A \in E$ with
$$\varphi(x_A) = \int_A \varphi \circ f \, d\mu \quad \text{for every } \varphi \in E^*,$$
where the right side is a [[Lebesgue integral|DWJF7ABPR1]].
The vector $x_A$ is unique, and it is the *Pettis integral* $\int_A f \, d\mu$.

## Remarks

The vector $x_A$ is unique because the continuous linear functionals separate the points of $E$, by the Hahn–Banach theorem.

Example: let $E = \R^n$ and let each component $f_k$ of $f$ be integrable.
Then $x_A = (\int_A f_1 \, d\mu, \dots, \int_A f_n \, d\mu)$ works, because every $\varphi \in E^*$ is a linear combination of the coordinates.

Non-example: let $X = \N$ with the counting measure, $E = c_0$, the space of sequences tending to $0$, and $f(n) = e_n$, the $n$-th unit vector.
For each $\varphi \in E^* = \ell^1$, the sum $\sum_n \abs{\varphi(e_n)}$ is finite, so $\varphi \circ f$ is integrable.
But for $A = \N$ the only candidate is the constant sequence $(1, 1, \dots)$, which is not in $c_0$, so $f$ is not Pettis integrable.

Every Bochner integrable function is Pettis integrable, with the same integral.
In infinite-dimensional spaces the converse fails.
