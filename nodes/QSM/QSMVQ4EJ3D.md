---
tag: QSMVQ4EJ3D
kind: example
name: The symmetric group S3 is not abelian
msc: [20B30]
topics: [BAZT8JJ70S]
audience: ug1
instance_of: [G5S1M9]
not_instance_of:
  - target: 082GHNPJ53
    note: two transpositions do not commute
  - target: 071DDFVG4J
    note: (1 2)(1 3) is not (1 3)(1 2)
uses: [0515A6D2Y1, 0FWVRHBRWM, 0ZKPH2BD1T]
sources:
  - url: https://en.wikipedia.org/wiki/Dihedral_group_of_order_6
    locator: lead section
---

## Example

Let $S_3$ be the [[symmetric group|0515A6D2Y1]] on $\{1, 2, 3\}$, the group of the $6$ [[permutations|05RWFKVTJ7]] of $\{1, 2, 3\}$ under composition.
We compose permutations from right to left: $\sigma \tau$ means first $\tau$, then $\sigma$.
Take the [[transpositions|0FWVRHBRWM]] $\sigma = (1\,2)$ and $\tau = (1\,3)$, written in [[cycle notation|0ZKPH2BD1T]].

1. Compute $\sigma \tau = (1\,2)(1\,3)$. The point $1$ goes to $3$ under $\tau$, and $3$ stays fixed under $\sigma$. So $1 \mapsto 3$.
2. The point $3$ goes to $1$ under $\tau$, and $1$ goes to $2$ under $\sigma$. So $3 \mapsto 2$.
3. The point $2$ stays fixed under $\tau$, and $2$ goes to $1$ under $\sigma$. So $2 \mapsto 1$. Thus $\sigma \tau = (1\,3\,2)$.
4. Compute $\tau \sigma = (1\,3)(1\,2)$. The point $1$ goes to $2$ under $\sigma$, and $2$ stays fixed under $\tau$. So $1 \mapsto 2$.
5. The point $2$ goes to $1$ under $\sigma$, and $1$ goes to $3$ under $\tau$. So $2 \mapsto 3$. Then $3 \mapsto 1$, and $\tau \sigma = (1\,2\,3)$.
6. The products differ: $\sigma \tau$ sends $1$ to $3$, and $\tau \sigma$ sends $1$ to $2$.

So $\sigma \tau \neq \tau \sigma$, and $S_3$ is not [[abelian|082GHNPJ53]].

## Remarks

The group $S_3$ has $3! = 6$ elements.
[[Each group of order at most 5 is abelian|G98PPG0FCC]], so $S_3$ is a smallest group that is not abelian.
For each $n \geq 3$, the group $S_n$ is not abelian, because the same two transpositions $(1\,2)$ and $(1\,3)$ are in $S_n$ and the same computation applies.
The group $S_2 = \{e, (1\,2)\}$ has $2$ elements, and it is abelian.
The group $S_3$ is [[isomorphic|08MG7H8JW5]] to the [[dihedral group|0JZ27DMJ5D]] of the symmetries of an equilateral triangle.
Each transposition $t$ has $t^2 = e$, so $S_3$ shows that the result that [[a group of exponent 2 is abelian|GGAT7CNA82]] needs $g^2 = e$ for each element $g$.

## Explanations

### L1 human

Put three cards in a row, in the places $1$, $2$ and $3$.
First swap the cards in places $1$ and $3$, then swap the cards in places $1$ and $2$.
Now start again and do the two swaps in the other order.
The two final rows are different.
So in this group, the order of two steps matters.

### L2 human

We follow the cards $A$, $B$, $C$ in the places $1$, $2$, $3$.

1. Swap places $1$ and $3$: the row is $C, B, A$. Then swap places $1$ and $2$: the row is $B, C, A$.
2. Start from $A, B, C$ again. Swap places $1$ and $2$: the row is $B, A, C$. Then swap places $1$ and $3$: the row is $C, A, B$.
3. The rows $B, C, A$ and $C, A, B$ are different.

The typical use of $S_3$ is as the first test case for a claim about groups that are not abelian.
A trap is to compose from left to right in one step and from right to left in another step: this exchanges the two products.
