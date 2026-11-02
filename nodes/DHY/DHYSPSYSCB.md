---
tag: DHYSPSYSCB
kind: statement
role: theorem
name: Yau–Tian–Donaldson conjecture
msc: [32Q20, 53C55, 14J45]
uses: [6ETEBA8827, CK1DCPC3D3, WJKA5YBTJ7, GT56RTG9X5]
about: [6ETEBA8827]
sources:
  - url: https://en.wikipedia.org/wiki/K-stability
---

## Statement

Let $X$ be a Fano manifold, that is a compact complex manifold whose anticanonical line bundle $-K_X$ is ample.
Then $X$ admits a [[Kähler–Einstein metric|6ETEBA8827]] if and only if the pair $(X, -K_X)$ is K-polystable.

Here K-polystable means the following.
A test configuration of $(X, -K_X)$ is a $\C^*$-equivariant degeneration of $X$ with a line bundle extending a power of $-K_X$.
For every normal test configuration, the Donaldson–Futaki invariant is nonnegative.
Moreover, it vanishes only for normal test configurations that are products of $X$ with $\C$ twisted by a $\C^*$-action on $X$.

## Remarks

This form of the conjecture, for Fano manifolds, was proved by Xiuxiong Chen, Simon Donaldson and Song Sun.
The direction "Kähler–Einstein implies K-polystable" is the easier one.
The converse uses the continuity method with metrics having cone singularities along a divisor, and [[Gromov–Hausdorff limits|GT56RTG9X5]] of these metrics, which are shown to be algebraic varieties.

Example: the blow-up of $\C P^2$ at one point is Fano but has no Kähler–Einstein metric.
Its automorphism group is not reductive, which rules out a Kähler–Einstein metric by Matsushima's theorem, and a test configuration coming from a $\C^*$-action has negative Donaldson–Futaki invariant.
By contrast $\C P^n$ with the Fubini–Study metric is Kähler–Einstein and K-polystable.

The general conjecture asks for a constant scalar curvature Kähler metric in $c_1(L)$ on a polarized manifold $(X, L)$, under a suitable notion of K-stability.
That general form is open, and the right stability notion for it is still discussed.

## Explanations

### L1 human

For manifolds with positive first Chern class, a Kähler–Einstein metric may or may not exist.
The theorem says that existence is equivalent to an algebraic condition called K-polystability.
This condition looks at all ways the manifold can degenerate and checks a sign on each of them.

### L2 human

The negative and zero cases of the Kähler–Einstein problem follow from the [[Calabi conjecture|WJKA5YBTJ7]] methods with no obstruction.
In the Fano case there are obstructions, such as the Futaki invariant and Matsushima's theorem, and K-stability collects them all.
The statement links a nonlinear partial differential equation to geometric invariant theory, in the spirit of the Hitchin–Kobayashi correspondence for vector bundles.
After the proof, much work has gone into deciding K-stability of explicit Fano manifolds by algebraic means.
