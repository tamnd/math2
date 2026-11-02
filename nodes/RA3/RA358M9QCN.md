---
tag: RA358M9QCN
kind: statement
role: theorem
name: Friedberg–Muchnik theorem
msc: [03D25, 03D28]
uses: [TN9G24VABN, PA4PYQ1PZ0, P5N2ND3VCG]
about: [TN9G24VABN, P5N2ND3VCG]
sources:
  - url: https://en.wikipedia.org/wiki/Friedberg–Muchnik_theorem
same_as:
  wikidata: Q111982312
  wikipedia: Friedberg–Muchnik theorem
---

## Statement

There are [[computably enumerable sets|TN9G24VABN]] $A, B \subseteq \N$ such that $A \not\le_T B$ and $B \not\le_T A$, where $\le_T$ is [[Turing reducibility|PA4PYQ1PZ0]].

## Remarks

The sets are built in stages by the [[priority method|3BZFSC5QZ2]].
The requirements are $R_{2e}$: $A \ne \Phi_e^B$ and $R_{2e+1}$: $B \ne \Phi_e^A$, where $\Phi_e$ is the $e$-th oracle machine.
To meet $R_{2e}$, one picks a witness $x$ and puts $x$ into $A$ once $\Phi_e^B(x) = 0$ appears, then tries to keep $B$ unchanged below the use of that computation.
Actions for requirements of lower priority may be undone, but each requirement is injured only finitely often, so all of them are met.

As a consequence, the degrees $\deg(A)$ and $\deg(B)$ are incomparable, so neither is $\mathbf{0}$ or $\mathbf{0}'$.
So both lie strictly between $\mathbf{0}$ and $\mathbf{0}'$, which solves [[Post's problem|1RVF7DWG8C]].

## Explanations

### L1 human

Some sets of numbers can be listed by a computer but not decided by one.
The theorem says that two such sets can be built so that neither helps to compute the other.
So the hardness of listable sets is not a single ladder: there are incomparable levels.

### L2 human

This is the result that solved Post's problem, and its proof introduced the finite-injury [[priority method|3BZFSC5QZ2]].
The same method, refined, shows that the computably enumerable [[Turing degrees|P5N2ND3VCG]] are dense (Sacks) and that every countable partial order embeds in them.
The construction is also a model for many other constructions in computability theory, where infinitely many conflicting requirements must be met at once.
