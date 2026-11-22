---
tag: 6SWBRH6W8X
kind: example
name: The Gram-Schmidt process fails on a dependent family
msc: ["15A63", "65F25"]
topics: [1D4JTZ9VS3]
audience: ug1
not_instance_of:
  - target: 0VT6P0GNQR
    note: the family (1, 2), (2, 4) is linearly dependent, the process gives u_2 = 0, and u_2 cannot be normalized
uses: [A1Y41YZFB6, 0EVHJFTG9Z]
sources:
  - url: https://en.wikipedia.org/wiki/Gram–Schmidt_process
    locator: Properties
---

## Example

In $\mathbb{R}^2$ with the dot product, let $v_1 = (1, 2)$ and $v_2 = (2, 4)$.
This list is not a valid input of the Gram-Schmidt process, and running the recursion anyway shows where it breaks.

1. The list is [[linearly dependent|0EVHJFTG9Z]], since $2v_1 - v_2 = (2, 4) - (2, 4) = 0$, so the hypothesis of the [[Gram-Schmidt process|A1Y41YZFB6]] fails.
2. The first step still works: $u_1 = (1, 2)$, with $u_1 \cdot u_1 = 1 + 4 = 5$.
3. The second step computes $v_2 \cdot u_1 = 2 + 8 = 10$, so the coefficient is $\tfrac{10}{5} = 2$.
4. Subtracting the shadow leaves nothing: $u_2 = (2, 4) - 2(1, 2) = (0, 0)$.
5. The normalization $e_2 = u_2 / \norm{u_2}$ would divide by $\norm{u_2} = 0$, so the process does not produce an orthonormal list of two vectors.

## Remarks

The example shows exactly why the process needs independence.
In general $u_j = 0$ happens precisely when $v_j$ lies in the span of $v_1, \dots, v_{j-1}$, because $u_j$ is $v_j$ minus its projection onto that span.
So the process doubles as a test for independence: run it and look for a zero vector.

If we skip the zero vector, the output $e_1 = \tfrac{1}{\sqrt5}(1, 2)$ is an orthonormal basis of the span, which is a line.

A small change of one number restores independence.
For $v_2 = (2, 4 + t)$ with $t \neq 0$, we get $v_2 \cdot u_1 = 10 + 2t$ and
$$u_2 = (2, 4 + t) - \frac{10 + 2t}{5}(1, 2) = \left(-\tfrac{2t}{5}, \tfrac{t}{5}\right) = \tfrac{t}{5}(-2, 1),$$
which is nonzero and orthogonal to $(1, 2)$.
As $t$ shrinks, $u_2$ shrinks with it, and on a computer the division by a tiny $\norm{u_2}$ magnifies rounding errors.

## Explanations

### L1 human

The two arrows $(1, 2)$ and $(2, 4)$ lie on the same line, and the second is twice the first.
When we remove from the second arrow its part along the first one, nothing is left.
A zero arrow has no direction, so we cannot stretch it to length $1$.
So the process cannot produce a second perpendicular direction, and indeed the two arrows only ever reach one line.

### L2 human

Here is the typical use of the failure: to find an orthonormal basis of the span of a list that may be dependent, run the process and drop each zero vector.
Take $v_1 = (1, 0, 1)$, $v_2 = (2, 0, 2)$ and $v_3 = (0, 1, 0)$ in $\mathbb{R}^3$.
First $u_1 = v_1$ with $u_1 \cdot u_1 = 2$.
Next $v_2 \cdot u_1 = 4$, so
$$u_2 = (2, 0, 2) - \tfrac42 (1, 0, 1) = 0,$$
and we drop it.
Then $v_3 \cdot u_1 = 0$, so $u_3 = (0, 1, 0)$.
So $\tfrac{1}{\sqrt2}(1, 0, 1)$ and $(0, 1, 0)$ form an orthonormal basis of the span, and the span has dimension $2$.
This computes the rank and an orthonormal basis of a column space in one pass.
Watch out: in floating point, test whether $\norm{u_j}$ is below a tolerance, not whether $u_j = 0$ exactly.
