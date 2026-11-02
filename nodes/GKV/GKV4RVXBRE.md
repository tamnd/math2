---
tag: GKV4RVXBRE
kind: statement
role: theorem
name: Fundamental theorem of projective geometry
msc: [51A10, 51N15]
uses: [ZT9A6JK8QF, V7PRPN24CV, P1MKTF7MWQ, 04C5ZBG1WT]
about: [V7PRPN24CV, P1MKTF7MWQ]
sources:
  - url: https://en.wikipedia.org/wiki/Homography
---

## Statement

Let $k$ and $k'$ be [[fields|04C5ZBG1WT]], and let $n \ge 2$.
Let $V$ and $W$ be vector spaces of dimension $n + 1$ over $k$ and $k'$.
Let $f \colon \mathbb{P}(V) \to \mathbb{P}(W)$ be a [[collineation|V7PRPN24CV]] between their [[projective spaces|ZT9A6JK8QF]].
Then there are a field isomorphism $\sigma \colon k \to k'$ and a bijection $T \colon V \to W$ such that:

1. $T(u + v) = T u + T v$ and $T(c v) = \sigma(c) T v$ for all $u, v \in V$ and $c \in k$;
2. $f([v]) = [T v]$ for every nonzero $v \in V$.

In particular, every collineation of $\mathbb{P}^n(\R)$ with $n \ge 2$ is a [[projective transformation|P1MKTF7MWQ]].

## Remarks

A map $T$ with property 1 is called $\sigma$-semilinear.
The proof fixes a frame of $n + 2$ points in general position and its image, and normalizes $T$ on the corresponding basis vectors.
Comparing the points of a line through two frame points with the scalars defines $\sigma$.
The configuration theorems that hold in $\mathbb{P}(V)$ show that $\sigma$ is additive and multiplicative.
For $k = \R$ the identity is the only field automorphism, so $T$ is linear and $f$ is a projective transformation.

The hypothesis $n \ge 2$ is needed: $\mathbb{P}^1(k)$ has only one line, so every bijection of it is a collineation.
The automorphism $\sigma$ cannot be dropped in general: complex conjugation of all coordinates is a collineation of $\mathbb{P}^2(\C)$ that is not a projective transformation.
The theorem also holds for vector spaces over division rings.
The collineation group of $\mathbb{P}^n(k)$, for $n \ge 2$, is therefore the group $\mathrm{P\Gamma L}(n + 1, k)$ of maps induced by semilinear bijections.

## Explanations

### L1 human

A collineation only promises to keep points on a line together.
The theorem says that, in a projective space of dimension at least $2$, this alone forces the map to come from linear algebra, up to a twist of the scalars.
Over the real numbers there is no twist, so every line-preserving bijection of the real projective plane is given by an invertible $3 \times 3$ matrix.

### L2 human

The theorem identifies the symmetry group of the incidence geometry $\mathbb{P}^n(k)$ with $\mathrm{P\Gamma L}(n + 1, k)$, which is $\mathrm{PGL}(n + 1, k)$ extended by the automorphisms of $k$.
Together with the [[Veblen–Young theorem|NPNNXWMVCC]], it shows that the incidence structure of a projective space of dimension at least $3$ determines its coordinate division ring up to isomorphism.
The [[fundamental theorem of affine geometry|W3YYX63R9R]] is the affine counterpart.
It is the reason why, in real projective geometry, one may freely replace "collineation" by "projective transformation".
