---
tag: 1AFTCHDDFE
kind: statement
role: theorem
name: Artin approximation theorem
msc: [13B40, 13J15, 13F25]
uses: [3E8ZG3NJYZ, 0SDC934R52, 917PGHVZPM, 2VF2TSJ3PY]
about: [3E8ZG3NJYZ, 917PGHVZPM]
sources:
  - url: https://en.wikipedia.org/wiki/Artin_approximation_theorem
same_as:
  wikidata: Q4801169
  wikipedia: Artin approximation theorem
---

## Statement

Let $k$ be a field and let $x = (x_1, \ldots, x_n)$ be variables.
Let $k[\![x]\!]$ be the [[ring of formal power series|3E8ZG3NJYZ]] in $x$.
Let $k\langle x \rangle \subseteq k[\![x]\!]$ be the ring of algebraic power series: those that are algebraic over the [[polynomial ring|0SDC934R52]] $k[x]$.
Let $y = (y_1, \ldots, y_N)$ be further variables and let $f_1, \ldots, f_m \in k[x, y]$ be polynomials.
Assume that $\hat{y} = (\hat{y}_1, \ldots, \hat{y}_N) \in k[\![x]\!]^N$ satisfies $f_j(x, \hat{y}) = 0$ for $j = 1, \ldots, m$.
Then for every integer $c \ge 1$ there is $\bar{y} \in k\langle x \rangle^N$ such that $f_j(x, \bar{y}) = 0$ for $j = 1, \ldots, m$ and $\bar{y}_i \equiv \hat{y}_i \pmod{(x_1, \ldots, x_n)^c}$ for $i = 1, \ldots, N$.

## Remarks

The ring $k\langle x \rangle$ is the [[Henselization|917PGHVZPM]] of the local ring of $k[x]$ at the ideal $(x_1, \ldots, x_n)$.
The theorem says that formal solutions of polynomial equations can be approximated, in the [[$(x)$-adic topology|2VF2TSJ3PY]], by algebraic solutions.
M. Artin proved it in 1969.
Popescu's theorem extends the result to every excellent Henselian local ring in place of $k\langle x \rangle$.

Example: the equation $y_1 - y_2 = 0$ has the formal solution $\hat{y}_1 = \hat{y}_2 = \sum_{i \ge 0} x^i / i!$ over $\Q$, which is not algebraic.
The truncations $\bar{y}_1 = \bar{y}_2 = \sum_{i < c} x^i / i!$ are polynomials, hence algebraic, and agree with $\hat{y}$ modulo $(x)^c$.
The theorem does not say that the formal solution itself is algebraic; it only gives algebraic solutions that agree with it to any given order.

## Explanations

### L1 human

Suppose a system of polynomial equations has a solution made of formal power series.
Such a solution may be wild: the series may not come from any algebraic equation.
The theorem says that there are tame solutions nearby, made of algebraic power series, which agree with the formal solution up to any order you choose.
So questions about formal solutions can often be moved to the much smaller world of algebraic functions.

### L2 human

In algebraic geometry, formal power series describe infinitesimal neighbourhoods, while algebraic power series describe étale neighbourhoods.
The theorem lets one pass from a formal statement about the completion of a local ring to a statement in the [[Henselization|917PGHVZPM]], and so to an étale neighbourhood.
This is used, for example, to compare the formal and the étale local structure of singularities.
It is also a key input in Artin's work on algebraic spaces and moduli problems.
