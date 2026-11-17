---
tag: 3MQ39PRCYJ
kind: statement
role: lemma
name: Arithmetical comprehension is equivalent to the existence of ranges of one-to-one functions
msc: ["03B30", "03F35"]
topics: [BY8AAFN7C5]
audience: grad
about: [NAASTN80QN]
uses: [DNXCKXZZ08, K9XG0Z2N9V]
sources:
  - url: https://en.wikipedia.org/wiki/Reverse_mathematics
    locator: Arithmetical comprehension ACA0
---

## Statement

Over [[RCA0|DNXCKXZZ08]], the following are equivalent:

1. [[arithmetical comprehension|K9XG0Z2N9V]];
2. $\Sigma^0_1$ comprehension: $\exists X\, \forall n\, (n \in X \leftrightarrow \varphi(n))$ for every $\Sigma^0_1$ formula $\varphi$ in which $X$ is not free;
3. for every one-to-one function $f \colon \N \to \N$, the range $\set{m : \exists i\, f(i) = m}$ exists.

## Remarks

### Why each hypothesis is needed

- The restriction in 3 to one-to-one functions makes the statement weaker in form, and so easier to reach in a reversal. The version for all functions is also equivalent.

### Consequences

- To show that a theorem implies $\mathsf{ACA}_0$ over $\mathsf{RCA}_0$, it suffices to compute, from a solution of an instance built from a one-to-one $f$, the range of $f$.
- The [[existence of Turing jumps|10NR4PGXHW]] is equivalent to $\mathsf{ACA}_0$.

### Converse

All three directions are part of the statement.

### Generalizations

For every $k \ge 1$, $\mathsf{RCA}_0$ proves that $\Sigma^0_1$ comprehension implies $\Sigma^0_k$ comprehension.
The same pattern holds one level up: over $\mathsf{ACA}_0$, $\Pi^1_1$ comprehension is equivalent to the statement that for every sequence of trees $(T_k)_k$ the set $\set{k : T_k \text{ has a path}}$ exists.

## Explanations

### L1 human

Arithmetical comprehension says that every set described with number quantifiers exists.
The lemma says that it is enough to ask for one kind of set: the set of values of a function that never repeats a value.
All other sets then follow, one quantifier at a time.

### L2 human

The lemma is the usual target of reversals to $\mathsf{ACA}_0$.
For example, the reversal of the Bolzano-Weierstrass theorem builds a sequence $c_n = \sum_{i \le n} 2^{-f(i) - 1}$, and the speed at which it converges tells whether $m$ is in the range of $f$.
A trap is to try to reach arithmetical comprehension in one step: one first gets $\Sigma^0_1$ comprehension, and then climbs.
