---
tag: ~8b8b3ceb
kind: example
name: Adding two vectors in the plane by the parallelogram rule
msc: ["51N20", "97G70"]
topics: [VKVAJ94SKZ]
audience: school
instance_of: [0QN3D80AWP]
uses: [0QN3D80AWP, 00EBGSR5NY]
sources:
  - url: https://en.wikipedia.org/wiki/Euclidean_vector
    locator: Addition and subtraction
---

## Example

Let $A = (1, 2)$ and $B = (4, 6)$ be points of the plane, let $u = \overrightarrow{AB}$, and let $v = (2, -1)$.
We compute $u$, the sum $u + v$ and two scalar multiples, and we check the parallelogram rule.

1. By the [[definition of a vector between two points|00EBGSR5NY]], $u = B - A = (4 - 1, 6 - 2) = (3, 4)$.
2. The sum is computed component by component: $u + v = (3 + 2, 4 + (-1)) = (5, 3)$.
3. We draw both vectors from $A$. The end of $u$ is $B = (4, 6)$, and the end of $v$ is $D = A + v = (3, 1)$.
4. Let $C = A + (u + v) = (6, 5)$. Then $C - B = (2, -1) = v$ and $C - D = (3, 4) = u$.
5. Step 4 shows that $\overrightarrow{BC} = \overrightarrow{AD}$ and $\overrightarrow{DC} = \overrightarrow{AB}$. So $ABCD$ is a parallelogram, and its diagonal $\overrightarrow{AC}$ is $u + v$.
6. The scalar multiples are $2u = (6, 8)$ and $-u = (-3, -4)$. The vector $-u$ is $\overrightarrow{BA}$.

## Remarks

The example shows that the coordinate rule for the sum and the parallelogram rule give the same vector.
The triangle rule is in step 4 too: $\overrightarrow{AB} + \overrightarrow{BC} = u + v = \overrightarrow{AC}$.
If we replace $v$ by $cu$ for a real number $c$, the parallelogram is flat, and $u + cu = (1 + c)u$ lies on the line of $u$.
If we move the start point $A$, the points $B$, $C$ and $D$ move by the same translation, but $u$, $v$ and $u + v$ do not change.

## Explanations

### L1 human

Walk 3 steps right and 4 steps up, then 2 steps right and 1 step down.
In total we walk 5 steps right and 3 steps up.
We can also walk the two moves in the other order and arrive at the same place.
The two routes are the two sides of a parallelogram, and the total move is its diagonal.

### L2 human

The parallelogram rule is the picture of the coordinate rule $u + v = (u_1 + v_1, u_2 + v_2)$.

1. Draw $u$ and $v$ from one point.
2. Complete the parallelogram.
3. The diagonal from the common start point is $u + v$.

A trap: the other diagonal, from the end of $v$ to the end of $u$, is $u - v = (1, 5)$, not $u + v$.
