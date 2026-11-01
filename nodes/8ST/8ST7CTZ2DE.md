---
tag: 8ST7CTZ2DE
kind: definition
name: Residue field
msc: [13H99, 13B30]
defines: NJ3APQ8BHH
uses: [MZ02BKPHJA, 0076HWHGHQ, 04C5ZBG1WT, X6JD4AG973]
sources:
  - url: https://en.wikipedia.org/wiki/Residue_field
---

## Definition

Let $(R, \mathfrak m)$ be a [[local ring|MZ02BKPHJA]].
The *residue field* of $R$ is the [[quotient ring|0076HWHGHQ]] $k = R/\mathfrak m$.
It is a [[field|04C5ZBG1WT]] because $\mathfrak m$ is a [[maximal ideal|0PV74TR5FP]].

Let $R$ be a [[commutative ring|0310REJJY8]] and $\mathfrak p$ a [[prime ideal|00MHHZ9SNE]].
The *residue field of $R$ at $\mathfrak p$* is the residue field
$$\kappa(\mathfrak p) = R_{\mathfrak p} / \mathfrak p R_{\mathfrak p}$$
of the [[localization|X6JD4AG973]] of $R$ at $\mathfrak p$.

## Remarks

The field $\kappa(\mathfrak p)$ is isomorphic to the [[field of fractions|0F2PTGX1A2]] of the [[integral domain|0QVD7WBFGN]] $R/\mathfrak p$.

Example: the residue field of $\Z_{(p)}$ is $\Z/p\Z$, since $a/b \mapsto a b^{-1} \bmod p$ is a surjection with kernel $p\Z_{(p)}$.
The residue field of $k[\![x]\!]$ is $k$, by taking the constant term.
For $R = \Z$, the residue field at $(0)$ is $\Q$ and the residue field at $p\Z$ is $\Z/p\Z$.

Non-example: in the local ring $\Z_{(p)}$, the quotient $\Z_{(p)}/p^2\Z_{(p)} \cong \Z/p^2\Z$ is not a field, because $p \ne 0$ there and $p \cdot p = 0$.
Only the quotient by the maximal ideal is a field.
