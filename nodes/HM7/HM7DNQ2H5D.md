---
tag: HM7DNQ2H5D
kind: statement
role: theorem
name: Karp–Lipton theorem
msc: [68Q15, 68Q06]
uses: [P0A5DVRYDW, QQRA9GBW51, TDQ7AXGM6P, 3QKF32ZAKN, PTD7E1PKV4]
about: [P0A5DVRYDW, TDQ7AXGM6P]
sources:
  - url: https://en.wikipedia.org/wiki/Karp–Lipton_theorem
same_as:
  wikidata: Q6373327
  wikipedia: Karp–Lipton theorem
---

## Statement

If $\mathrm{NP} \subseteq \mathrm{P/poly}$, then the [[polynomial hierarchy|TDQ7AXGM6P]] collapses to its second level:
$$\mathrm{PH} = \Sigma_2^p = \Pi_2^p.$$
Here [[P/poly|P0A5DVRYDW]] is the class of languages with polynomial-size circuits and [[NP|QQRA9GBW51]] is nondeterministic polynomial time.

## Remarks

It suffices to show $\Pi_2^p \subseteq \Sigma_2^p$.
Take a $\Pi_2^p$ language given by $x \in L \iff \forall y \, \exists z \, R(x, y, z)$ with $R$ in P and $y, z$ of polynomial length.
The inner question "$\exists z \, R(x, y, z)$" is an NP question, so it reduces to the [[Boolean satisfiability problem|3QKF32ZAKN]], which by hypothesis has polynomial-size circuits.
By self-reducibility one may take circuits that output a satisfying assignment whenever one exists.
Then $x \in L$ if and only if there is such a circuit $C$ with the following property: for all $y$, the assignment that $C$ produces for the instance $(x, y)$ satisfies $R$.
This is a $\Sigma_2^p$ condition, because a circuit that answers wrongly can only cause rejection.

## Explanations

### L1 human

If every NP problem could be solved by small circuits, even circuits that nobody knows how to build, then the polynomial hierarchy would shrink to two levels.
Since most researchers believe the hierarchy is infinite, they also believe that NP problems such as satisfiability need circuits of superpolynomial size.
This makes circuit lower bounds a natural way to attack the P versus NP problem.

### L2 human

Richard Karp and Richard Lipton published the result in 1980.
The trick is that a guessed circuit can be checked: a wrong circuit for a self-reducible problem is caught, so guessing it costs only one existential quantifier.
Later work improved the collapse, for example to $\mathrm{S}_2^p$ and to $\mathrm{ZPP}^{\mathrm{NP}}$.
Since $\mathrm{BPP} \subseteq \mathrm{P/poly}$, the theorem also shows that if NP were contained in [[BPP|PTD7E1PKV4]], the hierarchy would collapse.
