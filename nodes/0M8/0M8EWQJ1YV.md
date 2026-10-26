---
tag: 0M8EWQJ1YV
kind: statement
role: theorem
name: Vieta's formulas
msc: [12D10]
uses: [0ZMY8441GW, 0SHMC00RJV]
sources:
  - url: https://en.wikipedia.org/wiki/Vieta%27s_formulas
    locator: Basic formulas
  - url: https://en.wikipedia.org/wiki/Vieta%27s_formulas
    locator: Generalization to rings
same_as:
  wikidata: Q570779
  wikipedia: Vieta's formulas
---

## Statement

Let $R$ be a [[commutative ring|0GYGHKX834]] and let $f = a_n x^n + a_{n-1} x^{n-1} + \dots + a_0 \in R[x]$.
Suppose that $f = a_n (x - r_1)(x - r_2) \cdots (x - r_n)$ with $r_1, \dots, r_n \in R$.
Then for $1 \le k \le n$,
$$a_n \, e_k(r_1, \dots, r_n) = (-1)^k a_{n-k},$$
where $e_k$ is the $k$-th [[elementary symmetric polynomial|0ZMY8441GW]].

## Remarks

If $a_n$ is a unit, this says $e_k(r_1, \dots, r_n) = (-1)^k a_{n-k}/a_n$.
For $x^2 + b x + c = (x - r_1)(x - r_2)$, it gives $r_1 + r_2 = -b$ and $r_1 r_2 = c$.
The proof expands the product and compares coefficients.
Over a field, the hypothesis says that $f$ [[splits|0SHMC00RJV]] with roots $r_1, \dots, r_n$, counted with multiplicity.

## History

The formulas are named after the French mathematician François Viète, who derived them for positive roots.

## Explanations

### L1 human

Vieta's formulas say that the sum of the roots, the sum of their products in pairs, and so on, are given by the coefficients.
You can know these sums without finding the roots.
