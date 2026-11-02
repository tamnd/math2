---
tag: 6WB6TKE70H
kind: definition
name: Theta correspondence
msc: [11F27, "22E46", "22E50"]
defines: ZBGT50BW0Z
uses: [CCR7BAQ5N5, 8B0JM2YDE2, X12FS2JAP0, PQ7JJY0VPH, 42ZCE14AD2, FX3NEFYFFN, SZV8Y806Y7]
sources:
  - url: https://en.wikipedia.org/wiki/Theta_correspondence
---

## Definition

Let $W$ be a finite-dimensional real [[symplectic vector space|PQ7JJY0VPH]] with [[symplectic group|X12FS2JAP0]] $\mathrm{Sp}(W)$ and [[metaplectic group|8B0JM2YDE2]] $p \colon \mathrm{Mp}(W) \to \mathrm{Sp}(W)$.
A *reductive dual pair* in $\mathrm{Sp}(W)$ is a pair $(G, G')$ of [[reductive|42ZCE14AD2]] subgroups of $\mathrm{Sp}(W)$ with two properties.
The centralizer of $G'$ in $\mathrm{Sp}(W)$ is $G$, and the centralizer of $G$ is $G'$.
Let $\tilde G = p^{-1}(G)$ and $\tilde G' = p^{-1}(G')$, and let $\omega^\infty$ be the space of smooth vectors of the [[oscillator representation|CCR7BAQ5N5]] of $\mathrm{Mp}(W)$, as a representation of $\tilde G \times \tilde G'$.
Let $\mathcal R(\tilde G)$ be the set of classes of [[irreducible|FX3NEFYFFN]] [[admissible representations|SZV8Y806Y7]] $\pi$ of $\tilde G$ that occur as quotients of $\omega^\infty$.
Define $\mathcal R(\tilde G')$ in the same way.
By Howe duality, for each $\pi \in \mathcal R(\tilde G)$ there is exactly one $\pi' \in \mathcal R(\tilde G')$ such that $\pi \otimes \pi'$ is a quotient of $\omega^\infty$, and $\pi \mapsto \pi'$ is a bijection $\mathcal R(\tilde G) \to \mathcal R(\tilde G')$.
This bijection is the *theta correspondence* for the pair $(G, G')$, written $\pi' = \theta(\pi)$.

## Remarks

The theorem used in the definition is Howe's duality theorem for real groups; the same definition over $p$-adic fields rests on the work of several later authors.

Example: let $W = \R^2$, so $\mathrm{Sp}(W) = \mathrm{SL}_2(\R)$, and let $G = \set{\pm 1}$, which is the orthogonal group $\mathrm{O}(1)$.
The centralizer of $\set{\pm 1}$ is all of $\mathrm{SL}_2(\R)$, and the centralizer of $\mathrm{SL}_2(\R)$ is its center $\set{\pm 1}$, so $(\mathrm{O}(1), \mathrm{SL}_2(\R))$ is a dual pair.
In the Schrödinger model on $L^2(\R)$, the element $-1$ acts by $\psi(x) \mapsto \psi(-x)$, up to a constant depending on the lift.
So the two characters of $\mathrm{O}(1)$ correspond to the two irreducible pieces of the oscillator representation of $\mathrm{Mp}_2(\R)$, on even and on odd functions.

Non-example: in $\mathrm{SL}_2(\R)$, let $A = \set{\operatorname{diag}(a, a^{-1}) : a > 0}$.
The centralizer of $A$ is $\set{\operatorname{diag}(a, a^{-1}) : a \ne 0}$, which is larger than $A$, so $(A, A)$ is not a dual pair.

The standard dual pairs include $(\mathrm{O}(p, q), \mathrm{Sp}_{2m}(\R))$ in $\mathrm{Sp}(\R^{p+q} \otimes \R^{2m})$ and $(\mathrm{U}(p, q), \mathrm{U}(r, s))$.
