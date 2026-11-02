---
tag: TMCMTXNZ63
kind: definition
name: Eichler order
msc: [11R52, 16H10]
defines: W7PYDJZ8BC
uses: [MWBDFS2KJ5, ZWXW0T3EAC, 1ZBX4TKVZ9, E5DH1CSW1N, 0N5NJZKKN3]
sources:
  - url: https://en.wikipedia.org/wiki/Eichler_order
---

## Definition

Let $F$ be an [[algebraic number field|MWBDFS2KJ5]] with ring of integers $\mathcal{O}_F$, and let $B$ be a [[quaternion algebra|ZWXW0T3EAC]] over $F$.
An *Eichler order* in $B$ is an $\mathcal{O}_F$-[[order|1ZBX4TKVZ9]] $\mathcal{O} \subseteq B$ such that $\mathcal{O} = \mathcal{O}_1 \cap \mathcal{O}_2$ for two [[maximal orders|E5DH1CSW1N]] $\mathcal{O}_1, \mathcal{O}_2$ of $B$.

## Remarks

Example: $F = \Q$, $B = M_2(\Q)$, $N \ge 1$ and $g = \operatorname{diag}(1, N)$.
The order $g M_2(\Z) g^{-1}$ consists of the matrices $\begin{pmatrix} a & b/N \\ Nc & d \end{pmatrix}$ with $a, b, c, d \in \Z$.
Its intersection with $M_2(\Z)$ is
$$\mathcal{O}_0(N) = \set{\begin{pmatrix} a & b \\ c & d \end{pmatrix} \in M_2(\Z) : N \mid c},$$
so $\mathcal{O}_0(N)$ is an Eichler order; $N$ is called its level.
Non-example: the order $\Z + 2 M_2(\Z)$ in $M_2(\Q)$ is not an Eichler order.
Every maximal order of $M_2(\Q)$ is the endomorphism ring of a lattice in $\Q^2$.
By the elementary divisor theorem, two such lattices have a common adapted basis.
So every Eichler order of $M_2(\Q)$ contains an [[idempotent|0N5NJZKKN3]] other than $0$ and $1$.
An idempotent $e$ of $\Z + 2M_2(\Z)$ is congruent to $0$ or $1$ modulo $2M_2(\Z)$; if $e \equiv 0$ then $e = e^k \in 2^k M_2(\Z)$ for all $k$, so $e = 0$, and symmetrically $1 - e \equiv 0$ forces $e = 1$.
