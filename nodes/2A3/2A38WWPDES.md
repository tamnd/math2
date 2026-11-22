---
tag: 2A38WWPDES
kind: example
name: The bilinear dot product on the complex plane is not sesquilinear
msc: ["15A63"]
topics: [DYAK7YMK7B]
audience: ug1
instance_of: [0AXZNE5XNH]
not_instance_of:
  - target: 054YEQ0Y8M
    note: B(x, y) = x_1 y_1 + x_2 y_2 on C^2 is linear in y, so B(e_1, i e_1) = i, while a sesquilinear form gives -i h(e_1, e_1)
uses: [0W44K2VNBD, 0P799D6AMN, 3W8AFC4A9P]
sources:
  - url: https://en.wikipedia.org/wiki/Sesquilinear_form
    locator: Informal introduction
---

## Example

On $\mathbb{C}^2$ let
$$B(x, y) = x_1 y_1 + x_2 y_2,$$
the real dot product formula used on complex vectors, with no conjugation.
We show that $B$ is a symmetric bilinear form over $\mathbb{C}$ and that it is not sesquilinear.

1. $B$ is linear in $x$ for fixed $y$, and linear in $y$ for fixed $x$, because each term $x_k y_k$ is a product of one coordinate of $x$ and one coordinate of $y$. So $B$ is a [[bilinear form|0P799D6AMN]] over $\mathbb{C}$.
2. $B(y, x) = y_1 x_1 + y_2 x_2 = B(x, y)$, since complex multiplication is commutative. So $B$ is symmetric.
3. A [[sesquilinear form|0W44K2VNBD]] $h$, in our convention, is conjugate-linear in the second slot, so it gives $h(x, iy) = \bar{i}\, h(x, y) = -i\, h(x, y)$.
4. For $B$ take $x = y = e_1$:
$$B(e_1, i e_1) = 1 \cdot i = i, \qquad -i\, B(e_1, e_1) = -i.$$
5. Since $i \ne -i$, the rule of step 3 fails, and $B$ is not sesquilinear.

## Remarks

The example shows why the complex inner product needs a conjugate.
The vector $v = (1, i)$ is not zero, but
$$B(v, v) = 1 \cdot 1 + i \cdot i = 1 - 1 = 0,$$
and for every $v$ we get $B(iv, iv) = i^2 B(v, v) = -B(v, v)$.
So no nonzero complex bilinear form on $\mathbb{C}^2$ can be positive, and the example [[the bilinear dot product on C2 is not an inner product|3W8AFC4A9P]] treats the same form from the side of inner products.
The repair is to conjugate the second slot, which gives $x_1 \bar y_1 + x_2 \bar y_2$, the [[standard inner product|TFZ8DYVJ1J]].

Could a form be bilinear and sesquilinear at once?
Then $a\, h(x, y) = h(x, ay) = \bar a\, h(x, y)$ for every $a \in \mathbb{C}$, and $a = i$ gives $2i\, h(x, y) = 0$.
So only the zero form is both.
Over $\mathbb{R}$ the question does not arise, because $\bar a = a$ for every real $a$ and the two notions agree.

## Explanations

### L1 human

The rule "multiply matching entries and add" works well for real vectors.
Used on complex vectors, it gives $(1, i)$ paired with itself the value $1 + i^2 = 0$.
So the rule cannot measure length, and it does not conjugate the second vector as the complex rules do.

### L2 human

To test whether a form on $\mathbb{C}^n$ is sesquilinear in our convention, pick one pair with $h(x, y) \ne 0$ and compute $h(x, iy)$.
A sesquilinear form gives $-i\, h(x, y)$, and a bilinear form gives $i\, h(x, y)$.
For $B$ above and $x = y = (1, 1)$, we get $B(x, y) = 2$ and $B(x, iy) = 2i$, so $B$ is bilinear, not sesquilinear.
Watch out: books in physics conjugate the first slot, so there the test is $h(ix, y) = -i\, h(x, y)$.
