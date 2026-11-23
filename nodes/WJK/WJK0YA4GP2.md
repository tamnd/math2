---
tag: WJK0YA4GP2
kind: concept
name: Provability logic
msc: ["03F45", "03B45"]
topics: [3E7M66WW6Q]
audience: research
specializes: [C3RZY20ETK]
uses: [C3RZY20ETK, NB2BCZR40F, F6H4STF9RG, 3HD30YG3DG, HACXBCM7SS, MFJXPAF0R0, 4PZM5GJTR5]
sources:
  - url: https://en.wikipedia.org/wiki/Provability_logic
    locator: lead section
  - url: https://en.wikipedia.org/wiki/Provability_logic
    locator: History
  - book: isbn:9780521701464
same_as:
  wikidata: Q260168
  wikipedia: Provability logic
---

## Summary

Provability logic reads the modal box $\square p$ as "$\mathsf{PA}$ proves $p$" and asks which modal formulas stay true under every such reading.
The answer is a small modal logic, $\mathsf{GL}$, so the general laws of provability can be decided by checking finite frames.

To make this exact, let $T$ be a theory in the language of arithmetic that contains [[Peano arithmetic|HACXBCM7SS]] and has a decidable set of axioms.
Let $\mathrm{Prov}_T$ be its standard [[provability predicate|NB2BCZR40F]], and let $\ulcorner \cdot \urcorner$ be a [[Gödel numbering|MFJXPAF0R0]].
An arithmetical realization $*$ assigns to each propositional variable $p$ a sentence $p^*$ of arithmetic.
It extends to all modal formulas by the following clauses:
$$\bot^* = (0 = S0), \qquad (\varphi \to \psi)^* = (\varphi^* \to \psi^*), \qquad (\square \varphi)^* = \mathrm{Prov}_T(\ulcorner \varphi^* \urcorner).$$
The provability logic of $T$ is the set $\mathrm{PL}(T)$ of the modal formulas $\varphi$ such that $T \vdash \varphi^*$ for every realization $*$.
Its main system is $\mathsf{GL}$, the normal [[modal logic|C3RZY20ETK]] with [[Löb's axiom|QQ6PZFGGB3]] $\square(\square p \to p) \to \square p$, given in the [[definition of provability logic|61THBNS8WE]].
By [[Solovay's arithmetical completeness theorem|1ZRWVDYPX0]], $\mathrm{PL}(\mathsf{PA}) = \mathsf{GL}$.

## Motivation

Gödel's second incompleteness theorem and Löb's theorem use only a few properties of the provability predicate.
These are the [[derivability conditions|F6H4STF9RG]] D1 to D3 and the diagonal lemma.
In modal notation, D2 is the axiom $\square(p \to q) \to (\square p \to \square q)$ and D3 is $\square p \to \square \square p$.
So the arguments of the incompleteness theorems are really modal arguments, and it is natural to ask which modal formulas are laws of provability for every choice of sentences.

Löb's theorem gives one law that is missing from the usual modal systems.
Solovay showed in 1976 that no further law is needed: the laws of provability in $\mathsf{PA}$ are exactly the theorems of $\mathsf{GL}$.
So a question such as "does every Gödel sentence of $\mathsf{PA}$ say the same thing?" becomes a question about a finite modal formula.
The later pages on [[Kripke completeness|1DMFNR7FZT]], [[fixed points|TDDX1NHG8D]] and [[Magari algebras|YTA4C8QCB0]] turn such questions into finite computations.

## Notation

We write $\square \varphi$ for "$\varphi$ is provable in $T$" and $\lozenge \varphi := \neg \square \neg \varphi$ for "$\varphi$ is consistent with $T$".
The system $\mathsf{GL}$, named for Gödel and Löb, is also called $\mathsf{L}$ or $\mathsf{K4W}$, where $\mathrm{W}$ stands for well-foundedness.
A realization is also called an arithmetical interpretation or a translation, and books write it $*$, $f$ or $\sigma$.
The logic of the sentences true in $\mathbb{N}$ under every realization is written $\mathsf{GLS}$, with $\mathrm{S}$ for Solovay.
Watch the theory: $\square$ always refers to one fixed theory $T$, so $\square \square p$ says that $T$ proves a fact about $T$ itself.

## Remarks

### A first law, checked by hand

Take the axiom $\square(p \to q) \to (\square p \to \square q)$ and the realization with $p^*$ the sentence $0 = 0$ and $q^*$ the sentence $1 + 1 = 2$.
The realized formula reads as follows:
$$\mathrm{Prov}(\ulcorner 0 = 0 \to 1 + 1 = 2 \urcorner) \to \big(\mathrm{Prov}(\ulcorner 0 = 0 \urcorner) \to \mathrm{Prov}(\ulcorner 1 + 1 = 2 \urcorner)\big).$$
Why does $\mathsf{PA}$ prove it?
Given a proof of the implication and a proof of $0 = 0$, write the two proofs one after the other and add one step of modus ponens.
The result is a proof of $1 + 1 = 2$, and $\mathsf{PA}$ can verify this joining of codes, which is the derivability condition D2.
Nothing in the argument used the particular sentences, so every realization of the axiom is provable.
Check: the same joining works for any $p^*$ and $q^*$, and that is what makes the formula a law of provability.

### Three theorems of GL and what they say

The [[formalized second incompleteness theorem|3K967QR766]] is the theorem $\mathsf{GL} \vdash \neg \square \bot \to \neg \square \neg \square \bot$.
It reads "if $T$ is consistent, then $T$ does not prove its own consistency", and it is the instance $p = \bot$ of Löb's axiom.
[[Henkin's sentence|HJD67H8CXN]] gives the theorem $\mathsf{GL} \vdash \square(p \leftrightarrow \square p) \to \square p$, so every sentence that says "I am provable" is provable.
The Gödel sentence fits in the same way.
By the [[de Jongh-Sambin fixed-point theorem|TDDX1NHG8D]], $\mathsf{GL}$ proves that $(p \leftrightarrow \neg \square p) \wedge \square(p \leftrightarrow \neg \square p)$ implies $p \leftrightarrow \neg \square \bot$.
So every Gödel sentence of $T$ is equivalent in $T$ to the consistency of $T$.

### What is not a law of provability

The reflection axiom $\square p \to p$ fails, and so [[S4 is not the provability logic of PA|AXB7DEGR2D]].
Its instance $\square \bot \to \bot$ is realized as the consistency of $\mathsf{PA}$, which $\mathsf{PA}$ does not prove.
The theory matters too.
For $T = \mathsf{PA} + \neg \mathrm{Con}(\mathsf{PA})$, the formula $\square \bot$ is in $\mathrm{PL}(T)$ but not in $\mathsf{GL}$.
This $T$ is consistent, but it is not $\Sigma_1$-sound, so the hypothesis of Solovay's theorem fails.
The predicate matters as well.
With the [[Rosser provability predicate|Z0H1KA8ZHT]] in place of $\mathrm{Prov}_T$, the theory $T$ proves the realization of $\neg \square \bot$, which is not in $\mathsf{GL}$.

### First properties

$\mathsf{GL}$ is arithmetically sound: $\mathsf{GL} \subseteq \mathrm{PL}(T)$ for every $T$ as in the Summary.
The reason is that D1 to D3 and the formalized [[Löb's theorem|3HD30YG3DG]] give every axiom and preserve every rule.
$\mathsf{GL}$ proves axiom 4 and Löb's rule, and it does not prove $\square p \to p$, as the page on [[Löb's axiom|QQ6PZFGGB3]] shows.
$\mathsf{GL}$ is the logic of the finite transitive irreflexive frames, so it is decidable by the [[Kripke completeness of GL|1DMFNR7FZT]].
Every formula $A(p)$ in which $p$ occurs only under $\square$ has a unique fixed point in $\mathsf{GL}$.
Finally, $\mathrm{PL}(T) = \mathsf{GL}$ for every $\Sigma_1$-sound theory $T$ as in the Summary, with set theory $\mathsf{ZF}$ included through its interpretation of arithmetic.

### Watch out

Do not read $\square p \to p$ as a law of provability.
It is true in $\mathbb{N}$ for a sound theory, but by Löb's theorem $T$ proves the instance only when $T$ proves $p$.
Do not confuse $\mathrm{PL}(T)$ with the set of formulas whose realizations are all true.
The second set is the larger logic $\mathsf{GLS}$, which contains $\neg \square \bot$, and $\neg \square \bot$ is not in $\mathsf{GL}$.

### History

Gödel wrote the first paper on a provability reading of modal logic in 1933, where he translated intuitionistic propositional logic into the modal logic $\mathsf{S4}$.
Löb proved his theorem in 1955, and its formalized form is the axiom of $\mathsf{GL}$.
Solovay proved in 1976 that $\mathsf{GL}$ is the provability logic of $\mathsf{PA}$, in "Provability interpretations of modal logic", Israel Journal of Mathematics 25.
George Boolos wrote the standard text, "The Logic of Provability", published in 1993.

### Try it

First, show that $\mathsf{GL} \vdash \square \bot \to \square p$.
The formula $\bot \to p$ is a tautology, so necessitation gives $\square(\bot \to p)$, and the axiom K then gives $\square \bot \to \square p$.

Second, is $\neg \square \bot$ in $\mathrm{PL}(\mathsf{PA})$?
No, because its realization is $\mathrm{Con}(\mathsf{PA})$, which $\mathsf{PA}$ does not prove, but it is in $\mathsf{GLS}$ because $\mathsf{PA}$ is consistent.

## Explanations

### L1 human

Provability logic is the logic of the phrase "it can be proved that".
We write $\square p$ for "$p$ can be proved" in a fixed system of axioms for the whole numbers.
Some laws hold for every statement $p$, for example "if $p$ can be proved, then it can be proved that $p$ can be proved".
The law "if $p$ can be proved, then $p$" is true for a correct system, but the system itself cannot prove it.
For $p$ the false statement $0 = 1$, that law says "the system is consistent", and Gödel showed that a consistent system cannot prove this about itself.

### L2 human

We read one theorem of $\mathsf{GL}$ in arithmetic.
The page on [[Löb's axiom|QQ6PZFGGB3]] derives $\square p \to \square \square p$ from Löb's axiom.
Take the realization with $p^* = \mathrm{Con}(\mathsf{PA})$, the [[consistency statement|4NBAX3VRQ7]].
The realized formula is the following sentence:
$$\mathrm{Prov}(\ulcorner \mathrm{Con}(\mathsf{PA}) \urcorner) \to \mathrm{Prov}(\ulcorner \mathrm{Prov}(\ulcorner \mathrm{Con}(\mathsf{PA}) \urcorner) \urcorner).$$
By arithmetical soundness, $\mathsf{PA}$ proves this sentence, and we did not have to look at a single arithmetical proof.
This is the typical use: to prove a scheme about provability in $\mathsf{PA}$, prove the modal formula in $\mathsf{GL}$, or refute it on a finite frame.

### L3 human

Provability logic is the modal theory of the provability operator of one theory, in the same way as group theory is the theory of one operation.
The answer $\mathsf{GL}$ is stable: it is the same for all $\Sigma_1$-sound theories that contain enough arithmetic.
Its algebraic models are the [[Boolean algebras|0XADJKM699]] with a Löb operator, the [[Magari algebras|YTA4C8QCB0]].
Extensions describe other notions: [[Grzegorczyk logic|2Q8E4GQF3B]] for "true and provable" and [[Japaridze's polymodal logic GLP|3EDRQJJHMT]] for a hierarchy of provability notions.
[[Interpretability logic|BGKZTSQN3W]] treats interpretability between theories, and [[quantified provability logic|5K9J8R8SCP]] adds quantifiers, where the answer is no longer recursively axiomatizable.
The link with the [[provability predicate|NB2BCZR40F]] and [[reflection principles|NB485KFXKV]] of the incompleteness sub-area is direct: each reflection scheme is a set of realizations of $\square p \to p$.
