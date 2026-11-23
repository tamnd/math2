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

1. [[Modal logic|C3RZY20ETK]]: what the box and the diamond say, and how formulas are built from them.
2. [[Kripke semantics|NGHWZ9Y7ZV]]: how to evaluate a formula at a world, and the gap between truth in a model and validity on a frame.
3. [[Accessibility relation|XBCYFDPS2F]]: the relation that decides what is possible, and the properties it can have.
4. [[Normal modal logic|D1TJYZZDCY]]: the weakest set of laws that a relational semantics forces, and the first derivations in $\mathsf{K}$.
5. [[Necessitation rule|G989VP2NGP]]: why the box of a theorem is a theorem, and why $\varphi \to \square\varphi$ is not.
6. [[Common modal axiom schemata|FDFQFWPM4X]]: how to check by hand which frames validate $\mathrm{T}$, $\mathrm{D}$, $\mathrm{B}$, $\mathrm{4}$ and $\mathrm{5}$.
7. [[Modal logics T, D and K4|XVYMEZKH7R]]: the logics of reflexive, serial and transitive frames, and how they differ.
8. [[Modal logic S4|N60RVXSA5W]]: preorders, the reading of the box as an interior, and the link to intuitionistic logic.
9. [[Modal logic S5|VC3A2VWXND]]: why equivalence relations and universal frames give the same logic, and why iterated modalities collapse.
10. [[Brouwerian modal logic|2QPT4KCM0Q]]: the logic $\mathsf{KTB}$ of reflexive symmetric frames, and where its name comes from.
11. [[Strict implication|5JW54NP52K]]: how the subject began with Lewis, and his systems $\mathsf{S1}$ to $\mathsf{S5}$.
12. [[Canonical model|TVE4F04KME]]: the model of maximal consistent sets, [[the truth lemma|NM4CB7QAYT]], and [[completeness of K to S5|FXTCKYR3AQ]].
13. [[Filtration|6ZZSHAKG5F]]: how to shrink a model to finitely many worlds without changing the truth of chosen formulas, by [[the filtration theorem|T99DK51S0W]].
14. [[Finite model property|3NT8RCA6HE]]: [[the finite model property of K to S5|XNPJK6B921]], and how [[Harrop's theorem|VSYQ1AZ9G7]] turns it into decidability.
15. [[Standard translation|YW6YGBMVQY]]: how to read a modal formula as a first-order formula, with [[its correctness|1HQ1W36J4V]].
16. [[Complexity of modal satisfiability|1P2B0C7CQ4]]: why $\mathsf{K}$, $\mathsf{T}$ and $\mathsf{S4}$ are PSPACE-complete while $\mathsf{S5}$ is NP-complete.
17. [[Neighborhood semantics|CN7HK9K1B6]]: a semantics with sets of sets, which also covers the logics $\mathsf{E}$, $\mathsf{M}$, $\mathsf{C}$ and $\mathsf{N}$ below $\mathsf{K}$.
18. [[Multimodal logic|ERG3KAQWYF]]: several boxes at once, fusions, and axioms that link the boxes.

### Prerequisites

1. [[The propositional calculus|JDK63589SA]]: [[propositional calculus|09K9MWD2QQ]], tautologies and Hilbert systems.
2. [[Structures, satisfaction and truth|NJDME6F845]]: first-order structures and the satisfaction relation, used by the standard translation.
