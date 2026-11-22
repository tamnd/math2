---
tag: SRFY08ASBE
kind: proof
name: Proof that isometries preserve inner products by polarization
msc: ["15A04", "46C05"]
topics: [AZS5BPF5H3]
audience: ug1
proves: 0R7VXTYHYZ
uses: [0717XXPWM6, 05FKHRT0B4, 0KG4D8AP6G, 0VGSYBWHV2]
methods: [0NTF6DMVAP]
sources:
  - url: https://en.wikipedia.org/wiki/Polarization_identity
    locator: Isometries
---

## Proof

We prove part 1 with the polarization identity, which writes an inner product in terms of norms, and part 2 by expanding squared norms.

**Part 1.**

1. Let $V$ and $W$ have [[inner products|0VGSYBWHV2]] $\ip{\cdot}{\cdot}$ and [[induced norms|0KG4D8AP6G]] $\norm{\cdot}$, and let $T \colon V \to W$ be a [[linear isometry|0717XXPWM6]].
2. Let $u, v \in V$, and first let the scalars be real. The [[polarization identity|05FKHRT0B4]] in $W$ gives $\ip{Tu}{Tv} = \frac{1}{4}\left(\norm{Tu + Tv}^2 - \norm{Tu - Tv}^2\right)$.
3. By linearity, $Tu + Tv = T(u + v)$ and $Tu - Tv = T(u - v)$, and $T$ keeps the norms of these two vectors.
4. So $\ip{Tu}{Tv} = \frac{1}{4}\left(\norm{u + v}^2 - \norm{u - v}^2\right)$, and the polarization identity in $V$ says that this is $\ip{u}{v}$.
5. Now let the scalars be complex, with the inner products linear in the first argument. The polarization identity in $W$ gives $\ip{Tu}{Tv} = \frac{1}{4}\sum_{k=0}^{3} i^k \norm{Tu + i^k Tv}^2$.
6. By linearity, $Tu + i^k Tv = T(u + i^k v)$ for each $k$, and $T$ keeps the norm of this vector.
7. So $\ip{Tu}{Tv} = \frac{1}{4}\sum_{k=0}^{3} i^k \norm{u + i^k v}^2$, which is $\ip{u}{v}$ by the polarization identity in $V$.

**Part 2.** Now $V$ and $W$ are real, and $f \colon V \to W$ satisfies $f(0) = 0$ and $\norm{f(x) - f(y)} = \norm{x - y}$ for all $x, y$.

8. Take $y = 0$ in the hypothesis. Since $f(0) = 0$, this gives $\norm{f(x)} = \norm{x}$ for all $x \in V$.
9. For a real inner product, $\norm{a - b}^2 = \norm{a}^2 - 2\ip{a}{b} + \norm{b}^2$, by bilinearity and symmetry.
10. Apply step 9 to $f(x) - f(y)$ in $W$ and to $x - y$ in $V$. The two left sides are equal by hypothesis, so $\norm{f(x)}^2 - 2\ip{f(x)}{f(y)} + \norm{f(y)}^2 = \norm{x}^2 - 2\ip{x}{y} + \norm{y}^2$.
11. By step 8 the squared norms on the two sides cancel. So $\ip{f(x)}{f(y)} = \ip{x}{y}$ for all $x, y \in V$.
12. Let $x, y \in V$ and $a, b \in \R$, and put $z = ax + by$. Expand by bilinearity: $\norm{f(z) - af(x) - bf(y)}^2 = \norm{f(z)}^2 + a^2\norm{f(x)}^2 + b^2\norm{f(y)}^2 - 2a\ip{f(z)}{f(x)} - 2b\ip{f(z)}{f(y)} + 2ab\ip{f(x)}{f(y)}$.
13. By steps 8 and 11 we may remove every $f$ on the right side. The result is the expansion of $\norm{z - ax - by}^2$, which is $\norm{0}^2 = 0$.
14. So $\norm{f(z) - af(x) - bf(y)} = 0$, and a vector of norm $0$ is $0$. Hence $f(ax + by) = af(x) + bf(y)$, and $f$ is linear.
15. By step 8, $f$ is a linear isometry, and by step 11 it keeps inner products.

## Idea

The polarization identity expresses an inner product through the norms of a few combinations of the two vectors.
A linear map sends these combinations to the same combinations of the images, and an isometry keeps their norms, so the inner product survives.
For part 2, the distances from $0$ and between points recover all inner products of values of $f$.
Then the defect $f(ax + by) - af(x) - bf(y)$ is a vector whose squared norm expands to $0$, so the defect is $0$.

## Variants

Part 1 for real spaces also follows from the other form of polarization, $\ip{u}{v} = \frac{1}{2}\left(\norm{u + v}^2 - \norm{u}^2 - \norm{v}^2\right)$.

Part 2 has a proof by midpoints.
In an inner product space, $\frac{1}{2}(x + y)$ is the only point at distance $\frac{1}{2}\norm{x - y}$ from both $x$ and $y$.
So $f$ keeps midpoints, and with $f(0) = 0$ this gives $f(\tfrac{1}{2}x) = \tfrac{1}{2}f(x)$ and then $f(x + y) = 2f(\tfrac{1}{2}(x + y)) = f(x) + f(y)$.
An additive map that is continuous is real-linear, and $f$ is continuous because it keeps distances.
This is also the line of the proof of the Mazur-Ulam theorem in normed spaces, where the midpoint has to be found without an inner product.
