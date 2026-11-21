---
tag: DPADSQ4DFJ
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
We compute $u$ and $u + v$, check that the sum is the diagonal of a parallelogram, and compute two multiples of $u$.

1. By the [[definition of a vector between two points|00EBGSR5NY]], $u$ is end minus start:
   $$u = B - A = (4 - 1, \; 6 - 2) = (3, 4).$$
2. The sum is taken component by component:
   $$u + v = (3 + 2, \; 4 + (-1)) = (5, 3).$$
3. Draw both vectors from $A$. The arrow $u$ ends at $B = (4, 6)$, and the arrow $v$ ends at $D = A + v = (3, 1)$.
4. Let $C = A + (u + v) = (6, 5)$. Then the two remaining sides are
   $$C - B = (2, -1) = v, \qquad C - D = (3, 4) = u.$$
5. Step 4 says that $\overrightarrow{BC} = \overrightarrow{AD}$ and $\overrightarrow{DC} = \overrightarrow{AB}$, so opposite sides of $ABCD$ are equal and parallel. Hence $ABCD$ is a parallelogram, and its diagonal $\overrightarrow{AC}$ is $u + v$.
6. The multiples are $2u = (6, 8)$ and $-u = (-3, -4)$, and $-u$ is the arrow $\overrightarrow{BA}$ from $B$ back to $A$.

## Remarks

The coordinate rule for the sum and the parallelogram rule give the same vector, and the triangle rule is hidden in step 4 as well: $\overrightarrow{AB} + \overrightarrow{BC} = u + v = \overrightarrow{AC}$.
The parallelogram becomes flat when $v$ is a multiple of $u$.
For $v = cu$ the sum $u + cu = (1 + c)u$ lies on the line of $u$, and the "parallelogram" is a segment.
If you move the start point $A$, the points $B$, $C$ and $D$ move by the same translation, but $u$, $v$ and $u + v$ do not change, because a vector has no fixed start.

## Explanations

### L1 human

Walk 3 steps right and 4 steps up, then 2 steps right and 1 step down.
In total you walk 5 steps right and 3 steps up.
You can also do the two moves in the other order and arrive at the same place.
The two routes are the two pairs of sides of a parallelogram, and the total move is its diagonal.

### L2 human

The parallelogram rule is the picture of the coordinate rule $u + v = (u_1 + v_1, u_2 + v_2)$.
Draw $u$ and $v$ from one point, complete the parallelogram, and take the diagonal from the common start point.
Watch out: the other diagonal is not the sum.
It runs from the end of $v$ to the end of $u$, so it is
$$B - D = (4, 6) - (3, 1) = (1, 5) = u - v.$$
