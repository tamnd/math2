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

Let $n = 2$ or $n = 3$, and let $u$ and $v$ be nonzero vectors in $\mathbb{R}^n$.
Draw $u$ and $v$ as arrows $\overrightarrow{OU}$ and $\overrightarrow{OV}$ from the origin $O$.
Let $\theta \in [0, \pi]$ be the geometric [[angle between them|0ZEHZY85E6]], the angle $UOV$, with $\theta = 0$ or $\theta = \pi$ when the arrows lie on one line.
Let $u \cdot v = u_1 v_1 + \dots + u_n v_n$ be the [[dot product|0S52TNNTH9]], and let $\|u\|$ and $\|v\|$ be the [[lengths|0XKBKGTCPC]].
Then
$$u \cdot v = \|u\| \, \|v\| \cos \theta.$$

## Remarks

### Why each hypothesis is needed

- If $u = 0$ or $v = 0$, then there is no arrow, and the angle is not defined. Both sides would be $0$ for any choice of $\theta$, so the formula holds but says nothing.
- If $n \geq 4$, there is no geometric angle to compare with. In $\mathbb{R}^n$ the formula becomes the definition of the angle, and that definition needs the [[Cauchy-Schwarz inequality|0RFWW56Y22]] first.

### Consequences

- The coordinate dot product and the geometric dot product $\|u\| \, \|v\| \cos \theta$ are the same number.
- The angle is computable: $\cos \theta = \dfrac{u \cdot v}{\|u\| \, \|v\|}$.
- Two nonzero vectors are [[perpendicular if and only if their dot product is zero|03NK6RSRQ1]].
- The sign of $u \cdot v$ gives the type of the angle: positive for acute, zero for right, negative for obtuse.
- Since $|\cos \theta| \leq 1$, we get $|u \cdot v| \leq \|u\| \, \|v\|$ in the plane and in space.

### Converse

The formula determines $\theta$: the cosine is injective on $[0, \pi]$.
So if a number $\varphi \in [0, \pi]$ satisfies $u \cdot v = \|u\| \, \|v\| \cos \varphi$, then $\varphi$ is the angle between $u$ and $v$.

### Generalizations

In $\mathbb{R}^n$ and in each real [[inner product space|1D4JTZ9VS3]], the Cauchy-Schwarz inequality gives $-1 \leq \frac{\langle u, v \rangle}{\|u\| \, \|v\|} \leq 1$.
Then $\theta = \arccos \frac{\langle u, v \rangle}{\|u\| \, \|v\|}$ defines the angle, and the formula holds by definition.
The statement above shows that this definition agrees with geometry in dimensions $2$ and $3$.

## History

The law of cosines, the main tool of the proof, is in Euclid's Elements, Book II, Propositions 12 and 13, in a geometric form without the cosine.
The formula $u \cdot v = \|u\| \, \|v\| \cos \theta$ appears in the vector analysis of Gibbs and Heaviside in the 1880s.

## Explanations

### L1 human

The dot product is large and positive when two vectors point in nearly the same direction.
It is zero when they are perpendicular, and negative when they point in nearly opposite directions.
For example, $(3, 0)$ and $(2, 2)$ make an angle of $45^\circ$.
The formula gives $3 \cdot \sqrt{8} \cdot \cos 45^\circ = 3 \cdot 2\sqrt{2} \cdot \tfrac{\sqrt{2}}{2} = 6$, and the coordinates give $3 \cdot 2 + 0 \cdot 2 = 6$.

### L2 human

Worked example: the angle between $u = (1, 1, 0)$ and $v = (1, 0, 1)$.

1. $u \cdot v = 1 + 0 + 0 = 1$.
2. $\|u\| = \sqrt{2}$ and $\|v\| = \sqrt{2}$.
3. $\cos \theta = \tfrac{1}{2}$, so $\theta = \tfrac{\pi}{3} = 60^\circ$.
4. Check by geometry: $\|u - v\| = \|(0, 1, -1)\| = \sqrt{2}$. So the triangle $O$, $U$, $V$ has three sides $\sqrt{2}$, it is equilateral, and its angles are $60^\circ$.

The typical use is to compute an angle from coordinates.
A trap: the formula gives the angle in $[0, \pi]$ only; it does not give a direction of turning, so $u$ and $v$ in the other order give the same angle.

### L3 human

The proof shows a general pattern: a bilinear form is determined by its quadratic form through polarization, $u \cdot v = \tfrac{1}{2}\left(\|u\|^2 + \|v\|^2 - \|u - v\|^2\right)$.
So any notion of length that satisfies the law of cosines determines the dot product.
This is the reason why isometries of $\mathbb{R}^n$ that fix the origin preserve the dot product, a fact of the sub-area on [[isometries|AZS5BPF5H3]].
In higher dimensions the logic runs in the other direction: we define the angle from the dot product, after the [[Cauchy-Schwarz inequality|0RFWW56Y22]].
