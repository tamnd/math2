---
tag: YGR48AJMFD
kind: definition
name: Reflexive operator algebra
msc: [47L05, 47A15]
defines: 672HNBV803
uses: [HM2HHE3J51, BMDG4JQPEH, 0ACX5QT8TE]
sources:
  - url: https://en.wikipedia.org/wiki/Reflexive_operator_algebra
---

## Definition

Let $H$ be a Hilbert space and let $B(H)$ be the [[algebra of bounded operators|BMDG4JQPEH]] on $H$.
For a set $\mathcal{S} \subseteq B(H)$, let $\operatorname{Lat} \mathcal{S}$ be the set of closed subspaces of $H$ that are [[invariant|0ACX5QT8TE]] under every operator in $\mathcal{S}$.
For a set $\mathcal{L}$ of closed subspaces of $H$, let
$$\operatorname{Alg} \mathcal{L} = \set{T \in B(H) : T(L) \subseteq L \text{ for all } L \in \mathcal{L}}.$$
A subalgebra $\mathcal{A} \subseteq B(H)$ is *reflexive* if $\mathcal{A} = \operatorname{Alg} \operatorname{Lat} \mathcal{A}$.

## Remarks

Always $\mathcal{A} \subseteq \operatorname{Alg} \operatorname{Lat} \mathcal{A}$, so reflexivity is the reverse inclusion.
A reflexive algebra contains the identity and is closed in the weak operator topology, because each $\operatorname{Alg} \mathcal{L}$ has these properties.
Example: $\mathcal{A} = B(H)$ is reflexive, since $\operatorname{Lat} B(H) = \set{\set{0}, H}$ and $\operatorname{Alg} \set{\set{0}, H} = B(H)$.
Non-example: in $M_2(\C)$, let $\mathcal{A}$ be the matrices $\begin{pmatrix} a & b \\ 0 & a \end{pmatrix}$.
Its invariant subspaces are those of $\begin{pmatrix} 0 & 1 \\ 0 & 0 \end{pmatrix}$, namely $\set{0}$, $\C e_1$ and $\C^2$, so $\operatorname{Alg} \operatorname{Lat} \mathcal{A}$ is the algebra of all upper triangular matrices, which is strictly larger.
Every von Neumann algebra is reflexive: its invariant subspaces are the ranges of the projections in its commutant, and the bicommutant theorem gives the equality.
