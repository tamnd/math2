---
tag: FCXHSC6Z4R
kind: concept
name: Consequence relation
msc: ["03B22"]
topics: [H8QZY0RZXZ]
audience: grad
uses: [1HK0VYWTV7, 17FVAN6HXX]
sources:
  - url: https://en.wikipedia.org/wiki/Consequence_relation
    locator: lead section
  - url: https://en.wikipedia.org/wiki/Non-monotonic_logic
    locator: lead section
  - url: https://en.wikipedia.org/wiki/Structural_rule
    locator: lead section
---

## Summary

A consequence relation on a set $L$ of formulas is a relation $\Gamma \vdash \varphi$ between sets of formulas and formulas with three properties.
It is reflexive: $\Gamma \vdash \varphi$ when $\varphi \in \Gamma$.
It is monotone: enlarging $\Gamma$ keeps $\Gamma \vdash \varphi$.
It is closed under cut: if $\Gamma$ yields every formula of $\Delta$ and $\Gamma \cup \Delta \vdash \varphi$, then $\Gamma \vdash \varphi$.
The [[definition page|J78Y1M4GND]] gives the details, the variants (finitary, structural, multiple-conclusion) and the proof that consequence relations are the same as [[closure operators|17FVAN6HXX]] on sets of formulas.
The idea matters because it isolates what all notions of "follows from" share, both [[semantic consequence|1HK0VYWTV7]] and derivability in a proof system, so that results about many logics can be proved at once.

## Motivation

Classical logic, intuitionistic logic and modal logics have different formulas, proofs and models.
Each of them still has a relation "$\varphi$ follows from $\Gamma$", and some properties of this relation hold in all of them.
Tarski described consequence by a few general conditions on an operator, and the three conditions above are their core.
With them, a logic can be studied as a set with a consequence relation, without fixing its proof system or its semantics.

## Notation

We write $\Gamma \vdash \varphi$ for the relation and $\mathrm{Cn}(\Gamma) = \set{\varphi : \Gamma \vdash \varphi}$ for the consequence operator.
Semantic relations are usually written $\models$, and the conditions are often named (R), (M), (C) or identity, weakening, cut.

## Remarks

### Examples

- [[Classical propositional consequence|5X683DYC8S]] $\Gamma \models \varphi$: every valuation that makes $\Gamma$ true makes $\varphi$ true.
- [[Derivability in a Hilbert system|1H0WHK62VP]]: $\Gamma \vdash \varphi$ when some derivation from hypotheses in $\Gamma$ ends in $\varphi$.
- Intuitionistic consequence, defined by Kripke models: every world of every Kripke model that forces all of $\Gamma$ forces $\varphi$.
- First-order consequence between sets of sentences, with structures as models.
- The relation with $\Gamma \vdash \varphi$ when $\varphi \in \Gamma$ or $\varphi = p$, for a fixed variable $p$. It is a consequence relation, but it is not structural.

### Non-examples

- The [[closed-world assumption|W4QZGRCDPA]] fails monotonicity: from no information it concludes $\neg p$, but from $p$ it does not.
- "Most likely" inference fails monotonicity: a fair die most likely shows at least $3$, but if we learn that it shows at most $4$, the probability falls to $1/2$.
- One-step consequence fails cut. Let $\Gamma \vdash_1 \varphi$ when $\varphi \in \Gamma$ or $\varphi$ follows from two members of $\Gamma$ by one use of modus ponens. Then $\set{p, p \to q, q \to r} \vdash_1 q$ and $\set{p, p \to q, q \to r, q} \vdash_1 r$, but $\set{p, p \to q, q \to r} \nvdash_1 r$.

### Basic properties

- Consequence relations on $L$ correspond one to one to closure operators on the subsets of $L$; the proof is on the [[definition page|J78Y1M4GND]].
- The deductively closed theories form a complete lattice, and they determine the relation.
- Every consequence relation is the semantic consequence of some class of models, for example of its own closed theories.
- If a relation is finitary, then cut follows from its one-formula case "if $\Gamma \vdash \psi$ and $\Gamma, \psi \vdash \varphi$, then $\Gamma \vdash \varphi$".

### History

Alfred Tarski introduced consequence operations in his work on the methodology of deductive sciences around 1930.
Gerhard Gentzen's sequent calculus of 1934 and 1935 made reflexivity, weakening and cut explicit as structural rules.
Dana Scott studied consequence relations with multiple conclusions.
The book *Multiple-Conclusion Logic* by Shoesmith and Smiley, on the same subject, appeared in 1978.

### Common errors

- Confusing $\Gamma \vdash \varphi$ with the formula $\bigwedge \Gamma \to \varphi$. They agree for finite $\Gamma$ in classical logic, but the relation is a statement of the metalanguage, and in some logics there is no matching connective.
- Assuming that every consequence relation is finitary. Consequence in a logic with the $\omega$-rule, or in second-order logic, is not finitary.
- Calling a default or probabilistic inference a consequence relation without checking monotonicity.

## Explanations

### L1 human

"Follows from" can mean "true in every situation where the assumptions are true" or "can be proved from the assumptions".
Both meanings share three rules.
An assumption follows from itself.
More assumptions never remove a conclusion.
Conclusions can be used as new assumptions without changing what follows.
For example, from "it is Tuesday" follows "it is a weekday", and both together give "the shop is open" if the shop opens on weekdays, so "it is Tuesday" alone gives "the shop is open".

### L2 human

We check monotonicity and cut for semantic consequence over a class $K$ of models.

1. $\Gamma \models_K \varphi$ means: every model in $K$ that satisfies all of $\Gamma$ satisfies $\varphi$.
2. If $\Gamma \subseteq \Delta$, every model of $\Delta$ is a model of $\Gamma$, so $\Gamma \models_K \varphi$ gives $\Delta \models_K \varphi$.
3. For cut, let $\Gamma \models_K \psi$ for all $\psi \in \Delta$ and $\Gamma \cup \Delta \models_K \varphi$.
4. A model of $\Gamma$ satisfies each $\psi \in \Delta$ by the first assumption, so it is a model of $\Gamma \cup \Delta$.
5. By the second assumption, it satisfies $\varphi$. So $\Gamma \models_K \varphi$.

The typical use is to check that a new logic, given by models, has a well-behaved consequence relation.
A trap is to restrict the models after the fact: "satisfies $\varphi$ in the preferred models of $\Gamma$" depends on $\Gamma$ and usually fails monotonicity.

### L3 human

The theorem that consequence relations are closure operators puts logic inside lattice theory: the theories of a logic form an algebraic closure system when the relation is finitary.
Abstract algebraic logic studies structural consequence relations and their algebraic semantics, and [[abstract logical systems|RQXV7PM2WT]] add semantics, signatures and translations, as in institutions.
Proof theory refines the notion by keeping track of the structure of the premises, which leads to substructural logics and to the sequent calculus.
