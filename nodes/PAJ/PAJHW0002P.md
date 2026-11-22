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
We check that the sum $U + W$ is direct, but that it is not all of $\R^3$.

1. Intersection.
   If $a(1, 0, 0) = b(0, 1, 0)$, then comparing coordinates gives $a = 0$ and $b = 0$.
   So $U \cap W = \{0\}$, and the [[sum|0RMKABS2S5]] $U + W$ is [[direct|041JTZCK9Q]].
2. The sum.
   Every vector of $U + W$ has the form $a(1, 0, 0) + b(0, 1, 0) = (a, b, 0)$, so $U + W$ is the $xy$-plane.
3. The missing vector.
   The vector $(0, 0, 1)$ has third coordinate $1$, so it is not of the form $(a, b, 0)$.
   So $U + W \ne \R^3$, and $\R^3 \ne U \oplus W$.
4. The [[dimension criterion|P4JG9DJ2HH]] predicts this, since $\dim U + \dim W = 2 \ne 3$.

## Remarks

### What the example shows

The statement $V = U \oplus W$ contains two claims: the sum $U + W$ is direct, and it equals $V$.
This example satisfies the first claim and fails the second.
A direct sum $U \oplus W$ makes sense whenever $U \cap W = \{0\}$, but it is the subspace $U + W$, which can be smaller than $V$.

### How to repair it

To get a decomposition of $\R^3$, add a third line outside the $xy$-plane.
With the $z$-axis, $\R^3 = U \oplus W \oplus \R(0, 0, 1)$, and $(x, y, z) = (x, 0, 0) + (0, y, 0) + (0, 0, z)$.
Any line $\R(p, q, r)$ with $r \ne 0$ works just as well, since it meets the $xy$-plane only in $0$.

## Explanations

### L1 human

Two axes that cross only at the origin give a flat plane, not all of space.
Inside that plane every point splits in exactly one way, but points above or below the plane cannot be reached at all.

### L2 human

The two halves of a direct sum decomposition must be checked separately.
Here the intersection test passes in one line: $a(1, 0, 0) = b(0, 1, 0)$ forces $a = b = 0$.
The spanning test fails, and the quickest way to see it is the count $1 + 1 = 2 < 3$.
Watch out: the intersection test alone never shows that a sum fills the space.
