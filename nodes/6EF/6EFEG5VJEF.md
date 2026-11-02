---
tag: 6EFEG5VJEF
kind: statement
role: theorem
name: Chow's theorem
msc: [32J25, 14A10, 32C25]
uses: [VMDTGTMN9P, 7GJ4STCNNM, A4H4CZ2V35]
about: [GB7M582M5Y, A4H4CZ2V35]
sources:
  - url: https://en.wikipedia.org/wiki/Algebraic_geometry_and_analytic_geometry
---

## Statement

Let $n \ge 0$ and let $A$ be a closed [[analytic subset|VMDTGTMN9P]] of the [[complex projective space|7GJ4STCNNM]] $\mathbb{P}^n(\C)$.
Then $A$ is algebraic: there are finitely many homogeneous polynomials $P_1, \dots, P_m \in \C[z_0, \dots, z_n]$ such that
$$A = \set{[z_0 : \cdots : z_n] \in \mathbb{P}^n(\C) : P_1(z) = \cdots = P_m(z) = 0}.$$

## Remarks

A short proof uses the Remmert–Stein theorem.
Let $p \colon \C^{n+1} \setminus \set{0} \to \mathbb{P}^n(\C)$ be the projection, and let $C = p^{-1}(A)$, the cone over $A$; it is analytic in $\C^{n+1} \setminus \set{0}$, and each irreducible component has dimension at least $1$.
By the Remmert–Stein theorem, $C \cup \set{0}$ is an analytic subset of $\C^{n+1}$.
Near $0$ it is the zero set of holomorphic functions $f_1, \dots, f_r$.
Since $C$ is invariant under $z \mapsto \lambda z$, the homogeneous parts of the Taylor series of the $f_j$ also vanish on $C$.
By Hilbert's basis theorem, finitely many of these homogeneous polynomials define $C \cup \set{0}$.
Example: the image of $\mathbb{P}^1(\C)$ under $[s : t] \mapsto [s^3 : s^2 t : s t^2 : t^3]$ is a closed analytic subset of $\mathbb{P}^3(\C)$, and indeed it is the twisted cubic, defined by $z_0 z_2 = z_1^2$, $z_1 z_3 = z_2^2$ and $z_0 z_3 = z_1 z_2$.
Compactness of projective space is essential: in $\C$, the analytic subset $\Z$ is not the zero set of polynomials, since a nonzero polynomial has finitely many zeros.

## Explanations

### L1 human

In projective space, any set cut out locally by holomorphic equations is cut out globally by polynomial equations.
So every compact complex submanifold of projective space, however it is presented, is an algebraic variety.
This is a striking rigidity: holomorphic functions are much more flexible than polynomials, but the compactness of projective space forces algebraicity.

### L2 human

Chow's theorem is the first instance of the principle that compact analytic objects in projective space are algebraic, which Serre's GAGA theorems extend to coherent sheaves and their cohomology.
Combined with the Kodaira embedding theorem, it shows that every compact Kähler manifold with an integral Kähler class is a projective algebraic variety.
It also implies that holomorphic maps between projective varieties are algebraic, by applying the theorem to their graphs.
