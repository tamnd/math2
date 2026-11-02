---
tag: TDCY8TASCS
kind: statement
role: theorem
name: Peixoto's theorem
msc: [37C20, 34D30, 37D15]
uses: [D4MGFAHVMT, 0299VCW1TH, 01TPMXM6NM, 0AA97XA70K, 60TDCPY4Z4, 0BSJSX7ME2, 0AAQ73WRFB]
about: [D4MGFAHVMT]
sources:
  - url: https://en.wikipedia.org/wiki/Peixoto%27s_theorem
same_as:
  wikidata: Q7160983
  wikipedia: Peixoto's theorem
---

## Statement

Let $M$ be a compact, connected, orientable two-dimensional smooth manifold without boundary.
Let $\mathfrak{X}^1(M)$ be the space of $C^1$ [[vector fields|0299VCW1TH]] on $M$ with the $C^1$ topology.
Let $\varphi_t$ be the flow of $X$.
A point $p$ is *nonwandering* for $X$ if for every neighbourhood $U$ of $p$ and every $T > 0$, some $t > T$ has $\varphi_t(U) \cap U \neq \emptyset$.
A *saddle connection* is an orbit that tends to a saddle point both forward and backward in time.

1. A vector field $X \in \mathfrak{X}^1(M)$ is [[structurally stable|D4MGFAHVMT]] if and only if all four conditions below hold.
   (a) $X$ has finitely many zeros, and each of them is a [[hyperbolic equilibrium point|01TPMXM6NM]].
   (b) $X$ has finitely many [[periodic orbits|0AA97XA70K]], and each of them is hyperbolic.
   This means that the derivative of its [[Poincaré map|60TDCPY4Z4]] at a fixed point has no eigenvalue of modulus $1$.
   (c) $X$ has no saddle connection.
   (d) Every nonwandering point of $X$ is a zero of $X$ or lies on a periodic orbit.
2. The set of structurally stable vector fields is open and [[dense|0BSJSX7ME2]] in $\mathfrak{X}^1(M)$.

## Remarks

Vector fields with properties (a) to (d) are the Morse–Smale vector fields on a surface.
Necessity of each condition comes from small perturbations: a non-hyperbolic zero or orbit can be split or removed, and a saddle connection can be broken.
Sufficiency builds a homeomorphism between phase portraits from the finite combinatorial data of zeros, periodic orbits and separatrices.
Density is the harder part; its proof relies on the Poincaré–Bendixson theory, which is special to dimension two.
On the torus, the linear flow $\dot\theta_1 = 1$, $\dot\theta_2 = \alpha$ with $\alpha$ irrational has every point nonwandering and no periodic orbit, so it fails (d) and is not structurally stable.
In dimension three and higher, structurally stable systems need not be Morse–Smale; Anosov flows are an example.

## Explanations

### L1 human

On a closed surface, a flow is robust under small changes exactly when its picture is simple.
Simple means: finitely many rest points and cycles, all of them strongly attracting or repelling in some direction, no orbit joining two saddles, and no complicated recurrence.
The theorem also says that almost every flow on such a surface is of this kind.

### L2 human

The theorem extends the result of Andronov and Pontryagin for flows on a disc to all compact orientable surfaces.
It is the model for the notion of Morse–Smale systems in higher dimensions.
In a typical course it follows the study of [[hyperbolic equilibria|01TPMXM6NM]], [[limit cycles|0AAQ73WRFB]] and the Poincaré–Bendixson theorem.
