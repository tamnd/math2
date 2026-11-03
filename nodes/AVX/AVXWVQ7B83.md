---
tag: AVXWVQ7B83
kind: definition
name: Karoubi–Villamayor K-theory
msc: [19D25]
defines: QE20P81GXX
uses: [0B1261B5ED, 0SDC934R52, WK0A32TZHB, FDFYCM3YYC, P976WYEFMB, G8R9561PXT, 5GVFZWMWC8]
sources:
  - url: https://en.wikipedia.org/wiki/Algebraic_K-theory
---

## Definition

Let $R$ be a [[ring|0B1261B5ED]] with identity.
For $p \ge 0$, let
$$R[\Delta^p] = R[t_0, \ldots, t_p]/(t_0 + \cdots + t_p - 1),$$
a quotient of a [[polynomial ring|0SDC934R52]] in central variables.
These rings form a [[simplicial ring|WK0A32TZHB]] $R[\Delta^\bullet]$.
The face map $d_i \colon R[\Delta^p] \to R[\Delta^{p-1}]$ sends $t_j$ to $t_j$ for $j < i$, to $0$ for $j = i$, and to $t_{j-1}$ for $j > i$.
The degeneracy $s_i \colon R[\Delta^p] \to R[\Delta^{p+1}]$ sends $t_j$ to $t_j$ for $j < i$, to $t_i + t_{i+1}$ for $j = i$, and to $t_{j+1}$ for $j > i$.
Applying the [[stable general linear group|G8R9561PXT]] degreewise gives a simplicial group $GL(R[\Delta^\bullet])$.
For $n \ge 1$, the *Karoubi–Villamayor K-group* is
$$KV_n(R) = \pi_{n-1} \, GL(R[\Delta^\bullet]),$$
the $(n-1)$-st [[homotopy group|P976WYEFMB]] of this simplicial group.

## Remarks

A simplicial group is a [[Kan complex|FDFYCM3YYC]], so its homotopy groups are defined combinatorially.
Since $R[\Delta^1] \cong R[t]$, the group $KV_1(R)$ is the quotient of $GL(R)$ by the normal subgroup of matrices $g(1)$, where $g(t) \in GL(R[t])$ and $g(0) = 1$.
Each elementary matrix $e_{ij}(a)$ equals $g(1)$ for $g(t) = e_{ij}(ta)$, so the surjection $GL(R) \to KV_1(R)$ factors through $K_1(R) = GL(R)/E(R)$, and $K_1(R) \to KV_1(R)$ is surjective.

Example: for a regular Noetherian ring $R$, $KV_n(R) \cong K_n(R)$ for all $n \ge 1$, because $K$-theory is then homotopy invariant on all the rings $R[\Delta^p]$.

Non-example: $KV$ is not Quillen [[K-theory|5GVFZWMWC8]] in general.
Let $A = k[\varepsilon][t]$ with $k$ a field and $\varepsilon^2 = 0$.
The unit $1 + \varepsilon t$ has a nonzero class in $K_1(A)$, because its determinant $1 + \varepsilon t$ is not $1$.
But $g(s) = 1 + \varepsilon t s$ satisfies $g(0) = 1$ and $g(1) = 1 + \varepsilon t$, so its class in $KV_1(A)$ is trivial.
