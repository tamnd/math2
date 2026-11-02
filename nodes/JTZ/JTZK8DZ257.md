---
tag: JTZK8DZ257
kind: concept
name: Perturbation theory of linear operators
msc: [47A55, 47A10]
sources:
  - url: https://en.wikipedia.org/wiki/Perturbation_theory
---

## Summary

Perturbation theory of linear operators studies how the properties of an operator $T$ change under replacement by $T + V$.
Here $V$ is small in a suitable sense.
The main questions are whether closedness, self-adjointness, the [[spectrum|BMKATJ802A]] and the eigenvalues survive the change, and how they move.
The basic notion of smallness for unbounded operators is relative boundedness.
The theory underlies much of mathematical quantum mechanics, where a Hamiltonian is a free part plus an interaction.

## Explanations

### L1 human

Often one understands a simple operator well, such as the Laplacian, and wants to study a more complicated one obtained by adding a term.
Perturbation theory says when the new operator still behaves like the old one.
For matrices, this is the study of how [[eigenvalues move|VR89YHC0TX]] when the entries change a little.
For differential operators, the added term may be unbounded, so one measures it against the original operator instead of against the identity.
For example, a bounded real-valued potential $V$ added to the Laplacian on $\R^n$ never destroys self-adjointness.
