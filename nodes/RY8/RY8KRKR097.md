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

The Henkin construction builds a model of a [[consistent|VM8TQ70CVJ]] set of sentences out of the closed [[terms|6D3WA7N2W4]] of a larger language.
A set $\Delta$ of sentences has the witness property when, for each sentence $\neg \forall x \, \varphi$ in $\Delta$, some constant $c$ gives $\neg \varphi^x_c \in \Delta$.
Equivalently, in the abbreviation $\exists x = \neg \forall x \neg$, each sentence $\exists x \, \psi$ in $\Delta$ has a witness $\psi^x_c$ in $\Delta$.
A Henkin set is a maximal consistent set with the witness property.
The construction has three steps: add new constants with witness axioms, extend by [[Lindenbaum's lemma|SC0BSJ3GT6]], and take the term model modulo provable equality.
It is the standard proof of the [[model existence theorem|G0DTR159RN]], and so of [[Gödel's completeness theorem|WQ1ZE255SF]].

## Motivation

To prove completeness, we must find a model for every consistent set $\Gamma$, and the only material at hand is syntax.
The closed terms are the natural candidates for the elements of the model.
Two problems appear.
First, $\Gamma$ may say $\exists x \, P(x)$ with no closed term $t$ for which $P(t)$ follows; then no term names the required element.
Second, $\Gamma$ may decide neither $P(t)$ nor $\neg P(t)$, and then the term model has no definite answer.
New constants solve the first problem, and a maximal consistent extension solves the second.
Leon Henkin saw that these two steps are enough, and the result is a short and uniform proof.

## Notation

The language $L$ has the logical symbols $\neg$, $\to$, $\forall$ and $=$, and $\vdash$ is derivability in the Hilbert system $H$ of the [[soundness theorem|AVD7T7J063]].
$C = \set{c_0, c_1, \dots}$ is a set of new constant symbols, and $L(C)$ is $L$ with these constants added.
A witness axiom (Henkin axiom) is a sentence $\neg \forall x \, \varphi \to \neg \varphi^x_c$, often written $\exists x \, \psi \to \psi^x_c$ with $\psi = \neg \varphi$.
For a maximal consistent $\Delta$ in $L(C)$, the term model $\mathcal{M}_\Delta$ has as universe the closed terms of $L(C)$ modulo $t \sim u \iff (t = u) \in \Delta$.
Some books write $\Delta$ as $T^*$ or $\Gamma^*$, and call a set with the witness property "Henkin complete" or "saturated with witnesses".

## Remarks

### Examples

- [[A witness for an existential sentence|9NC0F9MZCT]]: for $\Gamma = \set{\exists x \, P(x), \neg P(a)}$, the witness axiom adds $P(c)$, and the Henkin set then contains $\neg (c = a)$.
- [[The equality quotient|GCX3RQVXXY]]: for $\Gamma = \set{\forall x \, \forall y \, (x = y)}$, infinitely many closed terms all collapse to one element of the term model.
- True arithmetic $\mathrm{Th}(\N, 0, S, +, \cdot)$ is already a Henkin set in its own language. Each element $n$ is the value of the numeral $S^n 0$, so each true $\exists x \, \psi$ has a numeral witness. Its term model is isomorphic to $\N$.
- A set $\Gamma = \set{\exists x \, P(x), \exists x \, \neg P(x)}$ in the language $\set{P}$: the witness axioms give $P(c_i)$ and $\neg P(c_j)$, so every Henkin extension contains $\neg (c_i = c_j)$, and the term model has at least two elements. The L2 explanation below works this example.
- Canonical models in modal logic use the same idea: maximal consistent sets are the worlds, and the witness lemma gives the successor worlds.

### Non-examples

- [[A maximal consistent set without witnesses|B3CSQE56G8]]: in the language $\set{a, f, P}$, $\Delta$ can contain $\exists x \, P(x)$ and $\neg P(t)$ for every closed term $t$. Its term model fails $\exists x \, P(x)$.
- The theory of dense linear orders without endpoints, in the language $\set{<}$, has no constant symbols. So there are no closed terms, and a term model would have an empty universe.
- A consistent set that is not maximal: $\set{\exists x \, P(x), P(a)}$ in the language $\set{a, P, Q}$ has the witness $a$, but it decides neither $Q(a)$ nor $\neg Q(a)$, so the term model has no definite interpretation of $Q$.

### Basic properties

1. Witness axioms are safe: if $\Gamma$ is consistent in $L$, then $\Gamma$ plus all witness axioms, with fresh constants chosen in turn, is consistent in $L(C)$. This is Step (d) of the [[proof of model existence|FMZMD0GGYK]].
2. Conservativity: for a sentence $\sigma$ of $L$, $\Gamma$ plus the witness axioms derives $\sigma$ if and only if $\Gamma \vdash \sigma$. Apply property 1 to $\Gamma \cup \set{\neg \sigma}$ and use fact (P5) of the [[enumeration proof|DCR0S91GYY]].
3. The witness property passes to supersets in the same language: a superset of a set with all witness axioms still contains them, and property 3 of Lindenbaum's lemma then gives the witnesses.
4. Truth lemma: for a Henkin set $\Delta$, $\mathcal{M}_\Delta \models \sigma$ if and only if $\sigma \in \Delta$, for every sentence $\sigma$ of $L(C)$. This is Step (g) of the proof of model existence.
5. Every element of $\mathcal{M}_\Delta$ is the value of a closed term, so $\mathcal{M}_\Delta$ has at most $\max(|L|, \aleph_0)$ elements. For countable $L$, it is [[countable|01TQB88H4C]].
6. Conversely, if every element of a structure $\mathcal{A}$ is the value of a closed term, then the theory of $\mathcal{A}$ in that language is a Henkin set, and its term model is isomorphic to $\mathcal{A}$.

### History

Kurt Gödel proved the completeness theorem in his thesis of 1929 by a different method.
Leon Henkin published the method of witness constants and term models in 1949.
Gisbert Hasenjaeger gave a simplified form of Henkin's proof in 1953.
Henkin also used the method for the theory of types, where it gives completeness with respect to general models.

### Common errors

- Adding witnesses only for the formulas of $L$. The new constants make new formulas $\exists x \, \psi$ of $L(C)$, and these also need witnesses. The construction must list all formulas of $L(C)$, or repeat in $\omega$ stages.
- Using an old constant as a witness. The axiom $\exists x \, \psi \to \psi^x_c$ is safe only when $c$ is new for $\psi$ and for the earlier axioms. With $\Gamma = \set{\exists x \, P(x), \neg P(a)}$, the witness $a$ gives an inconsistent set.
- Using induction on subformulas for the truth lemma. The case $\forall x \, \varphi$ needs the instances $\varphi^x_t$, which are not subformulas. The induction is on the number of logical symbols, which substitution of closed terms does not change.

## Explanations

### L1 human

Suppose a list of facts says "somebody did it" but names nobody.
The Henkin construction invents a name, say "the culprit", for each such claim.
Then it settles every open question about all the named people, without making a contradiction.
Finally, it lets the names themselves be the people.
A list of facts treated this way describes a small world in which all the facts are true.

### L2 human

We build a Henkin set for $\Gamma = \set{\exists x \, P(x), \exists x \, \neg P(x)}$, where $L$ has one unary relation symbol $P$.

1. In the abbreviation $\exists x = \neg \forall x \neg$, the two sentences are $\neg \forall x \, \neg P(x)$ and $\neg \forall x \, \neg \neg P(x)$.
2. Their witness axioms, with new constants $c_0, c_1$, give $\neg \neg P(c_0)$ and $\neg \neg \neg P(c_1)$. With Rule T, any extension that contains $\Gamma$ and these axioms derives $P(c_0)$ and $\neg P(c_1)$.
3. Lindenbaum's lemma gives a maximal consistent $\Delta$. It cannot contain $c_0 = c_1$, since axiom group 6 with $P(c_0)$ would give $P(c_1)$. So $\neg (c_0 = c_1) \in \Delta$.
4. The term model has the classes $[c_0] \ne [c_1]$, with $[c_0] \in P^{\mathcal{M}}$ and $[c_1] \notin P^{\mathcal{M}}$. Both sentences of $\Gamma$ hold in it.
5. The other constants $c_2, c_3, \dots$ go to classes that $\Delta$ decides. For example, if $\Delta$ contains $\forall x \, \forall y \, \forall z \, (x = y \lor x = z \lor y = z)$, then the model has exactly two elements.

The typical use is to prove that a consistent set has a model, and to bound the size of the model by the size of the language.
The trap is step 5: the size and shape of the term model depend on the choices made by Lindenbaum's lemma, so the model is not unique.

### L3 human

The Henkin construction meets countably many requirements, one for each formula, and each requirement is met by one finite extension.
In this form it is a forcing argument, or a Baire category argument in the Stone space of the theory.
The Rasiowa and Sikorski form makes this explicit: one needs an ultrafilter of the [[Lindenbaum-Tarski algebra|QC9M3Q8B8Q]] that respects countably many infinite joins.
The same scheme, with more requirements, proves the omitting types theorem.
The construction is effective relative to a consistency test: for a decidable consistent $\Gamma$ in a countable language, the halting problem computes a Henkin set, and so a model.
See also the essay [[completeness versus incompleteness|28AX3A4N86]].
