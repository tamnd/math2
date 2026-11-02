---
tag: W3YYX63R9R
kind: statement
role: theorem
name: Fundamental theorem of affine geometry
msc: [51A15, 51N10]
uses: [09XNAPTJQ7, 0JF0TVYGWT, 04C5ZBG1WT, 0AFNNTRTJE]
about: [0JF0TVYGWT, 09XNAPTJQ7]
sources:
  - url: https://en.wikipedia.org/wiki/Affine_transformation
---

## Statement

Let $k$ be a [[field|04C5ZBG1WT]] with at least $3$ elements, and let $n \ge 2$.
Let $A$ and $B$ be [[affine spaces|09XNAPTJQ7]] of dimension $n$ over $k$, with spaces of translations $V$ and $W$.
Let $f \colon A \to B$ be a bijection that maps every line of $A$ onto a line of $B$.
Then there are a field automorphism $\sigma$ of $k$ and a bijection $\varphi \colon V \to W$ such that:

1. $\varphi(u + v) = \varphi(u) + \varphi(v)$ and $\varphi(c v) = \sigma(c) \varphi(v)$ for all $u, v \in V$ and $c \in k$;
2. $f(p + v) = f(p) + \varphi(v)$ for all $p \in A$ and $v \in V$.

In particular, if $k = \R$, then $f$ is an [[affine map|0JF0TVYGWT]].

## Remarks

A map with properties 1 and 2 is called semi-affine.
The proof first shows that $f$ maps planes to planes and hence parallel lines to parallel lines.
Parallelograms then go to parallelograms, which makes the induced map $\varphi$ on vectors well defined and additive.
Comparing $f$ on the points of one line with its action on scalars defines $\sigma$ and shows that it is a field automorphism.
For $k = \R$ the only field automorphism is the identity, which gives the last sentence.

The hypothesis on $k$ is needed: over $\F_2$ each line has exactly two points, so every bijection maps lines to lines.
For $n \ge 3$ there are bijections of $\F_2^n$ that are not affine, for example the map that swaps two basis vectors $e_1$ and $e_2$ and fixes every other point.
It is not affine, since it fixes $0$, $e_3$ and $e_1 + e_3$ but moves $e_1$.
The hypothesis $n \ge 2$ is needed too: an affine line has only one line, so every bijection of it qualifies.
Over $\C$, the map $(z_1, \dots, z_n) \mapsto (\bar z_1, \dots, \bar z_n)$ maps lines to lines but is not affine, so $\sigma$ cannot be dropped.

## Explanations

### L1 human

Suppose a bijection of the plane or of space sends every straight line to a straight line.
Over the real numbers, the theorem says that it must then be an affine map: a linear map followed by a translation.
So keeping lines straight forces the map to keep ratios along lines and parallelism.
Over other fields the map can also twist the scalars by a field automorphism, such as complex conjugation.

### L2 human

The theorem shows that the incidence structure of points and lines determines the affine structure of $k^n$, up to the automorphisms of $k$.
It is the affine version of the [[fundamental theorem of projective geometry|GKV4RVXBRE]], and one can pass between the two by adding or removing a hyperplane at infinity.
It shows that the [[collineations|V7PRPN24CV]] of a real affine space are exactly the invertible affine maps.
It also explains why the automorphism group of a field enters the symmetry groups of geometries over that field.
