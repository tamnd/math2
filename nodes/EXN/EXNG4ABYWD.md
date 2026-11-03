---
tag: EXNG4ABYWD
kind: definition
name: Steinberg relations
msc: [19C20, 19C09]
defines: 5N139ECTM1
uses: [0B1261B5ED, 01REXW3WWE, 0PXW0BN7DW]
sources:
  - url: https://en.wikipedia.org/wiki/Steinberg_group_(K-theory)
---

## Definition

Let $R$ be a [[ring|0B1261B5ED]] with identity, and let $n \ge 3$.
Let $H$ be a group, and let $x_{ij}(r)$ be elements of $H$, one for each pair of indices $1 \le i, j \le n$ with $i \ne j$ and each $r \in R$.
For $g, h \in H$, write $[g, h] = g h g^{-1} h^{-1}$ for their [[commutator|0PXW0BN7DW]].
The elements $x_{ij}(r)$ satisfy the *Steinberg relations* if, for all $r, s \in R$:

1. $x_{ij}(r) \, x_{ij}(s) = x_{ij}(r + s)$.
2. $[x_{ij}(r), x_{jl}(s)] = x_{il}(rs)$ when $i$, $j$, $l$ are pairwise distinct.
3. $[x_{ij}(r), x_{kl}(s)] = 1$ when $j \ne k$ and $i \ne l$.

## Remarks

Example: the [[elementary matrices|01REXW3WWE]] $e_{ij}(r) = I + r E_{ij}$ in $GL_n(R)$ satisfy the Steinberg relations, where $E_{ij}$ is the matrix with $1$ at position $(i, j)$ and $0$ elsewhere.
Indeed $E_{ij} E_{kl}$ equals $E_{il}$ if $j = k$ and $0$ otherwise.
So $(I + rE_{ij})(I + sE_{ij}) = I + (r + s)E_{ij}$, because $E_{ij}^2 = 0$ for $i \ne j$.
For pairwise distinct $i, j, l$, a direct product of the four factors gives $[e_{ij}(r), e_{jl}(s)] = I + rs E_{il}$.
If $j \ne k$ and $i \ne l$, then $E_{ij}E_{kl} = 0 = E_{kl}E_{ij}$, so the two matrices commute.

Non-example: the case $l = i$ is excluded in clause 2.
For $n = 2$ and $R = \Z$, the matrices $e_{12}(1)$ and $e_{21}(1)$ have commutator $\begin{pmatrix} 3 & -1 \\ 1 & 0 \end{pmatrix}$, which is not an elementary matrix.
So no relation of the form of clause 2 holds for the pair $(i, j, l) = (1, 2, 1)$.

Clause 1 implies $x_{ij}(0) = 1$ and $x_{ij}(r)^{-1} = x_{ij}(-r)$.
