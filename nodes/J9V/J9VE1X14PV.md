---
tag: J9VE1X14PV
kind: example
name: Vector spaces over finite fields
msc: ["15A03"]
topics: [MVH97H8B2J]
audience: ug1
instance_of: [000AYPA9AJ]
uses: [05EGHEQZAW, 0VTQTPQGAV, PHTBCRD6WS]
sources:
  - url: https://en.wikipedia.org/wiki/Vector_space
    locator: Examples
  - url: https://en.wikipedia.org/wiki/General_linear_group
    locator: Over finite fields
---

## Example

Let $\mathbb{F}_2 = \{0, 1\}$ be the field with two elements, in which $1 + 1 = 0$, and let $V = \mathbb{F}_2^2$.
The space has $2^2 = 4$ vectors, namely $(0, 0)$, $(1, 0)$, $(0, 1)$ and $(1, 1)$.
Addition and scalar multiplication act entry by entry, with arithmetic modulo $2$.
We check the [[vector space axioms|05EGHEQZAW]] on explicit vectors, and then we count the bases.

1. Addition is commutative and associative, because it is so in each entry modulo $2$; for example $(1, 0) + (1, 1) = (0, 1) = (1, 1) + (1, 0)$.
2. The zero vector is $(0, 0)$, since adding it changes no entry.
3. Each vector is its own negative: $(1, 1) + (1, 1) = (1 + 1, 1 + 1) = (0, 0)$.
4. The scalar $1$ acts as the identity, and the scalar $0$ sends every vector to $(0, 0)$, so axioms 5 and 6 hold.
5. Both distributive laws hold entry by entry; for example $(1 + 1) \cdot (1, 1) = 0 \cdot (1, 1) = (0, 0)$, and $(1, 1) + (1, 1) = (0, 0)$.

Now the ordered [[bases|0VTQTPQGAV]].
The span of a nonzero vector $v$ is $\{0, v\}$, because the only scalars are $0$ and $1$.
So a pair $(v_1, v_2)$ is a basis exactly when $v_1 \ne 0$ and $v_2 \notin \{0, v_1\}$.

6. The first vector is one of the $3$ nonzero vectors.
7. The second vector is one of the $4 - 2 = 2$ vectors outside $\{0, v_1\}$.
8. So there are $3 \cdot 2 = 6$ ordered bases:
$$((1,0),(0,1)), \ ((0,1),(1,0)), \ ((1,0),(1,1)), \ ((1,1),(1,0)), \ ((0,1),(1,1)), \ ((1,1),(0,1)).$$

This agrees with the formula $(q^n - 1)(q^n - q) = (4 - 1)(4 - 2) = 6$ of [[the counting statement|PHTBCRD6WS]].

## Remarks

### Larger spaces and subspaces

In $\mathbb{F}_2^3$ there are $2^3 = 8$ vectors, and the same choice argument gives $(8 - 1)(8 - 2)(8 - 4) = 7 \cdot 6 \cdot 4 = 168$ ordered bases.
Subspaces can be counted the same way.
There are $(8 - 1)(8 - 2) = 42$ independent ordered pairs in $\mathbb{F}_2^3$, and each spans a plane through $0$.
Each plane contains $(4 - 1)(4 - 2) = 6$ of these pairs, its own ordered bases, so there are $42 / 6 = 7$ planes.
Each line is the span of one of the $7$ nonzero vectors, so there are also $7$ lines.
These numbers are values of the [[Gaussian binomial coefficient|YS09Z1YNEK]], which combinatorics studies in its own right.

### What the size tells you

A space of dimension $n$ over $\mathbb{F}_q$ has $q^n$ elements, so its size is a power of $q$.
In particular no vector space over $\mathbb{F}_2$ has $6$ elements.
A finite field is itself an example: $\mathbb{F}_4$ is a space of dimension $2$ over $\mathbb{F}_2$, with basis $1, \omega$, where $\omega^2 = \omega + 1$.

### What it is not

The group $\mathbb{Z}/4$, with the scalars of $\mathbb{F}_2$ acting by $0 \cdot v = 0$ and $1 \cdot v = v$, is not a vector space over $\mathbb{F}_2$.
Axiom 8 fails: $(1 + 1) \cdot 1 = 0 \cdot 1 = 0$, while $1 \cdot 1 + 1 \cdot 1 = 2$, which is not $0$ in $\mathbb{Z}/4$.
The trouble is that $v + v = 0$ must hold for every vector of a space over $\mathbb{F}_2$, and $1 + 1 \ne 0$ in $\mathbb{Z}/4$.

### Watch out

Over $\mathbb{F}_2$ a polynomial and the function it defines are different things.
The polynomial $x^2 + x$ is not zero in the [[space of polynomials|0JGZCDT5DN]], yet it takes the value $0$ at both points of $\mathbb{F}_2$.

## Explanations

### L1 human

A vector space can be finite.
Over the field with two elements, the plane has only four points: $(0, 0)$, $(1, 0)$, $(0, 1)$ and $(1, 1)$.
Each vector plus itself is zero, because $1 + 1 = 0$ in this field.
Such spaces are used in coding theory, where a linear code is a subspace of $\mathbb{F}_2^n$.

### L2 human

We count the ordered bases of $\mathbb{F}_3^2$, where the scalars are $0$, $1$ and $2$ with arithmetic modulo $3$.
The space has $3^2 = 9$ vectors, so the first basis vector has $9 - 1 = 8$ choices.
The span of the first vector $v_1$ is the line $\{0, v_1, 2v_1\}$, with $3$ elements, so the second vector has $9 - 3 = 6$ choices.
So there are $8 \cdot 6 = 48$ ordered bases.
Each line is spanned by $2$ of the $8$ nonzero vectors, so $\mathbb{F}_3^2$ has $8 / 2 = 4$ lines through $0$.
Check: the lines are spanned by $(1, 0)$, $(0, 1)$, $(1, 1)$ and $(1, 2)$, and their $4 \cdot 2 = 8$ nonzero points are all different.
