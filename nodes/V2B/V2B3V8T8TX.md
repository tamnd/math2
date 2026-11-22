---
tag: V2B3V8T8TX
kind: example
name: An orthonormal basis of C2
msc: ["15A63"]
topics: [1D4JTZ9VS3]
audience: ug1
instance_of: [0S9GGTR0EX, 0RW9TNNT87, 0Y2X7P2WB7]
uses: [0FWJ0VW561, TFZ8DYVJ1J, 0AR68JTMDT]
sources:
  - url: https://en.wikipedia.org/wiki/Orthonormal_basis
    locator: Basic formula
  - book: isbn:9783031410253
    locator: Chapter 6
---

## Example

On $\mathbb{C}^2$ use the [[standard inner product|TFZ8DYVJ1J]], which is linear in the first slot and conjugate-linear in the second:
$$\ip{x}{y} = x_1 \overline{y_1} + x_2 \overline{y_2}.$$
Let $f_1 = \tfrac{1}{\sqrt2}(1, i)$ and $f_2 = \tfrac{1}{\sqrt2}(1, -i)$.
We show that $(f_1, f_2)$ is an orthonormal basis, compute coordinates in it, and see what goes wrong when the slots are swapped.

1. The first vector has norm $1$, since $i \cdot \overline{i} = i \cdot (-i) = 1$:
$$\ip{f_1}{f_1} = \tfrac12 \left(1 \cdot 1 + i \cdot \overline{i}\right) = \tfrac12 (1 + 1) = 1.$$
2. The second vector has norm $1$ in the same way:
$$\ip{f_2}{f_2} = \tfrac12 \left(1 \cdot 1 + (-i) \cdot \overline{(-i)}\right) = \tfrac12 (1 + 1) = 1.$$
3. The two vectors are orthogonal, since $\overline{-i} = i$:
$$\ip{f_1}{f_2} = \tfrac12 \left(1 \cdot 1 + i \cdot \overline{(-i)}\right) = \tfrac12 (1 + i^2) = 0.$$
   By conjugate symmetry, $\ip{f_2}{f_1} = \overline{0} = 0$ as well.
4. So $(f_1, f_2)$ is orthonormal, and it has $2 = \dim \mathbb{C}^2$ members, so it is an [[orthonormal basis|0FWJ0VW561]].
5. Take $v = (0, 1)$.
   Its coordinates are $\ip{v}{f_1}$ and $\ip{v}{f_2}$, with $v$ in the first slot:
$$\ip{v}{f_1} = \tfrac{1}{\sqrt2}\left(0 + 1 \cdot \overline{i}\right) = -\tfrac{i}{\sqrt2}, \qquad \ip{v}{f_2} = \tfrac{1}{\sqrt2} \left(0 + 1 \cdot \overline{(-i)}\right) = \tfrac{i}{\sqrt2}.$$
6. Check that these coordinates rebuild $v$:
$$-\tfrac{i}{\sqrt2} f_1 + \tfrac{i}{\sqrt2} f_2 = -\tfrac{i}{2}(1, i) + \tfrac{i}{2}(1, -i) = \left(-\tfrac{i}{2} + \tfrac{i}{2}, \tfrac12 + \tfrac12\right) = (0, 1).$$
7. Swap the slots and see the error.
   The values $\ip{f_1}{v} = \tfrac{i}{\sqrt2}$ and $\ip{f_2}{v} = -\tfrac{i}{\sqrt2}$ are the conjugates, and
$$\tfrac{i}{2}(1, i) - \tfrac{i}{2}(1, -i) = \left(\tfrac{i}{2} - \tfrac{i}{2}, -\tfrac12 - \tfrac12\right) = (0, -1),$$
   which is $-v$, not $v$.
8. The matrix $U = \tfrac{1}{\sqrt2}\begin{pmatrix} 1 & 1 \\ i & -i \end{pmatrix}$ has columns $f_1$ and $f_2$.
   Steps 1 to 3 say $U^* U = I_2$, so $U$ is [[unitary|0AR68JTMDT]].

## Remarks

For a general $v = (a, b)$, the coordinates are
$$\ip{v}{f_1} = \frac{a - ib}{\sqrt2}, \qquad \ip{v}{f_2} = \frac{a + ib}{\sqrt2}.$$
Their squared moduli add up to the squared norm of $v$, because $\abs{z - w}^2 + \abs{z + w}^2 = 2\abs{z}^2 + 2\abs{w}^2$ for complex numbers, here with $z = a$ and $w = ib$:
$$\tfrac12 \left(\abs{a - ib}^2 + \abs{a + ib}^2\right) = \abs{a}^2 + \abs{b}^2 = \norm{v}^2.$$

The conjugates are not optional.
Without them, step 1 would give $\tfrac12(1 + i^2) = 0$, so $f_1$ would seem to have length $0$.
The order of the slots matters too, as step 7 shows: the wrong order conjugates each coordinate.
In physics notation, with linearity in the second slot, the coordinate of $v$ is written $\langle f_j | v \rangle$, and it has the same value as our $\ip{v}{f_j}$.

## Explanations

### L1 human

Complex vectors can be perpendicular too, once the inner product uses conjugates.
The vectors $(1, i)$ and $(1, -i)$ give $1 \cdot 1 + i \cdot \overline{(-i)} = 1 + i \cdot i = 0$.
After division by $\sqrt2$ each has length $1$, and together they form a pair of complex axes for $\mathbb{C}^2$.

### L2 human

Here are the coordinates of $v = (2, 2i)$ in the basis $(f_1, f_2)$.
The first coordinate uses $\overline{i} = -i$:
$$\ip{v}{f_1} = \tfrac{1}{\sqrt2}\left(2 + 2i \cdot (-i)\right) = \tfrac{4}{\sqrt2} = 2\sqrt2.$$
The second uses $\overline{-i} = i$:
$$\ip{v}{f_2} = \tfrac{1}{\sqrt2}\left(2 + 2i \cdot i\right) = 0.$$
So $v = 2\sqrt2\, f_1 = 2(1, i)$, which is correct.
The squared lengths agree: $\abs{2\sqrt2}^2 = 8$ and $\norm{v}^2 = 4 + 4 = 8$.
In optics, $f_1$ and $f_2$ describe the two circular polarizations of light in the basis of horizontal and vertical polarization, and $v$ here is purely of the first kind.
Watch out: with the slots swapped, each coordinate turns into its conjugate, as in step 7 of the example.
