---
tag: RW2B6EMK70
kind: example
name: A subset of a phase space that is not a fact
msc: ["03F52"]
topics: [98QF5J4W16]
audience: research
instance_of: [64MHHQQ6G6]
uses: [5M4Z5EE88F]
sources:
  - doi: 10.1016/0304-3975(87)90045-4
    locator: pages 1-101
    note: Girard, Linear logic, Theoretical Computer Science 50 (1987)
  - url: https://plato.stanford.edu/entries/logic-linear/
    locator: 3.1 Semantics of provability
    note: Di Cosmo and Miller, Linear Logic, Stanford Encyclopedia of Philosophy, revision of 2023-09-16
---

## Example

Let $M = (\mathbb{N}, +)$, with unit $0$, and let $\bot = \set{1}$.
In this [[phase space|5M4Z5EE88F]] the set $\set{0, 1}$ is not a fact.

1. For $X \subseteq \mathbb{N}$, $X^{\perp} = \set{m \mid m + x = 1 \text{ for all } x \in X}$.
2. $\set{0}^{\perp} = \set{1}$ and $\set{1}^{\perp} = \set{0}$.
3. If $X$ contains a number $x \geq 2$, then $m + x \geq 2$, so $X^{\perp} = \emptyset$.
4. $\set{0, 1}^{\perp} = \set{1} \cap \set{0} = \emptyset$.
5. So $\set{0, 1}^{\perp\perp} = \emptyset^{\perp} = \mathbb{N}$, which is not $\set{0, 1}$.

By steps 2 to 4, every set $X^{\perp}$ is one of $\mathbb{N}$, $\set{0}$, $\set{1}$ and $\emptyset$, so these four sets are the facts.

## Remarks

If an atom were given the value $\set{0, 1}$, then $(p^{\perp\perp})^* = \mathbb{N}$ would differ from $p^*$, though $p^{\perp\perp}$ is the formula $p$.
The condition that atoms take facts as values makes negation an involution on values.
In this space $1^* = \set{0}^{\perp\perp} = \set{0}$ and $\bot^* = \set{1}$, so the two units have different values, unlike in [[the model on $\mathbb{Z}/2$|25NVD1AHHE]].
Also $(\bot \otimes \bot)^* = \set{2}^{\perp\perp} = \emptyset^{\perp} = \mathbb{N} = \top^*$.

## Explanations

### L1 human

A fact must equal the negation of its negation.
Here the negation of $\set{0, 1}$ is empty, and the negation of the empty set is everything.
So $\set{0, 1}$ grows to all of $\mathbb{N}$ under two negations, and it is not a fact.

### L2 human

We find the closure $X^{\perp\perp}$ of each small set $X$.

1. $X = \set{0}$: $X^{\perp} = \set{1}$ and $X^{\perp\perp} = \set{0}$, so $X$ is a fact.
2. $X = \set{1}$: $X^{\perp} = \set{0}$ and $X^{\perp\perp} = \set{1}$, so $X$ is a fact.
3. $X = \set{2}$: $X^{\perp} = \emptyset$ and $X^{\perp\perp} = \mathbb{N}$.
4. $X = \emptyset$: $X^{\perp} = \mathbb{N}$, and $\mathbb{N}^{\perp} = \emptyset$, so $X$ is a fact.

The typical use of this computation is to see that most subsets of a phase space are not facts.
A trap: the tensor of two facts must be closed again, since $\set{1} + \set{1} = \set{2}$ is not a fact.
