---
tag: FB79N7AHZA
kind: example
name: Integers modulo n form a cyclic group
msc: ["20A05"]
topics: [BAVE5RN4EE]
audience: ug1
instance_of: [0KVGH0J5B3, 082GHNPJ53]
illustrates: [04RG02S6BA]
uses: [03VFZ2WETT, 0KVGH0J5B3, 08ABT85339, 082GHNPJ53]
sources:
  - url: https://en.wikipedia.org/wiki/Cyclic_group
    locator: Integer and modular addition
  - book: isbn:9781305657960
    locator: Chapter 4
---

## Example

Let $n \geq 1$, and let $\mathbb{Z}/n\mathbb{Z} = \{0, 1, \ldots, n-1\}$ be the [[integers modulo $n$|03VFZ2WETT]] under addition modulo $n$.
This is a group with identity $0$, and the inverse of $k$ is $n - k$ for $k \neq 0$.
We check that it is [[cyclic|0KVGH0J5B3]] and [[abelian|082GHNPJ53]].

1. In additive notation, the $k$th power of $1$ is the sum $1 + 1 + \cdots + 1$ of $k$ terms, which is $k$ for $0 \leq k \leq n-1$.
2. So each element of $\mathbb{Z}/n\mathbb{Z}$ lies in the [[cyclic subgroup|08ABT85339]] $\langle 1 \rangle$, and $\langle 1 \rangle = \mathbb{Z}/n\mathbb{Z}$.
3. Thus $\mathbb{Z}/n\mathbb{Z}$ is cyclic, with generator $1$, and it has order $n$.
4. For residues $j, k$, the sums $j + k$ and $k + j$ are equal integers, so they have the same remainder modulo $n$. So $\mathbb{Z}/n\mathbb{Z}$ is abelian.
5. Step 4 agrees with [[the theorem that cyclic groups are abelian|04RG02S6BA]].

For $n = 5$, the multiples of $1$ are $1, 2, 3, 4$ and $5 \equiv 0$, which are all $5$ elements.

## Remarks

The residue $1$ is not the only generator.
The residue $k$ generates $\mathbb{Z}/n\mathbb{Z}$ exactly when $\gcd(k, n) = 1$, as the page on [[cyclic groups|0KVGH0J5B3]] proves.
For $n = 5$ each nonzero residue is a generator, and for $n = 6$ only $1$ and $5$ are.
The group $\mathbb{Z}/n\mathbb{Z}$ is the standard model of the [[cyclic group of order $n$|0G0B3DRG65]].
Under multiplication, the set $\mathbb{Z}/n\mathbb{Z}$ is not a group for $n \geq 2$, because $0$ has no inverse.

## Explanations

### L1 human

Think of a clock with $n$ hours, numbered from $0$ to $n - 1$.
Adding hours on the clock is addition modulo $n$.
Starting at $0$ and moving one hour at a time, we reach every hour.
So the single step "add $1$" produces the whole group, and the group is cyclic.

### L2 human

We take $n = 6$ and compare two elements.

1. The multiples of $1$ are $1, 2, 3, 4, 5, 0$. So $1$ generates $\mathbb{Z}/6\mathbb{Z}$.
2. The multiples of $2$ are $2, 4, 0$. So $\langle 2 \rangle = \{0, 2, 4\}$, and $2$ does not generate.
3. Commutativity: $4 + 5 = 9 \equiv 3$ and $5 + 4 = 9 \equiv 3$.

The typical use: $\mathbb{Z}/n\mathbb{Z}$ is the model on which we test each statement about cyclic groups.
A trap: the residues are classes of integers, so $1$ and $7$ are the same element of $\mathbb{Z}/6\mathbb{Z}$.
