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

A resolution refutation with $L$ clauses of two CNFs that share variables $p$ gives a circuit with at most $4L$ gates that names, for each value of $p$, a CNF that fails.

Let $p$, $q$ and $r$ be disjoint lists of variables.
Let $A(p, q)$ be a CNF whose variables are among $p, q$, and $B(p, r)$ a CNF whose variables are among $p, r$.
For a $0$-$1$ assignment $a$ of $p$, write $A(a, q)$ and $B(a, r)$ for the results of substituting $a$ for $p$.
Let $\pi$ be a [[resolution refutation|6JSH907W5R]] of $A \wedge B$ with $L$ clauses.

**Theorem (Krajíček).**

1. There is a [[Boolean circuit|SQXNFGVADX]] $I(p)$ with AND, OR and NOT gates and at most $4L$ gates such that, for every $0$-$1$ assignment $a$ of $p$, $I(a) = 0$ implies that $A(a, q)$ is unsatisfiable, and $I(a) = 1$ implies that $B(a, r)$ is unsatisfiable.
2. If no variable of $p$ occurs negatively in $A$, then there is such a circuit with AND and OR gates only, and at most $4L$ gates.
3. In both cases the circuit can be computed from $\pi$ in time polynomial in the size of $\pi$.

So resolution has [[feasible interpolation|59GJCM8C66]] and monotone feasible interpolation.
The measure of the refutation is its number $L$ of clauses, and the measure of the circuit is its number of gates.

## Remarks

### A small case

For $A = \{q, \ \neg q \vee p\}$ and $B = \{\neg p \vee r, \ \neg r\}$, the refutation that derives $p$, then $\neg p$, then the empty clause has $L = 7$ clauses.
The construction labels the clauses of $A$ with $0$, the clauses of $B$ with $1$, takes OR at the pivot $q$ and AND at the pivot $r$.
At the pivot $p$ it outputs $(p \wedge 1) \vee (\neg p \wedge 0) = p$.
[[An interpolant from a refutation of seven clauses|KH4T0G84TD]] checks every step, and the circuit $p$ is far below the bound $4L = 28$.

### Why each hypothesis is needed

The private variables must be disjoint.
Let $y$ occur in both $A = \{y\}$ and $B = \{\neg y\}$, with $p$ empty, so a refutation has $3$ clauses.
A circuit with no inputs is a constant, the constant $0$ would claim that $A$ fails, the constant $1$ that $B$ fails, and both claims are false.

Part 2 needs the sign condition.
Let $A = \{\neg p\}$ and $B = \{p\}$, so that $p$ occurs negatively in $A$.
At $a = 1$ the set $B$ holds, so $I(1) = 0$, and at $a = 0$ the set $A$ holds, so $I(0) = 1$.
So $I = \neg p$, and no monotone circuit computes it.

The proof system matters.
For [[extended Frege|5YSE04SHFH]], Krajíček and Pudlák showed in 1998 that no polynomial bound of this kind holds if RSA is secure against circuits of polynomial size.

### What it gives you

Every monotone circuit lower bound for a function that separates the two sides gives a lower bound on $L$.
For the clique-coloring formulas this gives $2^{\Omega((n / \log n)^{1/3})}$ clauses: see [[monotone interpolation and the clique-coloring formulas|F8GJ402PH2]].
The theorem also gives, from every resolution refutation, a Craig interpolant computed by a circuit of size linear in $L$.
The general proof of [[Craig's theorem|TRS2HY57EG]] gives no such bound.

### The converse is false

A small interpolating circuit does not give a short refutation.
Let $A$ be the [[pigeonhole formula|RJ571F7FF0]] $\mathrm{PHP}^{n+1}_n$, with $p$ and $r$ empty and $B$ the empty CNF.
The constant $0$ is an interpolating circuit, since $A$ is unsatisfiable.
But every resolution refutation of $A$ has $2^{\Omega(n)}$ clauses, by [[Haken's theorem|4PCEYEW3JG]].

### Generalizations

Pudlák proved a form for [[cutting planes|KKCX2HQP2K]] with monotone real circuits, and used it for [[his lower bound|5RYPXFF0G2]].
The theorem is a version of Craig interpolation with the size of the interpolant bounded by the size of a refutation.

## History

Krajíček proved the theorem in a paper published in 1997 in the Journal of Symbolic Logic, which introduced feasible interpolation.

## Explanations

### L1 human

Two sets of rules share some switches, and a resolution proof shows that they cannot both be obeyed.
The theorem says that the proof can be turned into a small machine.
The machine reads the shared switches and names a set of rules that cannot be obeyed with those switch values.
The machine has at most four parts for each line of the proof.

### L2 human

The circuit has one node for each clause of the refutation, built from the premises.
A clause of $A$ gets the constant $0$, and a clause of $B$ gets the constant $1$.
A step on a variable of $q$ gets an OR of its two premises, and a step on a variable of $r$ gets an AND.
A step on a variable $x$ of $p$ gets the node of the premise with $\neg x$ when $x = 1$, and the node of the premise with $x$ when $x = 0$.
The node of the empty clause is the output.
The typical use is a lower bound: if every interpolating circuit is large, the refutation is long.
Watch out: the monotone form needs that no variable of $p$ occurs negatively in $A$.

### L3 human

The theorem reduces lower bounds for resolution to lower bounds for circuits, and in the monotone case those circuit bounds are known.
It also shows that resolution cannot prove in polynomial size that two NP sets are disjoint, unless a circuit of polynomial size separates them.
The same pattern holds for cutting planes, with real circuits in place of Boolean circuits.
For strong systems the pattern fails under cryptographic assumptions, which links interpolation with [[automatizability|WBECDG163W]].
