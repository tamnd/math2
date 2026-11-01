---
tag: D9B92SQ2GF
kind: statement
role: theorem
name: Ahlfors–Bers theorem
msc: [30C62, 30F60]
uses: [SB8KG46NHP, 9J7GFJ1GPF, 0NAHXR1FRH]
about: [SB8KG46NHP, 9J7GFJ1GPF]
sources:
  - url: https://en.wikipedia.org/wiki/Measurable_Riemann_mapping_theorem
---

## Statement

Let $\mu \colon \C \to \C$ be measurable with $\norm{\mu}_\infty < 1$.
Let $f^\mu \colon \C \to \C$ be the unique [[quasiconformal|SB8KG46NHP]] homeomorphism that fixes $0$ and $1$ and solves the [[Beltrami equation|9J7GFJ1GPF]] $f_{\bar z} = \mu f_z$ almost everywhere.
Its existence and uniqueness is the [[measurable Riemann mapping theorem|TZHD2WKNSD]].

Let $U \subset \C$ be open.
Let $t \mapsto \mu_t$ be a map from $U$ to the open unit ball of $L^\infty(\C)$ that is holomorphic as a map into the Banach space $L^\infty(\C)$.
Then for each $z \in \C$, the function $t \mapsto f^{\mu_t}(z)$ is [[holomorphic|0NAHXR1FRH]] on $U$.

## Remarks

For $\mu$ with compact support, the proof writes the derivative $\partial_{\bar z}$ of the principal solution as a Neumann series in the [[Beurling transform|TX32GDQ330]] $T$: $\mu + \mu T \mu + \mu T(\mu T \mu) + \cdots$.
The series converges in $L^p$ for some $p > 2$, because $T$ is an isometry of $L^2$ and its norm on $L^p$ tends to $1$ as $p \to 2$.
Each term depends holomorphically on $\mu$, and the convergence is locally uniform.
The same argument gives real-analytic dependence when $\mu_t$ depends real-analytically on a real parameter.

Example: for $\mu_t = t \chi$ with $\chi$ the indicator of a disc and $\abs{t} < 1$, the normalized solutions $f^{\mu_t}$ form a holomorphic family of quasiconformal maps through $f^{0} = \id$.

The condition $\norm{\mu_t}_\infty < 1$ is needed: when $\norm{\mu}_\infty = 1$ the Beltrami equation is degenerate, and a homeomorphic solution need not exist.

## Explanations

### L1 human

A Beltrami coefficient $\mu$ prescribes how a map should distort infinitesimal circles into ellipses.
The measurable Riemann mapping theorem gives exactly one normalized map with this distortion.
The Ahlfors–Bers theorem adds that if the prescribed distortion moves holomorphically with a complex parameter, then so does the map.

### L2 human

This holomorphic dependence is what makes [[Teichmüller space|ZZGC6BZNJ5]] a complex manifold: Beltrami coefficients give coordinates, and the solution maps vary holomorphically with them.
It is also the tool behind holomorphic motions and quasiconformal surgery in complex dynamics, where one deforms a rational map by moving an invariant Beltrami coefficient in a holomorphic family.
