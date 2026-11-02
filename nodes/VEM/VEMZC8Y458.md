---
tag: VEMZC8Y458
kind: definition
name: Independent component analysis
msc: [62H25, 94A12]
defines: NBX8FZY516
uses: [0GQ938GDE0, 0EB9N0S33C, 05AQE0QR0D]
sources:
  - url: https://en.wikipedia.org/wiki/Independent_component_analysis
---

## Definition

Let $p \ge 2$.
The *independent component analysis model* for a random vector $X$ in $\R^p$ is
$$X = A S,$$
where:

1. $A$ is an unknown [[invertible|0EB9N0S33C]] $p \times p$ matrix, the *mixing matrix*.
2. $S = (S_1, \ldots, S_p)$ is an unobserved random vector whose components are [[mutually independent|0GQ938GDE0]] and non-constant.
3. At most one of the $S_i$ has a [[normal distribution|05AQE0QR0D]].

*Independent component analysis* estimates, from observations of $X$, an unmixing matrix $W$ such that $W X$ has independent components.
Then $W X$ is the estimate of the sources $S$.

## Remarks

Under clauses 1 to 3, $A$ is determined up to a permutation of its columns and a nonzero scaling of each column.
So the sources are recovered up to order and scale.
Example: let $S_1, S_2$ be independent and uniform on $[-1, 1]$, and $A = \begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix}$.
Then $X = (S_1 + S_2, S_2)$ has dependent components, and $W = A^{-1}$ gives back $W X = S$.
Non-example: if $S_1$ and $S_2$ are independent standard normal, clause 3 fails.
For every rotation matrix $Q$, the vector $Q S$ is again standard normal with independent components, so $A$ and $A Q^T$ give the same law of $X$ and cannot be told apart.
Algorithms usually whiten $X$ first and then maximise a measure of non-Gaussianity, such as kurtosis or negentropy.
