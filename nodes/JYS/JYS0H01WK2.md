---
tag: JYS0H01WK2
kind: concept
name: Hamiltonian perturbation theory
msc: [70H09, 70H08]
sources:
  - url: https://en.wikipedia.org/wiki/Perturbation_theory
---

## Summary

Hamiltonian perturbation theory studies systems whose Hamiltonian is a small perturbation $H_0 + \varepsilon H_1$ of an integrable one $H_0$.
It looks for [[canonical transformations|AGA36YKX4F]] close to the identity that remove the dependence on the angles order by order in $\varepsilon$.
These are usually built from a [[generating function|NXK6HD49NZ]].
The method meets the problem of small divisors, which comes from resonances between the frequencies of the unperturbed motion.
Controlling these small divisors is the core of the [[Kolmogorov–Arnold–Moser theorem|3ZZSXKM16Z]].
See the [[definition|ARM5EN11YN]].

## Explanations

### L1 human

Many real systems are almost solvable: the planets almost follow Kepler ellipses, perturbed slightly by each other.
Perturbation theory starts from the solvable motion and corrects it step by step in powers of the small parameter.
In Hamiltonian mechanics the corrections are made by clever changes of variables that keep the Hamiltonian form.
Each step averages the perturbation over the fast periodic motion and keeps only its slow effect.
Trouble arises when two frequencies are in a simple ratio, since then the corrections can become large.
