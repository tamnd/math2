---
tag: SKY7AQFG1V
kind: topic
name: Syntax, Kripke semantics and completeness of modal logic
msc: ["03B45"]
topics: [DYJ0KGTPMR]
---

## Summary

This topic is a part of [[mathematical logic|DYJ0KGTPMR]], and it tells one story about propositional modal logic.
It starts with a language that adds a box $\square$ and a diamond $\lozenge$ to classical logic, and with Kripke models, where $\square p$ is true at a world when $p$ is true at every world it sees.
Axioms about the box then match properties of the seeing relation, so that $\square p \to p$ matches reflexivity and $\square p \to \square\square p$ matches transitivity.
Next come the normal logics from $\mathsf{K}$ to $\mathsf{S5}$, and a proof that each one is complete, using a single model built from maximal consistent sets.
Filtration then cuts any model down to at most $2^n$ worlds for a formula with $n$ subformulas, which gives decidability.
The story ends with complexity, the first-order view of modal formulas, and two variants of the semantics.
Bisimulation, correspondence theory and incompleteness continue it in [[modal model theory|SPQVNPZDTB]].
Logics of knowledge, time and obligation are in [[applied modal logics|CQM9SRN8PM]], and the logic of provability is in [[provability logics|3E7M66WW6Q]].

## Remarks

### Reading order

1. [[Modal logic|C3RZY20ETK]]: what the box and the diamond say, and how formulas are built.
2. [[Kripke semantics|NGHWZ9Y7ZV]]: truth at a world, and truth in a model versus validity on a frame.
3. [[Accessibility relation|XBCYFDPS2F]]: the relation that decides what is possible.
4. [[Normal modal logic|D1TJYZZDCY]]: the laws every frame forces, and first derivations in $\mathsf{K}$.
5. [[Necessitation rule|G989VP2NGP]]: why a theorem is necessary, and why $\varphi \to \square\varphi$ is not a law.
6. [[Common modal axiom schemata|FDFQFWPM4X]]: which frames validate $\mathrm{T}$, $\mathrm{D}$, $\mathrm{B}$, $\mathrm{4}$ and $\mathrm{5}$.
7. [[Modal logics T, D and K4|XVYMEZKH7R]]: reflexive, serial and transitive frames.
8. [[Modal logic S4|N60RVXSA5W]]: preorders, the box as an interior, and intuitionistic logic.
9. [[Modal logic S5|VC3A2VWXND]]: equivalence relations, universal frames, and collapsing modalities.
10. [[Brouwerian modal logic|2QPT4KCM0Q]]: reflexive symmetric frames.
11. [[Strict implication|5JW54NP52K]]: how Lewis began the subject with $\mathsf{S1}$ to $\mathsf{S5}$.
12. [[Canonical model|TVE4F04KME]]: maximal consistent sets, [[the truth lemma|NM4CB7QAYT]] and [[completeness|FXTCKYR3AQ]].
13. [[Filtration|6ZZSHAKG5F]]: shrinking a model to finitely many worlds, by [[the filtration theorem|T99DK51S0W]].
14. [[Finite model property|3NT8RCA6HE]]: [[the FMP of K to S5|XNPJK6B921]], and decidability by [[Harrop's theorem|VSYQ1AZ9G7]].
15. [[Standard translation|YW6YGBMVQY]]: modal formulas as first-order formulas, and [[its correctness|1HQ1W36J4V]].
16. [[Complexity of modal satisfiability|1P2B0C7CQ4]]: PSPACE for $\mathsf{K}$, $\mathsf{T}$ and $\mathsf{S4}$, and NP for $\mathsf{S5}$.
17. [[Neighborhood semantics|CN7HK9K1B6]]: sets of sets as semantics, for logics below $\mathsf{K}$.
18. [[Multimodal logic|ERG3KAQWYF]]: several boxes, fusions, and axioms that link them.

### Prerequisites

1. [[The propositional calculus|JDK63589SA]]: [[propositional calculus|09K9MWD2QQ]], tautologies and Hilbert systems.
2. [[Structures, satisfaction and truth|NJDME6F845]]: first-order structures and the satisfaction relation, used by the standard translation.
