---
tag: TD7S2HF19H
kind: definition
name: Coupling
msc: ["60E05", "60E15"]
defines: HTR7J0W66V
uses: [059TJN0NZ1, 0MXT6PRZZ6, 0PNRKMRC55, 0NFPJVJJHX]
sources:
  - url: https://en.wikipedia.org/wiki/Coupling_(probability)
---

## Definition

Let $\mu$ be a [[probability measure|059TJN0NZ1]] on a measurable space $(E, \mathcal{E})$ and $\nu$ a probability measure on a measurable space $(F, \mathcal{F})$.
A *coupling* of $\mu$ and $\nu$ is a probability measure $\gamma$ on the product space $(E \times F, \mathcal{E} \otimes \mathcal{F})$ whose [[marginals|0MXT6PRZZ6]] are $\mu$ and $\nu$:
$$\gamma(A \times F) = \mu(A) \quad \text{and} \quad \gamma(E \times B) = \nu(B) \qquad \text{for all } A \in \mathcal{E}, \ B \in \mathcal{F}.$$
Equivalently, a coupling is a pair of [[random variables|0PNRKMRC55]] $(X, Y)$ on one [[probability space|0NFPJVJJHX]] with $X$ of law $\mu$ and $Y$ of law $\nu$.
The joint law of such a pair is a coupling in the first sense.

## Remarks

Example: the product measure $\mu \otimes \nu$ is a coupling, the independent coupling. Indeed $(\mu \otimes \nu)(A \times F) = \mu(A) \nu(F) = \mu(A)$, and in the same way for the second marginal.
Example: for $0 \le p \le q \le 1$, let $U$ be uniform on $[0, 1]$, $X = \mathbf{1}_{\set{U < p}}$ and $Y = \mathbf{1}_{\set{U < q}}$. Then $X$ and $Y$ are [[Bernoulli|0386Y0Z7Y7]] with parameters $p$ and $q$, and $X \le Y$ everywhere.
Non-example: on $\set{0, 1}^2$, the point mass $\delta_{(0, 0)}$ is not a coupling of two Bernoulli laws with parameter $\frac{1}{2}$, because its first marginal is $\delta_0$.
If $E = F$ and the diagonal is measurable, every coupling satisfies the coupling inequality $d_{TV}(\mu, \nu) \le P(X \ne Y)$, where $d_{TV}$ is the total variation distance.
