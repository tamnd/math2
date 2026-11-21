---
tag: PHDF089S8P
kind: example
name: Length and unit vector of (2, -1, 2)
msc: ["51N20", "97G70"]
topics: [VKVAJ94SKZ]
audience: school
instance_of: [0XKBKGTCPC]
uses: [0XKBKGTCPC, 0DZS7ZG0QY]
sources:
  - url: https://en.wikipedia.org/wiki/Unit_vector
    locator: lead section
---

## Example

Let $v = (2, -1, 2)$ in $\mathbb{R}^3$.
We compute its [[length|0DZS7ZG0QY]], the unit vector in its direction, and the length of $-5v$.

1. Square the components: $2^2 = 4$, $(-1)^2 = 1$ and $2^2 = 4$.
2. Add and take the root: $\|v\| = \sqrt{4 + 1 + 4} = \sqrt{9} = 3$.
3. Divide by the length to get the unit vector:
   $$\hat v = \tfrac{1}{3} v = \left(\tfrac{2}{3}, -\tfrac{1}{3}, \tfrac{2}{3}\right).$$
4. Check: $\|\hat v\|^2 = \tfrac{4}{9} + \tfrac{1}{9} + \tfrac{4}{9} = 1$, so $\hat v$ is a unit vector.
5. The vector $-5v = (-10, 5, -10)$ has the length $\sqrt{100 + 25 + 100} = \sqrt{225} = 15$.
6. This agrees with homogeneity: $\|-5v\| = |-5| \cdot \|v\| = 5 \cdot 3 = 15$.

## Remarks

The vector $(2, -1, 2)$ is chosen so that the length is a whole number.
For $v = (1, 1, 1)$ the length is $\sqrt{3}$, and the unit vector $\tfrac{1}{\sqrt{3}}(1, 1, 1)$ has irrational components, but the method is the same.
The components of a unit vector are the cosines of the angles that it makes with the axes.
Here they are $\tfrac{2}{3}$, $-\tfrac{1}{3}$ and $\tfrac{2}{3}$, and the [[direction cosines example|8NJY1C9GVH]] turns them into angles.

## Explanations

### L1 human

To find the length of $(2, -1, 2)$, square each number, add, and take the square root.
This gives $4 + 1 + 4 = 9$ and $\sqrt{9} = 3$.
Dividing each component by $3$ gives a vector with the same direction and length $1$.

### L2 human

A unit vector keeps only the direction of a vector.
You use it to step a given distance $d$ in a given direction: the step is $d \hat v$, and here a step of $6$ is $6 \hat v = (4, -2, 4)$.
Watch out: dividing by the length needs $v \neq 0$, and the zero vector has no unit vector.
