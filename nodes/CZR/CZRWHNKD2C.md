---
tag: CZRWHNKD2C
kind: statement
role: theorem
name: Kodaira–Nakano vanishing theorem
msc: [32L20, 14F17]
uses: [JSGWAN2RJV, QAC7BYK9KX, J45KWFHENP, PQ6Q143ARJ, DC81TCR98Y]
about: [J45KWFHENP, PQ6Q143ARJ]
sources:
  - url: https://en.wikipedia.org/wiki/Kodaira_vanishing_theorem
---

## Statement

Let $X$ be a compact [[complex manifold|JSGWAN2RJV]] of dimension $n$, and let $L$ be a [[positive line bundle|J45KWFHENP]] on $X$.
For $p \ge 0$ let $\Omega_X^p$ be the sheaf of holomorphic $p$-forms on $X$.
Then
$$H^q(X, \Omega_X^p \otimes L) = 0 \quad \text{whenever } p + q > n,$$
where $H^q$ is [[sheaf cohomology|PQ6Q143ARJ]].

## Remarks

The theorem is also called the Akizuki–Nakano vanishing theorem.
A compact manifold with a positive line bundle is Kähler, with Kähler form $\omega = i\Theta_h$ given by the curvature of a positive metric $h$.
By Dolbeault's theorem, a class in $H^q(X, \Omega^p_X \otimes L)$ is represented by an $L$-valued harmonic [[$(p,q)$-form|DC81TCR98Y]] $u$.
The Bochner–Kodaira–Nakano identity gives $\langle [i\Theta_h, \Lambda] u, u \rangle \le 0$ for such $u$, and with $\omega = i\Theta_h$ the operator $[i\Theta_h, \Lambda]$ is multiplication by $p + q - n$ on $(p,q)$-forms.
So $(p + q - n)\norm{u}^2 \le 0$, which forces $u = 0$ when $p + q > n$.

The case $p = n$ is the [[Kodaira vanishing theorem|NY77DQ2AX8]]: $\Omega^n_X = K_X$ and $H^q(X, K_X \otimes L) = 0$ for $q \ge 1$.
By Serre duality the theorem is equivalent to $H^q(X, \Omega^p_X \otimes L^{-1}) = 0$ for $p + q < n$.

Positivity of $L$ cannot be dropped.
For $X = \mathbb{P}^1$, $n = 1$, $p = q = 1$ and $L$ trivial, one has $H^1(\mathbb{P}^1, \Omega^1) \cong \C \ne 0$, though $p + q = 2 > 1$.

## Explanations

### L1 human

The theorem says that many cohomology groups of a positive line bundle, twisted by holomorphic forms, are zero.
Zero cohomology means that local problems have global solutions, so it is a strong and useful conclusion.
The hypothesis is a positivity of curvature, the analytic form of ampleness.

### L2 human

The proof is a model of the Bochner technique: a curvature identity shows that harmonic representatives must vanish.
It extends Kodaira vanishing, which is the case $p = n$, to all bundles of holomorphic forms.
It is used to prove the Lefschetz hyperplane theorem for cohomology and to control cohomology of $\Omega^p$ on projective manifolds.
For vector bundles the analogous result needs Nakano positivity, not just Griffiths positivity.
