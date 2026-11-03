---
tag: B40G0GTJTA
kind: statement
role: theorem
name: Tennis racket theorem
msc: ["70E50", "70E15"]
uses: [PN15F4ZS8D, WVGTEH6P10, 0F2SYCKDT2, WWAXYRZ006]
about: [PN15F4ZS8D]
sources:
  - url: https://en.wikipedia.org/wiki/Tennis_racket_theorem
same_as:
  wikidata: Q944604
  wikipedia: Tennis racket theorem
---

## Statement

Let a rigid body move about its centre of mass with no external torque.
Let its principal moments of inertia satisfy $I_1 < I_2 < I_3$, with principal axes $e_1, e_2, e_3$.
Consider [[Euler's equations|PN15F4ZS8D]] with zero torque for the angular velocity $\omega = (\omega_1, \omega_2, \omega_3)$ in the body frame.
For $\Omega \ne 0$ and $i \in \set{1, 2, 3}$, the steady rotation $\omega = \Omega e_i$ is an equilibrium of these equations.
Then:

1. the rotations about $e_1$ and $e_3$, the axes of least and greatest moment, are [[Lyapunov stable|0F2SYCKDT2]];
2. the rotation about $e_2$, the intermediate axis, is unstable.

## Remarks

Linearize at $\omega = \Omega e_2$ by writing $\omega = (\varepsilon_1, \Omega, \varepsilon_3)$ and dropping products of the small terms.
The equations become $I_1 \dot\varepsilon_1 = (I_2 - I_3)\Omega\varepsilon_3$ and $I_3 \dot\varepsilon_3 = (I_1 - I_2)\Omega\varepsilon_1$, so $\ddot\varepsilon_1 = \frac{(I_2 - I_3)(I_1 - I_2)}{I_1 I_3}\Omega^2 \varepsilon_1$.
The coefficient is positive exactly because $I_2$ lies between $I_1$ and $I_3$, so the linearization has a positive eigenvalue, which gives instability.
At $\Omega e_1$ or $\Omega e_3$ the same coefficient is negative; stability then follows from the two conserved quantities, since the nearby [[polhodes|WWAXYRZ006]] are small closed curves around the axis.
If two principal moments are equal, the conclusion changes.
For $I_1 = I_2 < I_3$, the rotation $\Omega e_1$ is not Lyapunov stable: a small component $\omega_3 = \delta \ne 0$ makes $(\omega_1, \omega_2)$ turn at the constant rate $(I_3 - I_1)\delta / I_1$, so $\omega$ later comes close to $-\Omega e_1$.

Example: a tennis racket or a book tossed with a spin about its intermediate axis makes a half turn about another axis during the flight.
The same effect was seen in space by Vladimir Dzhanibekov with a spinning wing nut, and it is also called the Dzhanibekov effect.

## Explanations

### L1 human

Every rigid body has three special axes, about which it can spin steadily.
Spin it about the axis with the largest or the smallest moment of inertia, and it keeps spinning about it.
Spin it about the middle axis, and the smallest error grows: the body flips over and over during the spin.

### L2 human

The theorem is a model case of the stability analysis of equilibria by linearization and conserved quantities.
The instability at the middle axis is seen in the linearization.
The stability at the extreme axes needs the energy and angular momentum integrals, since the linearization only shows a centre.
The flips about the middle axis follow the separatrix polhodes and are described by Jacobi elliptic functions.
With slow loss of energy, as in a flexible spacecraft, the axis of greatest moment is the only stable one.
