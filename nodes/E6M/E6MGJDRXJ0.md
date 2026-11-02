---
tag: E6MGJDRXJ0
kind: definition
name: Infinite product measure
msc: [28A35, 60A10]
defines: 2HWVFHM13R
uses: [059TJN0NZ1, 6HVCTJGB61, 0NFPJVJJHX]
sources:
  - url: https://en.wikipedia.org/wiki/Product_measure
---

## Definition

Let $I$ be a nonempty index set and, for each $i \in I$, let $(X_i, \Sigma_i, \mu_i)$ be a [[probability space|0NFPJVJJHX]].
Let $X = \prod_{i \in I} X_i$ with the [[product σ-algebra|6HVCTJGB61]] $\Sigma = \bigotimes_{i \in I} \Sigma_i$.
The *product measure* $\bigotimes_{i \in I} \mu_i$ is the unique [[probability measure|059TJN0NZ1]] $\mu$ on $(X, \Sigma)$ with
$$\mu\Big( \prod_{i \in J} A_i \times \prod_{i \in I \setminus J} X_i \Big) = \prod_{i \in J} \mu_i(A_i)$$
for every finite $J \subseteq I$ and all $A_i \in \Sigma_i$, $i \in J$.

## Remarks

Such a measure exists for every family of probability spaces, without topological assumptions, and it is unique because the cylinder sets form a π-system that generates $\Sigma$.
For countable $I$, existence also follows from the [[Ionescu-Tulcea theorem|94ASD187AQ]] with kernels that do not depend on the past.

Example: let $X_n = \set{0, 1}$ and $\mu_n(\set{0}) = \mu_n(\set{1}) = \tfrac12$ for $n = 1, 2, 3, \ldots$
The product measure on the space of sequences $(x_1, x_2, \ldots)$ with $x_n \in \set{0, 1}$ is the law of a sequence of fair coin tosses.
The set of sequences starting with $0, 1$ is a cylinder set with $J = \set{1, 2}$ and measure $\tfrac12 \cdot \tfrac12 = \tfrac14$.

Non-example: on the same space, the Dirac measure at the constant sequence $(0, 0, 0, \ldots)$ is a probability measure.
It gives the cylinder set $\set{x : x_1 = 0}$ measure $1$ instead of $\tfrac12$, so it is not the product of the fair coin measures.

Under the product measure, the coordinate maps $\pi_i$ are independent random variables, and $\pi_i$ has law $\mu_i$.
