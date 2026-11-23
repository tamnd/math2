---
tag: 8FYX4VNRW8
kind: example
name: The theory of groups is not essentially undecidable
aliases: [group-theory-undecidable-but-not-essentially]
msc: ["03B25", "20A15"]
topics: [E4AVTNWE9E]
audience: grad
not_instance_of:
  - target: 9JDDFN8PT7
    note: the theory of groups is undecidable, but its consistent extension, the theory of the trivial group, is decidable
uses: [9JDDFN8PT7, RX9MB386C5, HWC687ES0Q, Y0753DF5R9]
sources:
  - url: https://en.wikipedia.org/wiki/Decidability_(logic)
    locator: Some undecidable theories
---

## Example

Let $T_G$ be the [[elementary theory of groups|RX9MB386C5]], the set of consequences of the group axioms in the signature $\{\cdot, {}^{-1}, e\}$.
We check that $T_G$ is not [[essentially undecidable|9JDDFN8PT7]].

1. Let $\mathcal{E}$ be the trivial group, with one element $e$, and $e \cdot e = e$ and $e^{-1} = e$.
2. $\mathcal{E}$ satisfies the group axioms, so $T_G \subseteq \operatorname{Th}(\mathcal{E})$.
3. $\operatorname{Th}(\mathcal{E})$ is consistent, because $\mathcal{E}$ is a model.
4. $\operatorname{Th}(\mathcal{E})$ is [[decidable|HWC687ES0Q]].
   To decide a sentence, we evaluate it in $\mathcal{E}$: each quantifier ranges over the single element $e$, and each term has the value $e$.
   For example, $\forall x \, \forall y \, (x \cdot y = y \cdot x)$ becomes $e \cdot e = e \cdot e$, which is true.
5. So $T_G$ has a consistent decidable extension, and the condition of essential undecidability fails.

Yet $T_G$ itself is undecidable, by a theorem of Tarski published in 1953.
So $T_G$ is an undecidable theory that is not essentially undecidable.

## Remarks

The example shows that undecidability does not pass to extensions.
Many other extensions of $T_G$ are decidable.
The theory of any finite group is decidable by evaluation, and the theory of abelian groups is decidable by [[Szmielew's theorem|Y0753DF5R9]].
The theory of abelian groups is not complete, so it is a decidable extension that is not the theory of a single finite group.

The picture changes when the base theory is arithmetic.
Every consistent extension of [[Robinson arithmetic|3K1AKGXF8A]] is undecidable, so no axiom such as $\forall x \, (x = 0)$ can be added there without making the theory inconsistent.
Tarski's proof of the undecidability of $T_G$ uses interpretations, the method of the [[transfer theorem|FMB2C20G8W]].

## Explanations

### L1 human

No computer can decide every statement that follows from the rules of a group.
But if we add the rule "there is only one element", the question becomes easy: a computer just checks the statement on that one element.
So the rules of a group are hard to decide, but not in the strong sense, because some extra rules make them easy.

### L2 human

We decide the sentence $\sigma = \exists x \, (x \ne e)$ in two extensions of $T_G$.

1. In the trivial group, the only element is $e$, so $\sigma$ is false and $\neg \sigma \in \operatorname{Th}(\mathcal{E})$.
2. In the theory of $\mathbb{Z} / 2 \mathbb{Z}$, the element $1$ differs from the identity $0$, so $\sigma$ is true.
3. So $\sigma$ is not decided by $T_G$, and the two extensions decide it in opposite ways.

The typical use of this example is to show the difference between "undecidable" and "essentially undecidable".
Watch out: the decidability of one extension does not make $T_G$ decidable, because decidability does not pass to subtheories either.
