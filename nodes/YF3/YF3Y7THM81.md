---
tag: YF3Y7THM81
kind: example
name: The image of a non-linear map need not be a subspace
msc: ["15A04"]
topics: [9080WQTZ3M]
audience: ug1
not_instance_of:
  - target: 0WSFKKT6FF
    note: the map x ↦ (x, x²) is not linear, and its image, a parabola, contains (1, 1) and (−1, 1) but not their sum (0, 2)
uses: [0JB228DCWB, 0EPTJA5QV4, 0RJF668P1T]
sources:
  - url: https://en.wikipedia.org/wiki/Image_(mathematics)
    locator: lead section
---

## Example

A curved map can have a curved set of values, and a curve through the origin is still not a subspace.
Let $f \colon \R \to \R^2$ be $f(x) = (x, x^2)$, with set of values the parabola $P = \{(x, y) : y = x^2\}$.

1. The map $f$ is not a [[linear map|0RJF668P1T]], since $f(2) = (2, 4)$ while $2 f(1) = (2, 2)$.
2. The points $f(1) = (1, 1)$ and $f(-1) = (-1, 1)$ lie on $P$.
3. Their sum is $(0, 2)$, and a point $(0, y)$ of $P$ has $y = 0^2 = 0$, so $(0, 2) \notin P$.
4. So $P$ is not closed under addition, and $P$ is not a [[subspace|0EPTJA5QV4]] of $\R^2$.
5. The [[image of a linear map|0JB228DCWB]] is always a subspace, so $P$ is not the image of any linear map into $\R^2$.

## Remarks

The set $P$ contains $(0, 0) = f(0)$, so the test "is $0$ in the set?" does not detect the failure here.
The set $P$ also fails closure under scalar multiples: $2\,(1, 1) = (2, 2)$, but $2 \ne 2^2$.
The span of $P$ is all of $\R^2$, since $(1, 1)$ and $(-1, 1)$ are independent, so the smallest subspace containing $P$ is much larger than $P$.

If we replace $x^2$ by $3x$, the map $x \mapsto (x, 3x)$ is linear, and its set of values is the line $y = 3x$ through the origin, which is a subspace.

## Explanations

### L1 human

The outputs of $x \mapsto (x, x^2)$ form a parabola.
A parabola is curved, while a subspace of the plane is the origin alone, a line through the origin or the whole plane.
So this set is not the image of any linear map.

### L2 human

The example shows why linearity matters for the image to be a subspace.
For a non-linear map, a sum of outputs need not be an output.
Watch out: checking only that $0$ is an output is not enough, since the parabola passes that test.
