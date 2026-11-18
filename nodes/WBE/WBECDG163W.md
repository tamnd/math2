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

Let $f$ be a [[propositional proof system|3V24CYWDT6]], and for a tautology $\tau$ let $s_f(\tau)$ be the least size of an $f$-proof of $\tau$.
The system $f$ is *automatizable* if there are an algorithm and a polynomial $t$ such that, for every tautology $\tau$, the algorithm outputs an $f$-proof of $\tau$ within $t(\abs{\tau} + s_f(\tau))$ steps.
For a refutation system, such as [[resolution|6JSH907W5R]], the input is an unsatisfiable CNF $F$, and the output is a refutation of $F$ within $t(\abs{F} + s(F))$ steps.
With other functions $t$ one speaks of automatizability in quasi-polynomial time, $t(m) = 2^{(\log m)^{O(1)}}$, or in subexponential time.
The system $f$ is *weakly automatizable* if some proof system $g$ and some algorithm output $g$-proofs within $t(\abs{\tau} + s_f(\tau))$ steps.

The idea matters because it asks whether the short proofs that a system has can also be found fast.

## Motivation

[[SAT solvers|3BW08M1EX7]] search for refutations: a run of the [[DPLL algorithm|K7R9D390SP]] on an unsatisfiable CNF gives a tree-like resolution refutation.
No algorithm can always find short proofs fast if short proofs do not always exist, so the right comparison is with the shortest proof.
Automatizability asks for proof search that is efficient relative to the best proof, not relative to the formula alone.

## Notation

Wikipedia and some authors write *automatable*.
The size $s(F)$ is the number of clauses for resolution, and the number of symbols in general.
Atserias and Müller measure the time against $r(F) + s(F)$, where $r(F)$ is the number of literal occurrences in $F$.

## Remarks

### Examples

- **Truth tables.** The [[truth-table system|67MYPBSHCJ]] is automatizable, for a trivial reason: see [[The truth-table system is automatizable|FV2E9MH87P]].
- **Bounded width.** [[Bounded-width search for resolution refutations|8SER6179F1]] finds a resolution refutation of width $w$ in time $n^{O(w)}$ for $n$ variables.
- **Tree-like resolution, in quasi-polynomial time.** Beame and Pitassi showed in 1996 that tree-like resolution is automatizable in quasi-polynomial time. With the [[size-width relation|GWDGRPAQSM]], the width search finds a resolution refutation in time $n^{O(w(F) + \log S_T(F \vdash \square))}$.
- **Polynomial calculus, with respect to degree.** A refutation of degree $d$ in [[polynomial calculus|ZERBQSTZB5]] can be found in time $n^{O(d)}$. This is search in terms of degree, not size.

### Non-examples

- **DPLL for general resolution.** [[DPLL does not automate general resolution|7R9XR9ANEC]]: its running time is at least the least tree-like size, which can be exponentially larger than the least size.
- **Resolution, unless P = NP.** By the [[Atserias-Müller theorem|W7FP9TZMVP]], resolution is not automatizable in polynomial time unless [[P = NP|MFN5GYZH5Z]].
- **Strong systems, under cryptographic assumptions.** Extended Frege is not weakly automatizable unless RSA is insecure against circuits of polynomial size (Krajíček and Pudlák, 1998). Results of the same kind hold for TC0-Frege and for bounded-depth Frege under assumptions on the Diffie-Hellman key exchange.
- **Other systems, by NP-hardness.** Automating Nullstellensatz and polynomial calculus is NP-hard (de Rezende, Göös, Nordström, Pitassi, Robere and Sokolov, 2020), and so is automating cutting planes (Göös, Koroth, Mertz and Pitassi, 2020).

### Basic properties

- **With short proofs, automatizability decides unsatisfiability.** If $f$ is [[polynomially bounded|3V24CYWDT6]] and automatizable, then $\mathrm{P} = \mathrm{NP}$. Run the algorithm on $F$ for the time allowed by the size bound, and check the output. The search succeeds exactly when $F$ is unsatisfiable, so the [[coNP|NBSD5FG7NY]]-complete problem of unsatisfiability is in P.
- **Transfer by simulation.** If $g$ is automatizable and $g$ p-simulates $f$, then $f$ is weakly automatizable, with $g$ as the output system.
- **Feasible interpolation.** If $f$ is automatizable and substitution of constants in an $f$-proof gives an $f$-proof that is not larger, then $f$ has [[feasible interpolation|59GJCM8C66]]. So every result against feasible interpolation for such a system is also a result against automatizability.
- **Width.** Search by width gives time $n^{O(w(F) + \sqrt{n \log S(F \vdash \square)})}$ for general resolution, by the [[size-width relation|GWDGRPAQSM]]. This bound is subexponential when the least size is polynomial, but it is not quasi-polynomial.

### History

Krajíček and Pudlák gave the first negative result in 1998, for extended Frege under the RSA assumption.
Alekhnovich and Razborov showed that resolution is not automatizable unless FPT = W[P].
In 2019 Mertz, Pitassi and Wei showed that it is not automatizable in time $n^{(\log \log n)^{0.14}}$, unless the [[exponential time hypothesis|5ZRQC3DG7W]] fails.
Atserias and Müller showed in 2019 that resolution is not automatizable unless P = NP.

### Common errors

- To read "not automatizable" as "has no short proofs". The notion is about finding proofs, and it compares the time with the shortest proof.
- To measure the time against the formula alone. Then no system with superpolynomial lower bounds, such as resolution by [[Haken's theorem|4PCEYEW3JG]], could be automatizable.
- To think that the Atserias-Müller theorem rules out weak automatizability of resolution. That question is open.

## Explanations

### L1 human

A proof system says what counts as a proof.
Some formulas have short proofs, but a short proof may still be hard to find.
A system is automatizable if a computer can always find a proof that is not much longer than the shortest one, in time not much longer than that.

### L2 human

We automate resolution on formulas of small width.

1. List all clauses of width at most $w$ over the $n$ variables. There are at most $(2n + 1)^w$ of them.
2. Start with the clauses of the formula, and add every resolvent of width at most $w$ of two clauses found so far.
3. Stop when the empty clause appears, or when no new clause appears.
4. The time is $n^{O(w)}$, and the empty clause appears exactly when a refutation of width at most $w$ exists.

The typical use is to find refutations of formulas whose least width is small, for example bounded by a constant.
A trap is to think that this automates resolution in general.
Some formulas have refutations of polynomial size whose least width grows like a power of $n$, and for them the bound $n^{O(w)}$ is not polynomial.

### L3 human

Automatizability links proof complexity with algorithms.
Negative results come in three kinds.
Some use cryptographic assumptions, through [[feasible interpolation|59GJCM8C66]].
Some use assumptions from parameterized complexity.
The newest use NP-hardness, as in the [[Atserias-Müller theorem|W7FP9TZMVP]].
The NP-hardness results reduce [[SAT|3QKF32ZAKN]] to the problem of finding short proofs, using formulas that say "this CNF has a refutation of length $s$".
Weak automatizability of resolution is open.
For the wider setting see [[Theory of computation|52TNMMSXD3]].
