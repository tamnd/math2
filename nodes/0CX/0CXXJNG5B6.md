---
tag: 0CXXJNG5B6
kind: statement
role: theorem
name: First isomorphism theorem
aliases: [fundamental-theorem-on-homomorphisms]
msc: [20A05]
uses: [0GJ83E78A5, 0C9ZKYSPYR, 0112DTS464, 085PND4KNT]
sources:
  - url: https://en.wikipedia.org/wiki/Isomorphism_theorems
    locator: Theorem A (groups)
---

## Statement

Let $G$ and $H$ be [[groups|G5S1M9]] and let $\varphi \colon G \to H$ be a [[group homomorphism|0JYTG5K9Y4]].
Then the map $g \ker \varphi \mapsto \varphi(g)$ is a well-defined [[isomorphism|08MG7H8JW5]] from the [[quotient group|0KYX2N69J0]] $G / \ker \varphi$ to the [[image|0S21GNW9ZB]] $\operatorname{im} \varphi$.

## Remarks

Here $\ker \varphi$ is normal by [[this fact|0C9ZKYSPYR]], so the quotient exists.
If $\varphi$ is surjective, then $H \cong G / \ker \varphi$.
For example, the determinant gives $\mathrm{GL}_n(\mathbb{R}) / \mathrm{SL}_n(\mathbb{R}) \cong \mathbb{R}^\times$.
For finite $G$, a consequence is $|G| = |\ker \varphi| \cdot |\operatorname{im} \varphi|$.

## Explanations

### L1 human

A homomorphism collapses each coset of its kernel to one point of the image.
After this collapse, nothing else is lost: the quotient by the kernel and the image are the same group.
For example, reduction modulo $n$ shows that $\mathbb{Z}/n\mathbb{Z}$ is the image of $\mathbb{Z}$.
