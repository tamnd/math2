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

A sentence that asserts its own provability, possibly by applying the provability predicate to itself.
For a theory $T$ with the standard [[provability predicate|NB2BCZR40F]] $\mathrm{Prov}_T$, a Henkin sentence is a [[sentence|DKFGQTRYZE]] $H$ with $T \vdash H \leftrightarrow \mathrm{Prov}_T(\ulcorner H \urcorner)$.
By [[Löb's theorem|3HD30YG3DG]], every Henkin sentence of a theory that contains [[Peano arithmetic|MPSCREYC3M]] is provable.

## Motivation

The Gödel sentence says "I am not provable", and it is unprovable in a consistent theory.
The Henkin sentence says "I am provable", and its claim is consistent with both answers: it could be true and provable, or false and unprovable.
Henkin asked which answer is right, and Löb's theorem settles it: the sentence is provable.

## Notation

Write $\square \varphi$ for $\mathrm{Prov}_T(\ulcorner \varphi \urcorner)$.
A Henkin sentence is a fixed point of $\square$: $T \vdash H \leftrightarrow \square H$.
The [[diagonal lemma|3PRW76471J]] applied to $\mathrm{Prov}_T(x)$ gives one, and any other sentence with the same property is also called a Henkin sentence.

## Remarks

### Examples

1. [[The diagonal Henkin sentence of PA is provable|~2f35c0c4]]: the sentence from the diagonal lemma, and its proof by Löb's theorem.
2. [[The sentence 0 = 0 is a Henkin sentence|~c5fb2860]]: every theorem of $T$ is a fixed point of $\square$.

### Non-examples

1. [[The Gödel sentence is not a Henkin sentence|~a2a9a3f4]] of a consistent $T$: it is a fixed point of $\neg \square$, not of $\square$.
2. For a consistent $T$, the sentence $0 = S0$ is not a Henkin sentence: $T \vdash \neg (0 = S0)$, while $T \nvdash \neg \square (0 = S0)$ by the second incompleteness theorem.

### Basic properties

1. Every Henkin sentence $H$ of $T \supseteq \mathsf{PA}$ is provable: $T \vdash \square H \to H$, so $T \vdash H$ by Löb's theorem.
2. Conversely, every theorem $\varphi$ of $T$ is a Henkin sentence, since $T \vdash \square \varphi$ by the derivability condition D1.
3. So all Henkin sentences of $T$ are provably equivalent to each other, and to $0 = 0$.
4. The answer depends on the predicate. For $P(x) := \mathrm{Prov}_T(x) \wedge \mathrm{Con}(T)$, which defines provability in $\N$ when $T$ is consistent, a sentence $H'$ with $T \vdash H' \leftrightarrow P(\ulcorner H' \urcorner)$ is unprovable: $T \vdash H'$ would give $T \vdash \mathrm{Con}(T)$.

### History

Henkin asked in 1952 whether a sentence that asserts its own provability is provable.
Löb answered in 1955, in "Solution of a problem of Leon Henkin", by proving Löb's theorem.

### Common errors

1. Arguing "$H$ is true because it says it is provable": this reasoning is circular, and Löb's theorem is needed.
2. Assuming that the answer does not depend on the predicate: property 4 shows that it does.
3. Confusing the Henkin sentence with the Gödel sentence: one asserts its provability, the other its unprovability.

## Explanations

### L1 human

Gödel built a sentence that says "I cannot be proved", and it cannot be proved.
Henkin asked about the sentence "I can be proved".
Both answers, provable or not, look consistent with what it says.
Löb showed that it is provable, so it is also true.

### L2 human

1. Build $H$ with $T \vdash H \leftrightarrow \square H$.
2. Then $T \vdash \square H \to H$.
3. Löb's theorem gives $T \vdash H$.

The typical use is as the first application of Löb's theorem, and as a contrast to the Gödel sentence.
A trap: Löb's theorem needs the standard predicate; for other formulas that define provability, the answer can change.

### L3 human

In [[provability logic|WJK0YA4GP2]], the fixed point theorem of $\mathsf{GL}$ says that the equation $p \leftrightarrow \square p$ has the unique solution $\top$ up to equivalence.
The fixed point of $\neg \square$ is $\neg \square \bot$, which matches the equivalence of the Gödel sentence with $\mathrm{Con}(T)$.
