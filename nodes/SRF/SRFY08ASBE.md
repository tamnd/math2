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

We prove part 1 with the polarization identity, which writes inner products with norms only.
Then we prove part 2 with two expansions of squared norms.

**Part 1.**

1. Let $V$ and $W$ be inner product spaces over $\R$ or $\C$, with [[inner products|0VGSYBWHV2]] $\ip{\cdot}{\cdot}$ and [[induced norms|0KG4D8AP6G]] $\norm{\cdot}$. Let $T \colon V \to W$ be a [[linear isometry|0717XXPWM6]].
2. Let $u, v \in V$, and first let the scalars be real. By the [[polarization identity|05FKHRT0B4]] in $W$, $\ip{Tu}{Tv} = \frac{1}{4}\left(\norm{Tu + Tv}^2 - \norm{Tu - Tv}^2\right)$.
3. By linearity, $Tu + Tv = T(u + v)$ and $Tu - Tv = T(u - v)$.
4. $T$ keeps norms, so $\norm{T(u + v)} = \norm{u + v}$ and $\norm{T(u - v)} = \norm{u - v}$.
5. So $\ip{Tu}{Tv} = \frac{1}{4}\left(\norm{u + v}^2 - \norm{u - v}^2\right) = \ip{u}{v}$, by the polarization identity in $V$.
6. Now let the scalars be complex, with the inner products linear in the first argument. By the polarization identity in $W$, $\ip{Tu}{Tv} = \frac{1}{4}\sum_{k=0}^{3} i^k \norm{Tu + i^k Tv}^2$.
7. By linearity, $Tu + i^k Tv = T(u + i^k v)$ for each $k$. Since $T$ keeps norms, $\norm{T(u + i^k v)} = \norm{u + i^k v}$.
8. So $\ip{Tu}{Tv} = \frac{1}{4}\sum_{k=0}^{3} i^k \norm{u + i^k v}^2 = \ip{u}{v}$, by the polarization identity in $V$.

**Part 2.** Now $V$ and $W$ are real, and $f \colon V \to W$ satisfies $f(0) = 0$ and $\norm{f(x) - f(y)} = \norm{x - y}$.

9. Take $y = 0$. Since $f(0) = 0$, we get $\norm{f(x)} = \norm{x}$ for all $x \in V$.
10. For a real inner product, $\norm{a - b}^2 = \norm{a}^2 - 2\ip{a}{b} + \norm{b}^2$, by bilinearity and symmetry.
11. Apply step 10 in $W$ and in $V$: $\norm{f(x)}^2 - 2\ip{f(x)}{f(y)} + \norm{f(y)}^2 = \norm{x}^2 - 2\ip{x}{y} + \norm{y}^2$. Both sides equal the same squared distance, by hypothesis.
12. By step 9, the squared norms on the two sides cancel. So $\ip{f(x)}{f(y)} = \ip{x}{y}$ for all $x, y \in V$.
13. Let $x, y \in V$ and $a, b \in \R$, and put $z = ax + by$. We expand $\norm{f(z) - af(x) - bf(y)}^2$ by bilinearity.
14. The expansion is $\norm{f(z)}^2 + a^2\norm{f(x)}^2 + b^2\norm{f(y)}^2 - 2a\ip{f(z)}{f(x)} - 2b\ip{f(z)}{f(y)} + 2ab\ip{f(x)}{f(y)}$.
15. By step 12, each inner product of values of $f$ equals the inner product of the arguments, and by step 9 each norm is unchanged.
16. So the expansion equals $\norm{z}^2 + a^2\norm{x}^2 + b^2\norm{y}^2 - 2a\ip{z}{x} - 2b\ip{z}{y} + 2ab\ip{x}{y}$.
17. This is the expansion of $\norm{z - ax - by}^2$, which is $\norm{0}^2 = 0$.
18. So $\norm{f(z) - af(x) - bf(y)} = 0$, and $f(ax + by) = af(x) + bf(y)$. Hence $f$ is linear.
19. By step 9, $f$ is a linear isometry, and by step 12 it keeps inner products.

## Idea

The polarization identity expresses an inner product through norms of a few combinations of the two vectors.
A linear map sends these combinations to the same combinations of the images, and an isometry keeps their norms.
For part 2, distances from $0$ and between points give the inner products, and a vector with norm $0$ is $0$.
So the failure of linearity, $f(ax + by) - af(x) - bf(y)$, has norm $0$.

## Variants

- Part 1 for real spaces also follows from the second form of polarization, $\ip{u}{v} = \frac{1}{2}\left(\norm{u + v}^2 - \norm{u}^2 - \norm{v}^2\right)$.
- Part 2 has a proof by midpoints: in an inner product space, $\frac{1}{2}(x + y)$ is the only point at distance $\frac{1}{2}\norm{x - y}$ from both $x$ and $y$. So $f$ keeps midpoints, and continuity gives linearity.
