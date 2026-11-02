---
tag: 6TJ7YHP2HE
kind: concept
name: Krylov–Bogolyubov averaging
msc: [34C29, 70K65]
sources:
  - url: https://en.wikipedia.org/wiki/Krylov%E2%80%93Bogoliubov_averaging_method
same_as:
  wikidata: Q6439640
  wikipedia: Krylov–Bogoliubov averaging method
---

## Summary

Krylov–Bogolyubov averaging is a method for differential equations with a small parameter and a fast periodic dependence on time.
It replaces the right-hand side by its average over one period and studies the simpler averaged equation.
The averaging theorem says that solutions of the two equations stay close over long time intervals, of length of order $1/\varepsilon$.
It is a basic tool for weakly nonlinear oscillations in mechanics and physics.
See the [[definition|NGYZK893VE]].

## Explanations

### L1 human

When a quantity changes slowly but is shaken quickly back and forth, the fast shaking mostly cancels out.
Only the average effect of each period of shaking matters over a long time.
For example, $x' = \varepsilon x \sin^2 t$ has the averaged equation $y' = \frac{1}{2} \varepsilon y$, because $\sin^2 t$ has average $\frac{1}{2}$.
The exact solution is $x_0 e^{\varepsilon (t/2 - \sin(2t)/4)}$, and it differs from $x_0 e^{\varepsilon t/2}$ only by the small wobbling factor $e^{-\varepsilon \sin(2t)/4}$.
