---
tag: XXZTMNBYFZ
kind: definition
name: Knot concordance
msc: [57K10, 57K40]
defines: 1C28287S75
uses: [QYEAZTYGPT, P68G28E4AD, AGZSZW7GYE]
sources:
  - url: https://en.wikipedia.org/wiki/Slice_knot
---

## Definition

Let $K_0$ and $K_1$ be oriented tame [[knots|QYEAZTYGPT]] in $S^3$.
They are *concordant* if there is a smoothly and properly embedded annulus $A \cong S^1 \times [0, 1]$ in $S^3 \times [0, 1]$ such that $\partial A = (K_0 \times \set{0}) \cup (K_1 \times \set{1})$.
The orientation of $A$ must induce the given orientation on $K_0$ and the opposite one on $K_1$.
A *concordance class* is an equivalence class under this relation.

## Remarks

Isotopic knots are concordant, since the trace of an isotopy is a concordance.
A knot is concordant to the [[unknot|1TQ06R4Q66]] if and only if it is [[slice|P68G28E4AD]].
The concordance classes form an abelian group $\mathcal{C}$ under [[knot sum|AGZSZW7GYE]], with the class of the unknot as zero.
The inverse of $K$ is $K^*$, the mirror image of $K$ with reversed orientation.
Example: $K \# K^*$ is slice, so it is concordant to the unknot.
Non-example: the [[trefoil knot|VYTYSVHN4A]] is not concordant to the unknot, since its signature is nonzero.
Signature is additive under knot sum, so the trefoil has infinite order in $\mathcal{C}$.
