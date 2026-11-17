---
tag: MXJMVKYEPZ
kind: example
name: Z/4Z and the Klein four-group are not isomorphic
msc: ["20A05"]
topics: [E1506A5A55]
audience: ug1
not_instance_of:
  - target: 08MG7H8JW5
    note: Z/4Z has an element of order 4, and the Klein four-group has none
uses: [03VFZ2WETT, 0PMRQJVTME, 0WE2NHZJ7B, 08MG7H8JW5]
sources:
  - url: https://en.wikipedia.org/wiki/Klein_four-group
    locator: lead section
  - url: https://en.wikipedia.org/wiki/Group_isomorphism
    locator: Properties
---

## Example

Let $\mathbb{Z}/4\mathbb{Z} = \{0, 1, 2, 3\}$ be the [[integers modulo 4|03VFZ2WETT]] under addition.
Let $V_4 = \{(0,0), (1,0), (0,1), (1,1)\}$ be the [[Klein four-group|0PMRQJVTME]], with addition modulo $2$ in each coordinate.
We claim that there is no isomorphism between them.

1. In $\mathbb{Z}/4\mathbb{Z}$, the multiples of $1$ are $1, 2, 3, 0$. So $1$ has [[order|0WE2NHZJ7B]] $4$.
2. In $V_4$, each element satisfies $(x, y) + (x, y) = (2x, 2y) = (0, 0)$. So each element has order $1$ or $2$.
3. An [[isomorphism|08MG7H8JW5]] preserves the order of each element. So an isomorphism would send $1$ to an element of order $4$ in $V_4$.
4. $V_4$ has no element of order $4$, by step 2. So no isomorphism exists.

## Remarks

The example shows that two groups of the same order need not be isomorphic.
Both groups have order $4$, and both are abelian, so these two invariants do not separate them.
The number of elements of each order does: $\mathbb{Z}/4\mathbb{Z}$ has one element of order $1$, one of order $2$ and two of order $4$, and $V_4$ has one of order $1$ and three of order $2$.
So $\mathbb{Z}/4\mathbb{Z}$ is cyclic and $V_4$ is not.
For $\mathbb{Z}/2\mathbb{Z} \times \mathbb{Z}/3\mathbb{Z}$ the answer changes: the element $(1, 1)$ has order $6$, so this group is cyclic and isomorphic to $\mathbb{Z}/6\mathbb{Z}$ ([[product of cyclic groups|08FDFEF8D1]]).

## Explanations

### L1 human

Both groups have four elements, so a count of elements cannot tell them apart.
In $\mathbb{Z}/4\mathbb{Z}$, adding $1$ again and again visits all four elements before it returns to $0$.
In $V_4$, adding any element to itself gives the identity at once.
A renaming of elements cannot change this behaviour, so the two groups are different.

### L2 human

We test a candidate bijection to see where it fails.

1. Let $f(0) = (0,0)$, $f(1) = (1,0)$, $f(2) = (0,1)$ and $f(3) = (1,1)$.
2. In $\mathbb{Z}/4\mathbb{Z}$, $1 + 1 = 2$, so a homomorphism would need $f(2) = f(1) + f(1) = (0,0)$.
3. But $f(2) = (0,1)$, so $f$ is not a homomorphism.

Step 2 of the example shows that every bijection fails in the same way: $f(2) = f(1) + f(1)$ is always $(0,0) = f(0)$.
The typical use of invariants is to replace the check of all $24$ bijections by one count.
The trap is to stop at the order of the group: equal orders never prove an isomorphism.
