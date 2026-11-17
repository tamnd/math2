---
tag: 0PMT9YJZVW
kind: statement
role: proposition
name: Order of an inverse
msc: [20A05]
topics: [BAZT8JJ70S]
audience: ug1
about: [0WE2NHZJ7B]
uses: [0WE2NHZJ7B, 00DRK90Z6K]
sources:
  - url: https://en.wikipedia.org/wiki/Order_(group_theory)
    locator: Order and structure
---

## Statement

Let $G$ be a [[group|G5S1M9]] with identity element $e$, and let $g \in G$ with inverse $g^{-1}$.
Then $g$ and $g^{-1}$ have the same [[order|0WE2NHZJ7B]].
In particular, $g$ has infinite order if and only if $g^{-1}$ has infinite order.

## Remarks

### Why each hypothesis is needed

The only hypothesis is that $g$ is an element of a group, and it is needed for $g^{-1}$ to exist.
In the monoid $(\mathbb{N}, \cdot)$ of [[natural numbers|0MWKJ44V5A]] with multiplication, the element $2$ has no inverse, so the statement has no meaning for $2$.

### Consequences

1. For each $k \geq 3$, a finite group has an even number of elements of order $k$. Reason: the map $g \mapsto g^{-1}$ sends these elements to elements of order $k$, it is its own inverse, and it fixes no such element, because $g = g^{-1}$ gives $g^2 = e$.
2. A finite group of even order has an element of order $2$. Reason: $e$ is the only element of order $1$, and by consequence 1 the elements of order at least $3$ are even in number. So the number of elements of order $2$ is odd, and it is at least $1$.

### Converse

The converse, "two elements of the same order are inverse to each other", is false.
In $\mathbb{Z}/5\mathbb{Z}$, the elements $1$ and $2$ both have order $5$, but the inverse of $1$ is $4$, not $2$.

### Generalizations

1. When $g$ has finite order $n$, the order of $g^k$ is $n / \gcd(n, k)$, by [[the order of a power|0VVPQNVM8S]]. For $k = -1$ this gives $n / \gcd(n, -1) = n$.
2. An [[isomorphism|08MG7H8JW5]] keeps the orders of elements. The statement is the case of the map $g \mapsto g^{-1}$, which is an isomorphism from $G$ to its [[opposite group|D33V8HE0KY]].

## Explanations

### L1 human

The inverse of an element walks the same path back to the identity, in the opposite direction.
It needs the same number of steps.
A rotation by $90$ degrees and a rotation by $-90$ degrees both have order $4$.

### L2 human

We check the statement in two groups.

1. In $\mathbb{Z}/6\mathbb{Z}$ with addition, the inverse of $2$ is $4$, because $2 + 4 = 6 \equiv 0$.
2. The multiples of $2$ are $2, 4, 0$, and the multiples of $4$ are $4, 2, 0$. So both elements have order $3$.
3. In the [[symmetric group|0515A6D2Y1]] $S_3$, the inverse of $(1\,2\,3)$ is $(1\,3\,2)$.
4. Both $3$-cycles have order $3$, because the cube of each $3$-cycle is the identity and its square is not.

The typical use of the statement is in counting arguments, as in the consequences above: the elements of order $k \geq 3$ come in pairs $\{g, g^{-1}\}$.
A trap is to think that $g^{-1}$ is always a different element; when $g$ has order $1$ or $2$, we have $g^{-1} = g$.

### L3 human

The order of $g$ equals the order of the [[cyclic subgroup|08ABT85339]] $\langle g \rangle$.
The subgroups $\langle g \rangle$ and $\langle g^{-1} \rangle$ are equal, because each of $g$ and $g^{-1}$ is a power of the other.
This gives a second view of the statement: the order is a property of the cyclic subgroup, not of the chosen generator.
In the language of homomorphisms, the map $n \mapsto g^{-n}$ is the map $n \mapsto g^n$ composed with the automorphism $n \mapsto -n$ of $\mathbb{Z}$, so both maps have the same kernel.
The same pairing $g \leftrightarrow g^{-1}$ appears in the proof of [[Cauchy's theorem|0JM7PA288B]] for the prime $2$ and in many counting arguments of the later sub-areas.
