---
tag: CTK8AH98Z1
kind: statement
role: theorem
name: Cook–Levin theorem
msc: [68Q17, 03B05]
uses: [3QKF32ZAKN, JGZWHWA8P8, QQRA9GBW51, V0K79AD81V, M7SDX137WE, 0B3D4C8YF2]
about: [3QKF32ZAKN, JGZWHWA8P8]
sources:
  - url: https://en.wikipedia.org/wiki/Cook%E2%80%93Levin_theorem
same_as:
  wikidata: Q377276
  wikipedia: Cook–Levin theorem
---

## Statement

The [[Boolean satisfiability problem|3QKF32ZAKN]] SAT is [[NP-complete|JGZWHWA8P8]].
That is, SAT lies in [[NP|QQRA9GBW51]], and $A \le_p \mathrm{SAT}$ for every $A \in \mathrm{NP}$, where $\le_p$ is [[polynomial-time reducibility|V0K79AD81V]].

## Remarks

SAT lies in NP because a satisfying assignment can be checked in polynomial time.
For the hardness, let $A$ be decided by a [[nondeterministic Turing machine|M7SDX137WE]] $M$ in time $p(n)$ for a polynomial $p$.
For an input $w$ of length $n$, the computation of $M$ on $w$ fits in a table of $(p(n)+1) \times (p(n)+1)$ cells, one row per step.
Boolean variables describe the content of each cell, the state, and the head position at each step.
A formula in [[conjunctive normal form|0B3D4C8YF2]] of size polynomial in $n$ then says that the table is a legal accepting computation, so it is satisfiable exactly when $M$ accepts $w$.

The same proof shows that SAT restricted to conjunctive normal form is NP-complete.
A further reduction, which splits long clauses with new variables, shows that 3-SAT is NP-complete.
Stephen Cook proved the theorem in 1971, and Leonid Levin proved it independently in 1973.

## Explanations

### L1 human

The theorem says that satisfiability of propositional formulas is among the hardest problems in NP.
Any problem whose solutions can be checked quickly can be rewritten, quickly, as a question about whether some formula can be made true.
So a fast algorithm for SAT would give fast algorithms for every problem in NP.

### L2 human

The theorem gives the first NP-complete problem, and every later proof of NP-completeness rests on it.
To show a new problem $C$ in NP is NP-complete, it suffices to reduce SAT, or a known NP-complete problem, to $C$.
Karp used this method in 1972 to show that 21 combinatorial problems, such as clique and Hamiltonian cycle, are NP-complete.
The proof idea, encoding a whole computation as a formula, appears again in the proof that true quantified Boolean formulas are PSPACE-complete.
