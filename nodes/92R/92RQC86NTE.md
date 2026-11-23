---
tag: 92RQC86NTE
kind: example
name: Cyclic betterness among exclusive outcomes
msc: ["03B45", "03A05"]
topics: [CQM9SRN8PM]
audience: grad
not_instance_of:
  - target: 4BRXSBXXWG
    note: a cycle of strict betterness among three pairwise incompatible outcomes is not the all-all lifting of any preorder of worlds
uses: [4BRXSBXXWG, 0VABYWJWH9]
sources:
  - url: https://en.wikipedia.org/wiki/Value_theory
    locator: Absolute and relative
  - url: https://en.wikipedia.org/wiki/Glossary_of_logic
    locator: Glossary of logic, section A
---

## Example

Let $a$, $b$ and $c$ be three pairwise incompatible outcomes, each true at some world, and suppose a judgment says $a \succ b$, $b \succ c$ and $c \succ a$.
We show that no [[preorder|0VABYWJWH9]] $\le$ of worlds gives these comparisons by the all-all lifting of [[axiological logic|4BRXSBXXWG]].

1. Since $a$ and $b$ are incompatible, $|a \wedge \neg b| = |a|$ and $|\neg a \wedge b| = |b|$.
   So $a \succ b$ says that every $a$-world is strictly better than every $b$-world.
2. In the same way, every $b$-world is strictly better than every $c$-world, and every $c$-world is strictly better than every $a$-world.
3. Pick worlds $x \in |a|$, $y \in |b|$ and $z \in |c|$.
   Then $y < x$, $z < y$ and $x < z$.
4. Transitivity of the strict part of $\le$ gives $x < x$, which is impossible.

So the cyclic judgment is not a betterness relation of the logic.

## Remarks

The argument uses only transitivity of the order of worlds.
So it applies to any lifting that, for incompatible outcomes, compares every world of one with every world of the other.
Some value theorists, for example Temkin, have argued that betterness between outcomes can be intransitive, and such views reject the preorder of worlds itself.
For propositions that are not incompatible, the all-all lifting can fail to be transitive even on a preorder of worlds.
On the ranking $11 > 10 > 01 > 00$ over atoms $p, q$, it gives $q \succ (p \leftrightarrow q)$ and $(p \leftrightarrow q) \succ \neg q$ but not $q \succ \neg q$.

## Explanations

### L1 human

Suppose someone says that apples are better than pears, pears are better than plums, and plums are better than apples.
Then no single ranking of the fruit agrees with all three statements.
Axiological logic assumes such a ranking of the possible outcomes, so it rejects the three statements together.

### L2 human

1. Reduce each comparison of incompatible outcomes to a comparison of worlds.
2. Follow the cycle through one world of each outcome.
3. Derive that a world is better than itself.

The typical use is to show that a set of value judgments cannot be represented by one ranking.
Watch out: for propositions that overlap, the lifting need not be transitive, so check incompatibility before using this argument.
