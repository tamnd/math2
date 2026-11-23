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

Let $T \supseteq \mathsf{PA}$ be [[consistent|VM8TQ70CVJ]], with the standard [[provability predicate|NB2BCZR40F]], and write $\square \varphi$ for $\mathrm{Prov}_T(\ulcorner \varphi \urcorner)$.
Let $G$ be the Gödel sentence of [[the first incompleteness theorem|X9WYNYE29C]], so $T \vdash G \leftrightarrow \neg \square G$.
We show that $G$, which says "I am not provable", is not a [[Henkin sentence|SBMQ5QHG9W]], a sentence that says "I am provable".

1. Assume, for a contradiction, that $T \vdash G \leftrightarrow \square G$.
2. Combine this with $T \vdash G \leftrightarrow \neg \square G$.
   Both right sides are equivalent to $G$, so $T \vdash \square G \leftrightarrow \neg \square G$.
3. A sentence that is provably equivalent to its negation is provable, and so is its negation.
   So $T$ proves both $\square G$ and $\neg \square G$.
4. This contradicts the consistency of $T$, so $T \nvdash G \leftrightarrow \square G$.

## Remarks

A second argument uses Löb's theorem.
Every Henkin sentence of $T$ is provable, and a consistent $T$ does not prove $G$, by the first incompleteness theorem.
So $G$ is not a Henkin sentence.

The negation $\neg G$ is not a Henkin sentence either, if $T$ is $\Sigma_1$-sound.
If it were, Löb's theorem would give $T \vdash \neg G$, and then $T \vdash \square G$ by the property of $G$.
But $\square G$ is a false $\Sigma_1$ sentence, because $G$ is not provable, and a $\Sigma_1$-sound theory proves no false $\Sigma_1$ sentence.

The hypothesis of consistency cannot be dropped.
In an inconsistent theory every biconditional is provable, so every sentence, $G$ included, is a Henkin sentence.

## Explanations

### L1 human

The Gödel sentence says "I am not provable", and the Henkin sentence says "I am provable".
In a theory without contradictions, one sentence cannot say both.
So the Gödel sentence is not a Henkin sentence.

### L2 human

We put the two fixed point equations side by side.
The Gödel sentence satisfies $G \leftrightarrow \neg \square G$, and a Henkin sentence would satisfy $G \leftrightarrow \square G$.
Together they give $\square G \leftrightarrow \neg \square G$, so the theory would prove a sentence and its negation.
The typical use is to separate the two kinds of self-reference: "I am not provable" is unprovable, while "I am provable" is provable.
Watch out: the conclusion depends on consistency, and in an inconsistent theory every sentence is a Henkin sentence.
