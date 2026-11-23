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

Lindenbaum's lemma says that a set of sentences without a contradiction can always be enlarged until it answers every question, still without a contradiction.

Let $L$ be a first-order language, and let $\vdash$ be derivability in the Hilbert system $H$ of the [[soundness theorem|AVD7T7J063]].
A set $\Gamma$ of [[sentences|DKFGQTRYZE]] is [[consistent|VM8TQ70CVJ]] when there is no formula $\psi$ with $\Gamma \vdash \psi$ and $\Gamma \vdash \neg \psi$.
A set $\Delta$ of sentences of $L$ is maximal consistent when it is consistent and, for every sentence $\sigma$ of $L$, $\sigma \in \Delta$ or $\neg \sigma \in \Delta$.

**Lemma (Lindenbaum).** Every consistent set $\Gamma$ of sentences of $L$ is contained in a maximal consistent set $\Delta$ of sentences of $L$.
When $L$ is [[countable|01TQB88H4C]], $\Delta$ can be built from a list of all sentences, with no use of the axiom of choice.
For an arbitrary $L$, the proof uses [[Zorn's lemma|04RXTQA5ZA]].

**Properties.** Let $\Delta$ be maximal consistent, and let $\sigma$, $\tau$ be sentences of $L$.

1. Deductive closure: if $\Delta \vdash \sigma$, then $\sigma \in \Delta$.
2. Exactly one of $\sigma$ and $\neg \sigma$ lies in $\Delta$.
3. $(\sigma \to \tau) \in \Delta$ if and only if $\sigma \notin \Delta$ or $\tau \in \Delta$.
4. If $\forall x \, \varphi \in \Delta$, then $\varphi^x_t \in \Delta$ for every closed term $t$.
5. $\Delta$ has no consistent proper superset of sentences of $L$, and conversely, a consistent set of sentences with no consistent proper superset is maximal consistent.

The [[proof by enumeration|DCR0S91GYY]] treats countable $L$ and also proves the properties, and the [[proof by Zorn's lemma|6F5F3GN6SJ]] treats arbitrary $L$.

## Remarks

### A first extension, step by step

Take a language with one unary relation symbol $P$ and nothing else, and start from $\Gamma = \{ \exists x \, P(x) \}$.
Suppose the list of all sentences begins with $\sigma_0 = \forall x \, P(x)$ and $\sigma_1 = \exists x \, \exists y \, \neg (x = y)$.
Is $\Gamma \cup \{ \sigma_0 \}$ consistent?
Yes, because the one-element structure $\{ 0 \}$ with $P = \{ 0 \}$ satisfies it, and soundness says that a satisfiable set is consistent.
So the first stage is
$$\Delta_1 = \{ \exists x \, P(x), \ \forall x \, P(x) \}.$$
Next, $\Delta_1 \cup \{ \sigma_1 \}$ is satisfied by $\{ 0, 1 \}$ with $P = \{ 0, 1 \}$, so $\sigma_1$ goes in as well.
The process runs through the whole list, and the test at each stage is consistency, not truth in one structure that we fixed in advance.

If the list had started with $\neg \forall x \, P(x)$ instead, that sentence would have gone in, and we would have reached a different maximal set.
So the result is not unique: the order of the list decides which complete extension we get.

### What a maximal consistent set looks like

A maximal consistent set behaves like the set of all sentences true in one structure.
It contains everything it derives (property 1), it decides every sentence (property 2), and it treats $\to$ by the truth table (property 3).
In other words, it is a [[complete theory|655K8Y7VS8]] in the language $L$.
Property 4 is the start of the quantifier clause, but only the start: nothing yet forces a set that contains $\exists x \, \varphi$ to contain an instance $\varphi^x_t$.
The [[Henkin construction|RY8KRKR097]] fixes exactly that gap, and the [[term model of a set without witnesses|B3CSQE56G8]] shows what goes wrong without it.

### Why each hypothesis is needed

Consistency of $\Gamma$ is needed because an inconsistent set derives every formula, and every superset of it is inconsistent too.

Both proofs also rely on derivations being finite, and the lemma can fail without that.
Add to arithmetic the $\omega$-rule "from $\varphi(\underline{0}), \varphi(\underline{1}), \dots$ infer $\forall x \, \varphi$".
Then the set $\{ \neg \forall x \, P(x) \} \cup \{ P(\underline{n}) : n \in \mathbb{N} \}$ is inconsistent, yet each finite part of it is consistent.
So a union of a chain of consistent sets can be inconsistent, and the step to the limit breaks.

Countability of $L$ is needed only for the first proof, since a list $\sigma_0, \sigma_1, \dots$ of all sentences exists only when there are countably many.
For larger $L$ we need a well-ordering of the sentences or Zorn's lemma.

### The converse, and choice

Every subset of a consistent set is consistent, because a derivation from the subset is also a derivation from the whole set.
So a set of sentences is consistent if and only if it lies inside some maximal consistent set.

In ZF without choice, the lemma for languages of every size is equivalent to the [[Boolean prime ideal theorem|STPBXBKSZP]].
The prime ideal theorem gives an ultrafilter of the [[Lindenbaum-Tarski algebra|QC9M3Q8B8Q]] above $\Gamma$, and that ultrafilter is a maximal consistent set.
Conversely, the lemma for propositional logic gives propositional compactness, which implies the prime ideal theorem.

### Watch out

Lindenbaum's lemma gives existence, not a recipe.
Peano arithmetic, if consistent, has no maximal consistent extension that is decidable, because a decidable complete consistent extension would contradict [[Gödel's incompleteness theorem|X9WYNYE29C]] in Rosser's form.
The enumeration proof does not contradict this: its test "is $\Delta_n \cup \{ \sigma_n \}$ consistent?" is not a computable test.

### Try it

First, in the language with one unary $P$, give two different maximal consistent sets that contain $\exists x \, P(x)$.
The theory of the structure $\{ 0 \}$ with $P = \{ 0 \}$ contains $\forall x \, P(x)$, and the theory of $\{ 0, 1 \}$ with $P = \{ 0 \}$ contains its negation.

Second, explain why $\{ \sigma, \neg \sigma \}$ has no maximal consistent extension.
It is already inconsistent, and every superset of an inconsistent set is inconsistent.

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

Here is how the lemma is used in the completeness proof.
Suppose $\Gamma$ is consistent and we want a model.
Lindenbaum's lemma gives a maximal consistent $\Delta \supseteq \Gamma$, and $\Delta$ already tells us, for every atomic sentence, whether it should be true.
For example, if $\Delta$ contains $R(c, d)$ and $\neg R(d, c)$, then the model we build will put the pair $(c, d)$ into $R$ and leave $(d, c)$ out.
The [[model existence theorem|G0DTR159RN]] builds the model in exactly this way, from the closed terms.
Watch out: a model built this way may still fail $\exists x \, \varphi$, because the lemma alone adds no witnesses; that is why the proof adds Henkin constants first.

### L3 human

The lemma is the syntactic form of the existence of ultrafilters.
In the [[Lindenbaum-Tarski algebra|QC9M3Q8B8Q]] of a theory, consistent sets generate proper filters, and maximal consistent sets are ultrafilters, that is, points of the Stone space of the algebra.
The same argument builds canonical models in modal logic, prime theories in intuitionistic logic, and maximal ideals in rings, where Zorn's lemma plays the same role.
The lemma has no computable form for arithmetic, which is one face of the [[incompleteness theorems|X9WYNYE29C]]; see also [[completeness versus incompleteness|28AX3A4N86]].
