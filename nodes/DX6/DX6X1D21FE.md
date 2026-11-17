---
tag: DX6X1D21FE
kind: example
name: The Klein four-group is abelian but not cyclic
msc: ["20A05"]
topics: [BAVE5RN4EE, BAZT8JJ70S]
audience: ug1
instance_of: [082GHNPJ53]
not_instance_of:
  - target: 0KVGH0J5B3
    note: no element generates the group
  - target: RXWA8TF2RM
    note: the group is finitely generated and not cyclic
illustrates: [04RG02S6BA]
uses: [0PMRQJVTME, 0WE2NHZJ7B, 08ABT85339, 0KVGH0J5B3, 082GHNPJ53, 0YB2NRP0T5]
sources:
  - url: https://en.wikipedia.org/wiki/Klein_four-group
    locator: lead section
  - book: isbn:9781305657960
    locator: Chapter 4
---

## Example

The [[Klein four-group|0PMRQJVTME]] is $V = \{e, a, b, c\}$ with the following multiplication table.

| $\cdot$ | $e$ | $a$ | $b$ | $c$ |
|---|---|---|---|---|
| $e$ | $e$ | $a$ | $b$ | $c$ |
| $a$ | $a$ | $e$ | $c$ | $b$ |
| $b$ | $b$ | $c$ | $e$ | $a$ |
| $c$ | $c$ | $b$ | $a$ | $e$ |

A model is $e = \mathrm{id}$, $a = (1\,2)(3\,4)$, $b = (1\,3)(2\,4)$ and $c = (1\,4)(2\,3)$ in the symmetric group $S_4$.

1. The table is symmetric about its main diagonal, so $xy = yx$ for all $x, y \in V$. Thus $V$ is [[abelian|082GHNPJ53]].
2. The diagonal gives $a^2 = b^2 = c^2 = e$. So each of $a, b, c$ has [[order|0WE2NHZJ7B]] $2$, and $e$ has order $1$.
3. So the [[cyclic subgroups|08ABT85339]] are $\langle e \rangle = \{e\}$, $\langle a \rangle = \{e, a\}$, $\langle b \rangle = \{e, b\}$ and $\langle c \rangle = \{e, c\}$.
4. Each of these has at most $2$ elements, and $V$ has $4$. So no element generates $V$.
5. Thus $V$ is abelian but not [[cyclic|0KVGH0J5B3]].
6. The elements $a$ and $b$ generate $V$, because $ab = c$. So $V$ is finitely generated and not cyclic, and it is not a [[locally cyclic group|RXWA8TF2RM]].

## Remarks

The example shows that the converse of [[the theorem that cyclic groups are abelian|04RG02S6BA]] is false.
Up to isomorphism, $V$ and $\mathbb{Z}/4\mathbb{Z}$ are the only groups of order $4$, and $\mathbb{Z}/4\mathbb{Z}$ is cyclic.
So $V$ is the smallest group that is abelian but not cyclic: each group of order $1$, $2$ or $3$ is cyclic.
Other models of $V$ are $\mathbb{Z}/2\mathbb{Z} \times \mathbb{Z}/2\mathbb{Z}$, the group $(\mathbb{Z}/8\mathbb{Z})^\times = \{1, 3, 5, 7\}$ under multiplication, and the symmetries of a rectangle that is not a square.

## Explanations

### L1 human

The Klein four-group has four elements.
Any two elements commute, so the group is abelian.
But each element, combined with itself, gives the identity.
So one element produces at most two elements, never all four, and the group is not cyclic.

### L2 human

We check the model $(\mathbb{Z}/8\mathbb{Z})^\times = \{1, 3, 5, 7\}$.

1. The squares are $1^2 = 1$, $3^2 = 9 \equiv 1$, $5^2 = 25 \equiv 1$ and $7^2 = 49 \equiv 1$ modulo $8$.
2. So each element has order at most $2$, and no element generates the group.
3. The products $3 \cdot 5 \equiv 7$, $3 \cdot 7 \equiv 5$ and $5 \cdot 7 \equiv 3$ match the table with $a = 3$, $b = 5$ and $c = 7$.

The typical use: to show that a finite group of order $n$ is not cyclic, show that it has no element of order $n$.
A trap: a group can be abelian and small and still not cyclic.
Commutativity is not enough.
