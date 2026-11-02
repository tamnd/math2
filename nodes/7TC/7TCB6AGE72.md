---
tag: 7TCB6AGE72
kind: definition
name: Path algebra
msc: [16G20, 16S10]
defines: 2PYANBGXFD
uses: [04C5ZBG1WT, RE9YFFS3TS, 000AYPA9AJ, 0KCQ9Y3QKA, 3CTW1P4HBP, 2P3Y2FRCSZ]
sources:
  - url: https://en.wikipedia.org/wiki/Quiver_(mathematics)
---

## Definition

Let $k$ be a [[field|04C5ZBG1WT]] and let $Q = (Q_0, Q_1, s, t)$ be a [[quiver|RE9YFFS3TS]], with vertex set $Q_0$, arrow set $Q_1$, and source and target maps $s, t \colon Q_1 \to Q_0$.
A *path* of length $m \ge 1$ is a sequence $p = \alpha_1 \alpha_2 \cdots \alpha_m$ of arrows with $t(\alpha_i) = s(\alpha_{i+1})$ for $1 \le i < m$; it has source $s(p) = s(\alpha_1)$ and target $t(p) = t(\alpha_m)$.
For each vertex $v$ there is also a path $e_v$ of length $0$ with $s(e_v) = t(e_v) = v$.
The *path algebra* $kQ$ is the [[vector space|000AYPA9AJ]] over $k$ with [[basis|0KCQ9Y3QKA]] the set of all paths.
The product of two paths $p$ and $q$ is the concatenation $pq$ if $t(p) = s(q)$ and $0$ otherwise.
Here $e_v$ acts as an identity on paths through $v$, and the product on $kQ$ is the bilinear extension.

## Remarks

The product is associative, so $kQ$ is an [[associative algebra|3CTW1P4HBP]]; it has an identity $\sum_{v \in Q_0} e_v$ when $Q_0$ is finite.
The $e_v$ are orthogonal idempotents: $e_v e_w = e_v$ if $v = w$ and $0$ otherwise.
Example: let $Q$ have vertices $1, 2$ and one arrow $\alpha \colon 1 \to 2$.
The paths are $e_1, e_2, \alpha$, and the nonzero products of basis elements are $e_1 e_1 = e_1$, $e_2 e_2 = e_2$ and $e_1 \alpha = \alpha = \alpha e_2$.
So $kQ$ has dimension $3$, and it is isomorphic to the algebra of upper triangular $2 \times 2$ matrices over $k$, via $e_1 \mapsto E_{11}$, $e_2 \mapsto E_{22}$, $\alpha \mapsto E_{12}$.
Non-example: for the quiver with one vertex and two loops $a, b$, the paths $ab$ and $ba$ are different basis elements.
So $kQ$ is the [[free algebra|2P3Y2FRCSZ]] $k\langle a, b \rangle$ and not the commutative ring $k[a, b]$.
$kQ$ is finite-dimensional if and only if $Q$ is finite and has no oriented cycles.
Some books compose paths in the opposite order, which replaces $kQ$ by its opposite algebra.
