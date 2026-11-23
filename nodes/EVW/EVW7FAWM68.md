---
tag: EVW7FAWM68
kind: example
name: Probability is not truth-functional
msc: ["03B48", "03B50"]
topics: [WZP584JQ06]
audience: ug2
instance_of: [Z2WRGJDRQT]
not_instance_of:
  - target: P7E926JK13
    note: no operation on [0, 1] computes the probability of a conjunction from the probabilities of its conjuncts, so a probability function is not a matrix valuation
uses: [AJEJS6TFWP, 0DAX8PMAJ4]
sources:
  - url: https://plato.stanford.edu/entries/logic-probability/
    locator: 2.1 Probabilistic Semantics
  - url: https://en.wikipedia.org/wiki/Probability_axioms
    locator: lead section
---

## Example

Toss two fair coins, and let the four outcomes $HH$, $HT$, $TH$, $TT$ each have probability $\tfrac14$.
Let $p$ say "the first coin shows heads".
We compare three readings of a second sentence $q$.

1. If $q$ says "the second coin shows heads", then $P(p) = P(q) = \tfrac12$ and $P(p \land q) = P(\{ HH \}) = \tfrac14$.
2. If $q$ is $p$ itself, then $P(p) = P(q) = \tfrac12$ and $P(p \land q) = P(p) = \tfrac12$.
3. If $q$ says "the first coin shows tails", then $P(p) = P(q) = \tfrac12$ and $P(p \land q) = 0$, since the events are disjoint.
4. The inputs $(\tfrac12, \tfrac12)$ are the same in steps 1 to 3, and the outputs $\tfrac14$, $\tfrac12$ and $0$ differ.
5. So no function $f \colon [0, 1]^2 \to [0, 1]$ satisfies $P(\varphi \land \psi) = f(P(\varphi), P(\psi))$ for all probability functions.

Hence a probability function on formulas is not a valuation in any [[logical matrix|AJEJS6TFWP]] on $[0, 1]$.

## Remarks

The [[probability axioms|0DAX8PMAJ4]] only bound the conjunction.

$$\max(0, P(\varphi) + P(\psi) - 1) \le P(\varphi \land \psi) \le \min(P(\varphi), P(\psi)).$$

The three cases above give the product, the upper bound and the lower bound.
These bounds are the Łukasiewicz and Gödel t-norms, and the product is the product t-norm, which is one reason why probability and fuzzy logic are often confused.
The example is a non-example for [[logical matrices|P7E926JK13]] and an example for [[probability logic|Z2WRGJDRQT]], which studies probabilities of sentences without assuming truth-functionality.

## Explanations

### L1 human

Suppose two events each have a chance of one half.
The chance that both happen can be one quarter, one half or zero, depending on how the events are related.
So we cannot compute it from the two chances alone.
Truth tables always compute the value of "and" from the values of the parts, so chances are not truth values of a truth table.

### L2 human

Fix the values $P(\varphi) = 0.7$ and $P(\psi) = 0.4$.
The lower bound is $\max(0, 0.7 + 0.4 - 1) = 0.1$, and the upper bound is $\min(0.7, 0.4) = 0.4$.
Every value in $[0.1, 0.4]$ occurs for some events with these probabilities.
Watch out: the product $0.28$ is the right value only for independent events.
