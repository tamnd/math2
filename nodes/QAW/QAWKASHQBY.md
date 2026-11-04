---
tag: QAWKASHQBY
kind: proof
name: Proof that abelian groups are solvable
msc: [20F16]
proves: 0R0X73XHAT
uses: [071DDFVG4J, 0P3KZK0FTV, 096HN851YZ, 0W77CVBCHQ, 0YYWCNTPWR]
sources:
  - url: https://en.wikipedia.org/wiki/Solvable_group
    locator: Abelian groups
---

## Proof

1. Let $G$ be an [[abelian group|071DDFVG4J]], and let $G_0 = \{e\}$ and $G_1 = G$.
2. The subgroup $\{e\}$ is [[normal|0W77CVBCHQ]] in $G$, because $geg^{-1} = e$ for each $g \in G$.
3. So $\{e\} = G_0 \trianglelefteq G_1 = G$ is a [[subnormal series|096HN851YZ]] of $G$ of length $1$.
4. Its only factor is the [[quotient group|0YYWCNTPWR]] $G/\{e\}$. For $a, b \in G$ we have $(a\{e\})(b\{e\}) = (ab)\{e\} = (ba)\{e\} = (b\{e\})(a\{e\})$, because $G$ is abelian.
5. So the factor $G/\{e\}$ is abelian, and $G$ is [[solvable|0P3KZK0FTV]] by definition.

## Idea

The shortest possible series, from the trivial group straight to $G$, already works. Its single factor is a copy of $G$, which is abelian.
