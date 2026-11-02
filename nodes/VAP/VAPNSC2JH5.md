---
tag: VAPNSC2JH5
kind: statement
role: proposition
name: Trigonometric definition of Chebyshev polynomials
msc: [33C45, 41A50, 42A05]
uses: [M6EAR1JHPP, CFWMB0S5NK]
about: [M6EAR1JHPP]
sources:
  - url: https://en.wikipedia.org/wiki/Chebyshev_polynomials
---

## Statement

Let $T_0 = 1$, $T_1 = x$ and $T_{n+1} = 2x \, T_n - T_{n-1}$ for $n \ge 1$ be the [[Chebyshev polynomials|M6EAR1JHPP]] of the first kind.
Then for every integer $n \ge 0$ and every real $\theta$,
$$T_n(\cos \theta) = \cos(n \theta).$$
Equivalently, $T_n(x) = \cos(n \arccos x)$ for all $x \in [-1, 1]$.
Moreover, $T_n$ is the only polynomial with this property.

## Remarks

Proof idea: the cases $n = 0$ and $n = 1$ are clear.
The sum formula for the [[cosine|CFWMB0S5NK]] gives $\cos((n + 1)\theta) + \cos((n - 1)\theta) = 2 \cos \theta \cos(n \theta)$.
This is the recursion of the $T_n$ evaluated at $x = \cos \theta$, so induction on $n$ gives the identity.
Uniqueness holds because two polynomials that agree on the infinite set $[-1, 1]$ are equal.

Example: $\cos(3\theta) = 4 \cos^3 \theta - 3 \cos \theta$, which matches $T_3 = 4x^3 - 3x$.

Many texts take the identity as the definition of $T_n$ and derive the recursion from it.
Outside $[-1, 1]$ the same polynomial satisfies $T_n(\cosh t) = \cosh(n t)$ for real $t$, by the same induction.

## Explanations

### L1 human

The cosine of $n$ times an angle can always be written as a polynomial in the cosine of the angle.
The Chebyshev polynomial $T_n$ is exactly that polynomial.
So on $[-1, 1]$, $T_n$ is a cosine wave seen through the change of variable $x = \cos \theta$.

### L2 human

The identity explains most properties of $T_n$ at once.
It gives $\abs{T_n} \le 1$ on $[-1, 1]$, the zeros $\cos \frac{(2k - 1)\pi}{2n}$ and the extreme points $\cos \frac{k\pi}{n}$.
It also turns expansions in $T_n$ on $[-1, 1]$ into cosine series in $\theta$, so Fourier methods apply to Chebyshev series.
The composition rule $T_m(T_n(x)) = T_{mn}(x)$ follows from $\cos(m \cdot n\theta) = \cos(mn\theta)$.
