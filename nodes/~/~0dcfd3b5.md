---
tag: ~0dcfd3b5
kind: statement
role: theorem
name: Correspondence theorem
aliases: [lattice-theorem, fourth-isomorphism-theorem]
msc: [20A05]
uses: [~7fdf454c, ~4f5a4072, ~011306f8]
sources:
  - url: https://en.wikipedia.org/wiki/Correspondence_theorem
    locator: lead section
  - url: https://en.wikipedia.org/wiki/Isomorphism_theorems
    locator: Theorem D (groups)
same_as:
  wikidata: Q3527189
  wikipedia: Correspondence theorem
---

## Statement

Let $G$ be a [[group|G5S1M9]] and let $N$ be a [[normal subgroup|~ebf813cb]] of $G$.
Then the map $K \mapsto K/N$ is a bijection from the set of [[subgroups|~b600248b]] $K$ of $G$ with $N \subseteq K$ to the set of all subgroups of $G/N$. Here $G/N$ is the [[quotient group|~592bfb26]].
Let $K$ and $L$ be subgroups of $G$ that contain $N$. Then $K \subseteq L$ if and only if $K/N \subseteq L/N$. Also, $K$ is normal in $G$ if and only if $K/N$ is normal in $G/N$.

## Remarks

The inverse map sends a subgroup $\bar{K}$ of $G/N$ to its preimage $\{g \in G : gN \in \bar{K}\}$.
The bijection is an isomorphism of [[lattices of subgroups|~011306f8]], and it keeps indices: $[L : K] = [L/N : K/N]$ when $N \subseteq K \subseteq L$.
For example, the subgroups of $\mathbb{Z}/12\mathbb{Z}$ correspond to the subgroups $d\mathbb{Z}$ of $\mathbb{Z}$ with $d$ dividing $12$.

## Explanations

### L1 human

The subgroups of a quotient group $G/N$ are the same as the subgroups of $G$ that contain $N$.
Passing to the quotient does not create new subgroups or lose old ones above $N$.
So the picture of the subgroups above $N$ in $G$ is the full picture of the subgroups of $G/N$.
