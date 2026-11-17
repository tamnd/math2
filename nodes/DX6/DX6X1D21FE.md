---
tag: DX6X1D21FE
kind: example
name: The Klein four-group is abelian but not cyclic
msc: [20A05]
topics: [BAZT8JJ70S]
audience: ug1
instance_of: [082GHNPJ53]
not_instance_of:
  - target: 0KVGH0J5B3
    note: no element generates the group
  - target: 0B85Q41RP6
    note: each element generates a subgroup with at most two elements
uses: [0PMRQJVTME, 0WE2NHZJ7B, 0YB2NRP0T5]
sources:
  - url: https://en.wikipedia.org/wiki/Klein_four-group
    locator: lead section
---

## Example

The [[Klein four-group|0PMRQJVTME]] is $V = \{e, a, b, c\}$ with this [[Cayley table|0YB2NRP0T5]].
The entry in row $x$ and column $y$ is $xy$.

| $\cdot$ | $e$ | $a$ | $b$ | $c$ |
|---|---|---|---|---|
| $e$ | $e$ | $a$ | $b$ | $c$ |
| $a$ | $a$ | $e$ | $c$ | $b$ |
| $b$ | $b$ | $c$ | $e$ | $a$ |
| $c$ | $c$ | $b$ | $a$ | $e$ |

We check that $V$ is a [[group|G5S1M9]], that it is [[abelian|082GHNPJ53]], and that it is not [[cyclic|0KVGH0J5B3]].

1. Closure. Each entry of the table is in $V$.
2. Identity. The row and the column of $e$ repeat the headings, so $ex = xe = x$ for each $x$.
3. Inverses. Each diagonal entry is $e$, so $x^{-1} = x$ for each $x$.
4. Associativity. Send $e \mapsto (0, 0)$, $a \mapsto (1, 0)$, $b \mapsto (0, 1)$ and $c \mapsto (1, 1)$. Then the table becomes addition of pairs with each coordinate modulo $2$. For example, $ab = c$ becomes $(1, 0) + (0, 1) = (1, 1)$. Addition of pairs modulo $2$ is associative, so the operation of $V$ is associative.
5. Commutativity. The table is symmetric about its diagonal, so $xy = yx$ for all $x, y$. Thus $V$ is abelian.
6. Orders. By step 3, each $x \neq e$ has $x^2 = e$, so it has [[order|0WE2NHZJ7B]] $2$. The subgroup that $x$ generates is $\{e, x\}$.
7. Not cyclic. The subgroup $\langle e \rangle$ is $\{e\}$, and each other $\langle x \rangle$ has $2$ elements. No element generates all $4$ elements, so $V$ is not cyclic.

## Remarks

The example shows that the converse of the result that [[cyclic groups are abelian|04RG02S6BA]] is false.
Up to [[isomorphism|08MG7H8JW5]], $V$ and $\mathbb{Z}/4\mathbb{Z}$ are the only groups of order $4$.
Indeed, the case of order $4$ in the proof that [[each group of order at most 5 is abelian|~86185f14]] shows that a group of order $4$ is cyclic or has $g^2 = e$ for each $g$.
In the first case it is isomorphic to $\mathbb{Z}/4\mathbb{Z}$.
In the second case it is isomorphic to $\mathbb{Z}/2\mathbb{Z} \times \mathbb{Z}/2\mathbb{Z}$, by the consequences of the result on [[exponent 2|~2dc226b7]], and so to $V$.
The two groups are not isomorphic, because $\mathbb{Z}/4\mathbb{Z}$ has an element of order $4$ and $V$ has none.
Step 4 shows that $V$ is isomorphic to the [[direct product|00HF4RJ5QN]] $\mathbb{Z}/2\mathbb{Z} \times \mathbb{Z}/2\mathbb{Z}$.
Since $x^2 = e$ for each $x$, commutativity also follows from the result that a group of exponent $2$ is abelian.

## Explanations

### L1 human

Take a rectangle that is not a square.
It has four symmetries: do nothing, turn it by a half turn, flip it left to right, and flip it top to bottom.
Each of them done two times does nothing.
Any two of them, done in either order, give the same result.
No single symmetry gives all four when we repeat it.

### L2 human

We find all products in the rectangle model.
Let $a$ be the flip left to right, $b$ the flip top to bottom, and $c$ the half turn.

1. A flip left to right and then a flip top to bottom send each corner to the opposite corner. So $ba = c$.
2. The two flips in the other order also send each corner to the opposite corner. So $ab = c$.
3. A half turn and then a flip left to right is a flip top to bottom. So $ac = b$, and in the same way $ca = b$.

The typical use of $V$ is as the smallest group that is not cyclic.
A trap is to think that each abelian group is cyclic.
