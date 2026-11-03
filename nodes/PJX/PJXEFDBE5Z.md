---
tag: PJXEFDBE5Z
kind: definition
name: Branch and bound
msc: [90C57, 90C10, 90C27]
defines: ZZ7C50WN56
uses: [NS0Q42Y3FX, PYMHHM5Z6F, 9GX3WH5EQF]
sources:
  - url: https://en.wikipedia.org/wiki/Branch_and_bound
---

## Definition

Let $S$ be a set and $f \colon S \to \R$ a function, and consider the [[optimization problem|NS0Q42Y3FX]] of minimizing $f$ over $S$.
Assume two procedures are given.
A *bounding* procedure takes a subset $T \subseteq S$ from a given class.
It returns a number $L(T)$ with $L(T) \le f(s)$ for all $s \in T$, and possibly an element of $T$.
A *branching* procedure splits such a subset $T$ into finitely many subsets $T_1, \dots, T_k$ of the class whose union is $T$.
*Branch and bound* is the following iteration, with a list $\mathcal{L}$ of open subproblems and an incumbent value $U$.

1. Start with $\mathcal{L} = \set{S}$, $U = +\infty$ and no incumbent.
2. If $\mathcal{L}$ is empty, stop: the incumbent, if any, is a minimizer, and if there is none then $S$ is empty.
3. Remove some $T$ from $\mathcal{L}$ and compute $L(T)$.
4. If $T$ is empty or $L(T) \ge U$, discard $T$ (*prune*) and go to step 2.
5. If the bounding procedure returned an element $s \in T$ with $f(s) < U$, make $s$ the incumbent and set $U = f(s)$.
6. If it returned an element $s$ with $f(s) = L(T)$, then $T$ is *solved*; go to step 2.
7. Otherwise branch $T$ into $T_1, \dots, T_k$, add them to $\mathcal{L}$, and go to step 2.

## Remarks

The method is correct because a discarded subset contains no element better than the incumbent, and the subsets in $\mathcal{L}$ always cover the part of $S$ not yet discarded.
It terminates when every chain of branchings ends after finitely many steps, for example when $S$ is finite and each branching makes proper subsets.

Example: for an [[integer program|9GX3WH5EQF]] with bounded variables, $L(T)$ is the optimal value of the [[linear programming relaxation|PYMHHM5Z6F]] over $T$.
If the relaxation optimum $x^*$ is integral, $T$ is solved and $x^*$ is a candidate incumbent.
Otherwise, for a variable with fractional value $x_i^*$, one branches into $T \cap \set{x_i \le \floor{x_i^*}}$ and $T \cap \set{x_i \ge \ceil{x_i^*}}$.

Non-example: plain enumeration of all elements of $S$ branches all the way down but never prunes.
It uses no bound, so it is not branch and bound in the useful sense.

The order in which subproblems are taken from $\mathcal{L}$ (depth-first, best-bound first) and the choice of branching variable strongly affect the running time but not the correctness.
