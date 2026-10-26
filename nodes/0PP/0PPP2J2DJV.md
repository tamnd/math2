---
tag: 0PPP2J2DJV
kind: statement
role: theorem
name: Second isomorphism theorem
aliases: [diamond-isomorphism-theorem]
msc: [20A05]
uses: [0CXXJNG5B6, 0TXWV1JGG1, 0YYWCNTPWR]
sources:
  - url: https://en.wikipedia.org/wiki/Isomorphism_theorems
    locator: Theorem B (groups)
---

## Statement

Let $G$ be a [[group|G5S1M9]], let $S$ be a [[subgroup|0X1JXT47GA]] of $G$, and let $N$ be a [[normal subgroup|0CB0DX5BVV]] of $G$.
Then $SN$ is a subgroup of $G$, $N$ is normal in $SN$, and $S \cap N$ is normal in $S$.
Moreover, the map $s(S \cap N) \mapsto sN$ is an [[isomorphism|08MG7H8JW5]] from $S/(S \cap N)$ to $SN/N$.

## Remarks

The proof applies the [[first isomorphism theorem|0CXXJNG5B6]] to the homomorphism $S \to SN/N$, $s \mapsto sN$, which is surjective with kernel $S \cap N$.
For finite groups, it gives $|SN| = |S| \, |N| / |S \cap N|$.
It is enough that $S$ normalizes $N$, that is, $sNs^{-1} = N$ for each $s \in S$.

## Explanations

### L1 human

Picture a diamond with $SN$ at the top, $S$ and $N$ in the middle, and $S \cap N$ at the bottom.
The theorem says that the two slanted sides opposite each other give the same quotient group.
For integers, with $S = 4\mathbb{Z}$ and $N = 6\mathbb{Z}$, it gives $4\mathbb{Z}/12\mathbb{Z} \cong 2\mathbb{Z}/6\mathbb{Z}$, both cyclic of order $3$.
