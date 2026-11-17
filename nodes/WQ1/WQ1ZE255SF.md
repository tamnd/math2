---
tag: WQ1ZE255SF
kind: statement
role: theorem
name: Gödel's completeness theorem
aliases: [completeness-theorem, godels-completeness-theorem, completeness-of-first-order-logic]
msc: ["03B10", "03C07"]
topics: [FBWW4J1XWG]
audience: ug2
uses: [DKFGQTRYZE, 1HK0VYWTV7, 1MGMQX43B8, MVCH6N9SNW, AVD7T7J063, G0DTR159RN, 983GZBQYT4, 2RBQPV02AS]
about: [1HK0VYWTV7, 086QKPF0A6]
history:
  first_stated: "Kurt Gödel, doctoral thesis, University of Vienna, 1929; published in 1930 in Monatshefte für Mathematik und Physik"
  notes: "Hilbert and Ackermann posed the question in 1928. Henkin gave the proof by witness constants in 1949."
sources:
  - url: https://en.wikipedia.org/wiki/Gödel's_completeness_theorem
    locator: lead section
  - url: https://en.wikipedia.org/wiki/G%C3%B6del%27s_completeness_theorem
    locator: More general form
  - url: https://en.wikipedia.org/wiki/G%C3%B6del%27s_completeness_theorem
    locator: Consequences
  - book: isbn:9780122384523
    locator: Section 2.5
  - book: isbn:9781482237726
    locator: Chapter 2
  - url: https://builds.openlogicproject.org/
    locator: The Completeness Theorem
same_as:
  wikidata: Q902052
  wikipedia: Gödel's completeness theorem
---

## Statement

Let $L$ be a first-order language with equality, and let $\vdash$ be derivability in the [[Hilbert system|1MGMQX43B8]] $H$ of the [[soundness theorem|AVD7T7J063]].
For a set $\Gamma$ of [[sentences|DKFGQTRYZE]] and a sentence $\varphi$, $\Gamma \models \varphi$ is [[logical consequence|1HK0VYWTV7]]: every [[model|MVCH6N9SNW]] of $\Gamma$ satisfies $\varphi$.

**Theorem (Gödel).**

1. Strong form: if $\Gamma \models \varphi$, then $\Gamma \vdash \varphi$.
2. Weak form: if $\varphi$ is valid, that is, true in every [[structure|983GZBQYT4]] for $L$, then $\vdash \varphi$.

With the soundness theorem, $\Gamma \vdash \varphi$ holds if and only if $\Gamma \models \varphi$ holds.
The theorem holds for languages of every cardinality; for uncountable $L$, the proof uses the axiom of choice.

Two proofs are given: [[a proof from the model existence theorem|3FR16954CY]], which is Henkin's proof, and [[an outline of Gödel's original proof|CS0R0WW2V9]].

## Remarks

### Why each hypothesis is needed

- First-order logic: for second-order logic with full semantics, no effective proof system is sound and complete. Second-order Peano arithmetic has only one model up to isomorphism, so its consequences would include all of true arithmetic, which is not computably enumerable. See [[second-order logic|G6X7SZSNC5]].
- The axioms of $H$: drop axiom group 5 ($x = x$). Then $=$ may be read as the empty relation, and the remaining axioms and MP keep truth. So the valid sentence $\forall x \, (x = x)$ is no longer derivable.
- Finite derivations and infinite $\Gamma$: the strong form needs the [[compactness theorem|1NR3HAWG9D]] in a hidden way. In $\omega$-logic, the set $\set{P(\underline{n}) : n \in \N}$ entails $\forall x \, P(x)$ over $\omega$-models, where the numerals name all elements. No finite part of it does, so no finite derivation can be found.
- Choice: in ZF, the theorem for languages of every size is equivalent to the [[Boolean prime ideal theorem|STPBXBKSZP]]. For countable languages it needs no choice.

### Consequences

- The valid sentences of a computable language form a computably enumerable set: list all derivations and keep the last lines. By [[Church's theorem|VA6BNNY2YC]], this set is not decidable when $L$ has a binary relation symbol.
- More generally, the consequences of a computably enumerable set of axioms are computably enumerable. Every [[recursively axiomatizable theory|3ANXZC3BEG]] has a computably enumerable set of theorems.
- The [[compactness theorem|1NR3HAWG9D]]: if $\Gamma \models \varphi$, then a finite part of $\Gamma$ entails $\varphi$, because a derivation is finite.
- Provability does not depend on the proof system: any two sound and complete proof systems derive the same sentences from the same axioms.
- Independence proofs: $\Gamma \nvdash \varphi$ holds as soon as some model of $\Gamma$ fails $\varphi$. Every result of the form "$\varphi$ is not provable" is in principle a model construction.

### Converse

The converse of the strong form is the [[soundness theorem|AVD7T7J063]]: if $\Gamma \vdash \varphi$, then $\Gamma \models \varphi$.
It is true, and it is proved by induction on derivations.

### Generalizations

- The [[model existence theorem|G0DTR159RN]] is an equivalent form: every consistent set of sentences has a model, of size at most $\max(|L|, \aleph_0)$.
- Formulas with free variables: for a set $\Gamma$ of formulas and a formula $\varphi$, $\Gamma \models \varphi$ implies $\Gamma \vdash \varphi$. Treat the free variables as new constants.
- Other proof systems: [[natural deduction|6KT3BJZ7D1]] and the cut-free [[sequent calculus|W72CA3R9MP]] are complete for the same semantics. For the sequent calculus, completeness without the cut rule gives [[cut elimination|AYRZ98Y0NW]] as a corollary.
- Other logics: many-sorted logic, higher-order logic with Henkin's general models, and many modal logics with Kripke models have completeness theorems proved by the same Henkin method. [[Intuitionistic logic|Q11N8X99FK]] is complete for Kripke models.
- Arithmetized form: let $T$ be a computably axiomatized theory. In Peano arithmetic, from the hypothesis that $T$ is consistent, one defines a model of $T$ by arithmetical formulas.

## History

David Hilbert and Wilhelm Ackermann posed the question of completeness for first-order logic in their 1928 book.
Kurt Gödel answered it in his doctoral thesis at the University of Vienna in 1929.
He published the proof in 1930 in Monatshefte für Mathematik und Physik.
Leon Henkin gave the modern proof with witness constants in 1949.

## Explanations

### L1 human

Some statements follow from given rules because they hold in every situation where the rules hold.
Other statements follow because we can write down a step-by-step proof from the rules.
The theorem says that these two ideas agree in first-order logic.
For example, in every group, $a \cdot b = a \cdot c$ forces $b = c$.
So there must be a written proof of this from the group axioms, and there is one: multiply on the left by $a^{-1}$.

### L2 human

We use the theorem to show that a sentence is provable without writing the proof.

1. Let $\Gamma$ be the axioms of a dense linear order without endpoints, in the language $\set{<}$.
2. Let $\varphi$ say "between any two different elements there are two more": $\forall x \, \forall y \, (x < y \to \exists u \, \exists v \, (x < u \land u < v \land v < y))$.
3. In every model of $\Gamma$, density gives $u$ with $x < u < y$, and density again gives $v$ with $u < v < y$.
4. So $\Gamma \models \varphi$, and the theorem gives $\Gamma \vdash \varphi$.

The typical use goes in both directions: a semantic argument shows provability, and a model shows non-provability.
The trap is to confuse this theorem with the [[incompleteness theorems|X9WYNYE29C]].
Completeness concerns the logic; incompleteness concerns a theory, which may leave a sentence undecided because it is true in some models and false in others.

### L3 human

The theorem identifies two consequence relations: the inductive relation $\vdash$ and the relation $\models$, which quantifies over all structures.
Since $\vdash$ is computably enumerable, the theorem shows that $\models$ has the same complexity, which its definition does not suggest.
In algebraic terms, for a countable language, it says that the [[Lindenbaum-Tarski algebra|QC9M3Q8B8Q]] of a theory, with its quantifiers, has enough ultrafilters that respect the quantifiers to separate its elements.
The theorem is a statement about first-order logic as a whole, and is the base of [[model theory|HFTBG5PMXC]].
See the essay [[completeness versus incompleteness|28AX3A4N86]] for its relation to the theorems of 1931.
