---
tag: WR3RBEH4QQ
kind: statement
role: theorem
name: Gibbs–Bogoliubov inequality
msc: [82B05, 82B10, 82B03]
uses: [G1P1A0N7NZ, 0RWMRTPC87, 0WQNRCNY3M]
about: [G1P1A0N7NZ]
sources:
  - url: https://en.wikipedia.org/wiki/Helmholtz_free_energy
---

## Statement

Let $(\Omega, \nu)$ be a $\sigma$-finite measure space and let $\beta > 0$.
Let $H, H_0 \colon \Omega \to \R$ be measurable with $Z_0 = \int_\Omega e^{-\beta H_0} \, d\nu \in (0, \infty)$ and $Z = \int_\Omega e^{-\beta H} \, d\nu < \infty$.
Let $\langle \cdot \rangle_0$ be the [[expected value|0WQNRCNY3M]] under the [[canonical ensemble|G1P1A0N7NZ]] $e^{-\beta H_0} \, d\nu / Z_0$, and assume $\langle \abs{H - H_0} \rangle_0 < \infty$.
Let $F = -\beta^{-1} \ln Z$ and $F_0 = -\beta^{-1} \ln Z_0$ be the free energies.
Then
$$F \le F_0 + \langle H - H_0 \rangle_0,$$
with equality if and only if $H - H_0$ is constant almost everywhere for the measure $e^{-\beta H_0} d\nu$.

## Remarks

Proof idea: $Z / Z_0 = \langle e^{-\beta (H - H_0)} \rangle_0$, and [[Jensen's inequality|0RWMRTPC87]] for the convex function $e^{-\beta x}$ gives $Z / Z_0 \ge e^{-\beta \langle H - H_0 \rangle_0}$.
Taking $-\beta^{-1} \ln$ of both sides gives the claim.
The same inequality holds for Hermitian matrices, with $Z = \tr e^{-\beta H}$ and $\langle A \rangle_0 = \tr(e^{-\beta H_0} A) / Z_0$; this is the Peierls–Bogoliubov inequality.
Example: in mean-field theory one takes $H_0$ to be a sum of independent single-site terms with free parameters.
Minimizing the right side over these parameters gives the best such upper bound on $F$.
It gives a variational principle: $F = \min_{H_0} \left( F_0 + \langle H - H_0 \rangle_0 \right)$, attained at $H_0 = H$.

## Explanations

### L1 human

The free energy of a hard system is at most the free energy of an easy trial system plus the average energy difference, measured in the easy system.
So one can bound a quantity that cannot be computed by quantities that can.
Choosing the best trial system gives the best bound.

### L2 human

This inequality is the rigorous basis of mean-field and variational approximations, such as the Curie–Weiss treatment of the Ising model.
It is equivalent to the nonnegativity of the Kullback–Leibler divergence between the trial ensemble and the true canonical ensemble.
It is also the finite-volume form of the [[Gibbs variational principle|BKWBKNEAKA]], which characterizes Gibbs measures as maximizers of entropy minus energy.
