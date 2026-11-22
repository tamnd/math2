---
tag: TFZ8DYVJ1J
kind: example
name: The standard inner product on Cn
msc: ["15A63"]
topics: [1D4JTZ9VS3]
audience: ug1
instance_of: [0NB0AWGJBW, 0QVNCJXRY3, 0MFJJV97RJ]
uses: [0VGSYBWHV2, 0BJV24C4SY, 0KW2X0TFBX, 0DXKE10PHF]
sources:
  - url: https://en.wikipedia.org/wiki/Inner_product_space
    locator: Complex coordinate space
  - book: isbn:9783031410253
    locator: Chapter 6
---

## Example

On $\mathbb{C}^n$ put
$$\ip{x}{y} = x_1 \overline{y_1} + x_2 \overline{y_2} + \dots + x_n \overline{y_n},$$
where the bar is the [[complex conjugate|0BJV24C4SY]].
With $x$ and $y$ written as columns, $\ip{x}{y} = y^* x$, where $y^*$ is the [[conjugate transpose|0DXKE10PHF]] of $y$.
We check the three axioms of an [[inner product|0VGSYBWHV2]], and then we compute in $\mathbb{C}^2$.

1. Linearity in the first slot holds by the distributive law:
$$\sum_k (a x_k + b z_k)\overline{y_k} = a\sum_k x_k \overline{y_k} + b\sum_k z_k \overline{y_k}.$$
2. Conjugate symmetry holds, because the conjugate of a sum or a product is the sum or the product of the conjugates:
$$\overline{\ip{x}{y}} = \sum_k \overline{x_k}\, y_k = \ip{y}{x}.$$
3. Positive definiteness holds, because $x_k \overline{x_k} = \abs{x_k}^2$ is the square of the [[modulus|0KW2X0TFBX]]:
$$\ip{x}{x} = \abs{x_1}^2 + \dots + \abs{x_n}^2.$$
This is a sum of nonnegative reals, and it is $0$ only when every $x_k$ is $0$.
4. Now let $x = (1 + i, 2)$ and $y = (i, 1 - i)$ in $\mathbb{C}^2$.
Multiply each entry of $x$ by the conjugate of the matching entry of $y$, and add:
$$\ip{x}{y} = (1 + i)(-i) + 2(1 + i) = (1 - i) + (2 + 2i) = 3 + i.$$
5. In the other order, the conjugates fall on the entries of $x$:
$$\ip{y}{x} = i(1 - i) + (1 - i) \cdot 2 = (1 + i) + (2 - 2i) = 3 - i.$$
Check: $3 - i$ is the conjugate of $3 + i$.
6. The square norms are $\norm{x}^2 = \abs{1 + i}^2 + \abs{2}^2 = 2 + 4 = 6$ and $\norm{y}^2 = \abs{i}^2 + \abs{1 - i}^2 = 1 + 2 = 3$.
7. The [[Cauchy-Schwarz inequality|0RFWW56Y22]] holds, since $\abs{\ip{x}{y}}^2 = 9 + 1 = 10$ and $\norm{x}^2 \norm{y}^2 = 18$.

So $\mathbb{C}^n$ with this inner product is an [[inner product space|0QVNCJXRY3]], and its [[induced norm|0MFJJV97RJ]] is $\norm{x} = \sqrt{\abs{x_1}^2 + \dots + \abs{x_n}^2}$.

## Remarks

The standard inner product is the model of every complex inner product space of finite dimension.
Each such space of dimension $n$ has an orthonormal basis, and the coordinates in that basis turn its inner product into this formula.
On real vectors the conjugates do nothing, and the formula is the [[dot product|0S52TNNTH9]] of $\mathbb{R}^n$.

The place of the conjugate is a convention.
Physics books and Mathlib use $\sum_k \overline{x_k}\, y_k = x^* y$, which is our $\ip{y}{x}$.
The two formulas give conjugate values, so in step 4 the physics formula gives $3 - i$.
If you remove the conjugates altogether, you get the [[bilinear form of the non-example|3W8AFC4A9P]], and positivity fails at $(1, i)$.

## Explanations

### L1 human

For complex vectors, multiply each entry of the first vector by the conjugate of the matching entry of the second vector, and add.
The conjugate makes a vector paired with itself into a sum of squared sizes, so the result is never negative.
For the vector $(i, 1)$ with itself, we get $i \cdot (-i) + 1 \cdot 1 = 1 + 1 = 2$.
So the length of $(i, 1)$ is $\sqrt{2}$, the same as for the real vector $(1, 1)$.

### L2 human

Here is a typical task: build an orthonormal basis of $\mathbb{C}^2$ that starts from the direction $(1, i)$.
First compute the length of $v = (1, i)$:
$$\ip{v}{v} = 1 \cdot 1 + i \cdot \overline{i} = 1 + 1 = 2,$$
so $\norm{v} = \sqrt{2}$ and $v / \sqrt{2}$ is a unit vector.
Next try $w = (1, -i)$, which also has $\ip{w}{w} = 1 + 1 = 2$:
$$\ip{w}{v} = 1 \cdot 1 + (-i) \cdot \overline{i} = 1 + (-i)(-i) = 1 - 1 = 0.$$
So $v / \sqrt{2}$ and $w / \sqrt{2}$ form an [[orthonormal basis of $\mathbb{C}^2$|V2B3V8T8TX]].
Vectors like these describe states in quantum mechanics and frequencies in signal processing.
Watch out: the matrix form is $y^* x$, not $x^* y$, and the second is the conjugate of the first.
