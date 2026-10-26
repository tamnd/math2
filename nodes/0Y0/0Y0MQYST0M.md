---
tag: 0Y0MQYST0M
kind: concept
name: Modus ponens
aliases: [implication-elimination]
msc: [03B05]
uses: [0ZNX6DQ3EJ]
sources:
  - url: https://en.wikipedia.org/wiki/Modus_ponens
    locator: lead section
same_as:
  wikidata: Q655742
  wikipedia: Modus ponens
---

## Summary

Modus ponens is the rule of inference that gets $q$ from the two premises $p$ and $p \to q$.
$$\frac{p \qquad p \to q}{q}$$
It is valid: when the two premises are true, the conclusion $q$ is true.

## Remarks

Most proof systems for [[propositional logic|09K9MWD2QQ]] use modus ponens as a rule.
Its partner modus tollens gets $\neg p$ from $\neg q$ and $p \to q$.

## Explanations

### L1 human

Modus ponens is the most common step in a proof.
If you know that $n$ is divisible by $4$, and that each number divisible by $4$ is even, then you know that $n$ is even.
