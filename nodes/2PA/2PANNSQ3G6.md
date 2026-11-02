---
tag: 2PANNSQ3G6
kind: statement
role: theorem
name: Lempert's theorem on convex domains
msc: [32F45, 32H02]
uses: [DY8QQ5GTTX, SYNST4W3FR, 275YT975A8, 02AS45T3H9]
about: [DY8QQ5GTTX, SYNST4W3FR]
sources:
  - url: https://en.wikipedia.org/wiki/Kobayashi_metric
---

## Statement

Let $\Omega \subseteq \C^n$ be a bounded [[convex|02AS45T3H9]] domain.
Let $k_\Omega$ be its [[Kobayashi pseudodistance|DY8QQ5GTTX]] and $c_\Omega$ its [[Carathéodory pseudodistance|SYNST4W3FR]], both normalised to equal the Poincaré distance on the unit disc.
Then:

1. $c_\Omega(p, q) = k_\Omega(p, q)$ for all $p, q \in \Omega$;
2. for all $p \ne q$ in $\Omega$ there is a [[complex geodesic|275YT975A8]] $\varphi \colon \mathbb{D} \to \Omega$ whose image contains $p$ and $q$.

## Remarks

László Lempert proved the theorem in 1981.
The infinitesimal Kobayashi–Royden and Carathéodory–Reiffen metrics of $\Omega$ also agree.
Proof idea: an extremal disc through $p$ and $q$ exists by a normal families argument.
For smoothly bounded strongly convex domains, Lempert studied the boundary behaviour of extremal discs and constructed, for each one, a holomorphic left inverse $\Omega \to \mathbb{D}$.
This left inverse shows that the Carathéodory distance is at least the Kobayashi distance, and the general convex case follows by exhaustion.
Example: for the unit ball $B$ and $p = 0$, both distances equal $\tanh^{-1}\abs{q}$, and the complex geodesics through $0$ include the maps $\zeta \mapsto \zeta v$ for unit vectors $v$.
Convexity cannot simply be dropped: for an annulus $A \subset \C$, which is not simply connected, one has $c_A(p, q) < k_A(p, q)$ for $p \ne q$.

## Explanations

### L1 human

There are two natural ways to measure distances in a domain of $\C^n$ using holomorphic maps.
One uses discs mapped into the domain, the other uses functions from the domain to the disc.
In general the second way gives smaller numbers.
Lempert's theorem says that for convex domains both ways give the same answer, and that the distance between two points is realised by a single holomorphic disc through them.

### L2 human

The theorem makes the invariant geometry of convex domains computable: distances are realised by extremal discs, which solve a variational problem with a rich structure.
It is used to study biholomorphic maps of convex domains, boundary behaviour of holomorphic maps, and the [[pluricomplex Green function|3MQVKVGYYY]], which on convex domains is determined by the Kobayashi distance.
For general pseudoconvex domains the two distances can differ, so the theorem singles out convexity, and later work extended it to strongly linearly convex domains.
