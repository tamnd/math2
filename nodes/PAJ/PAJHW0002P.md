---
tag: PAJHW0002P
kind: example
name: The x-axis and the y-axis do not split three-dimensional space
msc: ["15A03"]
topics: [QHKTJ89V6S]
audience: ug1
not_instance_of:
  - target: 0XYYT5KNTX
    note: the sum of the two axes is direct, but it is the xy-plane and not R³
illustrates: [P4JG9DJ2HH]
uses: [041JTZCK9Q, 0V33SPH7RR, 0RMKABS2S5]
sources:
  - book: isbn:9783031410253
    locator: Section 1C
---

## Example

Let $U = \R(1, 0, 0)$ and $W = \R(0, 1, 0)$ in $V = \R^3$.

1. Intersection. If $a(1, 0, 0) = b(0, 1, 0)$, then $a = 0$ and $b = 0$. So $U \cap W = \{0\}$.
2. So the [[sum|0RMKABS2S5]] $U + W$ is [[direct|041JTZCK9Q]].
3. The sum. $U + W = \{(a, b, 0) : a, b \in \R\}$, the $xy$-plane.
4. The vector $(0, 0, 1)$ is not of the form $(a, b, 0)$. So $U + W \ne \R^3$, and $\R^3 \ne U \oplus W$.
5. The [[dimension criterion|P4JG9DJ2HH]] predicts this: $\dim U + \dim W = 2 \ne 3$.

## Remarks

A direct sum $U \oplus W$ is always defined when $U \cap W = \{0\}$, but it is the subspace $U + W$, which can be smaller than $V$.
To get a decomposition of $\R^3$, we must add a third line outside the plane, such as the $z$-axis.

## Explanations

### L1 human

Two axes that cross only at the origin give a plane, not all of space.
They split the plane in a unique way, but they cannot reach points above or below it.

### L2 human

The statement $V = U \oplus W$ contains two claims: $U + W$ is direct, and $U + W = V$.
This example satisfies the first claim and fails the second.
