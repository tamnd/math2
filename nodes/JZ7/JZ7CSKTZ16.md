---
tag: JZ7CSKTZ16
kind: definition
name: Group extension
msc: ["20E22", 20J06]
defines: MF4N3VGGFV
uses: [G5S1M9, 0JYTG5K9Y4, 09NWETVTNY, 0S21GNW9ZB, 0H3WZXCZNF, 0DZ93493VN]
sources:
  - url: https://en.wikipedia.org/wiki/Group_extension
---

## Definition

Let $N$ and $Q$ be [[groups|G5S1M9]].
An *extension* of $Q$ by $N$ is a group $G$ together with two [[group homomorphisms|0JYTG5K9Y4]] $\iota \colon N \to G$ and $\pi \colon G \to Q$ such that:

1. $\iota$ is [[injective|09NWETVTNY]].
2. $\pi$ is surjective.
3. The [[image|0S21GNW9ZB]] of $\iota$ equals the kernel of $\pi$.

In other words, $1 \to N \xrightarrow{\iota} G \xrightarrow{\pi} Q \to 1$ is a short exact sequence of groups.
The extension is *split* if there is a homomorphism $s \colon Q \to G$ with $\pi \circ s = \id_Q$.
The extension is *central* if $\iota(N)$ lies in the [[centre|0DZ93493VN]] of $G$.

## Remarks

In an extension, $\iota(N)$ is a normal subgroup of $G$ and $G / \iota(N) \cong Q$.
Some authors call the same object an extension of $N$ by $Q$, so the order of the words varies between books.

Example: $G = S_3$, $N = A_3$ with the inclusion $\iota$, and $Q = \set{\pm 1}$ with $\pi$ the sign map.
The inclusion is injective, the sign map is onto, and the kernel of the sign map is $A_3$.
The extension is split: $s(-1) = (1\ 2)$ is a homomorphism with $\pi \circ s = \id$.

Non-example: $\iota \colon \Z \to \Z$, $n \mapsto 4n$, and $\pi \colon \Z \to \Z/2\Z$, reduction modulo $2$.
Clauses 1 and 2 hold, but the image $4\Z$ of $\iota$ is not the kernel $2\Z$ of $\pi$, so clause 3 fails.

The extension $0 \to 2\Z/4\Z \to \Z/4\Z \to \Z/2\Z \to 0$ does not split, because the only element of order $2$ in $\Z/4\Z$ lies in $2\Z/4\Z$.
A split extension is the same as a [[semidirect product|0H3WZXCZNF]] $N \rtimes Q$.
When $N$ is abelian, the extensions of $Q$ by $N$ that induce a given action of $Q$ on $N$ are classified up to equivalence by the second cohomology group $H^2(Q, N)$.
