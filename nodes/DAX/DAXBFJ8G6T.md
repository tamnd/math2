---
tag: DAXBFJ8G6T
kind: definition
name: Relative homology
msc: [55N10]
defines: 4BVWH0BN28
uses: [M0Q5CFJ7ZH, 0WS9P12FQR]
sources:
  - url: https://en.wikipedia.org/wiki/Relative_homology
---

## Definition

Let $X$ be a topological space and let $A \subseteq X$ be a subspace with the [[subspace topology|0WS9P12FQR]].
Let $C_\bullet(X)$ be the singular [[chain complex|WQ82C0M3QB]] of $X$.
Every singular simplex in $A$ is a singular simplex in $X$, so $C_\bullet(A)$ is a subcomplex of $C_\bullet(X)$.
The *relative chain complex* is the quotient $C_n(X, A) = C_n(X) / C_n(A)$, with the boundary map induced by the boundary of $C_\bullet(X)$.
The *relative [[homology|2J4JJJYP22]]* $H_n(X, A)$ is the homology of $C_\bullet(X, A)$ in degree $n$.

## Remarks

A class in $H_n(X, A)$ is represented by a *relative cycle*, a chain $c \in C_n(X)$ with $\partial c \in C_{n-1}(A)$.
Two relative cycles give the same class when their difference is $\partial b + a$ with $b \in C_{n+1}(X)$ and $a \in C_n(A)$.
For $A = \emptyset$, the group $H_n(X, \emptyset)$ is the [[singular homology|M0Q5CFJ7ZH]] $H_n(X)$.
A map of pairs $f \colon (X, A) \to (Y, B)$, that is, a continuous map with $f(A) \subseteq B$, induces maps $f_* \colon H_n(X, A) \to H_n(Y, B)$.

Example: for $n \ge 1$, $H_n(D^n, S^{n-1}) \cong \Z$ and the other relative groups vanish.
For $n = 1$, the path $\sigma(t) = 2t - 1$ in $D^1 = [-1, 1]$ is a relative cycle, since $\partial \sigma = (1) - (-1)$ lies in $C_0(S^0)$.

Non-example: in $X = [-1, 1]$ with $A = \set{-1}$, the same path is not a relative cycle, because its boundary contains the point $1 \notin A$.
