---
tag: RAHKB0ZHG8
kind: statement
role: theorem
name: Callan–Symanzik equation
msc: [81T17, 81T15]
uses: [1X0W3AEBEJ, HVGDXMPB29]
about: [1X0W3AEBEJ]
sources:
  - url: https://en.wikipedia.org/wiki/Callan%E2%80%93Symanzik_equation
same_as:
  wikidata: Q1027148
  wikipedia: Callan–Symanzik equation
---

## Statement

Consider the massless [[quartic interaction|HVGDXMPB29]] in four dimensions, renormalized at a momentum scale $M$ with renormalized coupling $\lambda$.
Let $G^{(n)}(x_1, \dots, x_n; M, \lambda)$ be its renormalized connected $n$-point function.
Define the beta function $\beta(\lambda) = M \, \partial\lambda/\partial M$ and the anomalous dimension $\gamma(\lambda) = \tfrac12 M \, \partial \log Z/\partial M$.
Both derivatives are taken with the bare coupling and the cutoff fixed, and $Z$ is the field strength renormalization.
Then, in perturbation theory and after the cutoff is removed,
$$\left( M \frac{\partial}{\partial M} + \beta(\lambda) \frac{\partial}{\partial \lambda} + n\,\gamma(\lambda) \right) G^{(n)}(x_1, \dots, x_n; M, \lambda) = 0.$$

## Remarks

The proof: the bare $n$-point function does not depend on $M$.
It equals $Z^{n/2}$ times the renormalized one.
Differentiating $Z^{n/2} G^{(n)}$ with respect to $M$ at fixed bare parameters, using the chain rule for $\lambda(M)$, gives the equation.

At one loop, for the coupling normalized as $\lambda\phi^4/4!$, one has $\beta(\lambda) = 3\lambda^2/(16\pi^2) + O(\lambda^3)$ and $\gamma = O(\lambda^2)$.
Since $\beta > 0$, the running coupling grows at high momenta, which is related to [[quantum triviality|H0VT0FGP6T]].
For a massive theory there is an extra term for the dependence on the mass.
The original equation of Callan and Symanzik is the version in which the mass is varied, with an inhomogeneous term.

## Explanations

### L1 human

After renormalization, a quantum field theory carries a reference energy scale $M$, chosen by the physicist.
Physics cannot depend on this choice.
The Callan–Symanzik equation says how the coupling and the normalization of the field must change when $M$ changes, so that predictions stay the same.

### L2 human

Solving the equation by the method of characteristics gives the running coupling $\bar\lambda(p)$.
A correlation function at momentum scale $p$ then equals a function computed at coupling $\bar\lambda(p)$, times a factor built from $\gamma$.
So perturbation theory is reliable at momenta where the running coupling is small.
The sign of $\beta$ decides between [[asymptotic freedom|RRN63RT562]], as in Yang–Mills theory, and growth at high energy, as in $\phi^4$ theory and quantum electrodynamics.
