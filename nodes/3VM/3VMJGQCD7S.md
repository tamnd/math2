---
tag: 3VMJGQCD7S
kind: statement
role: theorem
name: Hartman's uniqueness theorem for harmonic maps
msc: ["58E20", 53C43]
uses: [KZJYG9DS3M, 7CBT4SM83Y, 1X42JAA349, 9YA6S6HD9V, NSYMQMHPDN, E6HDE1DFXD, AP4A0GX0V2]
about: [KZJYG9DS3M]
sources:
  - url: https://en.wikipedia.org/wiki/Harmonic_map
---

## Statement

Let $M$ be a compact [[Riemannian manifold|7CBT4SM83Y]] without boundary.
Let $N$ be a compact Riemannian manifold whose [[sectional curvature|1X42JAA349]] is nonpositive everywhere.

1. Let $u_0, u_1 \colon M \to N$ be [[harmonic maps|KZJYG9DS3M]] that are [[homotopic|9YA6S6HD9V]].
Then there is a smooth homotopy $u_t$, $t \in [0, 1]$, from $u_0$ to $u_1$ such that each $u_t$ is harmonic and has the same [[energy|E6HDE1DFXD]] as $u_0$.
Moreover, for each $x \in M$ the curve $t \mapsto u_t(x)$ is a [[geodesic|NSYMQMHPDN]] traversed at constant speed, and this speed does not depend on $x$.
2. Suppose that the sectional curvature of $N$ is negative everywhere.
Let $u \colon M \to N$ be a harmonic map whose image is neither a point nor a closed geodesic.
Then $u$ is the only harmonic map in its homotopy class.

## Remarks

Lift to the universal cover of $N$, which is a Hadamard manifold, and join $u_0(x)$ to $u_1(x)$ by the unique geodesic in the right homotopy class.
In nonpositive curvature the squared distance between the two lifted maps is a subharmonic function on $M$, so it is constant on the compact manifold $M$.
Following the geodesics gives the homotopy $u_t$, and the second variation of the energy shows that every $u_t$ is again harmonic.
With strictly negative curvature the homotopy must be constant, unless all the geodesics $t \mapsto u_t(x)$ run along one closed geodesic, which forces the image of $u$ into that geodesic.

The curvature hypothesis is needed.
For $M = N = S^2$ with the round metric, every rotation is a harmonic map homotopic to the identity.
So harmonic maps in a homotopy class are far from unique.
Uniqueness also fails in the flat case: on a flat torus $N$, composing a harmonic map with a translation gives a family of homotopic harmonic maps, as part 1 allows.

## Explanations

### L1 human

When the target space curves like a saddle everywhere, harmonic maps are rigid.
Two harmonic maps that can be deformed into each other differ only by sliding along geodesics in a uniform way.
When the curvature is strictly negative, even this sliding is impossible except in degenerate cases, so the harmonic map is unique.

### L2 human

The theorem complements the [[Eells–Sampson theorem|AP4A0GX0V2]], which gives existence of a harmonic map in each homotopy class under the same curvature hypothesis.
Together they say that, for targets of negative curvature, a homotopy class of maps usually has a canonical harmonic representative.
This is used in rigidity theory, for example for maps between locally symmetric spaces and in the study of Teichmüller space.
