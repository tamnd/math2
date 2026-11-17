---
tag: 4PJETRFBEX
kind: example
name: The order does not classify finite groups
msc: ["00A35", "20K01"]
topics: [N4P3E53HM0]
audience: ug1
not_instance_of:
  - target: 9HQ3TADPA8
    note: the order is an invariant of finite groups under isomorphism, but it is not a complete invariant, so it does not classify finite groups
uses: [9HQ3TADPA8, 03VFZ2WETT, 0PMRQJVTME, 08MG7H8JW5, 0WE2NHZJ7B, 0B85S2V2DR]
sources:
  - url: https://en.wikipedia.org/wiki/Klein_four-group
    locator: lead section
  - url: https://en.wikipedia.org/wiki/Group_isomorphism
    locator: lead section
---

## Example

Let $X$ be the class of finite groups, with the relation "is isomorphic to".
The [[order|0B85S2V2DR]] $|G|$ is an invariant, because a [[group isomorphism|08MG7H8JW5]] is a bijection, and a bijection keeps the number of elements.
We show that the order is not a complete invariant.
Let $C = \mathbb{Z}/4\mathbb{Z}$ be the [[integers modulo 4|03VFZ2WETT]] with addition, and let $V = \{e, a, b, c\}$ be the [[Klein four-group|0PMRQJVTME]].

1. Both groups have order $4$.
2. In $C$, the element $1$ has [[order|0WE2NHZJ7B]] $4$, because its multiples $1, 2, 3, 0$ first reach $0$ at the fourth step.
3. In $V$, each element other than $e$ has order $2$, because $a^2 = b^2 = c^2 = e$. So no element of $V$ has order $4$.
4. An isomorphism $\varphi \colon C \to V$ keeps the order of each element. If $n \cdot x = 0$ in $C$, then $\varphi(x)^n = \varphi(n \cdot x) = \varphi(0) = e$, and the same argument works for $\varphi^{-1}$.
5. So an isomorphism would send the element $1$ of order $4$ to an element of order $4$ in $V$. No such element exists, by step 3.
6. So $C$ and $V$ are not isomorphic, although they have the same order.
7. Thus the order is an invariant that is not complete, and it does not classify finite groups.

## Remarks

The proof in steps 4 to 6 uses a finer invariant: the number of elements of each order.
For $C$, the orders of $0, 1, 2, 3$ are $1, 4, 2, 4$, so $C$ has one element of order $1$, one of order $2$ and two of order $4$.
For $V$, there is one element of order $1$ and three of order $2$.
These counts differ, so the groups differ.

For the groups of order $4$, the finer invariant is complete: each group of order $4$ is isomorphic to $C$ or to $V$.
For larger orders even this invariant fails.
The groups $\mathbb{Z}/4\mathbb{Z} \times \mathbb{Z}/4\mathbb{Z}$ and $\mathbb{Z}/2\mathbb{Z} \times Q_8$, with $Q_8$ the quaternion group, both have one element of order $1$, three of order $2$ and twelve of order $4$.
The first group is abelian and the second is not, so they are not isomorphic.
So the classification of groups needs still finer data.
For a prime order $p$ the order alone is complete, because each group of order $p$ is cyclic.

## Explanations

### L1 human

Two clubs can have four members each and still be organized in different ways.
The number of members does not tell us how the club works.
In the same way, two groups can both have four elements and still follow different rules.
In one of them, a single element can produce all the others by repetition.
In the other, each element returns to the start after two steps.
So the number of elements is not enough to tell groups apart.

### L2 human

We use the same method to show that $\mathbb{Z}/6\mathbb{Z}$ and the symmetric group $S_3$ are not isomorphic.

1. Both groups have order $6$.
2. In $\mathbb{Z}/6\mathbb{Z}$, the element $1$ has order $6$.
3. In $S_3$, the identity has order $1$, the three transpositions have order $2$, and the two $3$-cycles have order $3$.
4. So $S_3$ has no element of order $6$, and the groups are not isomorphic.

The typical use is to separate two groups of the same order by the orders of their elements.
A trap is to think that equal counts of element orders prove an isomorphism.
That is false in general, as the groups of order $16$ show.
