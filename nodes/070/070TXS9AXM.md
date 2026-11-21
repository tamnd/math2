---
tag: 070TXS9AXM
kind: statement
role: proposition
name: Geometric formula for the dot product
msc: ["51N20", "15A63"]
topics: [VKVAJ94SKZ]
audience: school
about: [0S52TNNTH9, 0ZEHZY85E6]
uses: [0S52TNNTH9, 0XKBKGTCPC, 0ZEHZY85E6]
sources:
  - url: https://en.wikipedia.org/wiki/Dot_product
    locator: Equivalence of the definitions
  - url: https://en.wikipedia.org/wiki/Law_of_cosines
    locator: lead section
---

## Statement

In the plane and in space, the dot product computed from coordinates equals the product of the two lengths and the cosine of the angle between the vectors.
Let $n = 2$ or $n = 3$, and let $u$ and $v$ be nonzero vectors in $\mathbb{R}^n$.
Draw them as arrows $\overrightarrow{OU}$ and $\overrightarrow{OV}$ from the origin $O$.
Let $\theta \in [0, \pi]$ be the geometric [[angle between them|0ZEHZY85E6]], the angle $UOV$, with $\theta = 0$ or $\theta = \pi$ when the arrows lie on one line.
Let $u \cdot v = u_1 v_1 + \dots + u_n v_n$ be the [[dot product|0S52TNNTH9]], and let $\|u\|$ and $\|v\|$ be the [[lengths|0XKBKGTCPC]].
Then
$$u \cdot v = \|u\| \, \|v\| \cos \theta.$$

## Remarks

### Why each hypothesis is needed

The vectors must be nonzero, because the zero vector has no arrow and no angle with anything.
If $u = 0$, both sides are $0$ for every choice of $\theta$, so the formula would hold but would say nothing about an angle.

The dimension must be $2$ or $3$, because only there do we have an angle from elementary geometry to compare with.
In $\mathbb{R}^n$ for $n \ge 4$ the formula becomes the definition of the angle, and that definition needs the [[Cauchy-Schwarz inequality|0RFWW56Y22]] first, to know that the quotient $u \cdot v / (\|u\| \, \|v\|)$ lies between $-1$ and $1$.

### What it gives you

The formula makes angles computable from coordinates:
$$\cos \theta = \frac{u \cdot v}{\|u\| \, \|v\|}.$$
For $u = (1, 1, 0)$ and $v = (1, 0, 1)$ this gives $\cos \theta = 1 / (\sqrt{2} \cdot \sqrt{2}) = \tfrac{1}{2}$, so $\theta = 60^\circ$.
Since $\|u\|$ and $\|v\|$ are positive, the sign of $u \cdot v$ is the sign of $\cos \theta$.
So the angle is acute when $u \cdot v > 0$, right when $u \cdot v = 0$, and obtuse when $u \cdot v < 0$; the middle case is the [[criterion for perpendicular vectors|03NK6RSRQ1]].
Since $|\cos \theta| \le 1$, the formula also gives $|u \cdot v| \le \|u\| \, \|v\|$ in the plane and in space.

### The converse

The formula determines the angle, because the cosine is one-to-one on $[0, \pi]$.
So if a number $\varphi \in [0, \pi]$ satisfies $u \cdot v = \|u\| \, \|v\| \cos \varphi$, then $\varphi$ is the angle between $u$ and $v$.

### Generalizations

In $\mathbb{R}^n$ and in every real [[inner product space|1D4JTZ9VS3]], the Cauchy-Schwarz inequality gives
$$-1 \le \frac{\langle u, v \rangle}{\|u\| \, \|v\|} \le 1,$$
and the arccosine of this quotient defines the angle, so the formula holds by definition.
The statement here is what shows that this definition agrees with geometry in dimensions $2$ and $3$.

## History

The law of cosines, the main tool of the proof, is in Euclid's *Elements*, Book II, Propositions 12 and 13, in a geometric form without the cosine.
The formula $u \cdot v = \|u\| \, \|v\| \cos \theta$ appears in the vector analysis of Gibbs and Heaviside in the 1880s.

## Explanations

### L1 human

The dot product is large and positive when two vectors point in nearly the same direction.
It is zero when they are perpendicular, and negative when they point in nearly opposite directions.
For example, $(3, 0)$ and $(2, 2)$ make an angle of $45^\circ$.
The formula gives $3 \cdot 2\sqrt{2} \cdot \tfrac{\sqrt{2}}{2} = 6$, and the coordinates give $3 \cdot 2 + 0 \cdot 2 = 6$.

### L2 human

Here is a check of the formula against a picture, with $u = (1, 1, 0)$ and $v = (1, 0, 1)$.
The coordinates give $u \cdot v = 1 + 0 + 0 = 1$, and both lengths are $\sqrt{2}$, so
$$\cos \theta = \frac{1}{\sqrt{2} \cdot \sqrt{2}} = \frac{1}{2}, \qquad \theta = 60^\circ.$$
Now look at the triangle with corners $O$, $U = (1, 1, 0)$ and $V = (1, 0, 1)$.
Its third side is $\|u - v\| = \|(0, 1, -1)\| = \sqrt{2}$, so all three sides are $\sqrt{2}$, the triangle is equilateral, and its angles are $60^\circ$.
The typical use is the first half: an angle straight from coordinates.
Watch out: the formula gives an angle in $[0, \pi]$ and no direction of turning, so $u, v$ and $v, u$ give the same angle.

### L3 human

The proof shows a general pattern: a symmetric bilinear form is fixed by its values on the diagonal, through the polarization identity
$$u \cdot v = \tfrac{1}{2}\left(\|u\|^2 + \|v\|^2 - \|u - v\|^2\right).$$
So any notion of length that satisfies the law of cosines determines the dot product.
This is why the isometries of $\mathbb{R}^n$ that fix the origin preserve the dot product, a fact of the sub-area on [[isometries|AZS5BPF5H3]].
In higher dimensions the logic runs the other way: the angle is defined from the dot product, after the [[Cauchy-Schwarz inequality|0RFWW56Y22]].
