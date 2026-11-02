---
tag: CTYQQWJPMB
kind: statement
role: theorem
name: Mackey imprimitivity theorem
msc: [22D30, 22D10]
uses: [AHV05ZBCYW, 74BPYJNZTM, 6Q7AHAZ6Q4, ATGT25E5FF, HM2HHE3J51]
about: [6Q7AHAZ6Q4]
sources:
  - url: https://en.wikipedia.org/wiki/System_of_imprimitivity
---

## Statement

Let $G$ be a second countable [[locally compact group|AHV05ZBCYW]], and let $H$ be a closed subgroup of $G$.
Let $\pi$ be a [[unitary representation|74BPYJNZTM]] of $G$ on a [[Hilbert space|HM2HHE3J51]] $\mathcal{H}$.
A *system of imprimitivity* for $\pi$ based on $G/H$ is a [[projection-valued measure|ATGT25E5FF]] $P$ on the Borel sets of $G/H$, acting on $\mathcal{H}$.
It must satisfy
$$\pi(g) P(E) \pi(g)^{-1} = P(gE)$$
for all $g \in G$ and all Borel sets $E \subseteq G/H$.
Every [[induced representation|6Q7AHAZ6Q4]] $\operatorname{Ind}_H^G \sigma$ has a canonical system of imprimitivity, where $P(E)$ multiplies a function by the indicator of $E$.
Let $(\pi, P)$ be any system of imprimitivity based on $G/H$.
Then there is a unitary representation $\sigma$ of $H$ such that $(\pi, P)$ is unitarily equivalent to the canonical system of $\operatorname{Ind}_H^G \sigma$.
The representation $\sigma$ is unique up to unitary equivalence.

## Remarks

In operator-algebra terms, a system of imprimitivity is a covariant representation of the action of $G$ on $C_0(G/H)$.
Such pairs correspond to representations of the crossed product $C_0(G/H) \rtimes G$.
This crossed product is Morita equivalent to the group $C^*$-algebra of $H$, and this equivalence gives one modern proof.

Example: take $G = \R$ and $H = \set{0}$, so $G/H = \R$.
A system of imprimitivity is a unitary group $\pi(t)$ together with a self-adjoint operator $Q$, through the spectral measure $P$ of $Q$.
The covariance condition is the Weyl form of the canonical commutation relation.
The theorem says that every such pair is a multiple of translations and multiplication by $x$ on $L^2(\R)$.
This is the [[Stone–von Neumann theorem|Z877XDBMQ3]].

The theorem also gives a criterion for being induced: $\pi$ is induced from $H$ exactly when it admits a system of imprimitivity based on $G/H$.

## Explanations

### L1 human

Some representations come with a way of cutting the space into pieces labelled by points of $G/H$, and $G$ permutes the pieces.
The theorem says that this extra structure is exactly what induced representations have.
So to recognise an induced representation, one only has to find such a compatible way of cutting the space.
In quantum mechanics, the pieces are the positions of a particle, and the group moves the positions.

### L2 human

The imprimitivity theorem is the engine of the [[Mackey machine|12CEWPMSG4]].
If $N$ is a closed abelian normal subgroup, the spectral measure of $\pi|_N$ lives on the dual $\widehat{N}$, and $G$ permutes it.
When $\pi$ is irreducible and the action is regular, this measure sits on one orbit $G/G_\chi$, and the theorem shows that $\pi$ is induced from the stabiliser $G_\chi$.
Wigner's classification of the particles through representations of the Poincaré group is an instance.
