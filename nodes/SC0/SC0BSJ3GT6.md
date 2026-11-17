---
tag: SC0BSJ3GT6
kind: statement
role: lemma
name: Lindenbaum's lemma
aliases: [lindenbaums-lemma, lindenbaum-lemma]
msc: ["03B10", "03C07"]
topics: [FBWW4J1XWG]
audience: ug2
about: [VM8TQ70CVJ, 655K8Y7VS8]
uses: [AVD7T7J063, VM8TQ70CVJ, DKFGQTRYZE, 05006AJ7DZ, 9X08XK5RV2, 01TQB88H4C, 04RXTQA5ZA]
history:
  first_stated: "Adolf Lindenbaum; first published by Alfred Tarski in 1930, who attributed it to Lindenbaum"
  notes: "Lindenbaum did not publish the lemma himself."
sources:
  - url: https://en.wikipedia.org/wiki/Lindenbaum%27s_lemma
    locator: lead section
  - book: isbn:9780122384523
    locator: Section 2.5
  - url: https://builds.openlogicproject.org/
    locator: The Completeness Theorem
---

## Statement

Let $L$ be a first-order language, and let $\vdash$ be derivability in the Hilbert system $H$ of the [[soundness theorem|AVD7T7J063]].
A set $\Gamma$ of [[sentences|DKFGQTRYZE]] is [[consistent|VM8TQ70CVJ]] when there is no formula $\psi$ with $\Gamma \vdash \psi$ and $\Gamma \vdash \neg \psi$.
A set $\Delta$ of sentences of $L$ is maximal consistent when it is consistent and, for every sentence $\sigma$ of $L$, $\sigma \in \Delta$ or $\neg \sigma \in \Delta$.

**Lemma (Lindenbaum).** Every consistent set $\Gamma$ of sentences of $L$ is contained in a maximal consistent set $\Delta$ of sentences of $L$.
When $L$ is [[countable|01TQB88H4C]], $\Delta$ can be built by a list of all sentences, with no use of the axiom of choice.
For an arbitrary $L$, the proof uses [[Zorn's lemma|04RXTQA5ZA]].

**Properties.** Let $\Delta$ be maximal consistent, and let $\sigma$, $\tau$ be sentences of $L$.

1. Deductive closure: if $\Delta \vdash \sigma$, then $\sigma \in \Delta$.
2. Exactly one of $\sigma$ and $\neg \sigma$ lies in $\Delta$.
3. $(\sigma \to \tau) \in \Delta$ if and only if $\sigma \notin \Delta$ or $\tau \in \Delta$.
4. If $\forall x \, \varphi \in \Delta$, then $\varphi^x_t \in \Delta$ for every closed term $t$.
5. $\Delta$ has no consistent proper superset of sentences of $L$. Conversely, a consistent set of sentences with no consistent proper superset is maximal consistent.

Two proofs are given: [[a proof by enumeration|DCR0S91GYY]] for countable $L$, which also proves the properties, and [[a proof by Zorn's lemma|6F5F3GN6SJ]] for arbitrary $L$.

## Remarks

### Why each hypothesis is needed

- Consistency of $\Gamma$: an inconsistent set derives every formula, and every superset of it is inconsistent too. So it has no consistent extension at all.
- Finite derivations: both proofs use that a derivation uses only finitely many members of $\Gamma$. Add the $\omega$-rule "from $\varphi(\underline{0}), \varphi(\underline{1}), \dots$ infer $\forall x \, \varphi$" to arithmetic. Then $\set{\neg \forall x \, P(x)} \cup \set{P(\underline{n}) : n \in \N}$ is inconsistent, but each finite part of it is consistent, so the union of a chain of consistent sets need not be consistent.
- Countability of $L$ in the first proof: the list $\sigma_0, \sigma_1, \dots$ of all sentences exists only when the set of sentences is countable. For larger $L$ one needs a well-ordering of the sentences or Zorn's lemma.

### Consequences

- A maximal consistent set is a complete theory: it is closed under $\vdash$ by property 1, and it decides every sentence by property 2. See [[complete theory|655K8Y7VS8]].
- Every consistent theory has a consistent complete extension in the same language.
- The lemma is the first step of the [[Henkin construction|RY8KRKR097]], which proves the [[model existence theorem|G0DTR159RN]] and so [[Gödel's completeness theorem|WQ1ZE255SF]].
- The propositional form is step (c) of the [[proof of the strong completeness theorem by maximal consistent sets|GNPVCQC55C]].

### Converse

Every subset of a consistent set is consistent, because a derivation from the subset is also a derivation from the whole set.
So a set of sentences is consistent if and only if it is contained in some maximal consistent set.

### Generalizations

- The lemma holds for every logic with finite derivations and a negation that satisfies property (P5) of the [[enumeration proof|DCR0S91GYY]]: $\Gamma \cup \set{\neg \sigma}$ is inconsistent exactly when $\Gamma \vdash \sigma$. Modal logics use it to build canonical models.
- Algebraic form: the maximal consistent sets that contain $\Gamma$ are the ultrafilters of the [[Lindenbaum-Tarski algebra|QC9M3Q8B8Q]] of $\Gamma$. So the lemma is a case of the ultrafilter lemma for Boolean algebras.
- In ZF, the lemma for languages of every size is equivalent to the [[Boolean prime ideal theorem|STPBXBKSZP]]. The prime ideal theorem gives the ultrafilters above. Conversely, the lemma for propositional logic gives the propositional compactness theorem, which implies the prime ideal theorem.
- No effective version: Peano arithmetic, if it is consistent, has no maximal consistent extension whose set of members is decidable. This follows from Gödel's [[incompleteness theorem|X9WYNYE29C]] in the strong form of Rosser.

## History

Adolf Lindenbaum found the lemma but did not publish it.
Alfred Tarski published it in 1930 and attributed it to Lindenbaum.
Leon Henkin used it in 1949 in his proof of the completeness theorem.

## Explanations

### L1 human

Think of a list of rules that do not contradict each other.
The lemma says that we can keep adding rules until every question has an answer, and still have no contradiction.
We go through all possible statements one by one.
For each statement we add it if it causes no contradiction, and otherwise we add its negation.
For example, start from "there are at least $2$ objects": we may add "there are at least $3$ objects", or we may add "there are at most $2$ objects", but not both.

### L2 human

We extend $\Gamma = \set{\exists x \, P(x)}$ in a language with one unary relation symbol $P$ and no other symbols.

1. List the sentences, and suppose the first two are $\sigma_0 = \forall x \, P(x)$ and $\sigma_1 = \exists x \, \exists y \, \neg (x = y)$.
2. $\Gamma \cup \set{\sigma_0}$ is consistent, because the structure $\set{0}$ with $P = \set{0}$ satisfies it and satisfiable sets are consistent by soundness. So $\Delta_1 = \set{\exists x \, P(x), \forall x \, P(x)}$.
3. $\Delta_1 \cup \set{\sigma_1}$ is consistent, because $\set{0, 1}$ with $P = \set{0, 1}$ satisfies it. So $\Delta_2 = \Delta_1 \cup \set{\sigma_1}$.
4. The process continues through the whole list. At each step the test is consistency, not truth in one fixed structure.

The typical use is the first step of a completeness proof.
The trap is to think that the result is unique: the order of the list decides which complete extension we get, and $\Gamma$ above has many.

### L3 human

The lemma is the syntactic form of the existence of ultrafilters.
In the [[Lindenbaum-Tarski algebra|QC9M3Q8B8Q]] of a theory, consistent sets generate proper filters, and maximal consistent sets are ultrafilters, that is, points of the Stone space of the algebra.
The same argument builds canonical models in modal logic, prime theories in intuitionistic logic, and maximal ideals in rings, where Zorn's lemma plays the same role.
The lemma has no computable form for arithmetic, which is one face of the [[incompleteness theorems|X9WYNYE29C]]; see also [[completeness versus incompleteness|28AX3A4N86]].
