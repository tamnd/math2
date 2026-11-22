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

A map that keeps lengths keeps angles too, and on a real inner product space a map that keeps distances and fixes the origin is automatically linear.
Let $V$ and $W$ be [[inner product spaces|01EK923SKP]] over $\mathbb{K} = \R$ or $\C$, with the [[induced norms|0KG4D8AP6G]].

1. Let $T \colon V \to W$ be a [[linear isometry|0717XXPWM6]]. Then $\ip{Tu}{Tv} = \ip{u}{v}$ for all $u, v \in V$.
2. Let $V$ and $W$ be real, and let $f \colon V \to W$ be any map with $f(0) = 0$ and $\norm{f(x) - f(y)} = \norm{x - y}$ for all $x, y \in V$. Then $f$ is linear, so $f$ is a linear isometry and it keeps inner products.

Neither part needs finite dimension, and part 2 does not need $f$ to be onto.

## Remarks

### Why each hypothesis is needed

Part 1 needs linearity.
The map $f(x) = \abs{x}$ on $\R$ keeps the norm of every number, but $f(1) f(-1) = 1$ while $1 \cdot (-1) = -1$.

Part 2 needs $f(0) = 0$.
A translation $x \mapsto x + a$ with $a \ne 0$ keeps distances, but it moves $0$ and so is not linear.

Part 2 needs distances, not only norms.
The same map $f(x) = \abs{x}$ fixes $0$ and keeps norms, but $\abs{f(1) - f(-1)} = 0$ while $\abs{1 - (-1)} = 2$, and $f$ is not linear.

Part 2 needs real scalars.
Complex conjugation $z \mapsto \bar z$ on $\C$ keeps distances and fixes $0$, but $\overline{i \cdot 1} = -i$, while $i \cdot \bar 1 = i$.
So it is real-linear and not complex-linear, and it gives $\ip{\bar z}{\bar w} = \overline{\ip{z}{w}}$ in place of $\ip{z}{w}$.
Over $\C$, the proof of part 2 still shows that $f$ is real-linear and keeps the real part of the inner product.

### What it gives you

A linear isometry keeps angles and orthogonality, because the angle between $u$ and $v$ is fixed by $\ip{u}{v}$, $\norm{u}$ and $\norm{v}$.
A map $f \colon \R^n \to \R^n$ that keeps distances and fixes $0$ is $f(x) = Qx$ for an [[orthogonal matrix|0W02QESPJQ]] $Q$.
Apply part 2 to $x \mapsto f(x) - f(0)$ to see that every distance-preserving map of $\R^n$ has the form $x \mapsto Qx + b$, the [[Euclidean isometries|0J1N3WTKM4]].

### The converse

Both converses hold.
A linear map that keeps inner products keeps norms, because $\norm{Tv}^2 = \ip{Tv}{Tv} = \ip{v}{v} = \norm{v}^2$.
A linear isometry fixes $0$ and keeps distances, because $\norm{Tx - Ty} = \norm{T(x - y)} = \norm{x - y}$.

### Generalizations

The [[Mazur-Ulam theorem|4J4EW7FXWW]] extends part 2 to real normed spaces: a surjective map between real normed spaces that keeps distances is affine, so it is linear when it fixes $0$.
In general normed spaces the surjectivity is needed.
Give $\R^2$ the norm $\max(\abs{a}, \abs{b})$ and take $f(t) = (t, \sin t)$ from $\R$ to $\R^2$.
It fixes $0$ and keeps distances, because $\abs{\sin t - \sin s} \le \abs{t - s}$, but it is not linear.
In inner product spaces part 2 needs no surjectivity, because the proof uses only inner products.

## History

Mazur and Ulam proved in 1932 that a surjective map between real normed spaces that keeps distances is affine.

## Explanations

### L1 human

If a motion keeps all lengths, then it keeps all angles too, because the three sides of a triangle fix its angles.
A triangle with sides $3$, $4$ and $5$ always has a right angle, since $9 + 16 = 25$.
A motion that keeps lengths sends it to another triangle with sides $3$, $4$ and $5$, so the right angle stays.
If the motion also keeps the origin in place, then it cannot bend or fold the space, and it is linear.

### L2 human

Here is part 1 at work for $T = \frac{1}{5}\begin{pmatrix} 3 & -4 \\ 4 & 3 \end{pmatrix}$ on $\R^2$, with $u = (1, 0)$ and $v = (1, 1)$.
First compute $\ip{u}{v} = 1$ directly, and then by polarization with $u + v = (2, 1)$ and $u - v = (0, -1)$:
$$\ip{u}{v} = \tfrac{1}{4}\left(\norm{u + v}^2 - \norm{u - v}^2\right) = \tfrac{1}{4}(5 - 1) = 1.$$
The images are $Tu = \frac{1}{5}(3, 4)$ and $Tv = \frac{1}{5}(-1, 7)$, so
$$\ip{Tu}{Tv} = \tfrac{1}{25}(3 \cdot (-1) + 4 \cdot 7) = \tfrac{25}{25} = 1.$$
Check: $\norm{Tv}^2 = \tfrac{1 + 49}{25} = 2 = \norm{v}^2$.
Once a map is known to keep lengths, every later step may use that it keeps dot products.
Watch out: part 2 fails over $\C$, as conjugation shows, and it fails without $f(0) = 0$, as translations show.

### L3 human

Part 1 says that the norm determines the inner product, through polarization.
Part 2 says that the metric of a real inner product space determines its linear structure once the origin is fixed.
Behind this is strict convexity: in an inner product space the [[midpoint|0S706JBZBG]] of $x$ and $y$ is the only point at distance $\frac{1}{2}\norm{x - y}$ from both.
In normed spaces without this property, such as $\R^2$ with the maximum norm, the Mazur-Ulam theorem needs surjectivity.
The result is the first step in the description of the isometry group of Euclidean space as the semidirect product $\R^n \rtimes O(n)$.
