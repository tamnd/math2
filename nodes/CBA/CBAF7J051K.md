---
tag: CBAF7J051K
kind: topic
name: Propositional proof complexity
msc: ["03F20"]
topics: [DYJ0KGTPMR]
---

## Summary

Propositional proof complexity is the part of [[mathematical logic|DYJ0KGTPMR]] that asks how long a proof of a tautology must be.
Every tautology has a proof, since a truth table is one, so the question is about size, and the answer depends on the proof system.
The subject starts with Cook and Reckhow in 1979, who defined a proof system as a polynomial-time checker and showed that a system with short proofs of every tautology exists exactly when $\mathrm{NP} = \mathrm{coNP}$.
That turns the question $\mathrm{NP} \ne \mathrm{coNP}$ into a program: prove superpolynomial lower bounds for stronger and stronger systems.
The program has succeeded for resolution, with Haken's bound on the pigeonhole formulas and the width method.
It has also succeeded for bounded-depth Frege, with Ajtai's theorem, and for cutting planes and the algebraic systems.
It stops at Frege systems, the ordinary systems of logic textbooks, where no superpolynomial lower bound is known.
Along the way the subject meets circuit complexity, through feasible interpolation, and the practice of SAT solving, through the question of how hard it is to find a short proof.

## Remarks

### Reading order: proof systems and Frege

1. [[Proof complexity|1Q046J0AW2]]: the measures of size, length and width, and the hierarchy of systems that the rest of the topic fills in.
2. [[Propositional proof system|3V24CYWDT6]]: the exact definition of a proof system, and the notion of p-simulation used to compare two systems.
3. [[Cook-Reckhow theorem|YS1T29B00B]]: why short proofs for every tautology are the same as $\mathrm{NP} = \mathrm{coNP}$.
4. [[Frege system|J2BAR09TPF]]: the textbook systems as proof systems, and Reckhow's theorem that the choice of rules does not matter.
5. [[Extended Frege system|5YSE04SHFH]]: how naming subformulas by new variables can shorten proofs, and its link to polynomial-time reasoning.
6. [[Lower bounds for Frege systems|ANSV13M4FS]]: the central open problem, and why the methods that work for weaker systems fail here.

### Reading order: weaker systems and their lower bounds

7. [[Resolution as a proof system|6JSH907W5R]]: the system behind SAT solvers, with tree-like, regular and general refutations.
8. [[Haken's theorem|4PCEYEW3JG]]: the first exponential lower bound for resolution, and the method of restrictions behind it.
9. [[Size-width relation for resolution|GWDGRPAQSM]]: the Ben-Sasson and Wigderson method, which reduces lower bounds on size to lower bounds on width.
10. [[Tseitin formulas|JXTCC6KXNG]]: parity on a graph, the cleanest hard example for resolution when the graph is an expander.
11. [[Pigeonhole formulas|RJ571F7FF0]]: the main test case, with the status of each proof system on it.
12. [[Bounded-depth Frege|41QJ1WEMJ3]]: Frege with lines of constant depth, and Ajtai's superpolynomial lower bound for it.
13. [[Cutting planes|KKCX2HQP2K]]: proofs with linear inequalities and rounding, and Pudlák's lower bound by monotone real circuits.
14. [[Algebraic proof systems|ZERBQSTZB5]]: Nullstellensatz and polynomial calculus, where the measure is the degree of the polynomials.
15. [[Feasible interpolation|59GJCM8C66]]: how a short proof yields a small circuit, so that circuit lower bounds become proof lower bounds.
16. [[Automatizability|WBECDG163W]]: whether short proofs can be found fast, up to the theorem of Atserias and Müller for resolution.

### Prerequisites

- [[The propositional calculus|JDK63589SA]]: formulas, tautologies, Hilbert systems and resolution.
- [[Theory of computation|52TNMMSXD3]]: polynomial time, NP, coNP and Boolean circuits.
- [[Bounded arithmetic|RA380RWEC0]]: the theories that correspond to the proof systems, for the remarks on logic.
