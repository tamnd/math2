---
tag: 9VMWRPJ96D
kind: example
name: A disjunctive hypothesis is not self-slashing
msc: ["03F05", "03B20"]
topics: [38EQ20GR7M]
audience: research
not_instance_of:
  - target: YRRKEEHNCD
    note: the set consisting of p or q does not slash its own member, so the slash method gives no disjunction property for it
uses: [YRRKEEHNCD]
sources:
  - url: https://en.wikipedia.org/wiki/Disjunction_and_existence_properties
    locator: Definitions
---

## Example

Let $\Gamma = \set{p \vee q}$ with distinct atoms $p$ and $q$.
We show that $\Gamma$ is not self-slashing for the [[slash|YRRKEEHNCD]].

1. By the clause for $\vee$, $\Gamma \mid p \vee q$ holds iff $\Gamma \mid p$ or $\Gamma \mid q$.
2. By the clause for atoms, $\Gamma \mid p$ iff $\Gamma \vdash p$, and $\Gamma \mid q$ iff $\Gamma \vdash q$.
3. The classical valuation with $p$ false and $q$ true satisfies $\Gamma$ and refutes $p$. So $\Gamma \nvdash p$.
4. In the same way, the valuation with $p$ true and $q$ false shows $\Gamma \nvdash q$.
5. So $\Gamma \mid p \vee q$ fails, although $p \vee q \in \Gamma$.

## Remarks

The set $\Gamma$ is consistent, and it fails the disjunction property: $\Gamma \vdash p \vee q$, but $\Gamma$ proves neither disjunct.
So the hypothesis "self-slashing" in the slash method can not be replaced by "consistent".
The formula $p \vee q$ is not Harrop, since a disjunction is not allowed in a positive position.

## Explanations

### L1 human

A hypothesis "$p$ or $q$" asserts a disjunction without saying which side holds.
The slash asks for a side at every disjunction.
So the hypothesis fails its own test.

### L2 human

1. List the members of $\Gamma$ and test each one with the slash.
2. The member $p \vee q$ needs $\Gamma \vdash p$ or $\Gamma \vdash q$.
3. Two classical valuations refute both.

The typical use is to see why the disjunction property is stated for Harrop theories only.
A trap: $\Gamma \mid p \vee q$ fails, while $\Gamma \vdash p \vee q$ holds, so the slash is strictly stronger than provability from $\Gamma$.
