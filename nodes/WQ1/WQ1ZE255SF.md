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

In every group, $a \cdot b = a \cdot c$ implies $b = c$.
The completeness theorem says that, because this sentence is true in every group, a formal derivation of it from the group axioms exists.
In general, what is true in every model of a set of axioms can be derived from the axioms in a finite number of steps.

Let $L$ be a first-order language with equality, and let $\vdash$ be derivability in the [[Hilbert system|1MGMQX43B8]] $H$ of the [[soundness theorem|AVD7T7J063]].
For a set $\Gamma$ of [[sentences|DKFGQTRYZE]] and a sentence $\varphi$, we write $\Gamma \models \varphi$ for [[logical consequence|1HK0VYWTV7]]: every [[model|MVCH6N9SNW]] of $\Gamma$ satisfies $\varphi$.

**Theorem (Gödel).**

1. Strong form: if $\Gamma \models \varphi$, then $\Gamma \vdash \varphi$.
2. Weak form: if $\varphi$ is valid, that is, true in every [[structure|983GZBQYT4]] for $L$, then $\vdash \varphi$.

With the soundness theorem, $\Gamma \vdash \varphi$ holds if and only if $\Gamma \models \varphi$ holds.
The theorem holds for languages of every cardinality.
For uncountable $L$, the proof uses the axiom of choice.

Two proofs are given.
The first is [[a proof from the model existence theorem|3FR16954CY]], which is Henkin's proof.
The second is [[an outline of Gödel's original proof|CS0R0WW2V9]].

## Remarks

### The big idea

The relation $\models$ speaks about all structures, and there are too many of them to check one by one.
The relation $\vdash$ speaks about finite strings of symbols, and we can list all derivations.
The theorem says that the two relations are the same.
So a question about all structures has a finite answer, a derivation, whenever the answer is yes.

The work is in the [[model existence theorem|G0DTR159RN]]: every consistent set of sentences has a model.
If $\Gamma \nvdash \varphi$, then $\Gamma \cup \{ \neg \varphi \}$ is consistent, its model satisfies $\Gamma$ and fails $\varphi$, and so $\Gamma \not\models \varphi$.

### Why each hypothesis is needed

The logic must be first-order.
For [[second-order logic|G6X7SZSNC5]] with full semantics, no effective proof system is sound and complete.
Second-order Peano arithmetic has only one model up to isomorphism, so its consequences would include all true sentences of arithmetic, and that set is not computably enumerable.

The proof system must contain the equality axioms.
Drop axiom group 5, the axioms $x = x$, and read $=$ as the empty relation.
The remaining axioms stay true and MP keeps truth, so the valid sentence $\forall x \, (x = x)$ is no longer derivable.

The semantics must allow all structures.
Add constants $\underline{0}, \underline{1}, \dots$ and let $\Gamma = \{ P(\underline{n}) : n \in \mathbb{N} \}$.
Over all structures, $\Gamma \not\models \forall x \, P(x)$, because a model can have an element with no name outside $P$.
Over the structures where the numerals name every element, $\Gamma$ would entail $\forall x \, P(x)$, but no finite part of $\Gamma$ would.
A derivation uses finitely many premises, so no derivation could exist, and the strong form would fail.

Choice matters only for uncountable languages.
In ZF, the theorem for languages of every size is equivalent to the [[Boolean prime ideal theorem|STPBXBKSZP]].
For countable languages, the theorem needs no choice.

### Consequences

- Let $L$ be a computable language.
  The valid sentences of $L$ form a computably enumerable set, since we can list all derivations and keep their last lines.
- By [[Church's theorem|VA6BNNY2YC]], this set is not decidable when $L$ has a binary relation symbol.
- The consequences of a computably enumerable set of axioms are computably enumerable, so every [[recursively axiomatizable theory|3ANXZC3BEG]] has a computably enumerable set of theorems.
- The [[compactness theorem|1NR3HAWG9D]] follows: if $\Gamma \models \varphi$, then a finite part of $\Gamma$ entails $\varphi$, because a derivation is finite.
- Any two sound and complete proof systems derive the same sentences from the same axioms.
- To show $\Gamma \nvdash \varphi$, it is enough to find a model of $\Gamma$ that fails $\varphi$.
  So every proof of independence is, in principle, a model construction.

### Converse

The converse of the strong form is the [[soundness theorem|AVD7T7J063]]: if $\Gamma \vdash \varphi$, then $\Gamma \models \varphi$.
It is true, and its proof is an induction on derivations.

### Generalizations

The [[model existence theorem|G0DTR159RN]] is an equivalent form: every consistent set of sentences has a model, of size at most $|L| + \aleph_0$.

For a set $\Gamma$ of formulas and a formula $\varphi$ with free variables, $\Gamma \models \varphi$ also implies $\Gamma \vdash \varphi$.
The proof treats the free variables as new constants.

Other proof systems have the same theorem.
[[Natural deduction|6KT3BJZ7D1]] and the cut-free [[sequent calculus|W72CA3R9MP]] are complete for the same semantics.
For the sequent calculus, completeness without the cut rule gives [[cut elimination|AYRZ98Y0NW]] as a corollary.

Other logics have completeness theorems that the same Henkin method proves.
Examples are many-sorted logic, higher-order logic with Henkin's general models, and many modal logics with Kripke models.
[[Intuitionistic logic|Q11N8X99FK]] is complete for Kripke models.

There is also an arithmetized form.
Let $T$ be a computably axiomatized theory.
In Peano arithmetic, from the hypothesis that $T$ is consistent, one defines a model of $T$ by arithmetical formulas.

### Watch out

Completeness and the [[incompleteness theorems|X9WYNYE29C]] do not contradict each other.
Completeness is about the logic: every sentence true in all models of $T$ is derivable from $T$.
Incompleteness is about a theory: some sentence is true in some models of $T$ and false in others, so $T$ derives neither it nor its negation.

### Try it

The group axioms do not derive $\forall x \, \forall y \, (x \cdot y = y \cdot x)$.
Which kind of argument shows this, a derivation or a model?
A model shows it: the symmetric group $S_3$ satisfies the axioms and fails the sentence, so by soundness the sentence is not derivable.

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

We use the theorem to show that a sentence is derivable without writing the derivation.

1. Let $\Gamma$ be the axioms of a dense linear order without endpoints, in the language $\{ < \}$.
2. Let $\varphi$ say "between any two different elements there are two more": $\forall x \, \forall y \, (x < y \to \exists u \, \exists v \, (x < u \land u < v \land v < y))$.
3. In every model of $\Gamma$, density gives $u$ with $x < u < y$, and density again gives $v$ with $u < v < y$.
4. So $\Gamma \models \varphi$, and the theorem gives $\Gamma \vdash \varphi$.

The typical use goes in both directions: a semantic argument shows derivability, and a model shows non-derivability.
The trap is to confuse this theorem with the [[incompleteness theorems|X9WYNYE29C]].
Completeness concerns the logic.
Incompleteness concerns a theory, which may leave a sentence undecided because it is true in some models and false in others.

### L3 human

The theorem identifies two consequence relations: the inductive relation $\vdash$ and the relation $\models$, which quantifies over all structures.
Since $\vdash$ is computably enumerable, the theorem shows that $\models$ has the same complexity, which its definition does not suggest.
In algebraic terms, for a countable language, the [[Lindenbaum-Tarski algebra|QC9M3Q8B8Q]] of a theory has enough ultrafilters that respect the quantifiers to separate its elements.
The theorem is a statement about first-order logic as a whole, and it is the base of [[model theory|HFTBG5PMXC]].
See the essay [[completeness versus incompleteness|28AX3A4N86]] for its relation to the theorems of 1931.
