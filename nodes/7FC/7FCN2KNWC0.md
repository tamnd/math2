---
tag: 7FCN2KNWC0
kind: example
name: The integers modulo 2 and the group of signs are isomorphic
msc: ["20A05"]
topics: [BAVE5RN4EE]
audience: ug1
instance_of: [08MG7H8JW5]
illustrates: [0736AXH2ME]
uses: [03VFZ2WETT, 08MG7H8JW5, 0KVGH0J5B3]
sources:
  - url: https://en.wikipedia.org/wiki/Group_isomorphism
    locator: Cyclic groups
  - book: isbn:9781305657960
    locator: Chapter 6
---

## Example

Let $\mathbb{Z}/2\mathbb{Z} = \{0, 1\}$ be the [[integers modulo $2$|03VFZ2WETT]] under addition.
Let $\{1, -1\}$ be the group of signs under multiplication.
Define $f \colon \mathbb{Z}/2\mathbb{Z} \to \{1, -1\}$ by $f(0) = 1$ and $f(1) = -1$, that is, $f(k) = (-1)^k$.

1. The map $f$ is a bijection: it sends the two elements $0, 1$ to the two different elements $1, -1$.
2. We check all four sums: $f(0 + 0) = f(0) = 1 = 1 \cdot 1$ and $f(0 + 1) = f(1) = -1 = 1 \cdot (-1)$.
3. Also $f(1 + 0) = f(1) = -1 = (-1) \cdot 1$ and $f(1 + 1) = f(0) = 1 = (-1) \cdot (-1)$.
4. So $f(j + k) = f(j) f(k)$ for all $j, k$, and $f$ is a homomorphism.
5. By steps 1 and 4, $f$ is a [[group isomorphism|08MG7H8JW5]].

## Remarks

Both groups are [[cyclic|0KVGH0J5B3]] of order $2$, with generators $1$ and $-1$.
So the isomorphism also follows from [[the classification of cyclic groups|0736AXH2ME]], and $f$ is the map $g^k \mapsto h^k$ of that theorem with $g = 1$ and $h = -1$.
It is the only isomorphism, because an isomorphism sends the identity $0$ to the identity $1$.
The isomorphism turns the parity rules into sign rules: "odd plus odd is even" becomes $(-1)(-1) = 1$.
The sign of a permutation is a homomorphism from $S_n$ to $\{1, -1\}$, and through $f$ it is the parity of the permutation in $\mathbb{Z}/2\mathbb{Z}$.

## Explanations

### L1 human

Even and odd numbers add like this: even plus even is even, even plus odd is odd, and odd plus odd is even.
Signs multiply like this: plus times plus is plus, plus times minus is minus, and minus times minus is plus.
Replace "even" by "plus" and "odd" by "minus", and the two rules are the same.
So the two groups are the same group with different names.

### L2 human

We use $f$ to compute a sign.

1. The product $(-1)^{7}$ corresponds to the sum of seven copies of $1$ in $\mathbb{Z}/2\mathbb{Z}$.
2. Seven copies of $1$ give $7 \equiv 1 \pmod 2$, and $f(1) = -1$. So $(-1)^7 = -1$.

The typical use: a group with $2$ elements is always a copy of $\mathbb{Z}/2\mathbb{Z}$, so we can compute in whichever copy is easier.
A trap: the isomorphism sends $0$ to $1$, not $0$ to $0$, because it must send identity to identity.
