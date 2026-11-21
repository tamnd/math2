---
tag: WW2RB40VYX
kind: example
name: The taxicab length is not the Euclidean length
msc: ["51N20", "97G70"]
topics: [VKVAJ94SKZ]
audience: school
not_instance_of:
  - target: 0XKBKGTCPC
    note: the sum of the absolute values of the components is a norm, but it differs from the Euclidean length, for example 7 instead of 5 for (3, 4)
uses: [0XKBKGTCPC]
sources:
  - url: https://en.wikipedia.org/wiki/Taxicab_geometry
    locator: lead section
---

## Example

For a vector $v = (v_1, v_2)$ of the plane, let $\|v\|_1 = |v_1| + |v_2|$, the taxicab length.
We show that $\|v\|_1$ is not the [[Euclidean length|0XKBKGTCPC]] $\|v\|$, and that the two behave differently under rotations.

1. For $v = (3, 4)$ the taxicab length is $\|v\|_1 = 3 + 4 = 7$.
2. For the same $v$ the Euclidean length is $\|v\| = \sqrt{9 + 16} = 5$.
3. The values differ, so $\|\cdot\|_1$ is not the Euclidean length.
4. The rotation by $45^\circ$ sends $(1, 0)$ to $\left(\tfrac{1}{\sqrt{2}}, \tfrac{1}{\sqrt{2}}\right)$. The taxicab length changes from $1$ to
   $$\tfrac{1}{\sqrt{2}} + \tfrac{1}{\sqrt{2}} = \sqrt{2}.$$
5. The Euclidean length of $\left(\tfrac{1}{\sqrt{2}}, \tfrac{1}{\sqrt{2}}\right)$ is $\sqrt{\tfrac{1}{2} + \tfrac{1}{2}} = 1$, the same as for $(1, 0)$.

## Remarks

The taxicab length has the three properties of a norm: positivity, homogeneity and the triangle inequality.
So it is a norm, only a different one, and it measures the distance that a car drives in a city with a square grid of streets.
The two lengths agree on vectors along an axis, such as $(5, 0)$, and they differ most on the diagonals, where the ratio is $\sqrt{2}$.
Step 4 is the real difference: a rotation keeps the Euclidean length, and every norm on the plane that no rotation changes is a constant multiple of the Euclidean length.

## Explanations

### L1 human

A taxi in a city with square blocks cannot drive along a diagonal.
To go 3 blocks east and 4 blocks north it drives $7$ blocks.
A bird flies straight and covers only $5$ blocks.
The length of a vector is the distance of the bird.

### L2 human

Why is a norm that rotations do not change a multiple of the Euclidean length?
Each vector is a rotation of a vector on the positive $x$-axis of the same Euclidean length, and on that axis homogeneity fixes the norm as $c$ times the length, with $c$ the norm of $(1, 0)$.
Step 4 shows that the taxicab length fails the hypothesis.
Watch out: two norms can agree on many vectors, here on the axes, and still be different norms.
