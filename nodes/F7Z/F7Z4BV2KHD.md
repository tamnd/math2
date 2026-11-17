---
tag: F7Z4BV2KHD
kind: concept
name: Turing and Feferman progressions
msc: ["03F15", "03F40", "03F30"]
topics: [HXHHWY3328]
audience: research
uses: [NB485KFXKV, 4NBAX3VRQ7, 4PZM5GJTR5, WHAP0K600D, 0YSCSX5YZC, 3ANXZC3BEG, F3Z30M606H, 0ZHQMQ2C1N]
sources:
  - url: https://en.wikipedia.org/wiki/Systems_of_Logic_Based_on_Ordinals
    locator: lead section
  - url: https://en.wikipedia.org/wiki/Ordinal_logic
    locator: lead section
  - url: https://en.wikipedia.org/wiki/Reflection_principle
    locator: For arithmetic
---

## Summary

Fix a base theory $T_0$ of arithmetic with a computably enumerable set of axioms, such as $\mathsf{PA}$ or $\mathsf{PRA}$, and an effective operation $T \mapsto T^{+}$ that adds to $T$ a consistency or [[reflection principle|NB485KFXKV]] for $T$, for example $T^{+} = T + \mathrm{Con}(T)$ or $T^{+} = T + \mathrm{RFN}(T)$.
A recursive progression of theories based on $T_0$ and ${}^{+}$ is a family $(T_a)$ of [[recursively axiomatizable theories|3ANXZC3BEG]], indexed by the notations $a$ of [[Kleene's O|WHAP0K600D]], with $T_1 = T_0$, $T_{2^a} = (T_a)^{+}$, and $T_{3 \cdot 5^e} = \bigcup_n T_{\varphi_e(n)}$.
The family is defined by effective transfinite recursion, so that a c.e. index of the axioms of $T_a$ is computed from $a$.
Turing (1939) introduced such families as "ordinal logics", with ${}^{+}$ the addition of the [[consistency statement|4NBAX3VRQ7]], and Feferman (1962) studied them under the name "transfinite recursive progressions".
They are the systematic answer to the incompleteness theorems by iteration: each step adds a true sentence that the previous theory does not prove, and the question is whether the iteration reaches every true sentence.

## Motivation

By [[Gödel's second incompleteness theorem|4PZM5GJTR5]], a consistent theory $T \supseteq \mathsf{PA}$ with c.e. axioms does not prove $\mathrm{Con}(T)$.
If $T$ is sound, $\mathrm{Con}(T)$ is true, so $T + \mathrm{Con}(T)$ is a sound and strictly stronger theory.
The same step applies again, and after the finite stages one takes the union, and continues.
To continue in an effective way past limit stages, the process needs names for the limits: a computable sequence of earlier stages whose union is the limit stage.
So the stages are indexed not by [[ordinals|0YSCSX5YZC]] but by notations for ordinals, and the outcome can depend on the notation.

## Notation

1. Kleene's $\mathcal{O}$: $1$ is the notation for $0$; if $a$ denotes $\alpha$, then $2^a$ denotes $\alpha + 1$; if $\varphi_e$ is a total computable function whose values denote a strictly increasing sequence (in the order $<_{\mathcal{O}}$), then $3 \cdot 5^e$ denotes its limit. We write $\abs{a}$ for the ordinal that $a$ denotes.
2. $\omega_1^{\mathrm{CK}}$, the Church-Kleene ordinal, is the least ordinal with no notation in $\mathcal{O}$.
3. A progression is called invariant if $\abs{a} = \abs{b}$ implies that $T_a$ and $T_b$ have the same theorems.
4. A path through $\mathcal{O}$ is a subset of $\mathcal{O}$ that is linearly ordered by $<_{\mathcal{O}}$ and closed downward. A progression along a path uses only the notations of that path.
5. Turing wrote "ordinal logic" and worked in the $\lambda$-calculus; Feferman recast the subject with recursive functions and introduced the name "recursive progression".

## Remarks

### Examples

1. The finite stages of the consistency progression over $\mathsf{PA}$ are $\mathsf{PA}$, $\mathsf{PA} + \mathrm{Con}(\mathsf{PA})$, and so on; each is strictly stronger than the one before. See [[the finite stages of the consistency progression|7SRG8BJRJV]].
2. Turing's completeness theorem: for each true $\Pi_1$ sentence $\pi$, there is a notation $a \in \mathcal{O}$ with $\abs{a} = \omega + 1$ such that the consistency progression over $\mathsf{PA}$ proves $\pi$ at stage $a$. See [[Turing's completeness construction for a Π1 sentence|SKNW7G0JG2]].
3. Over $\mathsf{PRA}$ with $T^{+} = T + \mathrm{RFN}(T)$, the first stage $T_2 = \mathsf{PRA} + \mathrm{RFN}(\mathsf{PRA})$ has the same theorems as $\mathsf{PA}$, by the Kreisel-Lévy theorem; see [[uniform reflection over PRA|DGQRT1BVJ3]].
4. Feferman's completeness theorem: for the uniform reflection progression over $\mathsf{PA}$, every true arithmetic sentence is a theorem of some $T_a$ with $a \in \mathcal{O}$.

### Non-examples

1. Iterating $T \mapsto T + \neg \mathrm{Con}(T)$ is not a progression of this kind: the step adds the negation of a consistency statement, and the stages are false in $\N$. See [[iterating the negation of consistency|F8C9XXMBRW]].
2. A family $(T_\alpha)$ indexed by the ordinals $\alpha < \omega_1^{\mathrm{CK}}$ themselves, with unions at limits, is not a recursive progression. The definition of a progression needs, at each limit, a computable sequence $\varphi_e$ of earlier stages, so that the axioms of $T_a$ are computed from $a$; an ordinal alone does not give such a sequence.
3. True arithmetic $\mathrm{Th}(\N)$ is not a stage of any progression: each $T_a$ is c.e., and $\mathrm{Th}(\N)$ is not c.e., by Tarski's and Gödel's theorems.

### Basic properties

1. If $T_0$ is sound (all axioms true in $\N$), then $T_a$ is sound for every $a \in \mathcal{O}$. The proof is by [[transfinite induction|0ZHQMQ2C1N]] on $\abs{a}$: the consistency or reflection statement for a sound theory is true, and a union of sound theories is sound.
2. For $a \notin \mathcal{O}$ the recursion still defines a theory $T_a$, and it may be inconsistent. Turing's construction uses exactly this.
3. Turing's completeness theorem for $\Pi_1$ (example 2). Turing also showed that, for a wide class of ordinal logics, completeness for $\Pi_1$ sentences and invariance cannot hold together.
4. Feferman (1962) showed that the progressions based on consistency, and even on local reflection, are not complete for true $\Pi_2$ sentences, the class that Turing had hoped to reach.
5. Feferman (1962) showed that the progression based on uniform reflection is complete for all true arithmetic sentences, and that there is a single path through $\mathcal{O}$ along which every true arithmetic sentence is provable.
6. Feferman and Spector (1962) showed that invariance fails badly, even for the uniform reflection progression: there are paths through $\mathcal{O}$ along which some true $\Pi_1$ sentence is never proved.
7. The completeness theorems do not give a way to decide truth: the set $\mathcal{O}$ is not arithmetical, so knowing that a given number $a$ is in $\mathcal{O}$ can be as hard as knowing the sentence that $T_a$ proves.

### History

Turing introduced ordinal logics in his Princeton doctoral thesis, written under Church and published in 1939 as "Systems of logic based on ordinals".
Feferman took up the problems left open by Turing in "Transfinite recursive progressions of axiomatic theories" (1962), and with Spector in a second paper of 1962 on incompleteness along paths.
Later, autonomous progressions, which may use a notation $a$ only after an earlier stage has proved that $a$ is a notation, were used by Kreisel to analyse finitist proof and by Feferman to analyse predicative proof.

### Common errors

1. A student thinks that Turing's theorem gives a method to prove all true $\Pi_1$ sentences. It moves the difficulty to the question whether a given number is a notation in $\mathcal{O}$, which is at least as hard.
2. A student identifies stages with ordinals. Two notations for the same ordinal $\omega + 1$ can give theories with different theorems; this is the failure of invariance.
3. A student thinks that every $T_a$ is consistent. This holds for $a \in \mathcal{O}$ and a sound $T_0$, but not for every number $a$ to which the recursion applies.

## Explanations

### L1 human

Gödel showed that a good list of axioms for arithmetic cannot prove its own consistency.
So we can add "the list is consistent" as a new axiom, and get a stronger list.
The new list has the same problem, so we add its consistency too, and so on, again and again.
After infinitely many steps we collect all the lists together and go on, counting the steps with infinite ordinals.
Turing and Feferman asked whether this process, carried far enough, proves every true statement about numbers.

### L2 human

We describe the first stages of the consistency progression over $\mathsf{PA}$.

1. Stage $0$ (notation $1$): $T_1 = \mathsf{PA}$.
2. Stage $1$ (notation $2$): $T_2 = \mathsf{PA} + \mathrm{Con}(\mathsf{PA})$.
3. Stage $2$ (notation $4 = 2^2$): $T_4 = T_2 + \mathrm{Con}(T_2)$.
4. Stage $\omega$: choose a computable function $\varphi_e$ that lists the notations $1, 2, 4, 16, \ldots$ of the finite stages; then $T_{3 \cdot 5^e}$ is the union of the finite stages.
5. Stage $\omega + 1$: $T_{2^{3 \cdot 5^e}} = T_{3 \cdot 5^e} + \mathrm{Con}(T_{3 \cdot 5^e})$.

The typical use is to measure a theory by the stage of a progression that has the same $\Pi_1$ theorems.
A trap is step 4: another index $e'$ gives another notation for $\omega$.
The union at $\omega$ has the same axioms, but $\mathrm{Con}$ at stage $\omega + 1$ is written with another presentation, and by Turing's construction two such stages can prove different $\Pi_1$ sentences.

### L3 human

Progressions connect incompleteness with the theory of constructive ordinals: completeness theorems hold because the question whether $a \in \mathcal{O}$ is $\Pi^1_1$-complete, so a notation can hide arbitrary arithmetic information.
Turing's proof uses [[Kleene's recursion theorem|F3Z30M606H]] to build a notation that refers to itself, and Feferman's uses the same idea with uniform reflection, which internalizes the $\omega$-rule.
Autonomous progressions remove the hidden information by asking for a proof that each notation used is well founded, and they give the characterizations of finitist and predicative mathematics; the bound of the predicative progression is the Feferman-Schütte ordinal $\Gamma_0$.
The same iteration of reflection, but along natural well-orderings, underlies the approach to [[ordinal analysis|XTTKZTYDSD]] by iterated consistency and the reflection algebras of [[provability logic|WJK0YA4GP2]].
