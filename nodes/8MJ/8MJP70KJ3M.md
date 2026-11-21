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
We check that it is linear and list its solutions.

1. The left side is a sum of the unknowns times the constants $2, 1, 1 \in \mathbb{F}_3$. So the equation is a [[linear equation|0Q3ZT8J05R]].
2. The coefficient of $y$ is $1 \ne 0$, so we solve for $y$. This gives $y = 1 - 2x - z$, and since $-2 = 1$ in $\mathbb{F}_3$, we get $y = 1 + x - z$.
3. The unknowns $x$ and $z$ can each take any of the $3$ values. So there are $3 \cdot 3 = 9$ solutions.
4. With $z = 0$ the solutions are $(0, 1, 0)$, $(1, 2, 0)$ and $(2, 0, 0)$. With $z = 1$ they are $(0, 0, 1)$, $(1, 1, 1)$ and $(2, 2, 1)$. With $z = 2$ they are $(0, 2, 2)$, $(1, 0, 2)$ and $(2, 1, 2)$.
5. Check $(1, 2, 0)$ and $(2, 2, 1)$ in $\mathbb{F}_3$:
$$2 \cdot 1 + 2 + 0 = 4 = 1, \qquad 2 \cdot 2 + 2 + 1 = 7 = 1.$$

## Remarks

The method is the same as over $\mathbb{R}$: solve for one unknown with a nonzero coefficient, and let the others be free.
The only change is that each free unknown has $3$ values instead of infinitely many, so the solutions can be counted.
The count $9 = 3^{3-1}$ agrees with the rule that a linear equation in $n$ unknowns over $\mathbb{F}_q$ with some nonzero coefficient has $q^{n-1}$ solutions.
The same idea for whole systems is the [[count of solutions over a finite field|8QM2Y41P69]].

## Explanations

### L1 human

In $\mathbb{F}_3$ we compute with remainders after division by $3$, like a clock with three hours.
So $2 \cdot 2 = 4$ becomes $1$.
We solve the equation as usual, and because each free unknown has only three values, we can write down every solution.

### L2 human

Suppose that you want to solve for $x$ instead of $y$.
Then you must divide by the coefficient $2$, and in $\mathbb{F}_3$ the inverse of $2$ is $2$, because $2 \cdot 2 = 4 = 1$.
Multiply $2x = 1 - y - z$ by $2$:
$$x = 2 - 2y - 2z = 2 + y + z.$$
Check with $y = 2$, $z = 0$: this gives $x = 4 = 1$, and $(1, 2, 0)$ is on the list above.
Watch out: you cannot divide by $2$ as if it were a real number, because $\tfrac12$ is not an element of $\mathbb{F}_3$ until you read it as the inverse $2$.
