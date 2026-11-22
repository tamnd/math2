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

Over a finite field, the dimension of a space fixes how many vectors and how many ordered bases it has.
Let $q$ be a prime power, let $\mathbb{F}_q$ be the field with $q$ elements, and let $V$ be a vector space over $\mathbb{F}_q$ of finite [[dimension|05G2G0P224]] $n$.
Then:

1. $V$ has exactly $q^n$ elements;
2. $V$ has exactly $\prod_{i = 0}^{n - 1} (q^n - q^i) = (q^n - 1)(q^n - q) \cdots (q^n - q^{n - 1})$ ordered [[bases|0VTQTPQGAV]].

## Remarks

### A first count

For $\mathbb{F}_2^2$, with $q = 2$ and $n = 2$, part 1 gives $4$ vectors and part 2 gives
$$(4 - 1)(4 - 2) = 3 \cdot 2 = 6$$
ordered bases, which the [[example of finite spaces|J9VE1X14PV]] lists one by one.
For $\mathbb{F}_2^3$ the counts are $8$ vectors and $7 \cdot 6 \cdot 4 = 168$ ordered bases.
Each factor $q^n - q^i$ counts the choices for the next basis vector: all $q^n$ vectors, minus the $q^i$ vectors in the span of the $i$ vectors already chosen.

### Why each hypothesis is needed

The field must be finite, since over $\mathbb{R}$ a single line already has infinitely many vectors.
The dimension must be finite, since $\mathbb{F}_2[x]$ is an infinite space over the finite field $\mathbb{F}_2$.
The case $n = 0$ is allowed and fits the formulas: the zero space has $q^0 = 1$ vector, and the empty product $1$ counts its one ordered basis, the empty family.

### What it gives you

The size of a finite vector space over $\mathbb{F}_q$ is a power of $q$, so, for example, no vector space over $\mathbb{F}_2$ has $6$ elements.
Applied to a finite field $K$ as a space over its prime subfield $\mathbb{F}_p$, part 1 shows that $|K| = p^n$ for some $n$.

The columns of an invertible $n \times n$ matrix form an ordered basis of $\mathbb{F}_q^n$, and every ordered basis arises from exactly one such matrix.
So part 2 is also the [[order of the general linear group|0JQ1KNQW2K]] $\mathrm{GL}_n(\mathbb{F}_q)$.
For $n = 2$ and $q = 3$ that order is $(9 - 1)(9 - 3) = 48$.
Since the $n$ vectors of a basis are distinct, each basis taken as a set gives $n!$ ordered bases, and so the number of bases as sets is the product divided by $n!$.

### The converse

If a space over $\mathbb{F}_q$ has $q^n$ elements, then its dimension is $n$.
The space is finite, so it is finite-dimensional, say of dimension $m$, and part 1 gives $q^m = q^n$, so $m = n$ because $q \ge 2$.

### Generalizations

The same choice argument counts the subspaces of dimension $k$ in $\mathbb{F}_q^n$: divide the number of independent ordered $k$-tuples by the number of ordered bases of one $k$-dimensional space.
The result is the [[Gaussian binomial coefficient|YS09Z1YNEK]], which belongs to enumerative combinatorics.

## Explanations

### L1 human

A vector in $\mathbb{F}_q^n$ is a list of $n$ entries, and each entry has $q$ possible values, so there are $q^n$ vectors.
To build a basis, choose the vectors one at a time, each one outside the span of the earlier ones.
For the plane over the field with two elements, that is $3$ choices and then $2$ choices, so $6$ ordered bases.

### L2 human

We count the ordered bases of $\mathbb{F}_5^2$.
There are $5^2 = 25$ vectors, so the first vector has $25 - 1 = 24$ choices.
The first vector spans a line with $5$ points, so the second vector has $25 - 5 = 20$ choices.
So there are $24 \cdot 20 = 480$ ordered bases, and $|\mathrm{GL}_2(\mathbb{F}_5)| = 480$.
Each basis as a set gives $2! = 2$ ordered bases, so there are $240$ unordered bases.
The typical use is in group theory and coding theory, where such counts give the orders of matrix groups and the numbers of codes.
Watch out: the second factor is $q^n - q$, not $q^n - 2$, because the line spanned by the first vector has $q$ points, not $2$.

### L3 human

The formula is the orbit count for the action of $\mathrm{GL}_n(\mathbb{F}_q)$ on ordered bases, which is free and transitive.
Dividing the order by the order of the stabilizer of a subspace or of a flag gives the $q$-analogues of binomial coefficients and factorials.
For example, the lines of $\mathbb{F}_q^2$ number $(q^2 - 1)(q^2 - q) / \bigl((q - 1)^2 q\bigr) = q + 1$, and this tends to $2 = 2!$ as $q \to 1$.
The sub-area on [[invertible matrices|0FCHE902D7]] returns to $\mathrm{GL}_n(\mathbb{F}_q)$ as a group.
