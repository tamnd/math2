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

On $\mathbb{C}^2$ use the [[standard inner product|TFZ8DYVJ1J]] $\ip{x}{y} = x_1\overline{y_1} + x_2\overline{y_2}$.
Let $f_1 = \frac{1}{\sqrt2}(1, i)$ and $f_2 = \frac{1}{\sqrt2}(1, -i)$.

1. $\ip{f_1}{f_1} = \frac12(1 \cdot 1 + i \cdot \overline{i}) = \frac12(1 + 1) = 1$.
2. $\ip{f_2}{f_2} = \frac12(1 \cdot 1 + (-i)\overline{(-i)}) = \frac12(1 + 1) = 1$.
3. $\ip{f_1}{f_2} = \frac12(1 \cdot 1 + i \cdot \overline{(-i)}) = \frac12(1 + i \cdot i) = 0$. So $f_1 \perp f_2$, and $\ip{f_2}{f_1} = \overline{0} = 0$.
4. So $(f_1, f_2)$ is orthonormal, and it has $2 = \dim \mathbb{C}^2$ vectors. Hence it is an [[orthonormal basis|0FWJ0VW561]].
5. Coordinates of $v = (0, 1)$: $\ip{v}{f_1} = \frac{1}{\sqrt2}(0 + 1 \cdot \overline{i}) = -\frac{i}{\sqrt2}$ and $\ip{v}{f_2} = \frac{1}{\sqrt2}\,\overline{(-i)} = \frac{i}{\sqrt2}$.
6. Check: $-\frac{i}{\sqrt2} f_1 + \frac{i}{\sqrt2} f_2 = -\frac{i}{2}(1, i) + \frac{i}{2}(1, -i) = (0, \frac12 + \frac12) = (0, 1)$.
7. The wrong slot gives $\ip{f_1}{v} = \frac{i}{\sqrt2}$ and $\ip{f_2}{v} = -\frac{i}{\sqrt2}$. Then $\frac{i}{2}(1, i) - \frac{i}{2}(1, -i) = (0, -1)$, which is $-v$, not $v$.
8. The matrix $U = \frac{1}{\sqrt2}\begin{pmatrix} 1 & 1 \\ i & -i \end{pmatrix}$ has columns $f_1$ and $f_2$. Steps 1 to 3 say $U^* U = I_2$, so $U$ is [[unitary|0AR68JTMDT]].

## Remarks

For a general $v = (a, b)$, the coordinates are $\ip{v}{f_1} = \frac{a - ib}{\sqrt2}$ and $\ip{v}{f_2} = \frac{a + ib}{\sqrt2}$.
Their squared moduli add to $\frac12(|a - ib|^2 + |a + ib|^2) = |a|^2 + |b|^2 = \norm{v}^2$, by the parallelogram law in $\mathbb{C}$.
Without conjugates, step 1 would give $\frac12(1 + i^2) = 0$, so the conjugates are necessary.
In physics notation, with linearity in the second slot, the coordinate of $v$ is written $\langle f_j | v \rangle$, and it has the same value as our $\ip{v}{f_j}$.

## Explanations

### L1 human

Complex vectors can be perpendicular too.
The vectors $(1, i)$ and $(1, -i)$ have inner product $1 + i \cdot i = 0$, once we use the conjugate.
After division by $\sqrt2$ they have length $1$, and they form a pair of complex axes.

### L2 human

Worked example: the coordinates of $v = (2, 2i)$ in the basis $(f_1, f_2)$.

1. $\ip{v}{f_1} = \frac{1}{\sqrt2}(2 + 2i \cdot (-i)) = \frac{1}{\sqrt2}(2 + 2) = 2\sqrt2$.
2. $\ip{v}{f_2} = \frac{1}{\sqrt2}(2 + 2i \cdot i) = 0$.
3. So $v = 2\sqrt2 f_1 = 2(1, i)$, which is correct.
4. The squared norms agree: $|2\sqrt2|^2 = 8$ and $\norm{v}^2 = 4 + 4 = 8$.

The typical use is in quantum mechanics, where $f_1$ and $f_2$ are two states of a system with two levels.
A trap: with the slots swapped, each coordinate becomes its conjugate, as in step 7 of the example.
