---
tag: SEYHKY2ZQT
kind: example
name: The MV-algebras Γ(ℤ, 1) and Γ(ℤ, n)
msc: ["06D35", "06F20"]
topics: [QYA4H5Y7VR]
audience: research
instance_of: [8T4M7RN9AC]
uses: [64NDFWQEZ2, QVWHWDJ5X1, 0WG43AC0EV]
sources:
  - url: https://en.wikipedia.org/wiki/MV-algebra
    locator: Examples of MV-algebras
---

## Example

The integers $\mathbb{Z}$ form a totally ordered abelian group, and every $n \ge 1$ is a strong unit.
By [[the $\Gamma$ theorem|64NDFWQEZ2]], $\Gamma(\mathbb{Z}, n) = \set{0, 1, \dots, n}$ is an [[MV-algebra|QVWHWDJ5X1]] with
$$x \oplus y = \min(n, x + y), \qquad \neg x = n - x.$$

1. For $n = 1$: $\Gamma(\mathbb{Z}, 1) = \set{0, 1}$ with $1 \oplus 1 = 1$ and $\neg 0 = 1$.
   This is the [[two-element Boolean algebra|0WG43AC0EV]], with $\oplus = \lor$.
2. For $n = 4$: $3 \oplus 2 = 4$, $1 \oplus 2 = 3$, $\neg 1 = 3$ and $3 \odot 2 = \max(0, 3 + 2 - 4) = 1$.
3. The map $k \mapsto k/n$ is an isomorphism from $\Gamma(\mathbb{Z}, n)$ onto the subalgebra $L_n = \set{0, \tfrac1n, \dots, 1}$ of $[0, 1]$.

## Remarks

1. $\Gamma(\mathbb{Z}, n)$ is Boolean only for $n = 1$: for $n \ge 2$, $1 \oplus 1 = 2 \ne 1$.
2. Functoriality: $x \mapsto 2x$ maps $(\mathbb{Z}, 2)$ to $(\mathbb{Z}, 4)$ and sends the unit to the unit.
   So it restricts to an MV-embedding $\Gamma(\mathbb{Z}, 2) \to \Gamma(\mathbb{Z}, 4)$, with $0, 1, 2 \mapsto 0, 2, 4$.
3. A unital map $(\mathbb{Z}, n) \to (\mathbb{Z}, m)$ is $x \mapsto (m/n) x$, so it exists iff $n$ divides $m$.

## Explanations

### L1 human

Count from $0$ to $n$, and add with a cap at $n$.
"Not $x$" is the distance from $x$ to the top.
With $n = 1$, this is ordinary true/false logic.

### L2 human

1. Take $n = 3$, so the elements are $0, 1, 2, 3$.
2. Compute $\neg(\neg 1 \oplus 2) \oplus 2 = \neg(2 \oplus 2) \oplus 2 = \neg 3 \oplus 2 = 2$.
3. Compute $\neg(\neg 2 \oplus 1) \oplus 1 = \neg(1 \oplus 1) \oplus 1 = 1 \oplus 1 = 2$.
4. Both equal $\max(1, 2) = 2$, as the last axiom requires.

The typical use: these are the finite MV-chains, and they model the finite-valued Łukasiewicz logics.
The trap: $\Gamma(\mathbb{Z}, n)$ has $n + 1$ elements, not $n$.
