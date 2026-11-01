---
tag: 68SJQEC11F
kind: definition
name: Automorphic form
msc: [11F70, 11F12, "22E55"]
defines: 3C73HND6XA
uses: [0V33BNKZ9S, GWKN5VG78A, 0X1JXT47GA]
sources:
  - url: https://en.wikipedia.org/wiki/Automorphic_form
---

## Definition

Let $G$ be a connected semisimple Lie group with finite center that is a closed [[subgroup|0X1JXT47GA]] of $\mathrm{GL}_n(\R)$.
Let $K$ be a maximal compact subgroup of $G$, and let $\mathfrak{g}$ be the complexified Lie algebra of $G$.
Let $Z(\mathfrak{g})$ be the center of its universal enveloping algebra.
It acts on smooth functions on $G$ as left-invariant differential operators.
Let $\Gamma$ be a discrete subgroup of $G$, in the main case an arithmetic subgroup.
For $g \in G$ let $\norm{g} = \max_{i,j} \max(\abs{g_{ij}}, \abs{(g^{-1})_{ij}})$.
An *automorphic form* for $\Gamma$ is a [[smooth function|0V33BNKZ9S]] $f \colon G \to \C$ such that:

1. ($\Gamma$-invariance) $f(\gamma g) = f(g)$ for all $\gamma \in \Gamma$ and $g \in G$.
2. ($K$-finiteness) The functions $g \mapsto f(gk)$ for $k \in K$ span a finite-dimensional vector space.
3. ($Z(\mathfrak{g})$-finiteness) There is an ideal $J$ of finite codimension in $Z(\mathfrak{g})$ with $Df = 0$ for all $D \in J$.
4. (Moderate growth) There are constants $C, N > 0$ with $\abs{f(g)} \le C \norm{g}^N$ for all $g \in G$.

## Remarks

Example: let $G = \mathrm{SL}_2(\R)$, $K = \mathrm{SO}(2)$, $\Gamma = \mathrm{SL}_2(\Z)$, and let $h$ be a [[modular form|GWKN5VG78A]] of weight $k$.
For $g = \begin{pmatrix} a & b \\ c & d \end{pmatrix}$ put $f(g) = h(g \cdot i)\,(ci + d)^{-k}$, where $g \cdot i = \frac{ai + b}{ci + d}$.
The modularity of $h$ gives clause 1.
Right translation by the rotation $k_\theta = \begin{pmatrix} \cos\theta & -\sin\theta \\ \sin\theta & \cos\theta \end{pmatrix}$ multiplies $f$ by $e^{-ik\theta}$, since $k_\theta \cdot i = i$ and $i \sin\theta + \cos\theta = e^{i\theta}$, which gives clause 2.
Holomorphy of $h$ makes the Casimir operator act on $f$ by a scalar, which gives clause 3.
The bound of $h$ at the cusp gives clause 4.

Non-example: on the same $G$, the function $f(g) = (\mathrm{Im}\, g \cdot i)^s$ satisfies clauses 2, 3 and 4, but it is not invariant under $\gamma = \begin{pmatrix} 0 & -1 \\ 1 & 0 \end{pmatrix} \in \Gamma$, so clause 1 fails.

This is the definition of Harish-Chandra.
A classical variant works on a symmetric space $G/K$ and allows a factor of automorphy $j(\gamma, z)$ in clause 1, as for modular forms of weight $k$.
In the adelic setting, $G$ is a reductive group over a number field $F$ and automorphic forms are functions on $G(F) \backslash G(\mathbb{A}_F)$.
