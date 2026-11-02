---
tag: ET9QA03J3F
kind: definition
name: Pontryagin dual
msc: [43A40, 22B05]
defines: FMW57WNPDB
uses: [ZR09S9R3AW, H1WNVN5V7F, 04EAFVFTF7, RG15F0TWPW]
sources:
  - url: https://en.wikipedia.org/wiki/Pontryagin_duality
---

## Definition

Let $G$ be a [[locally compact abelian group|ZR09S9R3AW]], and let $\mathbb{T}$ be the [[circle group|04EAFVFTF7]].
The *Pontryagin dual* of $G$ is the set $\widehat{G}$ of all continuous [[characters|H1WNVN5V7F]] $\chi \colon G \to \mathbb{T}$, with:

1. the group operation $(\chi\psi)(x) = \chi(x)\psi(x)$;
2. the [[compact-open topology|RG15F0TWPW]], that is, the topology of uniform convergence on compact subsets of $G$.

## Remarks

Example: for $G = \Z$ with the discrete topology, a character $\chi$ is fixed by $z = \chi(1) \in \mathbb{T}$, since $\chi(n) = z^n$, and each $z \in \mathbb{T}$ gives a character.
Uniform convergence on finite sets is pointwise convergence, so $\widehat{\Z} \cong \mathbb{T}$ as topological groups.
Non-example: the group of all characters of $\R$, continuous or not, is not the Pontryagin dual of $\R$.
There are discontinuous homomorphisms $\R \to \mathbb{T}$, built from a Hamel basis, and the dual excludes them.
With the compact-open topology, $\widehat{G}$ is again a locally compact abelian group.
If $G$ is compact, then $\widehat{G}$ is discrete, and if $G$ is discrete, then $\widehat{G}$ is compact.
