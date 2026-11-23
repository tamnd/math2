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

A consequence relation captures "follows from" in the abstract.
It keeps only the three rules that both truth in models and proof in a formal system obey, so that facts about many logics can be proved at once.

Start with one argument.
From $p$ and $p \to q$ we may conclude $q$, by every truth table and by modus ponens.
Add a third premise $r$, and $q$ still follows: extra premises never hurt.
If we also know that $q \to s$ follows from our premises, we may use it as a lemma, and $s$ then follows from the original premises alone.

A consequence relation on a set $L$ of formulas is a relation $\Gamma \vdash \varphi$ between sets of formulas and formulas that has exactly these three properties.
It is reflexive: $\Gamma \vdash \varphi$ when $\varphi \in \Gamma$.
It is monotone: if $\Gamma \vdash \varphi$ and $\Gamma \subseteq \Delta$, then $\Delta \vdash \varphi$.
It is closed under cut: if $\Gamma \vdash \psi$ for every $\psi \in \Delta$ and $\Gamma \cup \Delta \vdash \varphi$, then $\Gamma \vdash \varphi$.
The [[definition|J78Y1M4GND]] states the conditions in full, with the variants and the proof that consequence relations are the same as [[closure operators|17FVAN6HXX]].

## Motivation

Classical logic, intuitionistic logic and modal logics have different formulas, different proofs and different models.
Each still has a relation "$\varphi$ follows from $\Gamma$", and some properties of this relation hold in all of them.
Around 1930 Tarski described consequence by a few general conditions on an operator, and the three conditions above are their core.
With them, we can study a logic as a set with a consequence relation, without fixing its proof system or its semantics.

The notion joins the two halves of logic.
[[Semantic consequence|1HK0VYWTV7]], defined by models, and derivability in a [[formal system|439M8B4DY2]], defined by rules, are both consequence relations.
Soundness and completeness then become comparisons between two relations on the same set: ${\vdash} \subseteq {\models}$, and the reverse inclusion.
This comparison is the theme of [[soundness|4A84VHDTHV]] and returns in [[Gödel's completeness theorem|WQ1ZE255SF]].

## Notation

We write $\Gamma \vdash \varphi$ for the relation, and $\mathrm{Cn}(\Gamma) = \{ \varphi : \Gamma \vdash \varphi \}$ for its consequence operator.
Relations given by a semantics are usually written $\models$.
The three conditions are often named (R), (M) and (C), or identity, weakening and cut, after the structural rules of the sequent calculus.
A theory is any set of formulas, and it is deductively closed when $\mathrm{Cn}(T) = T$.

## Remarks

### Relations that pass the test

[[Classical propositional consequence|5X683DYC8S]] is the first example: $\Gamma \models \varphi$ when every valuation that makes all of $\Gamma$ true makes $\varphi$ true.
For example $p, p \to q \models q$, since the only row with both premises true has $q$ true.
[[Derivability in a Hilbert system|1H0WHK62VP]] is the second: $\Gamma \vdash \varphi$ when some derivation from hypotheses in $\Gamma$ ends in $\varphi$.
Cut holds there because we can paste a derivation of each lemma into the main derivation.
Intuitionistic consequence, defined by Kripke models, and first-order consequence between sets of sentences, defined by structures, are consequence relations by the same argument as the classical one.

A stranger example shows that the conditions do not force good behavior under renaming.
Fix a variable $p$, and let $\Gamma \vdash \varphi$ hold when $\varphi \in \Gamma$ or $\varphi = p$.
All three conditions hold, so this is a consequence relation.
Yet $\vdash p$ while $\nvdash q$, so the relation is not structural: substituting $q$ for $p$ does not keep consequence.

### Relations that fail

The [[closed-world assumption|W4QZGRCDPA]] concludes $\neg p$ from no information, because $p$ is not stored.
From the premise $p$ it no longer concludes $\neg p$, so monotonicity fails.

"Most likely" inference fails monotonicity too.
A fair die most likely shows at least $3$, since
$$P(\text{at least } 3) = \tfrac{4}{6} = \tfrac{2}{3} > \tfrac12.$$
Given that the die shows at most $4$, the probability drops to $\tfrac{2}{4} = \tfrac12$, so the conclusion is lost.

One-step consequence fails cut.
Let $\Gamma \vdash_1 \varphi$ when $\varphi \in \Gamma$ or $\varphi$ follows from two members of $\Gamma$ by one use of modus ponens.
Then $p, p \to q, q \to r \vdash_1 q$ and $p, p \to q, q \to r, q \vdash_1 r$, but $p, p \to q, q \to r \nvdash_1 r$.

### The first properties

Consequence relations on $L$ correspond one to one to closure operators on the subsets of $L$, and the [[definition|J78Y1M4GND]] proves it.
So the deductively closed theories form a complete lattice, and they determine the relation: $\Gamma \vdash \varphi$ exactly when $\varphi$ lies in every closed theory that contains $\Gamma$.
Every consequence relation is the semantic consequence of some class of models, for example of its own closed theories.
For a finitary relation, cut follows from its one-formula case: if $\Gamma \vdash \psi$ and $\Gamma, \psi \vdash \varphi$, then $\Gamma \vdash \varphi$.

### Watch out

Do not confuse $\Gamma \vdash \varphi$ with the formula $\bigwedge \Gamma \to \varphi$.
For finite $\Gamma$ in classical logic they match, through the deduction theorem.
But the relation is a statement of the metalanguage, $\Gamma$ may be infinite, and some logics have no connective that matches it.

Do not assume that every consequence relation is finitary.
Second-order consequence with full semantics is not: the set that says "there are at least $n$ elements" for each $n$, together with a second-order sentence saying "the domain is finite", has no model, but each finite part has one.
So that set has $\bot$ as a consequence, while no finite part does.

### History

Alfred Tarski introduced consequence operations in his work on the methodology of the deductive sciences around 1930.
Gerhard Gentzen's sequent calculus of 1934 and 1935 made reflexivity, weakening and cut explicit as structural rules.
Dana Scott studied consequence relations with multiple conclusions, and the book *Multiple-Conclusion Logic* by Shoesmith and Smiley appeared in 1978.

### Try it

Is the relation "$\Gamma \vdash \varphi$ when $\varphi \in \Gamma$" a consequence relation?
Yes: (R) is its definition, (M) holds because a larger set still contains $\varphi$, and for (C), $\varphi \in \Gamma \cup \Delta$ with $\Delta \subseteq \Gamma$ gives $\varphi \in \Gamma$.

Does "$\Gamma \vdash \varphi$ when $\Gamma$ has at most $5$ members and $\Gamma \models \varphi$" satisfy monotonicity?
No: $p \vdash p$, but the set $\{ p, q_1, \dots, q_5 \}$ has $6$ members, so it does not yield $p$.

## Explanations

### L1 human

"Follows from" can mean "true in every situation where the assumptions are true", or "can be proved from the assumptions".
Both meanings share three rules.
An assumption follows from itself.
More assumptions never remove a conclusion.
Conclusions can be used as new assumptions without changing what follows.
For example, "it is a weekday" follows from "it is Tuesday", and "the shop is open" follows from both if the shop opens on weekdays, so "it is Tuesday" alone gives "the shop is open".

### L2 human

We check monotonicity and cut for semantic consequence over any class $K$ of models.
Write $\Gamma \models_K \varphi$ when every model in $K$ that satisfies all of $\Gamma$ satisfies $\varphi$.

1. If $\Gamma \subseteq \Delta$, every model of $\Delta$ is a model of $\Gamma$, so $\Gamma \models_K \varphi$ gives $\Delta \models_K \varphi$.
2. For cut, let $\Gamma \models_K \psi$ for all $\psi \in \Delta$, and let $\Gamma \cup \Delta \models_K \varphi$.
3. A model of $\Gamma$ satisfies each $\psi \in \Delta$ by the first assumption, so it is a model of $\Gamma \cup \Delta$.
4. By the second assumption it satisfies $\varphi$, so $\Gamma \models_K \varphi$.

The typical use is to check that a new logic, given by models, has a well-behaved consequence relation.
Watch out for one move: "true in the preferred models of $\Gamma$" depends on $\Gamma$ itself, and such relations usually fail monotonicity.

### L3 human

Since consequence relations are closure operators, the theories of a logic form a closure system, and logic meets lattice theory.
Abstract algebraic logic studies structural consequence relations and their classes of algebras, as in [[algebraic logic|QYA4H5Y7VR]].
Proof theory refines the notion by keeping track of how premises are used, which leads to the sequent calculus and to [[substructural logics|98QF5J4W16]].
[[Abstract logical systems|RQXV7PM2WT]] pair a consequence relation with a semantics, and institutions give each signature its own consequence relation.
