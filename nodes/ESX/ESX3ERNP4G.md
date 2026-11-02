---
tag: ESX3ERNP4G
kind: definition
name: Geometric invariant theory
msc: [14L24, 14L30]
defines: 9EG3A21ET1
uses: [2XS84PWE3S, RW85C34GQW, A4H4CZ2V35, RRK8P6TXG2, A39XQHCVNW, 6VTR5EBNYC]
sources:
  - url: https://en.wikipedia.org/wiki/Geometric_invariant_theory
---

## Definition

Let $k$ be an algebraically closed field and let $G$ be a [[reductive group|2XS84PWE3S]] over $k$.
Let $G$ [[act|RW85C34GQW]] on a [[projective variety|A4H4CZ2V35]] $X$.
Let $L$ be an [[ample line bundle|RRK8P6TXG2]] on $X$ with a $G$-linearization, that is, a lift of the action of $G$ to $L$.
Write $R = \bigoplus_{m \ge 0} H^0(X, L^{m})$ and let $R^G$ be its [[ring of invariants|6VTR5EBNYC]].

1. A point $x \in X$ is *semistable* if there are $m \ge 1$ and an invariant section $s \in H^0(X, L^m)^G$ with $s(x) \ne 0$.
2. A semistable point $x$ is *stable* if its orbit $G x$ is closed in the semistable locus $X^{ss}$ and its stabilizer $G_x$ is finite.
3. A point that is not semistable is *unstable*.

The *GIT quotient* is the projective variety
$$X /\!\!/_L\, G = \operatorname{Proj} R^G,$$
built with the [[Proj construction|A39XQHCVNW]], together with the morphism $\pi \colon X^{ss} \to X /\!\!/_L\, G$ induced by the inclusion $R^G \subseteq R$.

## Remarks

The ring $R^G$ is finitely generated because $G$ is reductive, so the quotient is a projective variety.
The map $\pi$ is a good categorical quotient: two semistable points have the same image exactly when the closures of their orbits meet in $X^{ss}$.
On the stable locus $X^s$, which is open, $\pi$ restricts to a geometric quotient $X^s \to X^s / G$ whose fibres are single orbits.

Example: let $G = \mathbb{G}_m$ act on $X = \mathbb{P}^1$ by $t \cdot [x : y] = [t x : t^{-1} y]$, linearized on $L = \mathcal{O}(1)$ by the weights $1$ and $-1$.
A monomial $x^a y^b$ of degree $m = a + b$ is invariant exactly when $a = b$.
So the invariant sections are the multiples of powers of $xy$, and the semistable points are those with $xy \ne 0$.
They form a single orbit, which is closed in $X^{ss}$, and the stabilizer of $[1 : 1]$ is $\set{\pm 1}$, so these points are stable and the quotient is a point.

Non-example: the point $[1 : 0]$ is unstable, since every invariant section of positive degree is a multiple of $xy$ and vanishes there.

For an affine variety $X = \operatorname{Spec} A$ with the trivial linearization, the quotient is $X /\!\!/ G = \operatorname{Spec} A^G$.
