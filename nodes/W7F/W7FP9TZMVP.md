---
tag: W7FP9TZMVP
kind: statement
role: theorem
name: Atserias-Müller theorem
msc: ["03F20", "68Q17"]
topics: [CBAF7J051K]
audience: research
uses: [6JSH907W5R, WBECDG163W, 3QKF32ZAKN, SBDQH0TJ5X, MFN5GYZH5Z]
about: [6JSH907W5R, WBECDG163W]
proofs: [K496M1G1R0]
sources:
  - url: https://en.wikipedia.org/wiki/Proof_complexity
    locator: Automatability
history:
  first_stated: "2019"
  notes: "Albert Atserias and Moritz Müller, Automating Resolution is NP-Hard, Symposium on Foundations of Computer Science (FOCS) 2019; journal version in the Journal of the ACM, 2020."
---

## Statement

A polynomial-time map sends each 3-CNF $F$ to a CNF $G(F)$ that has a resolution refutation with polynomially many clauses when $F$ is satisfiable, and none with fewer than exponentially many when $F$ is unsatisfiable.

For a CNF $H$, let $r(H)$ be the number of occurrences of literals in the clauses of $H$.
Let $s(H)$ be the least number of clauses of a [[resolution refutation|6JSH907W5R]] of $H$, with $s(H) = \infty$ when $H$ is satisfiable.
For $t \colon \mathbb{N} \to \mathbb{N}$, resolution is *automatizable in time $t$* if an algorithm, given an unsatisfiable CNF $H$, outputs a resolution refutation of $H$ within $t(r(H) + s(H))$ steps.

**Theorem (Atserias and Müller).**

1. There are reals $c, d > 0$ and a function $G$, computable in polynomial time, from 3-CNFs to CNFs, with the following property.
   Let $F$ be a 3-CNF, and let $r = r(G(F))$ and $s = s(G(F))$.
   If $F$ is satisfiable, then $s < r^c$.
   If $F$ is unsatisfiable, then $s > 2^{r^{1/d}}$.
2. If resolution is automatizable in polynomial time, then $\mathrm{P} = \mathrm{NP}$.
3. If resolution is automatizable in quasi-polynomial time $2^{(\log m)^{O(1)}}$, then every problem in NP is decidable in quasi-polynomial time.
4. If resolution is automatizable in subexponential time $2^{m^{o(1)}}$, then every problem in NP is decidable in subexponential time.

The measure is the number of clauses, and the reduction maps satisfiable formulas to formulas with short refutations.
In the unsatisfiable case $G(F)$ may be satisfiable, and then $s = \infty$.

## Remarks

### Why each hypothesis is needed

The time is measured against $r + s$.
If it were measured against $r(H)$ alone, then no algorithm could automate resolution, with no assumption at all.
The [[pigeonhole formulas|RJ571F7FF0]] need $2^{\Omega(n)}$ clauses by [[Haken's theorem|4PCEYEW3JG]], and writing the output takes that long.

The output must be a resolution refutation.
The theorem says nothing about weak automatizability, where the output may be a proof in a stronger system.
Pudlák showed that weak automatizability is equivalent to a polynomial-time separation of the canonical pair: satisfiable formulas against formulas with short refutations.
To use $G$ against this pair one would need $G(F)$ satisfiable whenever $F$ is unsatisfiable.
Then $G$ would reduce unsatisfiability to [[SAT|3QKF32ZAKN]], and NP would equal [[coNP|NBSD5FG7NY]].

Part 4 needs subexponential time.
The argument compares the time bound with $2^{r^{1/d}}$ for large inputs, and it needs $t$ to be non-decreasing and computable within its own time bound.

### Consequences

It is NP-hard to approximate $s(H)$ within a factor $2^{r^{1/d}} / r^c$.
A [[SAT solver|3BW08M1EX7]] that produces resolution refutations cannot run in time polynomial in $r + s$ on all unsatisfiable inputs, unless P = NP.

### Converse

The converse of part 2 holds.
If P = NP, then the question "does $H$ have a resolution refutation with at most $\ell$ clauses?", with $\ell$ in unary, is in P, since a refutation is a certificate checkable in polynomial time.
A refutation can then be built clause by clause by the self-reduction of NP search problems, trying $\ell = 1, 2, 4, \dots$ in turn.
The first success has $\ell < 2 s(H)$, so the total time is polynomial in $r(H) + s(H)$.

### Watch out

The theorem does not say that short refutations fail to exist.
In the satisfiable case $G(F)$ has short refutations, and the hardness is in finding them.
It also does not transfer by itself to stronger systems, and hardness of automating Nullstellensatz, polynomial calculus and cutting planes was proved later by adapting the method.

## History

Atserias and Müller proved the theorem in a paper at FOCS 2019, and the journal version appeared in the Journal of the ACM in 2020.
The main earlier result for resolution was that it is not automatizable in polynomial time unless W[P] collapses to FPT.
This is due to Alekhnovich and Razborov, whose reduction used randomness, and Eickmeyer, Grohe and Grüber removed the randomness.
The earlier result also holds for tree-like resolution, which is automatizable in quasi-polynomial time, so it could not rule out quasi-polynomial automatization of resolution.

## Explanations

### L1 human

Resolution is a simple kind of proof that many computer programs for logic produce.
The theorem says that no fast program can always find a resolution proof about as short as the shortest one, unless every problem in NP has a fast solution.
So finding good proofs is hard, even for this simple kind of proof.

### L2 human

The theorem is used as follows.

1. Suppose an algorithm finds a resolution refutation of every unsatisfiable CNF $H$ in time $t(r(H) + s(H))$, with $t$ a non-decreasing polynomial.
2. Given a 3-CNF $F$, compute $G(F)$ and run the algorithm for $t(r + r^c)$ steps.
3. If $F$ is satisfiable, then $s < r^c$, so the algorithm finishes in time, and its output can be checked.
4. If $F$ is unsatisfiable, every refutation has more than $2^{r^{1/d}}$ clauses, so for large $r$ no refutation can be written in the budget.
5. So the run decides whether $F$ is satisfiable in polynomial time, and P = NP.

A trap is to read the theorem as "short refutations do not exist": in the satisfiable case they do exist, and the hardness is in finding them.

### L3 human

The map $G$ sends $F$ to a relativized form of the CNF "$F$ has a resolution refutation with $s$ lines".
If $F$ is satisfiable, a satisfying assignment shows line by line that no such refutation exists, and this argument is a short resolution refutation.
If $F$ is unsatisfiable, a random restriction and a width lower bound show that every refutation is long.
The method was then adapted to other systems, and the main open question became weak automatizability.
See [[automatizability|WBECDG163W]] for the other negative results, and [[NP|SBDQH0TJ5X]] for the class.
