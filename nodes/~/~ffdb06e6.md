---
tag: ~ffdb06e6
kind: statement
role: theorem
name: Holomorphic functions are analytic
aliases: [analyticity-of-holomorphic-functions]
msc: [30B10]
uses: [~1a187203, ~21d9a2cc, ~51582ceb]
sources:
  - url: https://en.wikipedia.org/wiki/Analyticity_of_holomorphic_functions
    locator: Proof
  - url: https://en.wikipedia.org/wiki/Analyticity_of_holomorphic_functions
    locator: lead section
same_as:
  wikidata: Q4751162
  wikipedia: Analyticity of holomorphic functions
---

## Statement

Let $U \subseteq \mathbb{C}$ be an open set and let $f : U \to \mathbb{C}$ be [[holomorphic|~1a187203]] on $U$.
Let $c \in U$ and $r > 0$ be such that the open disc $D = \{z : |z - c| < r\}$ is contained in $U$.
Then there are complex numbers $a_0, a_1, a_2, \dots$ such that the [[power series|~21d9a2cc]] $\sum_{n \ge 0} a_n (z - c)^n$ converges to $f(z)$ for each $z \in D$.
For each $\rho$ with $0 < \rho < r$, the coefficients are
$$a_n = \frac{1}{2 \pi i} \oint_{|z - c| = \rho} \frac{f(z)}{(z - c)^{n+1}} \, dz.$$
In particular, $f$ is analytic on $U$: near each point of $U$, $f$ is the sum of a convergent power series.

## Remarks

Proof idea: in [[Cauchy's integral formula|~51582ceb]], expand $\frac{1}{z - a}$ as a geometric series in $\frac{a - c}{z - c}$, and integrate term by term.
The radius of convergence of the Taylor series at $c$ is at least the distance from $c$ to the boundary of $U$.
For example, the Taylor series of $1/(1 - z)$ at $0$ has radius $1$, the distance from $0$ to the point $1$ where the function is not defined.
The converse is also true: [[power series are holomorphic in their disc of convergence|~e89eb384]].

## Explanations

### L1 human

A function with one complex derivative everywhere on an open set is automatically equal to its Taylor series near each point.
This is very different from real functions, where a differentiable function can fail to have a second derivative.
