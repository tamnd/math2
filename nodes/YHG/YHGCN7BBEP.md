---
tag: YHGCN7BBEP
kind: statement
role: theorem
name: Feasible interpolation for resolution
msc: ["03F20", "68Q17"]
topics: [CBAF7J051K]
audience: research
uses: [6JSH907W5R, 59GJCM8C66, SQXNFGVADX, TRS2HY57EG]
about: [6JSH907W5R, 59GJCM8C66]
proofs: [66YH6V1HBG]
sources:
  - url: https://en.wikipedia.org/wiki/Proof_complexity
    locator: Feasible interpolation
history:
  first_stated: "1997"
  notes: "Jan Krajíček, Interpolation theorems, lower bounds for proof systems, and independence results for bounded arithmetic, Journal of Symbolic Logic 62 (1997)."
---

## Statement

Let $p$, $q$ and $r$ be disjoint lists of variables.
Let $A(p, q)$ be a CNF whose variables are among $p, q$, and let $B(p, r)$ be a CNF whose variables are among $p, r$.
For a $0$-$1$ assignment $a$ of $p$, write $A(a, q)$ and $B(a, r)$ for the CNFs obtained by substituting $a$ for $p$.
Let $\pi$ be a [[resolution refutation|6JSH907W5R]] of $A \wedge B$ with $L$ clauses.

**Theorem (Krajíček).**

1. There is a [[Boolean circuit|SQXNFGVADX]] $I(p)$ with AND, OR and NOT gates and at most $4L$ gates such that, for every $0$-$1$ assignment $a$ of $p$:
   - if $I(a) = 0$, then $A(a, q)$ is unsatisfiable;
   - if $I(a) = 1$, then $B(a, r)$ is unsatisfiable.
2. If no variable of $p$ occurs negatively in $A$, then there is such a circuit with AND and OR gates only, and at most $4L$ gates.
3. In both cases the circuit can be computed from $\pi$ in time polynomial in the size of $\pi$.

So resolution has [[feasible interpolation|59GJCM8C66]] and monotone feasible interpolation.
The measure is the number $L$ of clauses of $\pi$, and the bound on the circuit is in gates.

## Remarks

### Why each hypothesis is needed

- **The private variables are disjoint.** Let $y$ occur in both $A = \set{y}$ and $B = \set{\neg y}$, with $p$ empty. A refutation has $3$ clauses. A circuit in no variables is a constant. The constant $0$ would claim that $A$ is unsatisfiable, and the constant $1$ that $B$ is, and both claims are false.
- **The sign condition in part 2.** Let $A = \set{\neg p}$ and $B = \set{p}$, so $p$ occurs negatively in $A$. At $a = 1$, $B(1)$ is satisfied, so $I(1) = 0$. At $a = 0$, $A(0)$ is satisfied, so $I(0) = 1$. So $I = \neg p$, and no monotone circuit computes it.
- **The proof system.** For [[extended Frege|5YSE04SHFH]] in place of resolution, Krajíček and Pudlák showed that no polynomial bound holds unless RSA can be broken by circuits of polynomial size.

### Consequences

- **Lower bounds from monotone circuits.** Every monotone circuit lower bound for a function that separates the sets of the two sides gives a lower bound on $L$. For the clique-colouring formulas this gives length $2^{\Omega((n / \log n)^{1/3})}$: see [[Monotone interpolation and the clique-colouring formulas|F8GJ402PH2]].
- **An interpolant of linear size.** Every short resolution refutation gives a Craig interpolant of linear size in $L$, in contrast with the general bound of [[Craig's theorem|TRS2HY57EG]].

### Converse

The converse is false.
A small interpolating circuit does not give a short refutation.
Let $A$ be the [[pigeonhole formula|RJ571F7FF0]] $\mathrm{PHP}^{n+1}_n$, with $p$ and $r$ empty and $B$ the empty CNF.
The constant $0$ is an interpolating circuit with one gate.
But every resolution refutation of $A \wedge B$ has $2^{\Omega(n)}$ clauses, by [[Haken's theorem|4PCEYEW3JG]].

### Generalizations

- **Cutting planes.** Pudlák proved a form for the [[cutting-planes system|KKCX2HQP2K]] with monotone real circuits, used in [[Pudlák's lower bound|5RYPXFF0G2]].
- **Craig's theorem.** The theorem is a version of Craig interpolation with a bound on the size of the interpolant in terms of a proof.

## History

Krajíček proved the theorem in a paper published in 1997, which introduced feasible interpolation.
The proof page gives a proof by induction along the refutation, with one circuit for each clause.

## Explanations

### L1 human

Two sets of rules share some switches, and a resolution proof shows that they cannot both be obeyed.
The theorem says that the proof can be turned into a small machine.
The machine reads the shared switches and names a set of rules that cannot be obeyed with those switch values.
The machine has at most four parts for each line of the proof.

### L2 human

The circuit has one node for each clause of the refutation.

1. A clause of $A$ gets the constant $0$, and a clause of $B$ gets the constant $1$.
2. A step on a variable of $q$ gets an OR of the two premises, and a step on a variable of $r$ gets an AND.
3. A step on a variable $x$ of $p$ gets "if $x$ then the node of the premise with $\neg x$, else the node of the premise with $x$".
4. The node of the empty clause is the output.

The typical use is a lower bound: if every interpolating circuit is large, the refutation is long.
A trap is to apply the monotone form when variables of $p$ occur negatively in $A$.

### L3 human

The theorem reduces lower bounds for resolution to lower bounds for circuits, and in the monotone case those lower bounds are known.
It also shows that resolution cannot prove the disjointness of a pair of sets in polynomial size unless a polynomial-size circuit separates them.
The same pattern holds for [[cutting planes|KKCX2HQP2K]], with real circuits in place of Boolean circuits.
For strong systems the pattern fails under cryptographic assumptions, which links interpolation with [[automatizability|WBECDG163W]].
