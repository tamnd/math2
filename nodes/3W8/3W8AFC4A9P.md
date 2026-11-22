---
tag: 3W8AFC4A9P
kind: example
name: The bilinear dot product on C2 is not an inner product
msc: ["15A63"]
topics: [1D4JTZ9VS3]
audience: ug1
not_instance_of:
  - target: 0NB0AWGJBW
    note: the form x_1 y_1 + x_2 y_2 on C^2 is bilinear and symmetric, but it is not conjugate symmetric, and it gives 0 on the nonzero vector (1, i) and -1 on (i, 0)
uses: [0VGSYBWHV2, 0SQZMXB6GP]
sources:
  - url: https://en.wikipedia.org/wiki/Inner_product_space
    locator: Complex coordinate space
---

## Example

On $\mathbb{C}^2$ let
$$\beta(x, y) = x_1 y_1 + x_2 y_2.$$
This is the formula of the real dot product, applied to complex vectors without conjugates.
We check the three axioms of an [[inner product|0VGSYBWHV2]] one at a time.

1. Linearity in the first slot holds:
$$\beta(ax + bz, y) = (ax_1 + bz_1)y_1 + (ax_2 + bz_2)y_2 = a\beta(x, y) + b\beta(z, y).$$
2. Conjugate symmetry fails.
For $x = (i, 0)$ and $y = (1, 0)$ we get $\beta(x, y) = i$ and $\beta(y, x) = i$, but the axiom asks for $\beta(y, x) = \overline{i} = -i$.
3. Positive definiteness fails at a nonzero vector with value $0$.
For $x = (1, i)$ we get $\beta(x, x) = 1 + i^2 = 0$.
4. Positive definiteness also fails at a vector with a negative value.
For $x = (i, 0)$ we get $\beta(x, x) = i^2 = -1$.

So $\beta$ is a symmetric [[bilinear form|0SQZMXB6GP]], but it is not an inner product.

## Remarks

The example shows why a complex inner product needs a conjugate.
Put a bar on the second factor and the formula becomes $x_1 \overline{y_1} + x_2 \overline{y_2}$, the [[standard inner product on $\mathbb{C}^2$|TFZ8DYVJ1J]].
Then $(1, i)$ gets $1 \cdot 1 + i \cdot \overline{i} = 1 + 1 = 2$, the square of its length.

The failure has nothing to do with the dimension.
For any symmetric bilinear form $\beta$ over $\mathbb{C}$, bilinearity gives $\beta(ix, ix) = i^2 \beta(x, x) = -\beta(x, x)$.
So if $\beta(x, x) > 0$ for one vector, then $\beta(ix, ix) < 0$, and no such form is positive definite on a nonzero space.
Already on $\mathbb{C}$ itself, the number $i$ gives $i \cdot i = -1$.

## Explanations

### L1 human

For real vectors, a vector times itself gives a sum of squares, which is never negative.
For complex numbers a square can be negative, since $i \cdot i = -1$.
So the plain formula $x_1 y_1 + x_2 y_2$ can give a negative "squared length", or $0$ for a nonzero vector such as $(1, i)$.
The cure is to conjugate the second vector, because $i$ times the conjugate of $i$ is $1$.

### L2 human

To show that a formula is not an inner product, one vector where it fails is enough.
A good first try over $\mathbb{C}$ is a basis vector times $i$, such as $x = (i, 0)$.
The computation is one line:
$$\beta(x, x) = i \cdot i + 0 \cdot 0 = -1.$$
A negative value violates positive definiteness, so $\beta$ is not an inner product.
This test catches a missing conjugate in a formula over $\mathbb{C}$.
Watch out: the form is fine on real vectors, so tests with real entries only will never find the error.
