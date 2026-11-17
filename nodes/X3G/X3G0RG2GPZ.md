---
tag: X3G0RG2GPZ
kind: concept
name: Relative consistency proof
aliases: [relative-consistency-proof, equiconsistency, consistency-relative-to]
msc: ["03F25", "03E35"]
topics: [H8QZY0RZXZ]
audience: grad
uses: [VM8TQ70CVJ, 92SWXST1ZM, MVCH6N9SNW, WQ1ZE255SF, MFJXPAF0R0]
sources:
  - wikipedia: en:76765067@r1368301704
    locator: Glossary of logic, section R
    note: adopted
    mention: wikipedia://en/76765067#USYQ
    sections: [Summary]
  - url: https://en.wikipedia.org/wiki/Equiconsistency
    locator: lead section
  - url: https://en.wikipedia.org/wiki/Consistency
    locator: lead section
  - book: isbn:9780521857840
  - book: isbn:9780122384523
inventory: [S360P2MY5Y]
---

## Summary

Let $S$ and $T$ be [[theories|92SWXST1ZM]], sets of sentences in first-order languages.
A *relative consistency proof* of $T$ with respect to $S$ is a proof of the implication "if $S$ is [[consistent|VM8TQ70CVJ]], then $T$ is consistent", written $\mathrm{Con}(S) \to \mathrm{Con}(T)$.
It does not claim that $S$ or $T$ is consistent; it reduces the question for $T$ to the question for $S$.
The two standard methods are models, "from a model of $S$ build a model of $T$", and interpretations, "translate each proof in $T$ into a proof in $S$".
When the translation is computable, the implication is provable in a weak arithmetic theory such as primitive recursive arithmetic (PRA), and then the proof is finitary.
Theories $S$ and $T$ are *equiconsistent* when both implications hold.
Relative consistency proofs matter because absolute consistency proofs are limited by the [[second incompleteness theorem|X9WYNYE29C]], while relative ones are the main tool for comparing the strength of theories and for independence results.

## Motivation

The parallel postulate resisted proof for two thousand years, and a proof that it does not follow from the other axioms needs the consistency of geometry without it.
Beltrami and Klein did not prove that hyperbolic geometry is consistent outright; they built a model of it inside Euclidean geometry.
So hyperbolic geometry is consistent if Euclidean geometry is.
Set theory needs the same kind of argument: ZF cannot prove its own consistency, but it can show that adding the axiom of choice or the continuum hypothesis creates no new contradiction.
Every independence result has this form: $T \nvdash \varphi$ follows from $\mathrm{Con}(S) \to \mathrm{Con}(T + \lnot\varphi)$ and the consistency of $S$.

## Notation

$\mathrm{Con}(S)$ denotes "S is consistent", either as a statement of the metatheory or as an arithmetic sentence obtained by a [[Gödel numbering|MFJXPAF0R0]].
"$T$ is consistent relative to $S$" and "$S$ proves the consistency of $T$ relatively" both mean $\mathrm{Con}(S) \to \mathrm{Con}(T)$.
An *interpretation* $I$ of $T$ in $S$ consists of an $L_S$-formula $\delta(x)$, the domain, and an $L_S$-formula for each symbol of $L_T$.
For an $L_T$-formula $\varphi$, the translation $\varphi^I$ replaces each symbol by its formula and restricts each quantifier to $\delta$.
The interpretation is required to satisfy $S \vdash \exists x \, \delta(x)$, $S \vdash \tau^I$ for each axiom $\tau$ of $T$, and $S \vdash$ "each function formula defines a function on $\delta$".

## Remarks

### The two methods

- By models. If every model of $S$ yields a model of $T$, then a consistent $S$ has a model, by [[Gödel's completeness theorem|WQ1ZE255SF]], so $T$ has a [[model|MVCH6N9SNW]] and is consistent by soundness. The argument takes place in a set-theoretic metatheory.
- By interpretations. If $I$ interprets $T$ in $S$, then by induction on derivations, $T \vdash \varphi$ implies $S \vdash \varphi^I$. If $T$ proves $\exists x \, (x \neq x)$, then $S$ proves $\exists x \, (\delta(x) \land x \neq x)$, so $S$ is inconsistent.
- The second method is a computable transformation of derivations, so the statement $\mathrm{Con}(S) \to \mathrm{Con}(T)$ is provable in PRA when $S$ and $T$ are recursively axiomatized and the proofs of the axioms $\tau^I$ are given by a computable list.
- Most model constructions are uniform definitions inside the model of $S$, and then they give interpretations; that is how the model-theoretic proofs below become finitary.

### Examples

- [[Hyperbolic geometry is consistent relative to Euclidean geometry|~caf25e34]], by the Beltrami-Klein model inside a disk of the Euclidean plane.
- [[ZFC together with GCH is consistent relative to ZF|~4a83d07d]], by Gödel's interpretation of set theory in the [[constructible universe|6TF2JBTPPJ]].
- Euclidean geometry is consistent relative to the theory of the real numbers, by coordinates. Hilbert's *Grundlagen der Geometrie* of 1899 used a model of this kind.
- Peano arithmetic is consistent relative to ZF, because the finite von Neumann ordinals interpret PA. If ZF is consistent, PA does not prove $\mathrm{Con}(\mathsf{PA}) \to \mathrm{Con}(\mathsf{ZF})$, because ZF proves $\mathrm{Con}(\mathsf{PA})$.
- $\mathsf{ZF} + \lnot\mathsf{CH}$ is consistent relative to ZF, by [[Cohen's independence proof|EMGBZ46GCD]]. The method of [[forcing|F2DTWW9HP7]] gives a syntactic relative consistency proof, although its motivating picture uses a model.

### Non-examples

- [[A relative consistency proof of PA plus Con(PA) from PA in PRA|~d5c2d3ad]] does not exist: the second incompleteness theorem forbids it.
- ZFC plus "there is an inaccessible cardinal" is not provably consistent relative to ZFC in ZFC, if it is consistent. The stronger theory proves $\mathrm{Con}(\mathsf{ZFC})$, and the same argument applies.
- A model of $T$ that is built from an assumption stronger than $\mathrm{Con}(S)$, for example from the existence of a transitive set model of ZF, gives a weaker result: consistency relative to that stronger assumption.

### Basic properties

- Relative consistency is transitive: from $\mathrm{Con}(R) \to \mathrm{Con}(S)$ and $\mathrm{Con}(S) \to \mathrm{Con}(T)$ follows $\mathrm{Con}(R) \to \mathrm{Con}(T)$.
- If $S \subseteq T$, then $\mathrm{Con}(T) \to \mathrm{Con}(S)$ holds, since a derivation from $S$ is a derivation from $T$. So a relative consistency proof of $T$ from $S$ for $T \supseteq S$ shows equiconsistency; ZF and ZFC are equiconsistent.
- Independence: if $\mathrm{Con}(S) \to \mathrm{Con}(T + \varphi)$ and $\mathrm{Con}(S) \to \mathrm{Con}(T + \lnot\varphi)$, and $S$ is consistent, then $T$ proves neither $\varphi$ nor $\lnot\varphi$.
- Limit: if $T \supseteq \mathsf{PA}$ is consistent, recursively axiomatized and proves $\mathrm{Con}(S)$, then $T$ does not prove $\mathrm{Con}(S) \to \mathrm{Con}(T)$; otherwise $T$ would prove $\mathrm{Con}(T)$, against the second incompleteness theorem.

### History

Beltrami gave the projective model of hyperbolic geometry in 1868, and Klein extended it in 1871 using the projective metric of Cayley.
Hilbert's *Grundlagen der Geometrie* of 1899 proved the consistency of his geometric axioms relative to the arithmetic of real numbers.
Gödel proved the consistency of the axiom of choice and of the generalized continuum hypothesis relative to ZF in 1938 and 1940, and Cohen proved the consistency of their negations in 1963.

### Common errors

- Reading "$T$ is consistent relative to $S$" as "$T$ is consistent". The statement is only an implication.
- Forgetting the metatheory. A model-theoretic argument in ZFC proves the implication in ZFC, and it is finitary only if the construction is an interpretation.
- Building a model of ZF "inside ZF" as a set. ZF cannot prove that a set model of ZF exists, by the second incompleteness theorem; Gödel's $L$ is a proper class, and the argument is an interpretation.

## Explanations

### L1 human

Suppose someone invents a new board game with strange rules and asks whether the rules can ever contradict each other.
Instead of checking every possible game, we can show how to play the new game with the pieces of chess, so that each move of the new game is a sequence of chess moves.
Then a contradiction in the new game would give a contradiction in chess.
We have not proved that chess is free of contradictions, but we have shown that the new game is no worse than chess.
This is a relative consistency proof.

### L2 human

We prove that the theory $T$ of an infinite set without structure is consistent relative to Peano arithmetic $S$.

1. The language of $T$ has only equality, and $T$ has the axioms $\lambda_n$: "there are at least $n$ elements", for $n = 2, 3, \ldots$.
2. Interpret $T$ in $S$ with domain $\delta(x) = (x = x)$ and equality as equality.
3. The translation of $\lambda_n$ is $\lambda_n$ itself, and PA proves it: the numerals $0, S(0), \ldots$ give $n$ elements that are pairwise different by the axioms $S(x) \neq 0$ and $S(x) = S(y) \to x = y$.
4. So each derivation from $T$ translates into a derivation from $S$, and a contradiction in $T$ would give one in $S$.

The typical use is in independence proofs, where one interprets $T + \lnot\varphi$ in a theory believed to be consistent.
A trap is to give a model of each axiom separately; the same model must satisfy all axioms of $T$ at once.

### L3 human

Interpretations order theories by consistency strength, and this order is the subject of much of modern logic.
In set theory, large cardinal axioms form a linear scale of consistency strength, and many natural statements are found to be equiconsistent with some level of it.
In proof theory, ordinal analysis gives relative consistency proofs of the form $\mathrm{PRA} + \mathrm{TI}(\alpha) \vdash \mathrm{Con}(T)$, as in [[Gentzen's consistency proof|QPV0HNP22S]].
Interpretability itself is studied in [[provability and interpretability logics|3E7M66WW6Q]], and the general theory of interpretations in [[interpretations and foundations|CXRQQZEKF8]].
Finitary relative consistency proofs are one part of [[Hilbert's program|P1RW6JWX73]] that survives the incompleteness theorems.
