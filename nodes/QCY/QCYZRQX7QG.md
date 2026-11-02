---
tag: QCYZRQX7QG
kind: statement
role: theorem
name: Generic smoothness
msc: [14A15, 14B25]
uses: [HV6YBS0YDH, EXKGG9X6J0, ESPG0BJERZ, 02SJG1HC32]
about: [EXKGG9X6J0]
sources:
  - url: https://en.wikipedia.org/wiki/Smooth_scheme
---

## Statement

Let $k$ be an [[algebraically closed field|02SJG1HC32]] of characteristic $0$.
Let $f \colon X \to Y$ be a morphism of [[varieties|HV6YBS0YDH]] over $k$, and assume that $X$ is nonsingular, that is, a [[regular scheme|ESPG0BJERZ]].
Then there is a nonempty open subset $V \subseteq Y$ such that the restriction $f^{-1}(V) \to V$ is a [[smooth morphism|EXKGG9X6J0]].

## Remarks

The proof reduces to the case where $f$ is dominant and then compares tangent spaces.
In characteristic $0$, the field extension $k(Y) \subseteq k(X)$ is separable, so the map on differentials is generically surjective.
Then $\Omega_{X/Y}$ is locally free of the right rank over a dense open set, which gives smoothness there.
For example, the map $\mathbb{A}^2_k \to \mathbb{A}^1_k$, $(x, y) \mapsto x^2 + y^2$, is smooth over $V = \mathbb{A}^1_k \setminus \set{0}$.
Its fibre over $0$ is the pair of lines $x = \pm i y$, which is singular at the origin.
The characteristic hypothesis is necessary.
In characteristic $p > 0$, the Frobenius map $\mathbb{A}^1_k \to \mathbb{A}^1_k$, $t \mapsto t^p$, is a morphism of smooth curves.
Its fibre over $a$ is $\operatorname{Spec} k[t]/(t^p - a) = \operatorname{Spec} k[t]/((t - b)^p)$ with $b^p = a$, a non-reduced point, so it is smooth over no nonempty open set.

## Explanations

### L1 human

Take a smooth variety and a map from it to another variety.
Some fibres of the map may be singular, but generic smoothness says that this only happens over a small closed set.
Over almost every point of the target, the fibre is a smooth variety.
In positive characteristic this can fail, because a map like $t \mapsto t^p$ has only thickened points as fibres.

### L2 human

Generic smoothness is the algebraic counterpart of Sard's theorem on critical values of smooth maps.
It is the main tool behind Bertini's theorem: a general hyperplane section of a smooth projective variety in characteristic $0$ is smooth.
It also shows that, in characteristic $0$, in a family with smooth total space over a curve, only finitely many fibres are singular.
Its proof uses that every finitely generated field extension in characteristic $0$ is separably generated.
