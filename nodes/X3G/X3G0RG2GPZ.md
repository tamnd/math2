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

A relative consistency proof shows that a theory is free of contradictions provided another theory is.
Hyperbolic geometry is the standard case.
Inside a disk of the Euclidean plane, read "line" as "chord" and give the disk a suitable notion of distance.
Then all axioms of hyperbolic geometry become theorems of Euclidean geometry.
So a contradiction in hyperbolic geometry would give a contradiction in Euclidean geometry, and hyperbolic geometry is consistent if Euclidean geometry is.

Let $S$ and $T$ be [[theories|92SWXST1ZM]], sets of sentences in first-order languages.
A *relative consistency proof* of $T$ with respect to $S$ is a proof of the implication "if $S$ is [[consistent|VM8TQ70CVJ]], then $T$ is consistent", written $\mathrm{Con}(S) \to \mathrm{Con}(T)$.
It does not claim that $S$ or $T$ is consistent; it reduces the question for $T$ to the question for $S$.
Theories $S$ and $T$ are *equiconsistent* when both implications hold.
Absolute consistency proofs are limited by the [[second incompleteness theorem|4PZM5GJTR5]], so relative ones are the main tool for comparing the strength of theories and for proving independence.

## Motivation

Mathematicians tried for two thousand years to prove the parallel postulate from Euclid's other axioms.
To show that no such proof exists, we need the consistency of geometry with the parallel postulate replaced by its negation.
Beltrami and Klein did not prove this outright; they built a model of hyperbolic geometry inside Euclidean geometry.
Set theory needs the same kind of argument.
ZF cannot prove its own consistency, but it can show that adding the axiom of choice or the continuum hypothesis creates no new contradiction.
Every independence result has this form: $T \nvdash \varphi$ follows from $\mathrm{Con}(S) \to \mathrm{Con}(T + \lnot\varphi)$ and the consistency of $S$.

## Notation

$\mathrm{Con}(S)$ denotes "$S$ is consistent", either as a statement of the metatheory or as an arithmetic sentence obtained by a [[Gödel numbering|MFJXPAF0R0]].
"$T$ is consistent relative to $S$" means $\mathrm{Con}(S) \to \mathrm{Con}(T)$.
An *interpretation* $I$ of $T$ in $S$ consists of an $L_S$-formula $\delta(x)$, the domain, and an $L_S$-formula for each symbol of $L_T$.
For an $L_T$-formula $\varphi$, the translation $\varphi^I$ replaces each symbol by its formula and restricts each quantifier to $\delta$.
The interpretation must satisfy three conditions.
First, $S \vdash \exists x\, \delta(x)$.
Second, $S \vdash \tau^I$ for each axiom $\tau$ of $T$.
Third, $S$ proves that each formula for a function symbol defines a function on $\delta$.

## Remarks

### Two methods

The first method uses models.
Suppose that every model of $S$ yields a model of $T$.
If $S$ is consistent, it has a model by [[Gödel's completeness theorem|WQ1ZE255SF]], so $T$ has a [[model|MVCH6N9SNW]] and is consistent by soundness.
This argument takes place in a set-theoretic metatheory.

The second method uses interpretations.
If $I$ interprets $T$ in $S$, then by induction on derivations, $T \vdash \varphi$ implies $S \vdash \varphi^I$.
If $T$ proves $\exists x\, (x \neq x)$, then $S$ proves $\exists x\, (\delta(x) \land x \neq x)$, so $S$ is inconsistent.
This method is a computable transformation of derivations.
So when $S$ and $T$ have decidable sets of axioms, $\mathrm{Con}(S) \to \mathrm{Con}(T)$ is provable in a weak arithmetic theory such as primitive recursive arithmetic (PRA), and the proof is finitary.

Most model constructions are uniform definitions inside the model of $S$, and then they give interpretations.
That is how the model-theoretic proofs below become finitary.

### Classical results

[[Hyperbolic geometry is consistent relative to Euclidean geometry|PVW9DJASNJ]], by the Beltrami-Klein model inside a disk of the Euclidean plane.
Euclidean geometry is consistent relative to the theory of the real numbers, by coordinates; Hilbert's *Grundlagen der Geometrie* of 1899 used a model of this kind.
[[ZFC together with GCH is consistent relative to ZF|J3F0KBH6JT]], by Gödel's interpretation of set theory in the [[constructible universe|6TF2JBTPPJ]].
$\mathsf{ZF} + \lnot\mathsf{CH}$ is consistent relative to ZF, by [[Cohen's independence proof|EMGBZ46GCD]].
The method of [[forcing|F2DTWW9HP7]] gives a syntactic relative consistency proof, although its motivating picture uses a model.

Peano arithmetic is consistent relative to ZF, because the finite von Neumann ordinals interpret PA.
The converse fails in a strong sense.
If ZF is consistent, PA does not even prove $\mathrm{Con}(\mathsf{PA}) \to \mathrm{Con}(\mathsf{ZF})$.
Otherwise ZF would prove it too, and ZF proves $\mathrm{Con}(\mathsf{PA})$, so ZF would prove $\mathrm{Con}(\mathsf{ZF})$.

### What cannot be done

There is [[no relative consistency proof of PA plus Con(PA) from PA in PRA|WF7S5N12DM]]: the second incompleteness theorem forbids it.
The same holds for ZFC plus "there is an inaccessible cardinal" relative to ZFC, with ZFC as the metatheory, if the stronger theory is consistent.
The stronger theory proves $\mathrm{Con}(\mathsf{ZFC})$, and the same argument applies.
A model of $T$ built from an assumption stronger than $\mathrm{Con}(S)$, for example from a set model of ZF, gives a weaker result: consistency relative to that stronger assumption.

### First properties

Relative consistency is transitive: from $\mathrm{Con}(R) \to \mathrm{Con}(S)$ and $\mathrm{Con}(S) \to \mathrm{Con}(T)$ follows $\mathrm{Con}(R) \to \mathrm{Con}(T)$.
If $S \subseteq T$, then $\mathrm{Con}(T) \to \mathrm{Con}(S)$ holds, since a derivation from $S$ is a derivation from $T$.
So a relative consistency proof of $T \supseteq S$ from $S$ shows equiconsistency; for example, ZF and ZFC are equiconsistent.

Independence follows from two relative consistency proofs.
If $\mathrm{Con}(S) \to \mathrm{Con}(T + \varphi)$ and $\mathrm{Con}(S) \to \mathrm{Con}(T + \lnot\varphi)$, and $S$ is consistent, then $T$ proves neither $\varphi$ nor $\lnot\varphi$.

There is also a limit.
Let $T \supseteq \mathsf{PA}$ be consistent, with a decidable set of axioms, and suppose that $T$ proves $\mathrm{Con}(S)$.
Then $T$ does not prove $\mathrm{Con}(S) \to \mathrm{Con}(T)$, since otherwise $T$ would prove $\mathrm{Con}(T)$, against the second incompleteness theorem.

### Watch out

"$T$ is consistent relative to $S$" does not say that $T$ is consistent; it is only an implication.

Keep track of the metatheory.
A model-theoretic argument in ZFC proves the implication in ZFC, and it is finitary only if the construction is an interpretation.

ZF cannot prove that a set model of ZF exists, by the second incompleteness theorem.
Gödel's $L$ is a proper class, and his argument is an interpretation, not a set model.

### History

Beltrami gave the projective model of hyperbolic geometry in 1868, and Klein extended it in 1871 using the projective metric of Cayley.
Hilbert's *Grundlagen der Geometrie* of 1899 proved the consistency of his geometric axioms relative to the arithmetic of real numbers.
Gödel proved the consistency of the axiom of choice and of the generalized continuum hypothesis relative to ZF in 1938 and 1940.
Cohen proved the consistency of their negations in 1963.

### Try it

Show that the theory of groups together with the axiom $\exists x\, (x \neq e)$ is consistent relative to Peano arithmetic.
Hint: interpret the group as the integers modulo $2$, coded by the numbers $0$ and $1$ with $\delta(x) = (x = 0 \lor x = S(0))$.

## Explanations

### L1 human

Suppose someone invents a new board game with strange rules and asks whether the rules can ever contradict each other.
Instead of checking every possible game, we can show how to play the new game with the pieces of chess, so that each move of the new game is a sequence of chess moves.
Then a contradiction in the new game would give a contradiction in chess.
We have not proved that chess is free of contradictions, but we have shown that the new game is no worse than chess.
This is a relative consistency proof.

### L2 human

We prove that the theory $T$ of an infinite set without structure is consistent relative to Peano arithmetic $S$.

1. The language of $T$ has only equality, and $T$ has the axioms $\lambda_n$, "there are at least $n$ elements", for $n = 2, 3, \ldots$.
2. Interpret $T$ in $S$ with domain $\delta(x) = (x = x)$ and equality as equality.
3. The translation of $\lambda_n$ is $\lambda_n$ itself, and PA proves it.
   The numerals $0, S(0), \ldots$ give $n$ elements, pairwise different by the axioms $S(x) \neq 0$ and $S(x) = S(y) \to x = y$.
4. So each derivation from $T$ translates into a derivation from $S$, and a contradiction in $T$ would give one in $S$.

The typical use is in independence proofs, where one interprets $T + \lnot\varphi$ in a theory believed to be consistent.
Watch out: a model for each axiom separately is not enough; the same model must satisfy all axioms of $T$ at once.

### L3 human

Interpretations order theories by consistency strength, and this order is a central subject of modern logic.
In set theory, the large cardinal axioms studied so far line up in a single scale of consistency strength, and many natural statements turn out to be equiconsistent with some level of it.
In proof theory, ordinal analysis gives relative consistency proofs of the form $\mathrm{PRA} + \mathrm{TI}(\alpha) \vdash \mathrm{Con}(T)$, as in [[Gentzen's consistency proof|QPV0HNP22S]].
Interpretability itself is studied in [[provability and interpretability logics|3E7M66WW6Q]], and the general theory of interpretations in [[interpretations and foundations|CXRQQZEKF8]].
Finitary relative consistency proofs are one part of [[Hilbert's program|P1RW6JWX73]] that survives the incompleteness theorems.
