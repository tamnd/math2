---
tag: BA2S40MM0Y
kind: statement
role: theorem
name: Margulis normal subgroup theorem
msc: ["22E40", 20F65]
uses: [XJS07AJ50Y, BTYF5Y5PFY, 0CB0DX5BVV, 0DZ93493VN, 0DTXBQPA2S]
about: [BTYF5Y5PFY]
sources:
  - url: https://en.wikipedia.org/wiki/Lattice_(discrete_subgroup)
---

## Statement

Let $G$ be a connected [[semisimple Lie group|XJS07AJ50Y]] with finite centre and no compact factors, of real rank at least $2$.
Let $\Gamma$ be an irreducible [[lattice|BTYF5Y5PFY]] in $G$.
Let $N$ be a [[normal subgroup|0CB0DX5BVV]] of $\Gamma$.
Then either $N$ is contained in the [[centre|0DZ93493VN]] of $G$, and so is finite, or $N$ has finite [[index|0DTXBQPA2S]] in $\Gamma$.

## Remarks

The proof has two halves, for a non-central $N$.
One half shows that $\Gamma/N$ is amenable, by an analysis of the measurable quotients of the boundary $G/P$, with $P$ a minimal parabolic subgroup.
The other half shows that $\Gamma/N$ has property (T) when $G$ has it; when $G$ does not, a different argument replaces this half.
A discrete group that is amenable and has property (T) is finite.

Example: $\Gamma = \mathrm{SL}_3(\Z)$.
The centre of $\mathrm{SL}_3(\R)$ is trivial, so every nontrivial normal subgroup of $\mathrm{SL}_3(\Z)$ has finite index.
The congruence subgroups, the kernels of reduction modulo $m$, are such normal subgroups.

The rank condition is necessary.
The principal congruence subgroup $\Gamma(3)$ of $\mathrm{SL}_2(\Z)$ is normal, of finite index and free of rank at least $2$.
Its commutator subgroup $N$ is characteristic in $\Gamma(3)$, so it is normal in $\mathrm{SL}_2(\Z)$.
But $N$ is infinite and has infinite index, since $\Gamma(3)/N$ is free abelian of positive rank.

## Explanations

### L1 human

A normal subgroup lets one form a quotient group.
For lattices in higher rank groups, such as $\mathrm{SL}_3(\Z)$, every quotient is either finite or almost the whole group.
So these groups are almost simple in an infinite sense: they cannot be mapped onto an infinite smaller group.

### L2 human

The theorem shows that higher rank lattices are just infinite up to the centre.
It is a strong contrast to lattices in $\mathrm{SL}_2(\R)$, which are often virtually free and have a huge supply of normal subgroups.
It works together with the [[Margulis superrigidity theorem|DSKV65NHZZ]] and the [[Margulis arithmeticity theorem|FEJK846N5X]] to describe these lattices completely.
