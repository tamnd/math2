---
tag: VNJ4V7FYBV
kind: definition
name: Irreducible representation
msc: [20C15]
defines: FX3NEFYFFN
uses: [WYGRXCG2RN, 0ACX5QT8TE, 000AYPA9AJ, MNP2HBWB5Q]
sources:
  - url: https://en.wikipedia.org/wiki/Irreducible_representation
---

## Definition

Let $G$ be a group, let $F$ be a field, and let $\rho \colon G \to GL(V)$ be a [[representation|WYGRXCG2RN]] of $G$ on a [[vector space|000AYPA9AJ]] $V$ over $F$.
A subspace $W \subseteq V$ is $G$-invariant if $\rho(g)(W) \subseteq W$ for all $g \in G$.
The representation $\rho$ is *irreducible* if $V \ne 0$ and the only $G$-invariant subspaces of $V$ are $0$ and $V$.

## Remarks

Example: let $G = \Z/4\Z$ act on $\R^2$, with the class of $1$ acting as the rotation $R$ by $90$ degrees.
A $G$-invariant line would be spanned by an eigenvector of $R$, but $R$ has characteristic polynomial $x^2 + 1$ with no real root.
So the only invariant subspaces are $0$ and $\R^2$, and the representation is irreducible.
Non-example: let $G = \Z$ act on $\C^2$, with $n$ acting by the matrix $\begin{pmatrix} 1 & n \\ 0 & 1 \end{pmatrix}$.
The line spanned by $(1, 0)$ is invariant, so the representation is not irreducible.
It is also not a direct sum of irreducible representations, because this line has no invariant complement.
Over $\C$, the same rotation representation of $\Z/4\Z$ on $\C^2$ is not irreducible: it splits into the eigenlines for $i$ and $-i$.
So irreducibility depends on the field.
An irreducible representation is also called simple, since it is the same as a simple module over the [[group algebra|MNP2HBWB5Q]].
