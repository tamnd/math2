---
tag: 0S9ZVZ34MD
kind: statement
role: theorem
name: Correspondence theorem
aliases: [lattice-theorem, fourth-isomorphism-theorem]
msc: [20A05]
uses: [0YYWCNTPWR, 0W77CVBCHQ, 0B8BW4YWTF]
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

Let $G$ be a [[group|G5S1M9]] and let $N$ be a [[normal subgroup|0CB0DX5BVV]] of $G$.
Then the map $K \mapsto K/N$ is a bijection from the set of [[subgroups|0X1JXT47GA]] $K$ of $G$ with $N \subseteq K$ to the set of all subgroups of $G/N$. Here $G/N$ is the [[quotient group|0KYX2N69J0]].
Let $K$ and $L$ be subgroups of $G$ that contain $N$. Then $K \subseteq L$ if and only if $K/N \subseteq L/N$. Also, $K$ is normal in $G$ if and only if $K/N$ is normal in $G/N$.

## Remarks

The inverse map sends a subgroup $\bar{K}$ of $G/N$ to its preimage $\{g \in G : gN \in \bar{K}\}$.
The bijection is an isomorphism of [[lattices of subgroups|0B8BW4YWTF]], and it keeps indices: $[L : K] = [L/N : K/N]$ when $N \subseteq K \subseteq L$.
For example, the subgroups of $\mathbb{Z}/12\mathbb{Z}$ correspond to the subgroups $d\mathbb{Z}$ of $\mathbb{Z}$ with $d$ dividing $12$.

## Explanations

### L1 human

The subgroups of a quotient group $G/N$ are the same as the subgroups of $G$ that contain $N$.
Passing to the quotient does not create new subgroups or lose old ones above $N$.
So the picture of the subgroups above $N$ in $G$ is the full picture of the subgroups of $G/N$.
