---
tag: 0CXXJNG5B6
kind: statement
role: theorem
name: First isomorphism theorem
aliases: [fundamental-theorem-on-homomorphisms]
msc: [20A05]
about: [0KYX2N69J0, 08MG7H8JW5, 0S21GNW9ZB, 0W88CEGQP1]
uses: [0GJ83E78A5, 0C9ZKYSPYR, 0112DTS464, 085PND4KNT]
formal:
  - system: lean4
    library: mathlib
    decl: QuotientGroup.quotientKerEquivRange
    match: variant
    adapter: Math2.Match.first_iso
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

### L2 agent

The first isomorphism theorem says what a homomorphism forgets. It identifies the elements in each coset of the kernel, and it forgets nothing else.

The proof builds the isomorphism directly. Let $K = \ker\varphi$.

1. Define $\psi(gK) = \varphi(g)$. This is well defined, because $gK = hK$ gives $g^{-1}h \in K$ and thus $\varphi(g) = \varphi(h)$.
2. $\psi$ is a homomorphism, because $\psi(gK\,hK) = \varphi(gh) = \varphi(g)\varphi(h)$.
3. $\psi$ is onto $\operatorname{im}\varphi$ by construction.
4. $\psi$ is injective, because its kernel is the single coset $K$.

A worked example with $\varphi : \mathbb{Z} \to \mathbb{C}^\times$, $\varphi(n) = i^n$:

1. The image is $\{1, i, -1, -i\}$, a cyclic group of order $4$.
2. $i^n = 1$ exactly when $4$ divides $n$. Thus the kernel is $4\mathbb{Z}$.
3. By the theorem, $\mathbb{Z}/4\mathbb{Z} \cong \{1, i, -1, -i\}$.

Other standard examples are $\mathrm{GL}_n(\mathbb{R})/\mathrm{SL}_n(\mathbb{R}) \cong \mathbb{R}^\times$ through the determinant, and $S_n/A_n \cong \{1, -1\}$ through the sign.

For a finite group, the theorem gives $|G| = |\ker\varphi| \cdot |\operatorname{im}\varphi|$. This often bounds the image of a homomorphism without any computation.

A common error is to write $G/\ker\varphi \cong H$. This is true only when $\varphi$ is onto. In general the quotient is isomorphic to the image, which can be a proper subgroup of $H$.
