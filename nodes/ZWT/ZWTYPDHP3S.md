---
tag: ZWTYPDHP3S
kind: example
name: The Gödel sentence is not a Henkin sentence
msc: ["03F40"]
topics: [HXHHWY3328]
audience: grad
not_instance_of:
  - target: SBMQ5QHG9W
    note: "The Gödel sentence is a fixed point of the negation of provability, and a consistent theory cannot make it a fixed point of provability as well."
uses: [SBMQ5QHG9W, X9WYNYE29C, NB2BCZR40F, VM8TQ70CVJ]
sources:
  - url: https://en.wikipedia.org/wiki/Gödel's_incompleteness_theorems
    locator: First incompleteness theorem
  - book: isbn:9780521857840
---

## Example

Let $T \supseteq \mathsf{PA}$ be [[consistent|VM8TQ70CVJ]] with the standard [[provability predicate|NB2BCZR40F]], and write $\square \varphi$ for $\mathrm{Prov}_T(\ulcorner \varphi \urcorner)$.
Let $G$ be the Gödel sentence of [[the first incompleteness theorem|X9WYNYE29C]], with $T \vdash G \leftrightarrow \neg \square G$.
We show that $G$ is not a [[Henkin sentence|SBMQ5QHG9W]] of $T$.

1. Assume, for a contradiction, that $T \vdash G \leftrightarrow \square G$.
2. With the property of $G$, $T \vdash \square G \leftrightarrow \neg \square G$.
3. A sentence equivalent to its negation makes $T$ inconsistent: $T$ proves both $\square G$ and $\neg \square G$.
4. This contradicts the consistency of $T$. So $T \nvdash G \leftrightarrow \square G$.

## Remarks

A second argument: every Henkin sentence is provable by Löb's theorem, and $G$ is not provable by the first incompleteness theorem.
If $T$ is $\Sigma_1$-sound, $\neg G$ is not a Henkin sentence either.
By Löb's theorem it would be provable, and then $T \vdash \square G$, a false $\Sigma_1$ sentence.

## Explanations

### L1 human

The Gödel sentence says "I am not provable", and the Henkin sentence says "I am provable".
One sentence cannot say both in a consistent theory, so the Gödel sentence is not a Henkin sentence.

### L2 human

1. Assume both fixed point equations for $G$.
2. They make $\square G$ equivalent to its negation.
3. So the theory would be inconsistent.

The typical use is to separate the two kinds of self-reference.
A trap: "not a Henkin sentence" depends on consistency; in an inconsistent theory every sentence is one.
