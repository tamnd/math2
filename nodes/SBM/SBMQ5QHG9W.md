---
tag: SBMQ5QHG9W
kind: concept
name: Henkin sentence
aliases: [henkin-sentence]
msc: ["03F40"]
topics: [HXHHWY3328]
audience: grad
uses: [DKFGQTRYZE, NB2BCZR40F, 3PRW76471J, 3HD30YG3DG, MPSCREYC3M]
sources:
  - wikipedia: en:76765067@r1368301704
    locator: Glossary of logic, section H
    note: adopted
    mention: wikipedia://en/76765067#D9RC
    sections: [Summary]
  - url: https://en.wikipedia.org/wiki/Löb's_theorem
    locator: lead section
  - book: isbn:9780521857840
inventory: [2ZNFRDAF8J]
---

## Summary

A Henkin sentence is a sentence that says "I am provable".
It is the mirror image of the Gödel sentence, which says "I am not provable", and it was the puzzle that led to Löb's theorem.
For a theory $T$ with the standard [[provability predicate|NB2BCZR40F]] $\mathrm{Prov}_T$, a Henkin sentence is a [[sentence|DKFGQTRYZE]] $H$ with
$$T \vdash H \leftrightarrow \mathrm{Prov}_T(\ulcorner H \urcorner).$$
By [[Löb's theorem|3HD30YG3DG]], every Henkin sentence of a theory that contains [[Peano arithmetic|MPSCREYC3M]] is provable, and so it is true.

## Motivation

The Gödel sentence $G$ says "I am not provable", and in a consistent theory it is indeed not provable.
The Henkin sentence $H$ says "I am provable", and at first sight either answer fits.
If $H$ is provable, then what it says is true, and nothing goes wrong.
If $H$ is not provable, then it is false, and a false sentence that nobody can prove causes no contradiction either.

Henkin asked which answer is right.
Löb's theorem settles it: $H$ is provable.
The question matters because it shows that self-reference alone does not decide a sentence, and that the answer comes from the derivability conditions.
The same question returns in [[provability logic|WJK0YA4GP2]], where the fixed points of $\square$ and of $\neg \square$ can be computed.

## Notation

Write $\square \varphi$ for $\mathrm{Prov}_T(\ulcorner \varphi \urcorner)$.
Then a Henkin sentence is a fixed point of $\square$: $T \vdash H \leftrightarrow \square H$.
The [[diagonal lemma|3PRW76471J]] applied to the formula $\mathrm{Prov}_T(x)$ gives one, and every other sentence with the same property is also called a Henkin sentence.
The name depends on $T$ and on the predicate, so "the Henkin sentence of $\mathsf{PA}$" means one for the standard predicate of $\mathsf{PA}$.

## Remarks

### The diagonal Henkin sentence

The diagonal lemma applied to $\mathrm{Prov}_{\mathsf{PA}}(x)$ gives a sentence $H$ with $\mathsf{PA} \vdash H \leftrightarrow \square H$.
The direction from right to left gives $\mathsf{PA} \vdash \square H \to H$, and that is exactly the hypothesis of Löb's theorem.
So $\mathsf{PA} \vdash H$, and since $\mathbb{N}$ is a model of $\mathsf{PA}$, $H$ is true.
[[The diagonal Henkin sentence of PA is provable|Y8G800QGAZ]] writes out each step.

### A Henkin sentence without self-reference

The definition asks only for a provable biconditional, so a sentence need not mention itself to qualify.
[[The sentence 0 = 0 is a Henkin sentence|6FWPDEK05X]]: $T$ proves $0 = 0$, D1 gives $T \vdash \square (0 = 0)$, and two theorems are provably equivalent.
The same three steps work for every theorem of $T$.

### What is not a Henkin sentence

[[The Gödel sentence is not a Henkin sentence|ZWTYPDHP3S]] of a consistent $T$.
It is a fixed point of $\neg \square$, and if it were also a fixed point of $\square$, then $T$ would prove $\square G \leftrightarrow \neg \square G$ and be inconsistent.

For a consistent $T \supseteq \mathsf{PA}$, the sentence $0 = S0$ is not a Henkin sentence either.
Since $T \vdash \neg (0 = S0)$, the biconditional $(0 = S0) \leftrightarrow \square (0 = S0)$ is equivalent in $T$ to $\neg \square (0 = S0)$, which is $\mathrm{Con}(T)$, and the second incompleteness theorem says that $T$ does not prove it.

### The rules you can use

Every Henkin sentence $H$ of $T \supseteq \mathsf{PA}$ is provable, because $T \vdash \square H \to H$ and Löb's theorem applies.
Every theorem of $T$ is a Henkin sentence, by the argument for $0 = 0$.
So the Henkin sentences of $T$ are exactly its theorems, and they are all provably equivalent to $0 = 0$.

The answer depends on the predicate.
Let $P(x) := \mathrm{Prov}_T(x) \wedge \mathrm{Con}(T)$.
When $T$ is consistent, $P$ defines the same set as $\mathrm{Prov}_T$ in $\mathbb{N}$.
But a sentence $H'$ with $T \vdash H' \leftrightarrow P(\ulcorner H' \urcorner)$ is not provable, because $T \vdash H'$ would give $T \vdash \mathrm{Con}(T)$.

### History

Henkin asked in 1952 whether a sentence that asserts its own provability is provable.
Löb answered the question in 1955, in "Solution of a problem of Leon Henkin", by proving Löb's theorem.

### Watch out

Do not argue "$H$ is true because it says it is provable, and it is provable because it is true".
That reasoning is circular, and it would work just as well for the predicate $P$ above, where the answer is "not provable".
The correct argument goes through Löb's theorem, which uses the derivability conditions of the standard predicate.

### Try it

Is $\forall x \, (x + 0 = x)$ a Henkin sentence of $\mathsf{PA}$?
Yes: $\mathsf{PA}$ proves it from the axiom $x + 0 = x$, and every theorem is a Henkin sentence.

Can a consistent $T \supseteq \mathsf{PA}$ have a Henkin sentence that it refutes?
No: every Henkin sentence is provable by Löb's theorem, and a consistent theory does not both prove and refute a sentence.

## Explanations

### L1 human

Gödel built a sentence that says "I cannot be proved", and it cannot be proved.
Henkin asked about the opposite sentence, "I can be proved".
Both answers, provable or not provable, seem to fit what it says.
Löb showed that it is provable, and so what it says is true.

### L2 human

We decide the Henkin sentence $H$ of $\mathsf{PA}$ in three lines.
The diagonal lemma gives $\mathsf{PA} \vdash H \leftrightarrow \square H$.
One direction of it is $\mathsf{PA} \vdash \square H \to H$.
Löb's theorem turns this into $\mathsf{PA} \vdash H$.
The typical use is as the first application of Löb's theorem, and as a contrast to the Gödel sentence.
Watch out: Löb's theorem needs the standard predicate, and for other formulas that define provability the answer can change.

### L3 human

In [[provability logic|WJK0YA4GP2]], the fixed point theorem of $\mathsf{GL}$ says that the equation $p \leftrightarrow \square p$ has the unique solution $\top$ up to provable equivalence.
The equation $p \leftrightarrow \neg \square p$ has the unique solution $\neg \square \bot$, which matches the equivalence of the Gödel sentence with $\mathrm{Con}(T)$.
Henkin sentences show in the simplest case that fixed points of modal formulas are determined up to equivalence, and that is the content of the de Jongh and Sambin fixed point theorem.
