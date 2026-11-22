---
tag: CX9P5CZF5N
kind: example
name: A two-dimensional quotient of R⁴
msc: ["15A03"]
topics: [QHKTJ89V6S]
audience: ug1
instance_of: [0BR3FY5Q8M]
illustrates: [0SXDQ6TN00]
uses: [0SVR29SV1V, 0VTQTPQGAV, 05G2G0P224]
sources:
  - url: https://en.wikipedia.org/wiki/Quotient_space_(linear_algebra)
    locator: Properties
---

## Example

Let $V = \R^4$ and $W = \operatorname{span}\{(1, 0, 1, 0), (0, 1, 0, 1)\}$.
We check the [[dimension formula|0SXDQ6TN00]] by finding a basis of the [[quotient space|0SVR29SV1V]] $V / W$, and we compute the coordinates of one coset.

1. The vectors $w_1 = (1, 0, 1, 0)$ and $w_2 = (0, 1, 0, 1)$ are independent, since neither is a multiple of the other.
   So $\dim W = 2$.
2. Add $e_1 = (1, 0, 0, 0)$ and $e_2 = (0, 1, 0, 0)$.
   Then $e_3 = w_1 - e_1$ and $e_4 = w_2 - e_2$, so $w_1, w_2, e_1, e_2$ span $\R^4$.
   Four spanning vectors in a space of [[dimension|05G2G0P224]] $4$ form a [[basis|0VTQTPQGAV]].
3. By the proof of the dimension formula, the cosets $e_1 + W$ and $e_2 + W$ form a basis of $V / W$.
   So $\dim(V / W) = 2 = 4 - 2$.
4. To find the coordinates of the coset of $v = (3, 5, 7, 2)$, solve $v = a w_1 + b w_2 + c e_1 + d e_2$, that is,
   $$(3, 5, 7, 2) = (a + c, \ b + d, \ a, \ b).$$
   The third entry gives $a = 7$ and the fourth gives $b = 2$.
   Then the first gives $c = 3 - 7 = -4$, and the second gives $d = 5 - 2 = 3$.
5. The terms $a w_1 + b w_2$ lie in $W$ and vanish in the quotient, so
   $$(3, 5, 7, 2) + W = -4(e_1 + W) + 3(e_2 + W).$$

Check: $(3, 5, 7, 2) - (-4e_1 + 3e_2) = (7, 2, 7, 2) = 7 w_1 + 2 w_2 \in W$.

## Remarks

The map $(x_1, x_2, x_3, x_4) \mapsto (x_1 - x_3, x_2 - x_4)$ from $\R^4$ to $\R^2$ is linear and surjective, and its kernel is $W$.
So it induces an isomorphism $V / W \cong \R^2$, which sends $e_1 + W$ to $(1, 0)$ and $e_2 + W$ to $(0, 1)$.
For $v = (3, 5, 7, 2)$ it gives $(3 - 7, 5 - 2) = (-4, 3)$, which matches step 5.

The choice of $e_1, e_2$ is not forced.
With $e_3, e_4$ instead, the basis of the quotient is $e_3 + W$, $e_4 + W$, and since $e_3 + W = -(e_1 + W)$ and $e_4 + W = -(e_2 + W)$, the coordinates of the same coset become $(4, -3)$.

## Explanations

### L1 human

The subspace $W$ ties the first entry to the third and the second entry to the fourth.
Modulo $W$, only the differences $x_1 - x_3$ and $x_2 - x_4$ matter.
These are two numbers, so the quotient is a plane.

### L2 human

The coordinates of a coset do not depend on the representative.
Take the other representative $v + w_1 = (4, 5, 8, 2)$ of the same coset.
The same computation gives $a = 8$, $b = 2$, $c = 4 - 8 = -4$ and $d = 5 - 2 = 3$.
So the coset again has coordinates $(-4, 3)$, as it must.
The typical use of the example is the recipe it shows: extend a basis of $W$ to a basis of $V$, and keep the cosets of the new vectors.
