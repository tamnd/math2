---
tag: 9ZBAX4ZPX0
kind: statement
role: theorem
name: Herglotz representation theorem
msc: [31A05, 31A20, 30H99]
uses: [0DEB0JMN0W, W19567AVYG, 0NAHXR1FRH]
about: [0DEB0JMN0W, TCYSWCTYYM]
sources:
  - url: https://en.wikipedia.org/wiki/Positive_harmonic_function
---

## Statement

Let $\mathbb{D} = \set{z \in \C : \abs{z} < 1}$ and $\mathbb{T} = \set{\zeta \in \C : \abs{\zeta} = 1}$.

1. Let $u \colon \mathbb{D} \to \R$ be a [[harmonic function|0DEB0JMN0W]] with $u \ge 0$. Then there is a unique finite positive Borel measure $\mu$ on $\mathbb{T}$ such that for every $z \in \mathbb{D}$
$$u(z) = \int_{\mathbb{T}} \frac{1 - \abs{z}^2}{\abs{\zeta - z}^2}\, d\mu(\zeta).$$
Its total mass is $\mu(\mathbb{T}) = u(0)$.
2. Let $f$ be a [[holomorphic function|0NAHXR1FRH]] on $\mathbb{D}$ with $\operatorname{Re} f \ge 0$. Then, with $\mu$ the measure of part 1 for $u = \operatorname{Re} f$, for every $z \in \mathbb{D}$
$$f(z) = \int_{\mathbb{T}} \frac{\zeta + z}{\zeta - z}\, d\mu(\zeta) + i \operatorname{Im} f(0).$$

## Remarks

The integrand in part 1 is the [[Poisson kernel|W19567AVYG]].
For $0 < r < 1$, the measures $\mu_r = u(r\zeta)\, \frac{\abs{d\zeta}}{2\pi}$ on $\mathbb{T}$ are positive with total mass $u(0)$, by the mean value property.
The Poisson formula on the disc of radius $r$ expresses $u(rz)$ through $\mu_r$; a weak-star limit of the $\mu_r$ as $r \to 1$ gives $\mu$.
Part 2 follows from part 1 as in the [[Schwarz integral formula|61WT6CE08W]].
Example: for the Dirac measure at $1$, the formula of part 1 gives $u(z) = (1 - \abs{z}^2)/\abs{1 - z}^2$, a positive harmonic function that is unbounded near $1$, and part 2 gives $f(z) = (1 + z)/(1 - z)$.
The hypothesis $u \ge 0$ is needed.
The function $u(z) = \operatorname{Re} \frac{(1 + z)^2}{(1 - z)^2}$ is harmonic but takes both signs.
It is not the Poisson integral of any finite signed measure, because it grows too fast near $1$.

## Explanations

### L1 human

A nonnegative harmonic function on the disc is a weighted average of the simplest ones, the Poisson kernels with their pole at a single boundary point.
The weights form a measure on the boundary circle.
So every such function is built from a mass distribution on the circle, and the mass distribution is unique.

### L2 human

The theorem identifies the cone of nonnegative harmonic functions on the disc with the cone of finite positive measures on the circle.
In the holomorphic form it describes all functions with nonnegative real part, the Carathéodory class, which is used in coefficient problems for [[univalent functions|R91E83SDBD]].
It also underlies spectral representations in operator theory, such as the moment problem and the spectral theorem for unitary operators.
Together with [[Harnack's inequality|YNH832D50W]] it controls the size of positive harmonic functions.
