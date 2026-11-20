---
tag: 9HYWPPKC1C
kind: example
name: The minimum-maximum valuation is not a probability function
aliases: [min-max-valuation-is-not-a-probability]
msc: ["03B48", "03B52"]
topics: [WZP584JQ06]
audience: grad
instance_of: [8DH4QM6AX8]
not_instance_of:
  - target: Z2WRGJDRQT
    note: the tautology p or not p gets the value 1/2, while every probability function gives a tautology the value 1
uses: [05006AJ7DZ, 0DAX8PMAJ4]
sources:
  - url: https://plato.stanford.edu/entries/logic-probability/
    locator: 2.1 Probabilistic Semantics
  - url: https://plato.stanford.edu/entries/logic-fuzzy/
    locator: 1. Fuzzy connectives based on t-norms
---

## Example

Let $v$ be the valuation on propositional formulas with values in $[0, 1]$ given by
$$v(\neg \varphi) = 1 - v(\varphi), \quad v(\varphi \land \psi) = \min(v(\varphi), v(\psi)), \quad v(\varphi \lor \psi) = \max(v(\varphi), v(\psi)),$$
and by $v(p) = \tfrac12$ for one variable $p$.
We show that $v$ is not a [[probability function|Z2WRGJDRQT]].

1. $v(\neg p) = 1 - \tfrac12 = \tfrac12$.
2. $v(p \lor \neg p) = \max(\tfrac12, \tfrac12) = \tfrac12$.
3. $p \lor \neg p$ is a [[tautology|05006AJ7DZ]], and a probability function gives every tautology the value $1$.
4. Since $\tfrac12 \ne 1$, the property for tautologies fails.
5. Additivity fails too. The formulas $p$ and $\neg p$ exclude each other, so additivity requires $v(p \lor \neg p) = v(p) + v(\neg p) = 1$.

So $v$ is not a probability function.

## Remarks

The example separates degrees of truth from probabilities.
The valuation $v$ is truth-functional, while a probability function is not.
If $v(p) \in \set{0, 1}$ for every variable $p$, then $v$ is a classical valuation, and it is a probability function.
So the failure comes from the middle values.

Change the value of $p$ to $t \in [0, 1]$.
Then $v(p \lor \neg p) = \max(t, 1 - t)$, which is $1$ only for $t = 0$ and $t = 1$.
For every $t$, a probability function with $P(p) = t$ gives $P(p \lor \neg p) = 1$ and $P(p \land \neg p) = 0$.

## Explanations

### L1 human

Give the statement "the glass is full" the degree one half.
With the minimum and maximum rules, "the glass is full or it is not full" also gets one half.
A probability, in contrast, gives "full or not full" the chance $1$, because one of the two always happens.
So degrees of truth and chances follow different rules.

### L2 human

1. Take $v(p) = 0.3$.
2. Then $v(\neg p) = 0.7$ and $v(p \lor \neg p) = 0.7$.
3. A probability function with $P(p) = 0.3$ has $P(\neg p) = 0.7$ and $P(p \lor \neg p) = 1$.

The typical use is to show that a fuzzy valuation does not model uncertainty about a true or false statement.
A trap: the Łukasiewicz strong disjunction $\min(1, x + y)$ gives $p \oplus \neg p$ the value $1$.
But a probability function is not truth-functional, so no choice of truth functions turns $v$ into a probability function.
