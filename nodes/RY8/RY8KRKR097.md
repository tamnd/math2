---
tag: RY8KRKR097
kind: concept
name: Henkin construction
aliases: [henkin-construction, henkin-theory, henkin-witness, witness-property]
msc: ["03C07", "03B10"]
topics: [FBWW4J1XWG]
audience: ug2
uses: [SC0BSJ3GT6, AVD7T7J063, VM8TQ70CVJ, DKFGQTRYZE, 6D3WA7N2W4, 983GZBQYT4, 655K8Y7VS8, 01TQB88H4C]
sources:
  - url: https://en.wikipedia.org/wiki/G%C3%B6del%27s_completeness_theorem
    locator: Proofs
  - book: isbn:9780122384523
    locator: Section 2.5
  - url: https://builds.openlogicproject.org/
    locator: The Completeness Theorem
---

## Summary

The Henkin construction builds a model of a [[consistent|VM8TQ70CVJ]] set of sentences out of pure syntax: the elements of the model are the names in the language.
Before it can do that, it adds a name for every element whose existence the sentences claim, and it settles every open question.

A set $\Delta$ of [[sentences|DKFGQTRYZE]] has the witness property when, for each sentence $\neg \forall x \, \varphi$ in $\Delta$, there is a constant $c$ with $\neg \varphi^x_c \in \Delta$.
In the abbreviation $\exists x = \neg \forall x \neg$, this says that each sentence $\exists x \, \psi$ in $\Delta$ has a witness $\psi^x_c$ in $\Delta$.
A Henkin set is a maximal consistent set with the witness property.
The construction has three steps.

1. Add new constants together with witness axioms $\exists x \, \psi \to \psi^x_c$.
2. Extend to a maximal consistent set by [[Lindenbaum's lemma|SC0BSJ3GT6]].
3. Take the closed [[terms|6D3WA7N2W4]] modulo provable equality as the universe of a [[structure|983GZBQYT4]].

It is the standard proof of the [[model existence theorem|G0DTR159RN]], and so of [[Gödel's completeness theorem|WQ1ZE255SF]].

## Motivation

To prove completeness, we must find a model for every consistent set $\Gamma$, and the only material at hand is syntax.
The closed terms are the natural candidates for the elements of the model.
Two problems appear at once.
First, $\Gamma$ may say $\exists x \, P(x)$ while no closed term $t$ has $P(t)$ derivable, so no term names the element we need.
Second, $\Gamma$ may decide neither $P(t)$ nor $\neg P(t)$, and then we do not know whether to put the element named $t$ into $P$.
New constants solve the first problem, and a maximal consistent extension solves the second.
Leon Henkin saw that these two steps are enough, and the result is a short proof that works the same way for every language.

The same idea returns throughout logic.
Canonical models in modal logic, the omitting types theorem and the completeness of Henkin semantics for higher-order logic all reuse it.

## Notation

We use the logical symbols $\neg$, $\to$, $\forall$ and $=$, and $\vdash$ is derivability in the Hilbert system $H$ of the [[soundness theorem|AVD7T7J063]].
We write $C = \{ c_0, c_1, \dots \}$ for a set of new constant symbols, and $L(C)$ for $L$ with these constants added.
A witness axiom, or Henkin axiom, is a sentence $\neg \forall x \, \varphi \to \neg \varphi^x_c$, usually written $\exists x \, \psi \to \psi^x_c$ with $\psi = \neg \varphi$.
For a maximal consistent $\Delta$ in $L(C)$, the term model $\mathcal{M}_\Delta$ has as universe the closed terms of $L(C)$ modulo the relation $t \sim u$ that holds when $(t = u) \in \Delta$.
Some books write $T^*$ or $\Gamma^*$ for $\Delta$, and call a set with the witness property "Henkin complete" or "saturated with witnesses".

## Remarks

### A run on a two-sentence theory

Let $L$ have one unary relation symbol $P$, and let $\Gamma = \{ \exists x \, P(x), \ \exists x \, \neg P(x) \}$.
The language has no constants, so at the start there are no closed terms at all.
We add new constants $c_0, c_1$ and the two witness axioms:
$$\exists x \, P(x) \to P(c_0), \qquad \exists x \, \neg P(x) \to \neg P(c_1).$$
With modus ponens, every extension of $\Gamma$ with these axioms derives $P(c_0)$ and $\neg P(c_1)$.
We also add witness axioms for the other existential sentences of $L(C)$, and then Lindenbaum's lemma gives a maximal consistent $\Delta$.
It cannot contain $c_0 = c_1$, since the equality axiom $c_0 = c_1 \to (P(c_0) \to P(c_1))$ would then give $P(c_1)$.
So $\neg (c_0 = c_1) \in \Delta$, and the term model has two different elements:
$$[c_0] \in P^{\mathcal{M}}, \qquad [c_1] \notin P^{\mathcal{M}}.$$
Check: both sentences of $\Gamma$ hold in this model, with witnesses $[c_0]$ and $[c_1]$.

### The model depends on choices

What about the other constants $c_2, c_3, \dots$?
They name elements too, and $\Delta$ decides whether each one equals $c_0$, equals $c_1$, or is new.
If $\Delta$ happens to contain "there are at most two elements", every $c_i$ collapses onto $[c_0]$ or $[c_1]$, and the model has two elements.
If it contains "there are at least three elements", the model is larger.
Both choices are consistent with $\Gamma$, so the term model is not unique, and its size depends on the choices made by Lindenbaum's lemma.

### More examples

The example of [[a witness that must be a new constant|9NC0F9MZCT]] starts from $\exists x \, P(x)$ and $\neg P(a)$, and shows that reusing $a$ as the witness would make the set inconsistent.
The [[equality quotient|GCX3RQVXXY]] shows the opposite effect: under $\forall x \, \forall y \, (x = y)$, infinitely many closed terms collapse to one element.
True arithmetic $\mathrm{Th}(\mathbb{N}, 0, S, +, \cdot)$ is already a Henkin set in its own language.
Each number $n$ is the value of the numeral $S^n 0$, so each true $\exists x \, \psi$ has a numeral witness, and the term model is isomorphic to $\mathbb{N}$.

### What fails without each step

Without witnesses, a maximal consistent set can still go wrong.
The [[set without witnesses|B3CSQE56G8]] in the language $\{ a, f, P \}$ contains $\exists x \, P(x)$ and $\neg P(f^n(a))$ for every $n$, so its term model fails $\exists x \, P(x)$.
Without new constants, a language with no constants, such as the language $\{ < \}$ of dense linear orders, has no closed terms, and a term model would have an empty universe.
Without maximality, the set $\{ \exists x \, P(x), P(a) \}$ in the language $\{ a, P, Q \}$ has the witness $a$, but it decides neither $Q(a)$ nor $\neg Q(a)$, so the term model has no definite interpretation of $Q$.

### The rules you can use

Witness axioms are safe: if $\Gamma$ is consistent in $L$, then $\Gamma$ plus all witness axioms, with each constant fresh when its axiom is added, is consistent in $L(C)$.
This is step (d) of the [[proof of model existence|FMZMD0GGYK]].
They are also conservative: for a sentence $\sigma$ of $L$, the extended set derives $\sigma$ if and only if $\Gamma \vdash \sigma$, by the safety fact applied to $\Gamma \cup \{ \neg \sigma \}$.

The truth lemma says that for a Henkin set $\Delta$, $\mathcal{M}_\Delta \models \sigma$ if and only if $\sigma \in \Delta$, for every sentence $\sigma$ of $L(C)$.
Every element of $\mathcal{M}_\Delta$ is the value of a closed term, so $\mathcal{M}_\Delta$ has at most $|L| + \aleph_0$ elements, and it is [[countable|01TQB88H4C]] when $L$ is.
Conversely, if every element of a structure $\mathcal{A}$ is the value of a closed term, then the theory of $\mathcal{A}$ is a Henkin set, and its term model is isomorphic to $\mathcal{A}$.

### Watch out

Three slips are common.
The first is to add witnesses only for formulas of $L$.
The new constants create new formulas $\exists x \, \psi$ of $L(C)$, and these need witnesses too, so the construction must list all formulas of $L(C)$, or repeat in $\omega$ stages.

The second is to reuse an old constant as a witness.
With $\Gamma = \{ \exists x \, P(x), \neg P(a) \}$, the axiom $\exists x \, P(x) \to P(a)$ makes the set inconsistent.

The third is to prove the truth lemma by induction on subformulas.
The case $\forall x \, \varphi$ needs the instances $\varphi^x_t$, which are not subformulas.
The induction is on the number of logical symbols, which a substitution of closed terms does not change.

### History

Kurt Gödel proved the completeness theorem in his dissertation of 1929, published in 1930, by a different method.
Leon Henkin published the method of witness constants and term models in 1949.
Gisbert Hasenjaeger gave a simplified form of Henkin's proof in 1953.
Henkin also used the method for the theory of types, where it gives completeness with respect to general models.

### Try it

First, run the construction on $\Gamma = \{ \exists x \, \exists y \, R(x, y) \}$, with $R$ binary.
One witness axiom gives a constant $c_0$ with $\exists y \, R(c_0, y)$, and a second gives $c_1$ with $R(c_0, c_1)$, so the term model puts the pair $([c_0], [c_1])$ into $R$.

Second, why does the term model of a Henkin set in a countable language have at most countably many elements?
Its elements are classes of closed terms, and there are countably many closed terms, since each is a finite string over a countable alphabet.

## Explanations

### L1 human

Suppose a list of facts says "somebody did it" but names nobody.
The Henkin construction invents a name, say "the culprit", for each such claim.
Then it settles every open question about all the named people, without making a contradiction.
Finally, it lets the names themselves be the people.
A list of facts treated this way describes a small world in which all the facts are true.

### L2 human

Here is the construction used to bound the size of a model.
Let $\Gamma$ be a consistent set of sentences in a countable language, for example the axioms of a group together with "there is an element of order $3$".
Add countably many constants and their witness axioms; the language stays countable.
Extend to a Henkin set $\Delta$, and form the term model.
Its elements are classes of closed terms, so the model is countable, and by the truth lemma it is a group with an element of order $3$.
This is the typical use: a consistent set has a model, and the model is no larger than the language plus $\aleph_0$.
Watch out: the model need not be the one you had in mind, since $\Delta$ may also decide, say, that the group is infinite.

### L3 human

The Henkin construction meets countably many requirements, one for each formula, and each requirement is met by one finite extension.
In this form it is a forcing argument, or a Baire category argument in the Stone space of the theory.
The Rasiowa and Sikorski form makes this explicit: one needs an ultrafilter of the [[Lindenbaum-Tarski algebra|QC9M3Q8B8Q]] that respects countably many infinite joins.
The same scheme, with more requirements, proves the omitting types theorem.
The construction is effective relative to a consistency test: for a decidable consistent $\Gamma$ in a countable language, the halting problem computes a Henkin set, and so a model.
See also the essay [[completeness versus incompleteness|28AX3A4N86]].
