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

Start with $\mathsf{PA}$.
It does not prove its own consistency, so add $\mathrm{Con}(\mathsf{PA})$ as an axiom, then the consistency of the new theory, and so on.
After all finite steps take the union, and go on into the transfinite.
A progression of theories is this process made exact, with ordinal notations as the names of the stages.

Exactly: fix a base theory $T_0$ of arithmetic with computably enumerable axioms, such as $\mathsf{PA}$, and an effective operation $T \mapsto T^{+}$ that adds a consistency or [[reflection principle|NB485KFXKV]] for $T$, for example $T^{+} = T + \mathrm{Con}(T)$ or $T^{+} = T + \mathrm{RFN}(T)$.
A recursive progression based on $T_0$ and ${}^{+}$ is a family $(T_a)$ of [[recursively axiomatizable theories|3ANXZC3BEG]], indexed by the notations $a$ of [[Kleene's O|WHAP0K600D]], with
$$T_1 = T_0, \qquad T_{2^a} = (T_a)^{+}, \qquad T_{3 \cdot 5^e} = \bigcup_n T_{\varphi_e(n)}.$$
The family is defined by effective transfinite recursion, so that an index for the axioms of $T_a$ is computed from $a$.

## Motivation

By [[Gödel's second incompleteness theorem|4PZM5GJTR5]], a consistent theory $T \supseteq \mathsf{PA}$ with c.e. axioms does not prove $\mathrm{Con}(T)$.
If $T$ is sound, $\mathrm{Con}(T)$ is true, so $T + \mathrm{Con}(T)$ is sound and strictly stronger.
Each step adds a true sentence that the previous theory misses, and the natural question is whether the iteration, carried far enough, reaches every true sentence.

To continue past a limit in an effective way, the process needs a name for the limit: a computable sequence of earlier stages whose union is the limit stage.
So the stages are indexed by notations for [[ordinals|0YSCSX5YZC]], not by ordinals, and the outcome can depend on the notation.
This dependence is the main lesson of the subject.

## Notation

In Kleene's $\mathcal{O}$, the number $1$ denotes $0$, and if $a$ denotes $\alpha$, then $2^a$ denotes $\alpha + 1$.
If $\varphi_e$ is a total computable function whose values denote a strictly increasing sequence, then $3 \cdot 5^e$ denotes its limit.
We write $\lvert a \rvert$ for the ordinal that $a$ denotes, and $\omega_1^{\mathrm{CK}}$, the Church-Kleene ordinal, is the least ordinal with no notation.
A progression is invariant if $\lvert a \rvert = \lvert b \rvert$ implies that $T_a$ and $T_b$ have the same theorems.
A path through $\mathcal{O}$ is a subset that is linearly ordered by $<_{\mathcal{O}}$ and closed downward.
Turing wrote "ordinal logic" and worked with the $\lambda$-calculus; Feferman recast the subject with recursive functions and called it a "recursive progression".

## Remarks

### The first stages

The finite stages of the consistency progression over $\mathsf{PA}$ are
$$\mathsf{PA}, \quad \mathsf{PA} + \mathrm{Con}(\mathsf{PA}), \quad (\mathsf{PA} + \mathrm{Con}(\mathsf{PA})) + \mathrm{Con}(\mathsf{PA} + \mathrm{Con}(\mathsf{PA})), \quad \ldots$$
at the notations $1, 2, 4, 16, 65536, \ldots$, each $2$ to the power of the one before.
Each stage is sound and strictly stronger than the one before; [[the finite stages of the consistency progression|7SRG8BJRJV]] checks this.
Over $\mathsf{PRA}$ with uniform reflection, the very first step already gives a theory with the same theorems as $\mathsf{PA}$, by the Kreisel-Lévy theorem; see [[uniform reflection over PRA|DGQRT1BVJ3]].

### What the progressions reach

Turing proved a completeness theorem for $\Pi_1$ sentences.
For each true $\Pi_1$ sentence $\pi$ there is a notation $a$ with $\lvert a \rvert = \omega + 1$ such that the consistency progression over $\mathsf{PA}$ proves $\pi$ at stage $a$.
The construction is worked out in [[Turing's completeness construction|SKNW7G0JG2]].

Feferman (1962) showed that the progression based on uniform reflection is complete for all true arithmetic sentences.
He also showed that a single path through $\mathcal{O}$ suffices for this.
On the other side, he showed that the consistency progression is not complete for true $\Pi_2$ sentences.

### Why notations matter

Turing's theorem already shows that the consistency progression is not invariant.
Every true $\Pi_1$ sentence is proved at some stage with ordinal $\omega + 1$.
If all these stages had the same theorems, one sound theory with c.e. theorems would prove every true $\Pi_1$ sentence, and that is impossible, since the set of true $\Pi_1$ sentences is not c.e.
Feferman and Spector (1962) showed that even for uniform reflection some paths through $\mathcal{O}$ miss a true $\Pi_1$ sentence.

The completeness theorems also give no method to decide truth.
The set $\mathcal{O}$ is not arithmetical, so knowing that a number is a notation can be as hard as knowing the truth that its stage proves.

### What a progression is not

Iterating $T \mapsto T + \neg \mathrm{Con}(T)$ is effective, but the added sentences are false and the stages are unsound; see [[iterating the negation of consistency|F8C9XXMBRW]].
A family indexed by the ordinals below $\omega_1^{\mathrm{CK}}$ themselves is not a recursive progression either.
At a limit it needs a computable sequence of earlier stages, and an ordinal alone does not give one.
True arithmetic is not a stage of any progression, because every $T_a$ has c.e. axioms and true arithmetic does not.

### The rules you can use

If $T_0$ is sound, then $T_a$ is sound for every $a \in \mathcal{O}$.
The proof is by [[transfinite induction|0ZHQMQ2C1N]] on $\lvert a \rvert$: the consistency or reflection statement of a sound theory is true, and a union of sound theories is sound.
For a number $a \notin \mathcal{O}$ the recursion still defines a theory $T_a$, and it may be inconsistent; Turing's construction uses exactly this.

### Watch out

Do not think that Turing's theorem gives a method to prove all true $\Pi_1$ sentences.
It moves the difficulty into the question whether a given number is a notation in $\mathcal{O}$, which is at least as hard.
Do not identify stages with ordinals either.
Two notations for $\omega + 1$ can give theories with different theorems, as the argument above shows.

### History

Turing introduced ordinal logics in his Princeton doctoral thesis, written under Church and published in 1939 as "Systems of logic based on ordinals".
Feferman took up the problems that Turing left open in "Transfinite recursive progressions of axiomatic theories" (1962), and with Spector in a second paper of 1962 on incompleteness along paths.
Later, autonomous progressions were used by Feferman and by Schütte to analyze predicative mathematics, and their limit is the ordinal $\Gamma_0$.

### Try it

What is the notation of stage $3$ in the consistency progression, and which theory sits there?
The notation is $2^4 = 16$, and the theory is $T_4 + \mathrm{Con}(T_4)$, where $T_4$ is the stage at notation $4$.

Why is every stage $T_a$ with $a \in \mathcal{O}$ consistent, if the base is $\mathsf{PA}$?
Because $\mathsf{PA}$ is sound, soundness passes to every stage, and a sound theory does not prove $0 = 1$.

## Explanations

### L1 human

Gödel showed that a good list of axioms for arithmetic cannot prove its own consistency.
So we can add "the list is consistent" as a new axiom and get a stronger list.
The new list has the same problem, so we add its consistency too, and so on.
After infinitely many steps we put all the lists together and go on, counting the steps with infinite ordinals.
Turing and Feferman asked whether this process, carried far enough, proves every true statement about numbers.

### L2 human

Here are the first stages of the consistency progression over $\mathsf{PA}$, with their notations.
Stage $0$ has notation $1$ and theory $T_1 = \mathsf{PA}$.
Stage $1$ has notation $2$ and theory $T_2 = \mathsf{PA} + \mathrm{Con}(\mathsf{PA})$.
Stage $2$ has notation $4 = 2^2$ and theory $T_4 = T_2 + \mathrm{Con}(T_2)$.
For stage $\omega$, choose a computable $\varphi_e$ that lists $1, 2, 4, 16, \ldots$; then $T_{3 \cdot 5^e}$ is the union of the finite stages.
Stage $\omega + 1$ is $T_{3 \cdot 5^e} + \mathrm{Con}(T_{3 \cdot 5^e})$.
The typical use is to measure a theory by the stage that has the same $\Pi_1$ theorems.
Watch out: another index $e'$ for the same list gives another notation for $\omega$, and $\mathrm{Con}$ at stage $\omega + 1$ is then written with another axiom formula, which can change its strength.

### L3 human

Progressions tie incompleteness to the theory of constructive ordinals.
Completeness theorems hold because membership in $\mathcal{O}$ is $\Pi^1_1$-complete, so a notation can hide arbitrary arithmetic information.
Turing's proof uses [[Kleene's recursion theorem|F3Z30M606H]] to build a notation that refers to itself.
Feferman's uses the same idea with uniform reflection, which acts inside the theory like the $\omega$-rule.
Autonomous progressions remove the hidden information by asking for a proof that each notation used is well founded.
Iterated reflection along natural well-orderings underlies the approach to [[ordinal analysis|XTTKZTYDSD]] by iterated consistency and the reflection algebras of [[provability logic|WJK0YA4GP2]].
