---
tag: 464TFVZ9JA
kind: definition
name: Block system
msc: [20B05, 20B15]
defines: SF738NKWJ0
uses: [0WCY42EV9V, 02GK6HZYBT, 0AYMP41THN, 0YQPZB5Q1G, 0CB0DX5BVV, Y10S0751KG]
sources:
  - url: https://en.wikipedia.org/wiki/Block_(permutation_group_theory)
---

## Definition

Let a group $G$ [[act|0WCY42EV9V]] on a set $\Omega$.
A *block* of $G$ is a nonempty subset $B \subseteq \Omega$ such that, for every $g \in G$, either $gB = B$ or $gB \cap B = \emptyset$.
A *block system* of $G$ is a partition $\mathcal{P}$ of $\Omega$ such that $gB \in \mathcal{P}$ for every $g \in G$ and every part $B \in \mathcal{P}$.

## Remarks

Each part of a block system is a block.
Conversely, if $G$ is [[transitive|02GK6HZYBT]] and $B$ is a block, then $\set{gB : g \in G}$ is a block system.
For transitive $G$ all parts of a block system have the same size, so for finite $\Omega$ this size divides $\abs{\Omega}$.
The partition into singletons and the partition $\set{\Omega}$ are the *trivial* block systems.
A transitive action whose only block systems are trivial is [[primitive|Y10S0751KG]].

Example: the eight symmetries of a square acting on the corners $1, 2, 3, 4$ in cyclic order, and $\mathcal{P} = \set{\set{1, 3}, \set{2, 4}}$.
Each symmetry maps a pair of opposite corners to a pair of opposite corners, so it maps each part of $\mathcal{P}$ to a part of $\mathcal{P}$.

Non-example: for the same action, $\mathcal{P}' = \set{\set{1, 2}, \set{3, 4}}$.
The quarter turn $(1\,2\,3\,4)$ maps $\set{1, 2}$ to $\set{2, 3}$, which is not a part of $\mathcal{P}'$.

If $G$ is transitive and $\omega \in \Omega$, the blocks containing $\omega$ correspond to the subgroups $H$ with $G_\omega \le H \le G$, where $G_\omega$ is the [[stabiliser|0AYMP41THN]]: $H$ gives the block $H\omega$.
The [[orbits|0YQPZB5Q1G]] of a [[normal subgroup|0CB0DX5BVV]] of $G$ form a block system.
