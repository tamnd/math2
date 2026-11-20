---
tag: 0R7VXTYHYZ
kind: statement
role: theorem
name: Isometries preserve inner products
aliases: [isometries-preserve-inner-products, linear-isometry-preserves-inner-product]
msc: ["15A04", "46C05"]
topics: [AZS5BPF5H3]
audience: ug1
about: [07SJXTWVQW, 0NB0AWGJBW]
uses: [0717XXPWM6, 05FKHRT0B4, 01EK923SKP, 0KG4D8AP6G]
sources:
  - url: https://en.wikipedia.org/wiki/Isometry
    locator: Linear isometry
  - url: https://en.wikipedia.org/wiki/Polarization_identity
    locator: Isometries
  - url: https://en.wikipedia.org/wiki/Mazur%E2%80%93Ulam_theorem
    locator: lead section
---

## Statement

Let $V$ and $W$ be [[inner product spaces|01EK923SKP]] over $\mathbb{K} = \R$ or $\C$, with the [[induced norms|0KG4D8AP6G]].

1. Let $T \colon V \to W$ be a [[linear isometry|0717XXPWM6]]. Then $\ip{Tu}{Tv} = \ip{u}{v}$ for all $u, v \in V$.
2. Let $V$ and $W$ be real, and let $f \colon V \to W$ be any map with $f(0) = 0$ and $\norm{f(x) - f(y)} = \norm{x - y}$ for all $x, y \in V$. Then $f$ is linear. So $f$ is a linear isometry, and it keeps inner products.

## Remarks

### Why each hypothesis is needed

- Part 1 needs linearity. The map $f(x) = \abs{x}$ on $\R$ keeps the norm of every number, but $f(1)f(-1) = 1$ while $1 \cdot (-1) = -1$.
- Part 2 needs $f(0) = 0$. A translation $x \mapsto x + a$ with $a \neq 0$ keeps distances, but it is not linear.
- Part 2 needs distances, not only norms. The map $f(x) = \abs{x}$ on $\R$ fixes $0$ and keeps norms, but $\abs{f(1) - f(-1)} = 0 \neq 2$, and $f$ is not linear.
- Part 2 needs real scalars. Complex conjugation $z \mapsto \overline{z}$ on $\C$ keeps distances and fixes $0$, but $\overline{iz} = -i\,\overline{z}$. So it is only $\R$-linear, and $\ip{\overline{z}}{\overline{w}} = \overline{\ip{z}{w}}$.

### Consequences

- A linear isometry keeps angles and orthogonality, because the angle between $u$ and $v$ is fixed by $\ip{u}{v}$, $\norm{u}$ and $\norm{v}$.
- A map $f \colon \R^n \to \R^n$ that keeps distances and fixes $0$ is $f(x) = Qx$ for an [[orthogonal matrix|0W02QESPJQ]] $Q$.
- So every distance-preserving map of $\R^n$ has the form $x \mapsto Qx + b$, see [[Euclidean isometries|0J1N3WTKM4]]. Apply part 2 to $x \mapsto f(x) - f(0)$.

### Converse

Both converses are true.
A linear map that keeps inner products keeps norms, because $\norm{Tv}^2 = \ip{Tv}{Tv} = \ip{v}{v} = \norm{v}^2$.
A linear isometry fixes $0$ and keeps distances, because $\norm{Tx - Ty} = \norm{T(x - y)} = \norm{x - y}$.

### Generalizations

- [[The Mazur-Ulam theorem|4J4EW7FXWW]]: a surjective map between real normed spaces that keeps distances is affine. So it is linear when it fixes $0$.
- In general normed spaces, surjectivity is needed. The map $t \mapsto (t, \sin t)$ from $\R$ to $\R^2$ with the norm $\max(\abs{a}, \abs{b})$ keeps distances and fixes $0$, but it is not linear. The reason: $\abs{\sin t - \sin s} \le \abs{t - s}$.
- In inner product spaces, part 2 needs no surjectivity, because the proof uses only inner products.

## History

Mazur and Ulam proved in 1932 that a surjective map between real normed spaces that keeps distances is affine.
They answered a question of Banach.

## Explanations

### L1 human

If a motion keeps all lengths, then it keeps all angles too.
The reason: the sides of a triangle fix its angles.
For example, a triangle with sides $3$, $4$ and $5$ always has a right angle.
A motion that keeps lengths sends it to another triangle with sides $3$, $4$ and $5$, so the right angle stays.
If the motion also keeps the origin fixed, then it cannot bend or fold space, so it is linear.

### L2 human

Worked example: let $T = \frac{1}{5}\begin{pmatrix} 3 & -4 \\ 4 & 3 \end{pmatrix}$, a linear isometry of $\R^2$, and let $u = (1, 0)$ and $v = (1, 1)$.

1. $\ip{u}{v} = 1$.
2. By polarization, $\ip{u}{v} = \frac{1}{4}\left(\norm{u + v}^2 - \norm{u - v}^2\right) = \frac{1}{4}(5 - 1) = 1$, with $u + v = (2, 1)$ and $u - v = (0, -1)$.
3. $Tu = \frac{1}{5}(3, 4)$ and $Tv = \frac{1}{5}(-1, 7)$.
4. $\ip{Tu}{Tv} = \frac{1}{25}(-3 + 28) = 1$, as part 1 says.

The typical use: once a map keeps lengths, we may use that it keeps dot products in any later step.
A trap: part 2 is false over $\C$, as complex conjugation shows.
It is also false without $f(0) = 0$, as translations show.

### L3 human

Part 1 is the statement that the norm determines the inner product, through polarization.
Part 2 says that the metric of a real inner product space determines its linear structure, once the origin is fixed.
The reason is strict convexity: in an inner product space, the midpoint of $x$ and $y$ is the only point at distance $\frac{1}{2}\norm{x - y}$ from both.
In normed spaces without this property, such as $\R^2$ with the maximum norm, the [[Mazur-Ulam theorem|4J4EW7FXWW]] needs surjectivity.
The result is the first step of the classification of the isometries of Euclidean space as the group $\R^n \rtimes O(n)$.
