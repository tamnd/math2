---
tag: FWNY6EYBC3
kind: example
name: The affine functions on the plane are not its dual space
msc: ["15A04"]
topics: [9K7FFF26QR]
audience: ug1
not_instance_of:
  - target: 07JBSZE0V4
    note: the space of affine functions ax + by + c on R^2 has dimension 3 and contains the constant 1, which is not linear
uses: [0M856Q1AMZ, 0RT96J4D3H, 0VTQTPQGAV, 05G2G0P224, 00YC1D652K]
sources:
  - url: https://en.wikipedia.org/wiki/Linear_form
    locator: Non-example
---

## Example

Let $A$ be the set of functions $g \colon \R^2 \to \R$ of the form $g(x, y) = ax + by + c$ with $a, b, c \in \R$.
With the pointwise operations, $A$ is a vector space, because sums and multiples of such functions have the same form.
We show that $A$ is not the [[dual space|0M856Q1AMZ]] $(\R^2)^*$, in two ways: one element of $A$ fails linearity, and the dimensions differ.

1. The constant function $1$ lies in $A$, with $a = b = 0$ and $c = 1$.
2. Every [[linear form|0RT96J4D3H]] $f$ sends the origin to $0$, because
$$f(0, 0) = f\big(0 \cdot (0, 0)\big) = 0 \cdot f(0, 0) = 0.$$
3. The constant function $1$ takes the value $1 \ne 0$ at $(0, 0)$. So it is not a linear form, and $A \ne (\R^2)^*$.
4. The functions $1, x, y$ span $A$, by the definition of $A$.
5. They are independent. If $c + ax + by = 0$ at every point, then the point $(0, 0)$ gives $c = 0$, the point $(1, 0)$ gives $a = 0$, and the point $(0, 1)$ gives $b = 0$.
6. So $1, x, y$ is a [[basis|0VTQTPQGAV]] of $A$, and $\dim A = 3$. Since $\dim (\R^2)^* = 2$, the [[dimensions|05G2G0P224]] also show that the spaces differ.
7. The linear forms are the elements of $A$ with $c = 0$, and they form a [[subspace|00YC1D652K]] of $A$ of dimension $2$.

## Remarks

The example separates two words that school mathematics often mixes.
A function such as $x \mapsto 3x + 1$ is often called linear in school, but in linear algebra it is affine, and only the case $c = 0$ is a linear form.
Each affine function is a linear form plus a constant, $g = f + g(0, 0)$ with $f$ linear, so $A \cong (\R^2)^* \oplus \R$.

The difference also shows in the geometry.
The zero sets $\{g = 0\}$ of nonconstant affine functions are all the lines of the plane, including those that miss the origin.
The kernels of nonzero linear forms are only the lines through the origin.
If we move the origin to $(1, 0)$, the linear form $x$ becomes the affine function $x + 1$ in the new coordinates, so the notion of a linear form depends on the choice of origin.

## Explanations

### L1 human

The function $3x + 2y + 1$ on the plane is not a linear form, because it gives $1$ at the origin instead of $0$.
Linear forms are the functions $ax + by$ with no constant term.
Allowing the constant term gives a larger space, of dimension $3$ instead of $2$.

### L2 human

To test whether a function belongs to the dual space, a quick first test is its value at the origin.
For $g(x, y) = 2x - y + 4$ we get $g(0, 0) = 4 \ne 0$, so $g$ is not a linear form.
For $g(x, y) = 2x - y$ we get $g(0, 0) = 0$, and in this case the formula $ax + by$ shows that $g$ is linear.
The typical use is to keep the words linear and affine apart.
Watch out: for general functions the test $g(0) = 0$ is necessary but not sufficient.
The function $(x, y) \mapsto xy$ is zero at the origin, but $(1, 1)$ gives $1$ and $(2, 2)$ gives $4$, not $2$, so it is not linear.
