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

Let $\mathbb{F}_2 = \set{0, 1}$, with $1 + 1 = 0$, and let $V = \mathbb{F}_2^2$.
The space has $2^2 = 4$ vectors: $(0, 0)$, $(1, 0)$, $(0, 1)$, $(1, 1)$.
Addition and scalar multiplication act entrywise, with arithmetic modulo $2$.

Check of the [[vector space axioms|05EGHEQZAW]] with explicit vectors:

1. Addition is commutative and associative, entry by entry, because addition modulo $2$ is: for example, $(1, 0) + (1, 1) = (0, 1) = (1, 1) + (1, 0)$.
2. The zero vector is $(0, 0)$: $(1, 1) + (0, 0) = (1, 1)$.
3. Each vector is its own negative: $(1, 1) + (1, 1) = (1 + 1, 1 + 1) = (0, 0)$.
4. The scalar $1$ acts as the identity, and $0 \cdot v = (0, 0)$ for each $v$.
5. Distributivity: $1 \cdot ((1, 0) + (0, 1)) = (1, 1) = 1 \cdot (1, 0) + 1 \cdot (0, 1)$, and $(1 + 1) \cdot (1, 1) = (0, 0) = (1, 1) + (1, 1)$.

The ordered [[bases|0VTQTPQGAV]] of $V$:

1. A basis is a pair of independent vectors; over $\mathbb{F}_2$, this means two distinct nonzero vectors, since the span of a nonzero $v$ is $\set{0, v}$.
2. The nonzero vectors are $(1, 0)$, $(0, 1)$, $(1, 1)$, so there are $3 \cdot 2 = 6$ ordered bases.
3. The list: $((1, 0), (0, 1))$, $((0, 1), (1, 0))$, $((1, 0), (1, 1))$, $((1, 1), (1, 0))$, $((0, 1), (1, 1))$, $((1, 1), (0, 1))$.
4. This agrees with the formula $(q^n - 1)(q^n - q) = (4 - 1)(4 - 2) = 6$ of [[the counting statement|PHTBCRD6WS]].

## Remarks

The space $\mathbb{F}_2^3$ has $8$ vectors and $(8 - 1)(8 - 2)(8 - 4) = 168$ ordered bases.
The field $\mathbb{F}_4$ is a vector space of dimension $2$ over $\mathbb{F}_2$, with basis $1, \omega$, where $\omega^2 = \omega + 1$.
No vector space over $\mathbb{F}_2$ has $6$ elements, because the size must be a power of $2$.
Non-example: $\Z / 4$ with $0 \cdot v = 0$ and $1 \cdot v = v$ fails axiom 8, distributivity over scalars.
Check: $(1 + 1) \cdot 1 = 0 \cdot 1 = 0$, but $1 \cdot 1 + 1 \cdot 1 = 2 \ne 0$ in $\Z / 4$.
Over $\mathbb{F}_2$, the polynomial $x^2 + x$ is a nonzero polynomial but the zero function on $\mathbb{F}_2$; see the [[space of polynomials|0JGZCDT5DN]].
The lines through $0$ in $\mathbb{F}_2^2$ are the spans of the $3$ nonzero vectors, so there are $3 = (4 - 1) / (2 - 1)$ lines.
Finite vector spaces are used in coding theory: a linear code is a subspace of $\mathbb{F}_q^n$.

## Explanations

### L1 human

A vector space can be finite: over the field with two elements, the plane has only four points.
Each vector plus itself is zero, because $1 + 1 = 0$ in this field.

### L2 human

To count the bases of $\mathbb{F}_2^2$, choose the first vector: $3$ nonzero choices.
Then choose the second vector outside the span $\set{0, v_1}$ of the first: $4 - 2 = 2$ choices.
So there are $3 \cdot 2 = 6$ ordered bases, and $6 / 2 = 3$ bases as sets.
