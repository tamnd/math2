---
tag: YQC53G3JNP
kind: definition
name: Chern–Connes character
msc: [46L80, 19D55, 58B34]
defines: MM8TS81BAX
uses: [Q14JS2MA1C, 676K167XS8, 0KCE8CG86P, 0KZDNGA561]
sources:
  - url: https://en.wikipedia.org/wiki/Noncommutative_geometry
---

## Definition

Let $A$ be a unital algebra over $\C$.
For $m \ge 0$, let $C^\lambda_m(A)$ be the quotient of $A^{\otimes (m+1)}$ by the image of $1 - t$, where $t(a_0 \otimes \cdots \otimes a_m) = (-1)^m a_m \otimes a_0 \otimes \cdots \otimes a_{m-1}$.
With the Hochschild boundary $b$, these spaces form Connes' complex, whose homology is the [[cyclic homology|676K167XS8]] $HC_*(A)$.
Let $e \in M_k(A)$ be an [[idempotent matrix|0KCE8CG86P]], so $e^2 = e$, with entries $e_{ij}$.
Set
$$\operatorname{tr}(e^{\otimes(2n+1)}) = \sum_{i_0, \ldots, i_{2n}} e_{i_0 i_1} \otimes e_{i_1 i_2} \otimes \cdots \otimes e_{i_{2n} i_0} \in A^{\otimes(2n+1)}.$$
Its image in $C^\lambda_{2n}(A)$ is a cycle, and its class depends only on the class $[e]$ of $e$ in [[$K_0(A)$|Q14JS2MA1C]].
The *Chern–Connes character* in degree $2n$ is the group homomorphism
$$\operatorname{ch}_n \colon K_0(A) \to HC_{2n}(A), \quad [e] \mapsto [\operatorname{tr}(e^{\otimes(2n+1)})].$$

## Remarks

The chain is a cycle: since $e^2 = e$, each face of $b$ gives the same chain $\operatorname{tr}(e^{\otimes 2n})$, and the alternating sum is $\operatorname{tr}(e^{\otimes 2n})$.
This chain is fixed by the cyclic permutation of the factors, so $t$ acts on it by the sign $(-1)^{2n-1} = -1$, and its image in $C^\lambda_{2n-1}(A)$ is $0$.

Example: for $n = 0$, $HC_0(A) = A/[A, A]$ and $\operatorname{ch}_0[e]$ is the class of the [[trace|0KZDNGA561]] $\sum_i e_{ii}$.
For $A = \C$ this is the rank of $e$, which is the usual isomorphism $K_0(\C) \cong \Z$.

Non-example: the idempotent condition is needed.
In $A = \C[x]$ take the $1 \times 1$ matrix $a = x$, which is not idempotent.
Then $b(x \otimes x \otimes x) = x^2 \otimes x - x \otimes x^2 + x^2 \otimes x$, which equals $3\, x^2 \otimes x \ne 0$ in $C^\lambda_1(A)$, so $x \otimes x \otimes x$ is not a cycle.

Many authors multiply $\operatorname{ch}_n$ by a constant such as $(-1)^n (2n)!/n!$, so that the periodicity operator $S$ of cyclic homology sends $\operatorname{ch}_n$ to $\operatorname{ch}_{n-1}$.
Dually, a cyclic $2n$-cocycle $\varphi$ pairs with $K_0(A)$ by $[e] \mapsto \sum \varphi(e_{i_0 i_1}, e_{i_1 i_2}, \ldots, e_{i_{2n} i_0})$, up to the same kind of normalization.
For $A = C^\infty(M)$ with $M$ a closed manifold, periodic cyclic homology is de Rham cohomology, and the character corresponds to the classical Chern character of vector bundles.
