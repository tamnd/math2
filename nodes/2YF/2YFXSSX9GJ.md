---
tag: 2YFXSSX9GJ
kind: example
name: A complex line has no orientation as a complex vector space
msc: [15A04, 15A15]
topics: [DTBK11SR77]
audience: ug2
not_instance_of:
  - target: 0QJJAQ6ZYZ
    note: C as a complex line has change of basis determinants such as i, which have no sign, so its bases do not split into two classes
uses: [0Q8BZXVT1Z]
sources:
  - url: https://en.wikipedia.org/wiki/Orientation_(vector_space)
---

## Example

Let $V = \mathbb{C}$, viewed as a vector space of dimension $1$ over $\mathbb{C}$.
It is not an example of an [[oriented space|0QJJAQ6ZYZ]], because the [[definition|0Q8BZXVT1Z]] of orientation needs a sign that complex numbers do not have.

1. The ordered bases of $V$ are the families $(w)$ with one nonzero number $w \in \mathbb{C}$.
2. The change of basis matrix from $(1)$ to $(i)$ is the $1 \times 1$ matrix $(i)$, so its determinant is $i$.
3. The number $i$ is neither positive nor negative.
   So the rule "same orientation when the determinant is positive" cannot be applied to these two bases.
4. The path description fails to give two classes as well.
   The family $w(t) = e^{i \pi t}$ for $t \in [0, 1]$ is never $0$, so it is a path of bases from $(1)$ to $(-1)$.
5. Over $\mathbb{R}$, the bases $(1)$ and $(-1)$ of the real line $\mathbb{R}$ have opposite orientations, since the determinant $-1$ is negative.
   Over $\mathbb{C}$ the same two bases are joined by the path of step 4, so all bases of $V$ lie in one connected piece, and no split into two classes arises.

## Remarks

The condition that fails is that the scalars are real.
The same set $\mathbb{C}$, viewed as a real vector space of dimension $2$ with basis $(1, i)$, has two orientations in the usual way.
Multiplication by $w = a + bi \ne 0$ sends $1$ to $a + bi$ and $i$ to $-b + ai$, so its real matrix and real determinant are
$$\begin{pmatrix} a & -b \\ b & a \end{pmatrix}, \qquad a^2 + b^2 > 0.$$
So every complex-linear isomorphism of $\mathbb{C}$ keeps the real orientation of $(1, i)$.
The same holds in every dimension, and so every complex vector space has a canonical orientation as a real space.

## Explanations

### L1 human

An orientation needs a sign, positive or negative, for each change of basis.
A complex number such as $i$ has no sign.
So the bases of a complex space do not fall into two teams, and the idea of orientation does not apply.

### L2 human

The path $e^{i \pi t}$ turns the basis $(1)$ into the basis $(-1)$ without ever passing through $0$.
Over the real numbers, any path from $1$ to $-1$ must pass through $0$, and that is why the real line has two orientations.
Watch out: a complex space still has an orientation when we view it as a real space of twice the dimension, and that orientation is even canonical.
