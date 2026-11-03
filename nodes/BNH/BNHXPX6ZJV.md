---
tag: BNHXPX6ZJV
kind: statement
role: theorem
name: Elias–Bassalygo bound
msc: [94B65]
uses: [TAE6K8NQ46, M2X88AXM17, 6E7ZZ4DYX3, 95CYGNRQQ6, GCRQN6TFHK]
about: [TAE6K8NQ46]
sources:
  - url: https://en.wikipedia.org/wiki/Elias_Bassalygo_bound
same_as:
  wikidata: Q5360449
  wikipedia: Elias Bassalygo bound
---

## Statement

Let $q \ge 2$ be an integer, let $\theta = 1 - 1/q$, and let $0 < \delta < \theta$.
Let
$$J_q(\delta) = \theta \left(1 - \sqrt{1 - \frac{\delta}{\theta}}\right),$$
and let $H_q$ be the [[q-ary entropy function|95CYGNRQQ6]].
Let $(C_n)$ be a sequence of [[codes|TAE6K8NQ46]] over an alphabet with $q$ symbols, where $C_n$ has length $n$ and [[minimum distance|M2X88AXM17]] at least $\delta n$.
Then
$$\limsup_{n \to \infty} \frac{\log_q \abs{C_n}}{n} \le 1 - H_q\big(J_q(\delta)\big).$$

## Remarks

The proof combines a list-decoding form of the [[Johnson bound|GCRQN6TFHK]] with an averaging argument.
The Johnson bound shows that a Hamming ball of radius $r$ slightly below $J_q(\delta) n$ contains at most a number of codewords that grows only polynomially in $n$.
On the other hand, summing over all centers $y$ of the [[Hamming space|6E7ZZ4DYX3]] gives $\sum_y \abs{B(y, r) \cap C} = \abs{C} \cdot \abs{B(0, r)}$, so some ball contains at least $\abs{C} \abs{B(0, r)} / q^n$ codewords.
Comparing the two counts and using $\abs{B(0, r)} \approx q^{n H_q(r/n)}$ gives the bound.
Since $J_q(\delta) > \delta/2$ for $0 < \delta < \theta$, it is stronger than the asymptotic Hamming bound $1 - H_q(\delta/2)$.
Example: for $q = 2$ and $\delta = 1/4$, $J_2(1/4) = \tfrac{1}{2}(1 - \sqrt{1/2}) \approx 0.146$, while $\delta/2 = 0.125$.

## Explanations

### L1 human

The Elias–Bassalygo bound caps the rate of long codes with a given fraction of correctable errors.
The idea is to find a small region of the space that holds many codewords.
Then one shows that a code with good distance cannot crowd any region that much.
It improves on the sphere-packing idea behind the Hamming bound.

### L2 human

It is stronger than the Hamming bound, but for binary codes the best known asymptotic upper bounds come from the linear programming method of McEliece, Rodemich, Rumsey and Welch.
The gap between these upper bounds and the Gilbert–Varshamov lower bound $1 - H_q(\delta)$ remains one of the central open problems of coding theory.
The function $J_q$ is also the radius up to which list decoding with small lists is always possible.
