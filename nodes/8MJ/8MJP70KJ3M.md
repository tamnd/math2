---
tag: 8MJP70KJ3M
kind: example
name: A linear equation over the field with three elements
msc: ["15A06"]
topics: [DXSXFVDMXQ]
audience: ug1
instance_of: [0Q3ZT8J05R]
uses: [0Q3ZT8J05R, 0ZXZ82FTX2, 03VFZ2WETT]
sources:
  - url: https://en.wikipedia.org/wiki/Finite_field
    locator: lead section
---

## Example

Let $\mathbb{F}_3 = \set{0, 1, 2}$ be the [[integers modulo 3|03VFZ2WETT]], a [[finite field|0ZXZ82FTX2]].
Consider the equation $2x + y + z = 1$ over $\mathbb{F}_3$.

1. The left side is a sum of the unknowns times the constants $2, 1, 1 \in \mathbb{F}_3$, so the equation is a [[linear equation|0Q3ZT8J05R]].
2. The coefficient of $y$ is $1 \ne 0$, so we solve for $y$: $y = 1 - 2x - z$.
3. In $\mathbb{F}_3$ we have $-2 = 1$, so $y = 1 + x - z$.
4. The unknowns $x$ and $z$ can take any of the $3$ values each, so there are $3 \cdot 3 = 9$ solutions.
5. With $z = 0$: $x = 0$ gives $(0, 1, 0)$, $x = 1$ gives $(1, 2, 0)$, $x = 2$ gives $(2, 0, 0)$.
6. Check $(1, 2, 0)$: $2 \cdot 1 + 2 + 0 = 4 = 1$ in $\mathbb{F}_3$.
7. Check $(2, 0, 0)$: $2 \cdot 2 = 4 = 1$ in $\mathbb{F}_3$.

## Remarks

The count $9 = 3^{3-1}$ agrees with the rule that a nonzero linear equation in $n$ unknowns over $\mathbb{F}_q$ has $q^{n-1}$ solutions.
The general count for systems is in [[the theorem on finite fields|8QM2Y41P69]].

## Explanations

### L1 human

In $\mathbb{F}_3$ we compute with remainders after division by $3$, like a clock with three hours.
So $2 \cdot 2 = 4$ becomes $1$.
The same method as for real numbers works: solve for one unknown and let the others be free.
The only change is that each free unknown has $3$ possible values, so we can list all solutions.

### L2 human

We list the solutions with $z = 1$.

1. Then $y = 1 + x - 1 = x$.
2. So the solutions are $(0, 0, 1)$, $(1, 1, 1)$ and $(2, 2, 1)$.
3. Check $(2, 2, 1)$: $4 + 2 + 1 = 7 = 1$ in $\mathbb{F}_3$.

A trap: do not divide by $2$ as if it were a real number; in $\mathbb{F}_3$ the inverse of $2$ is $2$, because $2 \cdot 2 = 1$.
