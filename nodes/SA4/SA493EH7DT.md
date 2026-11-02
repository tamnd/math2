---
tag: SA493EH7DT
kind: definition
name: Reduced homology
msc: [55N10]
defines: NJQMWVK3QK
uses: [M0Q5CFJ7ZH, 4BVWH0BN28]
sources:
  - url: https://en.wikipedia.org/wiki/Reduced_homology
---

## Definition

Let $X$ be a nonempty topological space with singular [[chain complex|WQ82C0M3QB]] $C_\bullet(X)$.
The *augmentation* is the homomorphism $\varepsilon \colon C_0(X) \to \Z$ given by $\varepsilon\left(\sum_i n_i \sigma_i\right) = \sum_i n_i$.
The *augmented chain complex* is
$$\cdots \to C_2(X) \xrightarrow{\partial_2} C_1(X) \xrightarrow{\partial_1} C_0(X) \xrightarrow{\varepsilon} \Z \to 0,$$
with $\Z$ placed in degree $-1$; it is a chain complex because $\varepsilon \circ \partial_1 = 0$.
The *reduced [[homology|2J4JJJYP22]]* $\tilde H_n(X)$ is the homology of the augmented chain complex in degree $n$.

## Remarks

For $n \ge 1$, $\tilde H_n(X) = H_n(X)$, where $H_n$ is [[singular homology|M0Q5CFJ7ZH]].
In degree $0$, $H_0(X) \cong \tilde H_0(X) \oplus \Z$, and $\tilde H_{-1}(X) = 0$ because $\varepsilon$ is onto.
For any point $x_0 \in X$, $\tilde H_n(X) \cong H_n(X, \set{x_0})$ for all $n$, a [[relative homology|4BVWH0BN28]] group.

Example: for a one-point space $X$, $C_n(X) \cong \Z$ for every $n \ge 0$, and $\varepsilon$ is an isomorphism, so $\tilde H_n(X) = 0$ for all $n$.

Non-example: the hypothesis that $X$ is nonempty matters.
For $X = \emptyset$ the map $\varepsilon \colon 0 \to \Z$ is not onto, so the augmented complex gives $\tilde H_{-1}(\emptyset) = \Z$, and the formula $H_0 \cong \tilde H_0 \oplus \Z$ fails.
