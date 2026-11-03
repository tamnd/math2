---
tag: 7KNNFSJDZQ
kind: definition
name: Wall's finiteness obstruction
msc: [19J05, "57Q10"]
defines: 6DNJDT9AMH
uses: [5W95QFHXPR, S1XK3HXHFX, Y1YPE6PM52, 4NMTSX0XDS, WQ82C0M3QB, 4EBHAWJJ8C, HQA9YHDSH5, GBJ1S3M5QV, F2F143KQ2M]
sources:
  - url: https://en.wikipedia.org/wiki/Wall%27s_finiteness_obstruction
---

## Definition

Let $X$ be a connected [[CW complex|5W95QFHXPR]] with [[fundamental group|S1XK3HXHFX]] $\pi$.
Assume $X$ is *finitely dominated*: there are a finite CW complex $K$ and maps $i \colon X \to K$ and $r \colon K \to X$ with $r \circ i$ [[homotopic|F2F143KQ2M]] to the identity of $X$.
Consider the cellular [[chain complex|WQ82C0M3QB]] $C_*(\tilde X)$ of the [[universal cover|Y1YPE6PM52]], a complex of free modules over the [[group ring|4NMTSX0XDS]] $\Z[\pi]$.
It is [[chain homotopy|4EBHAWJJ8C]] equivalent to a complex $P_*$ with only finitely many nonzero terms.
Each $P_i$ is a [[finitely generated projective|HQA9YHDSH5]] $\Z[\pi]$-module.
*Wall's finiteness obstruction* of $X$ is
$$\sigma(X) = \sum_i (-1)^i [P_i] \in \tilde K_0(\Z[\pi]),$$
the class in the [[reduced K0|GBJ1S3M5QV]] of the alternating sum.
It does not depend on the choice of $P_*$.

## Remarks

Example: if $X$ is itself a finite CW complex, one can take $P_* = C_*(\tilde X)$, which consists of finitely generated free modules, so $\sigma(X) = 0$.
Non-example: an infinite wedge of circles is not finitely dominated, since its first homology is not finitely generated, so it has no finiteness obstruction.
Wall's theorem says that $\sigma(X) = 0$ if and only if $X$ is homotopy equivalent to a finite CW complex.
Some authors define the unreduced class in $K_0(\Z[\pi])$; its image in $\tilde K_0(\Z[\pi])$ is the obstruction above.
