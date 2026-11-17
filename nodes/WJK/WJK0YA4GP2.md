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

Let $T$ be a theory in the language of arithmetic that contains [[Peano arithmetic|HACXBCM7SS]] and has a decidable set of axioms, and let $\mathrm{Prov}_T$ be its standard [[provability predicate|NB2BCZR40F]].
An arithmetical realization $*$ assigns to each propositional variable $p$ a sentence $p^*$ of arithmetic, and extends to all modal formulas by $\bot^* = (0 = S0)$, $(\varphi \to \psi)^* = (\varphi^* \to \psi^*)$ and $(\square \varphi)^* = \mathrm{Prov}_T(\ulcorner \varphi^* \urcorner)$, with $\ulcorner \cdot \urcorner$ a [[Gödel numbering|MFJXPAF0R0]].
The provability logic of $T$ is the set $\mathrm{PL}(T)$ of the modal formulas $\varphi$ such that $T \vdash \varphi^*$ for every realization $*$.
Its main system is $\mathsf{GL}$, the normal [[modal logic|C3RZY20ETK]] with [[Löb's axiom|QQ6PZFGGB3]] $\square(\square p \to p) \to \square p$, given in the [[definition of provability logic|61THBNS8WE]].
By [[Solovay's arithmetical completeness theorem|1ZRWVDYPX0]], $\mathrm{PL}(\mathsf{PA}) = \mathsf{GL}$.
The subject matters because it turns every question about the general laws of provability into a question about finite frames, which a computer can decide.

## Motivation

Gödel's second incompleteness theorem and Löb's theorem use only a few properties of the provability predicate.
These are the [[derivability conditions|F6H4STF9RG]] D1 to D3 and the diagonal lemma.
In modal notation, D2 is the axiom $\square(p \to q) \to (\square p \to \square q)$ and D3 is $\square p \to \square \square p$.
So it is natural to ask which modal formulas are laws of provability, for every choice of the sentences.
Löb's theorem gives one law that is not in the usual modal systems, and Solovay showed that no other new law is needed.

## Notation

1. We write $\square \varphi$ for "$\varphi$ is provable in $T$" and $\lozenge \varphi := \neg \square \neg \varphi$ for "$\varphi$ is consistent with $T$".
2. The system $\mathsf{GL}$ (for Gödel and Löb) is also called $\mathsf{L}$ or $\mathsf{K4W}$, where $\mathrm{W}$ stands for well-foundedness.
3. A realization is also called an arithmetical interpretation or a translation, and it is written $*$, $f$ or $\sigma$.
4. The logic of the sentences true in $\N$ under every realization is written $\mathsf{GLS}$, with $\mathrm{S}$ for Solovay.

## Remarks

### Examples

1. $\mathsf{GL} \vdash \square p \to \square \square p$ ([[Löb's axiom in provability logic|QQ6PZFGGB3]]). Its realizations are instances of the third derivability condition.
2. [[The formalized second incompleteness theorem in GL|3K967QR766]]: $\mathsf{GL} \vdash \neg \square \bot \to \neg \square \neg \square \bot$, which reads "if $T$ is consistent, then $T$ does not prove its own consistency".
3. [[Henkin's sentence in GL|HJD67H8CXN]]: $\mathsf{GL} \vdash \square(p \leftrightarrow \square p) \to \square p$, so every sentence equivalent to its own provability is provable.
4. The Gödel sentence: by the [[de Jongh-Sambin fixed-point theorem|TDDX1NHG8D]], $\mathsf{GL} \vdash (p \leftrightarrow \neg \square p) \wedge \square(p \leftrightarrow \neg \square p) \to (p \leftrightarrow \neg \square \bot)$. So every Gödel sentence of $T$ is equivalent in $T$ to the consistency of $T$.
5. Other theories: Solovay's theorem holds for every $\Sigma_1$-sound theory with decidable axioms that contains $\mathsf{PA}$. The proof also works for set theory $\mathsf{ZF}$, through its interpretation of arithmetic, when $\mathsf{ZF}$ is $\Sigma_1$-sound.

### Non-examples

1. [[S4 is not the provability logic of PA|AXB7DEGR2D]]: the reflection axiom $\square p \to p$ fails, because its instance $\square \bot \to \bot$ is realized as the consistency of $\mathsf{PA}$.
2. For $T = \mathsf{PA} + \neg \mathrm{Con}(\mathsf{PA})$, the formula $\square \bot$ is in $\mathrm{PL}(T)$ but not in $\mathsf{GL}$. Here $T$ is consistent, but it is not $\Sigma_1$-sound, so the condition of Solovay's theorem fails.
3. Replace $\mathrm{Prov}_T$ by the [[Rosser provability predicate|Z0H1KA8ZHT]]. Then $T$ proves the realization of $\neg \square \bot$, which is not in $\mathsf{GL}$. The standard predicate is needed.

### Basic properties

1. Arithmetical soundness: $\mathsf{GL} \subseteq \mathrm{PL}(T)$ for every $T$ as in the Summary. This is the first half of [[Solovay's theorem|1ZRWVDYPX0]], and it uses D1 to D3 and the formalized [[Löb's theorem|3HD30YG3DG]].
2. $\mathsf{GL}$ proves axiom 4 and Löb's rule, and it does not prove $\square p \to p$; see [[Löb's axiom in provability logic|QQ6PZFGGB3]].
3. $\mathsf{GL}$ is the logic of the finite transitive irreflexive frames, so it is decidable; see the [[Kripke completeness of GL|1DMFNR7FZT]].
4. Every formula $A(p)$ in which $p$ occurs only under $\square$ has a unique fixed point in $\mathsf{GL}$; see the [[de Jongh-Sambin fixed-point theorem|TDDX1NHG8D]].
5. The provability logic of $T$ depends on $T$ only through $\Sigma_1$-soundness: it is $\mathsf{GL}$ for every $\Sigma_1$-sound $T$ as above.

### History

Gödel wrote the first paper on a provability reading of modal logic in 1933, where he translated intuitionistic propositional logic into the modal logic $\mathsf{S4}$.
Löb proved his theorem in 1955, and its formalized form is the axiom of $\mathsf{GL}$.
Solovay proved in 1976 that $\mathsf{GL}$ is the provability logic of $\mathsf{PA}$, in "Provability interpretations of modal logic", Israel Journal of Mathematics 25.
George Boolos led the field until his death in 1996, and his book "The Logic of Provability" is the standard text.

### Common errors

1. Reading $\square p \to p$ as a law of provability. It is true in $\N$ for a sound theory, but the theory cannot prove it, by Löb's theorem.
2. Confusing $\mathrm{PL}(T)$ with the set of formulas whose realizations are true. The second set is the larger logic $\mathsf{GLS}$, which contains $\neg \square \bot$.
3. Forgetting that $\square$ refers to one fixed theory $T$. The formula $\square \varphi \to \square \square \varphi$ is about $T$ proving facts about $T$, not about a stronger metatheory.

## Explanations

### L1 human

Provability logic is the logic of the phrase "it can be proved that".
We write $\square p$ for "$p$ can be proved" in a fixed system of axioms for the whole numbers.
Some laws hold for every statement $p$, for example "if $p$ can be proved, then it can be proved that $p$ can be proved".
The law "if $p$ can be proved, then $p$" is true for a correct system, but the system itself cannot prove it.
For instance, with $p$ the false statement $0 = 1$, that law says "the system is consistent", and Gödel showed that a consistent system cannot prove this about itself.

### L2 human

We read one realization of the theorem $\square p \to \square \square p$ of $\mathsf{GL}$.

1. By [[Löb's axiom in provability logic|QQ6PZFGGB3]], part 1, $\mathsf{K} + \mathrm{L} \vdash \square p \to \square \square p$.
2. Take the realization with $p^* = \mathrm{Con}(\mathsf{PA})$, the [[consistency statement|4NBAX3VRQ7]].
3. The realized formula is $\mathrm{Prov}(\ulcorner \mathrm{Con}(\mathsf{PA}) \urcorner) \to \mathrm{Prov}(\ulcorner \mathrm{Prov}(\ulcorner \mathrm{Con}(\mathsf{PA}) \urcorner) \urcorner)$.
4. By arithmetical soundness, $\mathsf{PA}$ proves this sentence.

The typical use: to prove a scheme about provability in $\mathsf{PA}$, prove the modal formula in $\mathsf{GL}$, or refute it on a finite frame.
A trap: a formula valid in $\mathsf{GLS}$, such as $\neg \square \bot$, is true but not provable in $\mathsf{PA}$.

### L3 human

Provability logic is the modal theory of the provability operator of one theory, in the same way as group theory is the theory of one operation.
The answer $\mathsf{GL}$ is stable: it is the same for all $\Sigma_1$-sound theories that contain enough arithmetic, and its algebraic models are the [[Boolean algebras|0XADJKM699]] with a Löb operator, the [[Magari algebras|YTA4C8QCB0]].
Extensions describe other notions: [[Grzegorczyk logic|2Q8E4GQF3B]] for "true and provable", [[Japaridze's polymodal logic GLP|3EDRQJJHMT]] for a hierarchy of provability notions, [[interpretability logic|BGKZTSQN3W]] for interpretability between theories, and [[quantified provability logic|5K9J8R8SCP]] for formulas with quantifiers, where the answer is no longer recursively axiomatizable.
The connection with the [[provability predicate|NB2BCZR40F]] and [[reflection principles|NB485KFXKV]] of sub-area 11 is direct: each reflection scheme is a set of realizations of $\square p \to p$.
