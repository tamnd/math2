---
tag: SREW4HZRM4
kind: definition
name: Weak homotopy equivalence
msc: [55P10, 55Q05]
defines: 4Q3WY1RX91
uses: [P976WYEFMB, 0VGFHTM75Y]
sources:
  - url: https://en.wikipedia.org/wiki/Weak_equivalence_(homotopy_theory)
---

## Definition

Let $X$ and $Y$ be topological spaces, and let $f \colon X \to Y$ be a [[continuous map|0VGFHTM75Y]].
The map $f$ is a *weak homotopy equivalence* if both of the following hold:

1. $f$ induces a bijection $\pi_0(X) \to \pi_0(Y)$ between the sets of path components;
2. for every $x \in X$ and every $n \ge 1$, the induced map $f_* \colon \pi_n(X, x) \to \pi_n(Y, f(x))$ of [[homotopy groups|P976WYEFMB]] is an isomorphism.

## Remarks

Example: every homotopy equivalence $f$ with homotopy inverse $g$ is a weak homotopy equivalence, since $g_*$ inverts $f_*$ up to the change-of-base-point isomorphisms along the homotopies.

Example: all homotopy groups of the [[Warsaw circle|17VG475BRV]] are trivial, so the map from it to a point is a weak homotopy equivalence.
This map is not a homotopy equivalence.

Non-example: the inclusion $S^1 \hookrightarrow D^2$ of the boundary circle into the disk is a bijection on $\pi_0$.
It fails clause 2, because $\pi_1(S^1) \cong \Z$ while $\pi_1(D^2)$ is trivial.

Weak homotopy equivalences induce isomorphisms on singular homology and cohomology.
A weak homotopy equivalence is also called a weak equivalence.
