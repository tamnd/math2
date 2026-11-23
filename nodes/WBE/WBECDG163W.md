---
tag: WBECDG163W
kind: concept
name: Automatizability
msc: ["03F20", "68Q17", "68V15"]
topics: [CBAF7J051K]
audience: research
uses: [3V24CYWDT6, 6JSH907W5R, GWDGRPAQSM, 3BW08M1EX7, MFN5GYZH5Z]
sources:
  - url: https://en.wikipedia.org/wiki/Proof_complexity
    locator: Automatability
  - url: https://en.wikipedia.org/wiki/Proof_complexity
    locator: Feasible interpolation
---

## Summary

A proof system is automatizable when its short proofs can be found in time close to their length.

Take the four clauses $x \vee y$, $x \vee \neg y$, $\neg x \vee y$ and $\neg x \vee \neg y$.
A program that resolves every pair of clauses and keeps the resolvents with at most $2$ literals finds $x$ and $\neg x$ in its first round and the empty clause in its second.
The [[resolution|6JSH907W5R]] refutation it outputs has $7$ clauses, and the program spent time polynomial in that number.
Automatizability asks for this behavior on every input.

Let $f$ be a [[propositional proof system|3V24CYWDT6]], and for a tautology $\tau$ let $s_f(\tau)$ be the least size of an $f$-proof of $\tau$.
The system $f$ is *automatizable* if there are an algorithm and a polynomial $t$ such that, for every tautology $\tau$, the algorithm outputs an $f$-proof of $\tau$ within $t(\lvert \tau \rvert + s_f(\tau))$ steps.
For a refutation system such as resolution, the input is an unsatisfiable CNF $F$, and the output is a refutation of $F$ within $t(\lvert F \rvert + s(F))$ steps.
With $t(m) = 2^{(\log m)^{O(1)}}$ one speaks of automatizability in quasi-polynomial time, and with $t(m) = 2^{m^{o(1)}}$ of automatizability in subexponential time.
The system $f$ is *weakly automatizable* if, for some proof system $g$, an algorithm outputs $g$-proofs of every tautology $\tau$ within $t(\lvert \tau \rvert + s_f(\tau))$ steps.

## Motivation

[[SAT solvers|3BW08M1EX7]] search for refutations, and a run of the [[DPLL algorithm|K7R9D390SP]] on an unsatisfiable CNF is a tree-like resolution refutation.
No algorithm can find short proofs where none exist, so the fair comparison is with the shortest proof.
Automatizability asks for proof search that is efficient relative to the best proof, and not relative to the formula alone.

## Notation

Wikipedia and some authors write *automatable*.
For resolution the size $s(F)$ is the number of clauses, and in general it is the number of symbols.
Atserias and Müller measure the time against $r(F) + s(F)$, where $r(F)$ is the number of literal occurrences in $F$.

## Remarks

### Systems that are automatizable

The [[truth-table system|67MYPBSHCJ]] is automatizable because its proofs are as long as the search: see [[The truth-table system is automatizable|FV2E9MH87P]].
[[Bounded-width search|8SER6179F1]] finds a resolution refutation of width $w$ in time $n^{O(w)}$ for $n$ variables, up to a factor polynomial in $\lvert F \rvert$.
Beame and Pitassi showed in 1996 that tree-like resolution is automatizable in quasi-polynomial time.
With the [[size-width relation|GWDGRPAQSM]], the width search gives a bound of the same kind, $n^{O(w(F) + \log S_T(F \vdash \square))}$, where $S_T$ is the least tree-like size.
Its output may be dag-like, so it automates tree-like resolution only in the weak sense.
In [[polynomial calculus|ZERBQSTZB5]] a refutation of degree $d$ can be found in time $n^{O(d)}$, which is search in terms of degree and not of size.

### Systems that are not, under assumptions

DPLL does not automate general resolution, by [[DPLL does not automate general resolution|7R9XR9ANEC]]: its running time is at least the least tree-like size, which can be exponentially larger than the least size.
By the [[Atserias-Müller theorem|W7FP9TZMVP]], no algorithm automates resolution in polynomial time unless [[P = NP|MFN5GYZH5Z]].
Krajíček and Pudlák showed in 1998 that extended Frege is not automatizable unless RSA can be broken by circuits of polynomial size.
Results of the same kind hold for TC0-Frege and for bounded-depth Frege under assumptions on the Diffie-Hellman key exchange.
Automating Nullstellensatz and polynomial calculus is NP-hard by work of de Rezende, Göös, Nordström, Pitassi, Robere and Sokolov.
Automating cutting planes is NP-hard by work of Göös, Koroth, Mertz and Pitassi.

### Basic properties

- If $f$ is [[polynomially bounded|3V24CYWDT6]] by a polynomial $q$ and automatizable, then $\mathrm{P} = \mathrm{NP}$.
  Run the algorithm on $F$ for $t(\lvert F \rvert + q(\lvert F \rvert))$ steps and check the output, which succeeds exactly when $F$ is unsatisfiable, so the [[coNP|NBSD5FG7NY]]-complete problem of unsatisfiability is in P.
- If $g$ is automatizable and $g$ p-simulates $f$, then $f$ is weakly automatizable with $g$ as the output system.
  The reason is that $s_g(\tau)$ is at most a polynomial in $s_f(\tau)$.
- If $f$ is automatizable and setting variables to constants in an $f$-proof gives an $f$-proof that is not larger, then $f$ has [[feasible interpolation|59GJCM8C66]].
  So every result against feasible interpolation for such a system is also a result against automatizability.
- Width search gives time $n^{O(w(F) + \sqrt{n \log S(F \vdash \square)})}$ for general resolution, by the second part of the size-width relation.
  The bound is subexponential when $S$ is polynomial and $w(F)$ is small, but it is not quasi-polynomial.

### Watch out

"Not automatizable" does not mean "has no short proofs".
The notion is about finding proofs, and it compares the time with the shortest proof that exists.
If the time were measured against the formula alone, no system with a superpolynomial lower bound could be automatizable, and resolution has one by [[Haken's theorem|4PCEYEW3JG]].
The Atserias-Müller theorem does not rule out weak automatizability of resolution, and that question is open.

### History

Krajíček and Pudlák gave the first negative result in 1998, for extended Frege under the RSA assumption.
Alekhnovich and Razborov then showed that resolution is not automatizable unless W[P] collapses to FPT.
Atserias and Müller proved in 2019 that resolution is not automatizable unless P = NP, with the journal version in 2020.

### Try it

First, for the two clauses $x$ and $\neg x$, how many clauses does the width search output, and with which width bound?
It outputs $3$ clauses, $x$, $\neg x$ and $\square$, already with $w = 1$.

Second, why does an automating algorithm for a polynomially bounded system decide unsatisfiability?
On a satisfiable CNF no refutation exists, so no checked output can appear, while on an unsatisfiable CNF a checked refutation appears within the time bound.

## Explanations

### L1 human

A proof system says what counts as a proof.
Some formulas have short proofs, but a short proof may still be hard to find.
A system is automatizable if a computer can always find a proof not much longer than the shortest one, in time not much longer than that.

### L2 human

We automate resolution on formulas whose refutations are narrow.

1. List all clauses of width at most $w$ over the $n$ variables.
   There are at most $(2n + 1)^w$ of them.
2. Start with the clauses of the formula, and add every resolvent of width at most $w$ of two clauses found so far.
3. Stop when the empty clause appears, or when no new clause appears.
4. The time is $n^{O(w)}$ up to a factor polynomial in the formula.
   The empty clause appears exactly when a refutation of width at most $w$ exists.

The typical use is to find refutations of formulas whose least width is bounded by a constant.
A trap is to think that this automates resolution in general.
Some formulas have refutations of polynomial size whose least width grows like a power of $n$, and for them the bound $n^{O(w)}$ is not polynomial.

### L3 human

Automatizability links proof complexity with algorithms.
Negative results come in three kinds.
Some use cryptographic assumptions, through [[feasible interpolation|59GJCM8C66]].
Some use assumptions from parameterized complexity.
The newest use NP-hardness, as in the [[Atserias-Müller theorem|W7FP9TZMVP]].
These reduce [[SAT|3QKF32ZAKN]] to the problem of finding short proofs, using formulas that say "this CNF has a refutation with $s$ lines".
Weak automatizability of resolution is open.
For the wider setting see [[Theory of computation|52TNMMSXD3]].
