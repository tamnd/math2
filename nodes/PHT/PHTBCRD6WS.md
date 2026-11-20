---
tag: PHTBCRD6WS
kind: statement
role: proposition
name: Number of vectors and of ordered bases over a finite field
msc: ["15A03", "05A10"]
topics: [MVH97H8B2J]
audience: ug1
about: [03GSZ8RTZJ]
uses: [05G2G0P224, 0VTQTPQGAV]
proofs: [ESTJN487JS]
sources:
  - url: https://en.wikipedia.org/wiki/General_linear_group
    locator: Over finite fields
  - book: isbn:9780387728285
    locator: Chapter 1
---

## Statement

Let $q$ be a prime power, let $\mathbb{F}_q$ be the field with $q$ elements, and let $V$ be a vector space over $\mathbb{F}_q$ of finite [[dimension|05G2G0P224]] $n$.

1. $V$ has exactly $q^n$ elements.
2. $V$ has exactly $(q^n - 1)(q^n - q) \cdots (q^n - q^{n - 1}) = \prod_{i = 0}^{n - 1} (q^n - q^i)$ ordered [[bases|0VTQTPQGAV]].

## Remarks

### Why each hypothesis is needed

The field must be finite: over $\R$, a line already has infinitely many vectors.
The dimension must be finite: $\mathbb{F}_2[x]$ is infinite, although $\mathbb{F}_2$ is finite.
For $n = 0$, the formulas give $q^0 = 1$ vector and the empty product $1$, for the one ordered basis, the empty family.

### Consequences

1. The size of a finite vector space over $\mathbb{F}_q$ is a power of $q$; so no vector space over $\mathbb{F}_2$ has $6$ elements.
2. A finite field $K$ with prime subfield $\mathbb{F}_p$ is a vector space over $\mathbb{F}_p$, so $\abs{K} = p^n$ for some $n$.
3. The number of ordered bases of $\mathbb{F}_q^n$ equals the [[order of the general linear group|0JQ1KNQW2K]] $\mathrm{GL}_n(\mathbb{F}_q)$, because the columns of an invertible matrix form an ordered basis.
4. The $n$ vectors of a basis are distinct, so each basis as a set gives $n!$ ordered bases.
   So there are $\frac{1}{n!} \prod_{i = 0}^{n - 1} (q^n - q^i)$ bases as sets.

### Converse

If $V$ is finite with $q^n$ elements, then $\dim V = n$, because the map $n \mapsto q^n$ is injective for $q \ge 2$.

### Generalizations

The number of subspaces of dimension $k$ is the [[Gaussian binomial coefficient|YS09Z1YNEK]], which belongs to enumerative combinatorics.

## Explanations

### L1 human

A vector in $\mathbb{F}_q^n$ is a list of $n$ entries, each with $q$ choices, so there are $q^n$ vectors.
To build a basis, choose the vectors one at a time, each outside the span of the earlier ones.

### L2 human

Example: $\mathbb{F}_3^2$ has $3^2 = 9$ vectors.
The first basis vector has $9 - 1 = 8$ choices, and the second has $9 - 3 = 6$ choices, because the span of the first vector has $3$ elements.
So $\mathbb{F}_3^2$ has $8 \cdot 6 = 48$ ordered bases.
