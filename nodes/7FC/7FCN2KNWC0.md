---
tag: 7FCN2KNWC0
kind: example
name: The integers modulo 2 and the group of signs are isomorphic
msc: ["20A05"]
topics: [E1506A5A55]
audience: ug1
instance_of: [08MG7H8JW5]
illustrates: [0736AXH2ME]
uses: [03VFZ2WETT, 08MG7H8JW5]
sources:
  - url: https://en.wikipedia.org/wiki/Group_isomorphism
    locator: Cyclic groups
---

## Example

Let $\mathbb{Z}/2\mathbb{Z} = \{0, 1\}$ be the [[integers modulo 2|03VFZ2WETT]] under addition.
Let $\{1, -1\}$ be the group of signs under multiplication.
Define $f(0) = 1$ and $f(1) = -1$.

1. The map $f$ is a bijection, because it takes the two values $1$ and $-1$.
2. We check the four sums: $f(0 + 0) = 1 = 1 \cdot 1$ and $f(0 + 1) = -1 = 1 \cdot (-1)$.
3. Also $f(1 + 0) = -1 = (-1) \cdot 1$ and $f(1 + 1) = f(0) = 1 = (-1) \cdot (-1)$.
4. So $f$ is a bijective homomorphism, that is, an [[isomorphism|08MG7H8JW5]].
5. Its inverse sends $1 \mapsto 0$ and $-1 \mapsto 1$.

## Remarks

The example shows that two groups with different operations can have the same structure.
Both groups are cyclic of order $2$, so the result also follows from the [[classification of cyclic groups|0736AXH2ME]].
The isomorphism is unique: it must send the identity $0$ to the identity $1$, so it must send $1$ to $-1$.
For $n \ge 1$, the map $k \mapsto e^{2\pi i k/n}$ is an isomorphism from $\mathbb{Z}/n\mathbb{Z}$ to the group of $n$th roots of unity, and $n = 2$ gives this example.
The [[sign|02DKV69ZH0]] of a permutation takes values in this group, and the isomorphism turns the sign into the parity, even or odd.

## Explanations

### L1 human

Even plus even is even, even plus odd is odd, and odd plus odd is even.
Plus times plus is plus, plus times minus is minus, and minus times minus is plus.
The two rules are the same rule with different names.
Rename "even" as $1$ and "odd" as $-1$, and one table becomes the other.

### L2 human

We compare the two tables entry by entry.

1. In $\mathbb{Z}/2\mathbb{Z}$: $0 + 0 = 0$, $0 + 1 = 1$, $1 + 0 = 1$ and $1 + 1 = 0$.
2. Replace $0$ by $1$ and $1$ by $-1$: $1 \cdot 1 = 1$, $1 \cdot (-1) = -1$, $(-1) \cdot 1 = -1$ and $(-1) \cdot (-1) = 1$.
3. Each line is true in $\{1, -1\}$, so the renaming respects the operation.

The typical use is to turn a question about parity into a computation with signs, for example $(-1)^{a + b} = (-1)^a(-1)^b$.
The trap is the other bijection, $0 \mapsto -1$ and $1 \mapsto 1$.
It sends the identity $0$ to $-1$, so it is not a homomorphism.
