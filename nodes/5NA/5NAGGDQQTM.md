---
tag: 5NAGGDQQTM
kind: definition
name: Residue field of a point
msc: [14A15]
defines: G51E8MW7J1
uses: [5A35TYZD02, JTAKAPTT8H, NJ3APQ8BHH, MZ02BKPHJA]
sources:
  - url: https://en.wikipedia.org/wiki/Residue_field
---

## Definition

Let $X$ be a [[scheme|5A35TYZD02]] and let $x \in X$.
The [[stalk|JTAKAPTT8H]] $\mathcal{O}_{X,x}$ is a [[local ring|MZ02BKPHJA]]; let $\mathfrak{m}_x$ be its maximal ideal.
The *residue field* of $X$ at $x$ is the field
$$\kappa(x) = \mathcal{O}_{X,x} / \mathfrak{m}_x.$$
For an open set $U \ni x$ and $s \in \mathcal{O}_X(U)$, the *value* $s(x)$ is the image of $s$ in $\kappa(x)$.

## Remarks

Example: for $X = \operatorname{Spec} A$ and a prime ideal $\mathfrak{p}$ of $A$, the residue field is $\kappa(\mathfrak{p}) = A_{\mathfrak p} / \mathfrak{p} A_{\mathfrak p}$.
It is isomorphic to the field of fractions of $A / \mathfrak{p}$.
For $A = \Z$ this gives $\kappa((p)) = \F_p$ for a prime $p$ and $\kappa((0)) = \Q$.
For $A = \R[x]$ and $\mathfrak{p} = (x^2 + 1)$ it gives $\R[x]/(x^2+1) \cong \C$, so this point has residue field larger than $\R$.
Non-example: the stalk $\mathcal{O}_{X,x}$ itself is in general not a field; for $\Z$ at $(p)$ it is $\Z_{(p)}$, which has the non-unit $p \ne 0$.
For a field $K$, morphisms $\operatorname{Spec} K \to X$ correspond to pairs of a point $x \in X$ and a field embedding $\kappa(x) \to K$.
