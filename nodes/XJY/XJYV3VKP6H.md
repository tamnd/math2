---
tag: XJYV3VKP6H
kind: example
name: Symmetry does not place an extremum at the symmetric point
msc: ["00A35", "26B12"]
topics: [MEKKHHQTKB]
audience: school
not_instance_of:
  - target: H840D9TM2X
    note: the problem has two extremal points that the symmetry exchanges, so symmetry does not force the extremum to the fixed point
uses: [H840D9TM2X]
sources:
  - url: https://en.wikipedia.org/wiki/Symmetry_in_mathematics
    locator: lead section
  - book: isbn:9780691164076
    locator: Part III
---

## Example

Let $F(x, y) = x^2 + y^2$ on the segment
$$K = \{(x, y) \in \mathbb{R}^2 : x + y = 2,\ x \ge 0,\ y \ge 0\}.$$
Both $F$ and $K$ are unchanged by the exchange $(x, y) \mapsto (y, x)$, and the only point of $K$ that the exchange fixes is $(1, 1)$.
A student argues: "by symmetry, the maximum of $F$ on $K$ is at $(1, 1)$".
The claim is false, so the argument is not a valid [[symmetry argument|H840D9TM2X]].

1. On $K$, $y = 2 - x$ with $0 \le x \le 2$, so $F = x^2 + (2 - x)^2 = 2(x - 1)^2 + 2$.
2. Since $(x - 1)^2 \ge 0$, $F \ge 2$ on $K$, with equality only at $x = 1$, so the minimum $2$ is at the symmetric point $(1, 1)$.
3. Since $\lvert x - 1 \rvert \le 1$ on $K$, $F \le 4$, with equality only at $x = 0$ and $x = 2$.
4. So the maximum is $4$, at $(0, 2)$ and $(2, 0)$, and neither is the symmetric point.

The student's "maximum" $F(1, 1) = 2$ is in fact the minimum.

## Remarks

The symmetry does give a true conclusion: the exchange maps the set of maximum points to itself.
Here that set is $\{(0, 2), (2, 0)\}$, and the exchange swaps its two points.
A symmetry forces an answer onto the fixed point only when the answer is unique, and the maximum here is not.

The minimum lies at the symmetric point for an extra reason, the convexity of $F$, and not by symmetry alone.
For a convex symmetric function on a convex symmetric set, the average of a minimum point and its image is at least as good, so some minimum point is symmetric.
On the same segment, $G(x, y) = xy = 1 - (x - 1)^2$ has its maximum $1$ at $(1, 1)$ and its minimum $0$ at $(0, 2)$ and $(2, 0)$.
So the symmetric point can be a maximum, a minimum, or neither.

## Explanations

### L1 human

Two numbers that are not negative add up to $2$.
When is the sum of their squares largest?
The guess "when the numbers are equal" gives $1^2 + 1^2 = 2$.
But $2^2 + 0^2 = 4$ is larger, so the guess is wrong.
The two best choices, $2$ and $0$ or $0$ and $2$, are mirror images, and symmetry only says that they come as a pair.

### L2 human

We test the same claim in three variables: maximize $x^2 + y^2 + z^2$ on $x + y + z = 3$ with $x, y, z \ge 0$.

1. At the symmetric point $(1, 1, 1)$ the value is $3$.
2. At $(3, 0, 0)$ the value is $9$, so the symmetric point is not the maximum.
3. On the whole set, $x^2 + y^2 + z^2 \le (x + y + z)^2 = 9$, because the cross terms $2xy + 2yz + 2zx$ are not negative.
4. So the maximum is $9$, at $(3, 0, 0)$, $(0, 3, 0)$ and $(0, 0, 3)$, which form one orbit under permutations of the coordinates.

Read this example as a warning before any "by symmetry" step in an optimization problem.
Watch out: "the problem is symmetric" does not mean "the answer is symmetric"; only a unique answer must be.
