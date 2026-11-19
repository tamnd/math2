---
tag: TFGECQ5C32
kind: example
name: The Minkowski form on the plane is not a dot product
msc: ["15A63", "97G70"]
topics: [VKVAJ94SKZ]
audience: ug1
not_instance_of:
  - target: 0S52TNNTH9
    note: the form u_1 v_1 - u_2 v_2 is symmetric and bilinear, but the nonzero vector (1, 1) has square 0, so the form is not positive
uses: [0S52TNNTH9]
sources:
  - url: https://en.wikipedia.org/wiki/Minkowski_space
    locator: Minkowski metric
---

## Example

For $u, v \in \mathbb{R}^2$ let $u \star v = u_1 v_1 - u_2 v_2$.
This form has two of the three basic properties of the [[dot product|0S52TNNTH9]], but not the third.

1. Symmetry holds: $v \star u = v_1 u_1 - v_2 u_2 = u \star v$, by the commutativity of real multiplication.
2. Linearity in $u$ holds: $(au + bw) \star v = (au_1 + bw_1)v_1 - (au_2 + bw_2)v_2 = a(u \star v) + b(w \star v)$.
3. Positivity fails. Let $u = (1, 1)$. Then $u \star u = 1 - 1 = 0$, but $u \neq 0$.
4. Positivity fails in a second way. Let $u = (0, 1)$. Then $u \star u = -1 < 0$, so $\sqrt{u \star u}$ is not a real number.
5. So the form gives no length: a "length" from $\star$ would be $0$ for $(1, 1)$ and undefined for $(0, 1)$.

## Remarks

The example shows that positivity is a separate condition, and it does not follow from symmetry and bilinearity.
The form $\star$ is the Minkowski form of special relativity in one space dimension, with the time coordinate first.
Vectors with $u \star u = 0$, such as $(1, 1)$, are light-like.
If we change the sign to $u_1 v_1 + u_2 v_2$, we get the dot product back.

## Explanations

### L1 human

The dot product of a vector with itself is the square of its length, so it is never negative.
The form here subtracts the second product instead of adding it.
Then the vector $(1, 1)$ gets the value $1 - 1 = 0$, as if it had length $0$.
A real nonzero arrow cannot have length $0$, so this form is not a dot product.

### L2 human

To test whether a symmetric bilinear form is an inner product, test $u \star u > 0$ for all $u \neq 0$.
One vector with $u \star u \leq 0$ and $u \neq 0$ is enough to show that the form is not one.
A trap: positive values on the basis vectors do not prove positivity.
The form $u_1 v_1 - 2u_1 v_2 - 2u_2 v_1 + u_2 v_2$ gives $1$ on $(1, 0)$ and on $(0, 1)$, but $-2$ on $(1, 1)$.
