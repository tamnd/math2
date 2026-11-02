---
tag: WKJ4EP6E1X
kind: definition
name: Alexander polynomial
msc: [57K14, 57K10]
defines: JKA25KDPQP
uses: [QYEAZTYGPT, K866ND3WF7, 00KDZRW4C0]
sources:
  - url: https://en.wikipedia.org/wiki/Alexander_polynomial
---

## Definition

Let $K \subset S^3$ be an oriented tame [[knot|QYEAZTYGPT]], and let $F$ be an oriented [[Seifert surface|K866ND3WF7]] of $K$ of genus $g$.
Let $a_1, \ldots, a_{2g}$ be oriented simple closed curves on $F$ whose classes form a basis of $H_1(F; \Z)$.
For a curve $a$ on $F$, let $a^+$ be the curve $a$ pushed off $F$ slightly in the positive normal direction.
The *Seifert matrix* is the $2g \times 2g$ integer matrix $V$ with entries $V_{ij} = \operatorname{lk}(a_i, a_j^+)$, where $\operatorname{lk}$ is the linking number.
The *Alexander polynomial* of $K$ is
$$\Delta_K(t) = \det\big(V - t V^{T}\big) \in \Z[t, t^{-1}],$$
taken up to multiplication by a unit $\pm t^{k}$ with $k \in \Z$.

## Remarks

Different Seifert surfaces and bases change $\Delta_K$ only by such a unit.
The usual normalization, due to Conway, is the representative with $\Delta_K(t^{-1}) = \Delta_K(t)$ and $\Delta_K(1) = 1$.
Example: the [[trefoil knot|VYTYSVHN4A]] has a genus-one Seifert surface with $V = \begin{pmatrix} -1 & 1 \\ 0 & -1 \end{pmatrix}$.
Then $\det(V - tV^T) = (t - 1)^2 + t = t^2 - t + 1$, normalized to $t - 1 + t^{-1}$.
The [[unknot|1TQ06R4Q66]] bounds a disk with $g = 0$, so its polynomial is the empty determinant $1$.
Non-example of detection: the [[Conway knot|ZSAMVFPWN6]] is knotted but also has $\Delta = 1$, so $\Delta_K = 1$ does not imply that $K$ is the unknot.
The [[figure-eight knot|C01XBGAHC6]] has $\Delta = -t + 3 - t^{-1}$.
The degree span of $\Delta_K$ is at most $2g(K)$.
