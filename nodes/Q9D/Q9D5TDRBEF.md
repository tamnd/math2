---
tag: Q9D5TDRBEF
kind: statement
role: theorem
name: Coifman–Rochberg–Weiss commutator theorem
msc: [42B20, 47B47, 42B35]
uses: [QJYTXFT8Y4, HTMCEARGDD, FRNDFJ9WQ5, SASP14MA1Z, NSCEBXM7ZM]
about: [QJYTXFT8Y4, HTMCEARGDD]
sources:
  - url: https://en.wikipedia.org/wiki/Bounded_mean_oscillation
---

## Statement

Let $n \ge 1$ and $1 < p < \infty$.
For a locally integrable function $b$ on $\R^n$ and an operator $T$, let $[b, T]$ be the commutator $[b, T] f = b \, Tf - T(bf)$, defined for smooth $f$ with compact support.

Let $T$ be a [[singular integral operator|HTMCEARGDD]] with kernel $\Omega(x/\abs{x})/\abs{x}^n$.
Here $\Omega$ is infinitely differentiable on the unit sphere and has mean zero.
Let $R_1, \dots, R_n$ be the [[Riesz transforms|FRNDFJ9WQ5]], and write $\norm{\cdot}$ for the operator norm on the [[Lp space|SASP14MA1Z]] $L^p(\R^n)$.

1. If $b$ has [[bounded mean oscillation|QJYTXFT8Y4]], then $[b, T]$ extends to a bounded operator on $L^p(\R^n)$.
Moreover $\norm{[b, T]} \le C \norm{b}_{\mathrm{BMO}}$, where $C$ depends only on $n$, $p$ and $\Omega$.
2. If $[b, R_j]$ is bounded on $L^p(\R^n)$ for every $j = 1, \dots, n$, then $b$ is in BMO.
Moreover $\norm{b}_{\mathrm{BMO}} \le C \sum_{j=1}^n \norm{[b, R_j]}$, where $C$ depends only on $n$ and $p$.

## Remarks

One proof of part 1 uses a conjugation trick.
For complex $z$, the operator $T_z f = e^{zb} T(e^{-zb} f)$ satisfies $\frac{d}{dz} T_z \big\vert_{z = 0} = [b, T]$.
By the John–Nirenberg inequality, $e^{p \, \mathrm{Re}(z) b}$ is a Muckenhoupt $A_p$ weight when $\abs{z} \norm{b}_{\mathrm{BMO}}$ is small.
So, by weighted theory, $T_z$ is bounded on $L^p$ uniformly for small $\abs{z}$.
The Cauchy integral formula for the derivative then gives the bound on $[b, T]$.

For $n = 1$ the only Riesz transform is the [[Hilbert transform|NSCEBXM7ZM]] $H$, and the theorem says that $[b, H]$ is bounded on $L^p(\R)$ exactly when $b \in \mathrm{BMO}(\R)$.
Example: $b(x) = \log \abs{x}$ is unbounded, so the multiplication operator by $b$ is unbounded on $L^p$, yet $[b, H]$ is bounded because $b \in \mathrm{BMO}$.

## Explanations

### L1 human

A commutator $[b, T]$ measures how much the order of two operations matters: first apply $T$ and then multiply by $b$, or first multiply by $b$ and then apply $T$.
For a singular integral $T$, the theorem says that this difference is a bounded operator exactly when $b$ has bounded mean oscillation.
So BMO is precisely the class of multipliers that almost commute with singular integrals.

### L2 human

The theorem gives a new characterization of BMO through operators, complementing its definition by mean oscillations and Fefferman's duality with $H^1$.
By duality it is equivalent to a factorization theorem for $H^1$: every $f \in H^1(\R^n)$ can be written as $\sum_k \sum_j \left( g_{k,j} R_j h_{k,j} + h_{k,j} R_j g_{k,j} \right)$ with $\sum_k \sum_j \norm{g_{k,j}}_{p'} \norm{h_{k,j}}_p < \infty$.
Commutators with BMO functions appear in the study of div-curl lemmas in compensated compactness and of elliptic equations with VMO coefficients.
The commutator $[b, T]$ is compact on $L^p$ exactly when $b$ is in the closure of smooth compactly supported functions in BMO, a result of Uchiyama.
