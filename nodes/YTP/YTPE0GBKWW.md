---
tag: YTPE0GBKWW
kind: statement
role: theorem
name: Expansion in spherical harmonics
msc: [31B05, 33C55]
uses: [0DEB0JMN0W, MVYFSYMECG, 2C3PAQ7H50, 0YE5868HZB, 08VZ57PT26]
about: [0DEB0JMN0W, 3F32Y21HP4]
sources:
  - url: https://en.wikipedia.org/wiki/Spherical_harmonics
---

## Statement

Let $n \ge 2$, let $R > 0$, and let $B = \set{x \in \R^n : \abs{x} < R}$ be the [[open ball|0YE5868HZB]] of radius $R$ centred at $0$.
Let $u$ be a [[harmonic function|0DEB0JMN0W]] on $B$.
Then there is a unique sequence $(p_k)_{k \ge 0}$ with the following property.
Each $p_k$ is a [[harmonic|MVYFSYMECG]] [[homogeneous polynomial|2C3PAQ7H50]] of degree $k$ on $\R^n$, and
$$u(x) = \sum_{k=0}^{\infty} p_k(x), \qquad x \in B.$$
The series converges absolutely and [[uniformly|08VZ57PT26]] on each compact subset of $B$.

## Remarks

Proof idea: on a smaller closed ball, $u$ is the Poisson integral of its boundary values.
The [[Poisson kernel|TCYSWCTYYM]] of the ball expands as a series of zonal harmonics, each a homogeneous harmonic polynomial in $x$; integrating term by term gives the $p_k$.
Uniqueness follows by comparing homogeneous parts of the Taylor series of $u$ at $0$, since $p_k$ is the degree $k$ part.
In polar form $x = r\zeta$ with $\abs{\zeta} = 1$, the expansion reads $u(r\zeta) = \sum_k r^k p_k(\zeta)$, and the restriction of $p_k$ to the unit sphere is a [[spherical harmonic|3F32Y21HP4]] of degree $k$.
The restrictions to the sphere of harmonic polynomials of different degrees are orthogonal in $L^2$ of the sphere.
In fact, $L^2$ of the sphere is the orthogonal direct sum of the spaces of spherical harmonics of each degree.
Example: on the unit disc in $\R^2 = \C$, $u = \operatorname{Re} \frac{1}{1 - z}$ is harmonic, and $u(r e^{i\theta}) = \sum_{k \ge 0} r^k \cos k\theta$, where $r^k \cos k\theta = \operatorname{Re} z^k$ is a homogeneous harmonic polynomial of degree $k$.

## Explanations

### L1 human

A harmonic function on a ball can be written as an infinite sum of harmonic polynomials, one for each degree.
This is like a Taylor series, but each piece is itself harmonic.
On the sphere, the pieces become the spherical harmonics, the analogues of $\cos k\theta$ and $\sin k\theta$ on a circle.

### L2 human

This is the higher-dimensional version of the Fourier series of a harmonic function on the disc.
It solves the Dirichlet problem on a ball by separation of variables: expand the boundary data in spherical harmonics and multiply the degree $k$ part by $(\abs{x}/R)^k$.
In $\R^3$ the space of spherical harmonics of degree $k$ has dimension $2k + 1$, and the expansion is the one used for gravitational and electrostatic potentials.
The [[Fischer decomposition|JWNRB34ZGV]] describes how all polynomials, not only harmonic ones, split into harmonic pieces.
