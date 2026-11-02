---
tag: 12V4MHVV0N
kind: example
name: Baker's map
msc: [37A05, 37A25, 37D20]
instance_of: [556WBDAHNP, S3RJQ9CX2P]
uses: [2Z2QVWZ262, D33JK3AXRZ, X1D1C7VH6P]
sources:
  - url: https://en.wikipedia.org/wiki/Baker%27s_map
same_as:
  wikidata: Q1018917
  wikipedia: Baker's map
---

## Example

Let $X = [0, 1) \times [0, 1)$ be the unit square with two-dimensional [[Lebesgue measure|2Z2QVWZ262]] $\lambda$.
The *baker's map* $B \colon X \to X$ is $B(x, y) = (2x, y/2)$ for $0 \le x < 1/2$.
For $1/2 \le x < 1$, it is $B(x, y) = (2x - 1, (y + 1)/2)$.
It stretches the square to twice its width and half its height.
Then it cuts the result in two and stacks the right half on top of the left half, as a baker folds dough.

It is a bijection: the left half $[0, 1/2) \times [0, 1)$ goes onto the bottom half $[0, 1) \times [0, 1/2)$, and the right half goes onto the top half.
On each half, $B$ is affine with Jacobian determinant $2 \cdot \frac{1}{2} = 1$, so $\lambda(B^{-1} E) = \lambda(E)$ for every Borel set $E$, and $B$ is a [[measure-preserving transformation|556WBDAHNP]].

Write $x = 0.x_1 x_2 x_3 \dots$ and $y = 0.y_1 y_2 y_3 \dots$ in binary, and code the point $(x, y)$ by the two-sided sequence $\dots y_2 y_1 . x_1 x_2 \dots$.
Then $B$ moves the binary point one step to the right: the digit $x_1$ leaves $x$ and becomes the first digit of the new $y$.
This coding is an isomorphism, up to null sets, from $B$ to the two-sided [[Bernoulli scheme|D33JK3AXRZ]] $B(1/2, 1/2)$.
Hence $B$ is invertible, [[mixing|S3RJQ9CX2P]], and has [[Kolmogorov–Sinai entropy|X1D1C7VH6P]] $\log 2$.

## Explanations

### L1 human

Roll the dough out to double length, cut it in the middle, and put one piece on top of the other.
The area of the dough does not change, so the map preserves area.
Two raisins that start close together in the horizontal direction are pulled apart, doubling their distance at each step, while vertical distances shrink.
After many steps any small blob of dye is spread in thin layers across the whole square, which is what mixing means.
The baker's map is the invertible partner of the doubling map.
