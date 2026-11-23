---
tag: VM8TQ70CVJ
kind: concept
name: Consistency
aliases: [absolute-consistency, consistancy, consistencies, consistency-mathematical-logic, consistency-proof, consistent, consistent-set, consistent-theory, henkins-theorem, inconsistancy, inconsistency, inconsistency-principle, inconsistent, inconsistent-theory, incosistent, internal-logic, logical-consistency, logically-consistent, relative-consistency, self-consistent]
msc: ["03B10", "03B05", "03F25"]
topics: [H8QZY0RZXZ]
audience: ug2
uses: [92SWXST1ZM, DKFGQTRYZE, 1HK0VYWTV7, QN7M1JCGT9, MVCH6N9SNW]
sources:
  - wikipedia: en:75802@r1369696261
    locator: Consistency
    note: adopted
    mention: wikipedia://en/75802
    sections: [Summary]
  - url: https://en.wikipedia.org/wiki/Consistency
    locator: lead section
  - book: isbn:9780122384523
  - book: isbn:9781482237726
same_as:
  wikidata: Q1319773
  wikipedia: Consistency
inventory: [SYA32FTV69]
---

## Summary

A set of axioms is consistent when no derivation from it reaches a contradiction.
Take the three propositional formulas $p$, $p \to q$ and $\lnot q$.
Modus ponens on the first two derives $q$, and the third is $\lnot q$, so these axioms derive a formula and its negation.
They are [[inconsistent|HYMTN6457G]].
Replace $\lnot q$ by $\lnot r$, and no derivation reaches a contradiction any more.
The reason is that the valuation with $p$ and $q$ true and $r$ false makes all three axioms true, and sound rules preserve truth.

Fix a logic with a notion of derivation, such as a [[Hilbert system|1MGMQX43B8]] for first-order logic.
Write $T \vdash \varphi$ when the formula $\varphi$ is derivable from the set $T$.
A set $T$ of [[sentences|DKFGQTRYZE]] is *consistent* when there is no formula $\varphi$ with both $T \vdash \varphi$ and $T \vdash \lnot\varphi$.
It is *inconsistent* when such a formula exists.

This is a syntactic notion: it speaks only of derivations.
The semantic notion is [[satisfiability|QN7M1JCGT9]]: $T$ is satisfiable when it has a [[model|MVCH6N9SNW]], a structure in which every sentence of $T$ is true.
The two notions have different definitions.
For first-order logic they agree, by soundness in one direction and by [[Gödel's completeness theorem|WQ1ZE255SF]] in the other.
Consistency matters because in classical logic an inconsistent set derives every sentence, so its theorems carry no information.

## Motivation

A [[theory|92SWXST1ZM]] is useful only if some sentence fails to be a theorem.
Frege's system of the *Grundgesetze* derived a contradiction, [[Russell's paradox|0HESMMSYEG]], and with it every sentence.
After such failures, mathematicians asked for a guarantee that the axioms of arithmetic, analysis and set theory cannot lead to a contradiction.

There are two ways to give such a guarantee.
One can exhibit a model, which is a semantic argument.
One can study the derivations themselves and show that none of them ends in a contradiction, which is a syntactic argument.
The two ways answer two different questions.
The completeness theorem shows that, for first-order logic, the answers agree.

## Notation

A theory is any set of sentences, its axioms.
It is deductively closed when it equals its deductive closure $\{ \varphi : T \vdash \varphi \}$.
A theory and its deductive closure are consistent together, because they derive the same formulas.
We write $T \vdash \varphi$ for derivability and $T \models \varphi$ for [[logical consequence|1HK0VYWTV7]].

Many books write $\mathrm{Con}(T)$ for the statement "$T$ is consistent".
The same symbol also names the arithmetical sentence that expresses it through a [[Gödel numbering|MFJXPAF0R0]].
Some books write $T \vdash \bot$ for "$T$ is inconsistent", when the language has the constant $\bot$ for falsity.
Older books say "simply consistent" or "negation consistent" for this notion, to separate it from [[absolute consistency|WK2P0E82B4]].

## Remarks

### Equivalent forms

Call a logic explosive when $\lnot\varphi \to (\varphi \to \psi)$ is derivable for all formulas $\varphi$ and $\psi$, and modus ponens is a rule.
Classical and [[intuitionistic logic|Q11N8X99FK]] are explosive.
In an explosive logic the following statements about a theory $T$ are equivalent.

1. $T$ is consistent: no formula $\varphi$ has $T \vdash \varphi$ and $T \vdash \lnot\varphi$.
2. Some formula is not derivable from $T$.
3. $T \nvdash \varphi \land \lnot\varphi$ for one formula $\varphi$, and then for every formula $\varphi$.
4. $T \nvdash \bot$, when the language has $\bot$.

From 1 to 2: if every formula were derivable, then $\varphi$ and $\lnot\varphi$ would both be derivable for any $\varphi$.
From 2 to 1: if $T \vdash \varphi$ and $T \vdash \lnot\varphi$, then two uses of [[modus ponens|0Y0MQYST0M]] on $\lnot\varphi \to (\varphi \to \psi)$ give $T \vdash \psi$ for every $\psi$.
This step is the principle of [[explosion|TTKZGJEEK7]].
Form 3 matches form 1, because $T \vdash \varphi \land \lnot\varphi$ holds exactly when $T \vdash \varphi$ and $T \vdash \lnot\varphi$.
Form 4 matches form 2, because $\bot \to \psi$ is derivable for every $\psi$, and $\bot$ is itself a formula.

In a [[paraconsistent logic|C7YWCR87QJ]] explosion fails, and form 1 and form 2 come apart.
A theory can then contain $p$ and $\lnot p$ and still not derive $q$.
Form 2 is the more useful notion there, and it is called [[Post consistency|WK2P0E82B4]] or absolute consistency.

### Showing consistency with a model

The usual way to show consistency is to find a model and apply [[soundness|4A84VHDTHV]].
If $M$ is a model of $T$ and $T \vdash \varphi$, then $\varphi$ is true in $M$, so $\varphi$ and $\lnot\varphi$ cannot both be derivable.

The set $\{ p \lor q, \; p \to r, \; \lnot q \}$ is consistent, because the [[valuation that makes p and r true and q false|WTRZG7SQM2]] satisfies it.
The group axioms together with $\exists x \, \exists y \, (x y \neq y x)$ form a consistent theory, because the [[symmetric group on three letters is a model|WATWZWV11Q]].
The empty theory is consistent, because every structure is a model of it.
The three axioms of [[a four-point geometry|MJ5S28Y5WV]] are consistent, because the six edges of a complete graph on four vertices form a model.

[[Peano arithmetic|0QFT7Z76N5]] is consistent, because the natural numbers with their usual operations form a model.
This argument treats the set $\mathbb{N}$ as a completed object, so it does not satisfy a finitist.

### Inconsistent theories

The set $\{ p, \; p \to q, \; \lnot q \}$ is [[inconsistent|HYMTN6457G]]: modus ponens derives $q$, and $\lnot q$ is a member.
The theory $\{ \forall x \, \forall y \, (x = y), \; \exists x \, \exists y \, (x \neq y) \}$ is inconsistent.
Its second axiom is logically equivalent to the negation of the first.

Naive set theory with the axiom $\exists y \, \forall x \, (x \in y)$ and the separation schema of [[ZF|0HE5WDQ9FJ]] is inconsistent.
Separation gives the set $r = \{ x \in y : x \notin x \}$, and then $r \in r$ holds exactly when $r \notin r$.

### Consistency and satisfiability

Soundness gives one direction: a satisfiable theory is consistent.
The other direction, that a consistent first-order theory is satisfiable, is a form of [[Gödel's completeness theorem|WQ1ZE255SF]].
Henkin proved the theorem in this form, by building a model from a consistent theory.
Here "complete" refers to the proof system: it derives every logical consequence.

Consistency has finite character: $T$ is consistent exactly when every finite subset of $T$ is consistent.
The reason is that a derivation is a finite list, so it uses only finitely many members of $T$.
The semantic version, "if every finite subset has a model then $T$ has a model", is the [[compactness theorem|1NR3HAWG9D]].
It does not follow from the definitions alone, but it follows from the syntactic version through the completeness theorem.

### Consistency and unprovability

In classical logic, for a sentence $\varphi$, $T \nvdash \varphi$ exactly when $T \cup \{ \lnot\varphi \}$ is consistent.
Likewise $T \nvdash \lnot\varphi$ exactly when $T \cup \{ \varphi \}$ is consistent.
The proof uses the [[deduction theorem|9X08XK5RV2]].

A consistent theory that derives $\varphi$ or $\lnot\varphi$ for every sentence $\varphi$ is a [[complete theory|655K8Y7VS8]].
Here "complete" means negation complete: the theory decides each sentence.
This differs from the completeness of a proof system.

Consistency proofs have limits.
By [[Gödel's second incompleteness theorem|4PZM5GJTR5]], a consistent, computably axiomatized theory that contains Peano arithmetic does not prove its own consistency statement.
A [[relative consistency proof|X3G0RG2GPZ]] shows "if $S$ is consistent, then $T$ is consistent".
It avoids the limit, because it does not claim that $S$ is consistent.

### Watch out

"Consistent" and "true" are different.
The theory $\{ \forall x \, \forall y \, (x = y) \}$ is consistent, since a one-element structure is a model, although it is false in every larger structure.

"Consistent" and "satisfiable" are different definitions.
They agree for first-order logic only because of a theorem.
They can differ for other logics, for example for second-order logic with a fixed incomplete proof system.

A theory that derives neither $\varphi$ nor $\lnot\varphi$ is not inconsistent.
That situation is failure of negation completeness, and it is compatible with consistency.

### History

David Hilbert proved the consistency of his axioms for Euclidean geometry relative to arithmetic in his *Grundlagen der Geometrie* of 1899.
His proof used a model built from numbers.
In 1900 he listed the consistency of the arithmetic of the real numbers as the second of his 23 problems.
Gödel proved the completeness theorem in his thesis of 1929, so for first-order logic consistency and satisfiability agree.
In 1931 his second incompleteness theorem showed that a consistency proof for arithmetic cannot be carried out in arithmetic itself.
In 1936 Gentzen gave a [[consistency proof for Peano arithmetic|QPV0HNP22S]] with transfinite induction up to $\varepsilon_0$.

### Try it

Is $\{ p \to q, \; q \to r, \; p, \; \lnot r \}$ consistent?
Answer: no.
Modus ponens twice derives $q$ and then $r$, and $\lnot r$ is a member.

Show that $T$ is inconsistent exactly when some finite subset of $T$ is inconsistent.
Answer: the derivations of $\varphi$ and of $\lnot\varphi$ are finite, so together they use only finitely many members of $T$.
Conversely, a derivation from a subset is a derivation from $T$.

Must a consistent theory derive $\varphi$ or $\lnot\varphi$ for every sentence?
Answer: no.
In a language with one unary predicate $P$, the empty theory derives neither $\exists x \, P(x)$ nor its negation.
By soundness, a structure with $P$ empty shows $\nvdash \exists x \, P(x)$, and a structure with $P$ nonempty shows $\nvdash \lnot \exists x \, P(x)$.

## Explanations

### L1 human

A list of rules is consistent when the rules never contradict each other.
Take the two rules "every box is red" and "box number 3 is blue".
Together they force box 3 to be red and not red, so the list is inconsistent.
Drop the second rule and add "box number 3 is large" instead.
Now a world with only large red boxes obeys all rules, so the list is consistent.
Logicians check consistency in two ways: by building such a world, or by showing that no chain of reasoning ever reaches a contradiction.

### L2 human

We test the theory $T = \{ \forall x \, (P(x) \to Q(x)), \; P(c), \; \lnot Q(c) \}$ in a language with unary predicates $P$, $Q$ and a constant $c$.

1. From $\forall x \, (P(x) \to Q(x))$ we derive the instance $P(c) \to Q(c)$, by the rule for the [[universal quantifier|0GHS47PDAQ]].
2. From $P(c)$ and $P(c) \to Q(c)$, modus ponens gives $Q(c)$.
3. The theory contains $\lnot Q(c)$, so $T \vdash Q(c)$ and $T \vdash \lnot Q(c)$.
4. So $T$ is inconsistent, and by explosion $T$ derives every formula.
5. Now remove $\lnot Q(c)$.
   The structure with one element $a$, with $P$ and $Q$ both true of $a$ and $c$ named $a$, satisfies the other two sentences.
6. By soundness, the smaller theory is consistent.

The typical use is the pair of steps 5 and 6: a model gives consistency without any search through derivations.
A trap is to trust a failed search for a contradiction.
Not finding one is no proof of consistency, because derivations can be arbitrarily long.

### L3 human

Consistency is the syntactic shadow of satisfiability, and the completeness theorem says that for first-order logic the shadow is exact.
Henkin's proof makes this precise.
It extends a consistent theory to a maximal consistent theory with witnesses, by Lindenbaum's lemma, and builds a model from its closed terms.
In algebraic logic, a theory is consistent when the filter it generates in the [[Lindenbaum-Tarski algebra|QC9M3Q8B8Q]] is proper.
A maximal consistent theory corresponds to an ultrafilter, that is, to a homomorphism onto the two-element Boolean algebra.

For other logics the notions separate.
Full second-order logic has no complete, effective proof system, so a theory can be consistent for a given proof system and still have no model.
In paraconsistent logics simple consistency and [[Post consistency|WK2P0E82B4]] differ, and only the second one measures triviality.
Within arithmetic, the consistency statement $\mathrm{Con}(T)$ is a $\Pi^0_1$ sentence.
The study of which theories prove which consistency statements leads to [[Gödel's incompleteness theorems and related limits|HXHHWY3328]] and to [[relative consistency proofs|X3G0RG2GPZ]].
It also leads to ordinal analysis and to [[Hilbert's program|P1RW6JWX73]].
