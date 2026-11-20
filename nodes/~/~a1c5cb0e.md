---
tag: ~a1c5cb0e
kind: example
name: Łukasiewicz's three-valued connectives are not functionally complete
msc: ["03B50"]
topics: [WZP584JQ06]
audience: research
instance_of: [~d7a9d81e]
not_instance_of:
  - target: TDZVCWYJ9F
    note: the many-valued analog fails, since the terms preserve the set {0, 1}
  - target: ~e204f5cc
    note: unlike Post's connectives, they do not define every three-valued function
uses: [~09f1e8d9, ~fbe0fcc9]
sources:
  - url: https://en.wikipedia.org/wiki/Many-valued_logic
    locator: Functional completeness of many-valued logics
  - url: https://plato.stanford.edu/entries/lukasiewicz/
    locator: 5.4 Axioms and Definitions
---

## Example

Take the connectives $\neg x = 1 - x$ and $x \to y = \min(1, 1 - x + y)$ of [[Łukasiewicz's three-valued logic|~09f1e8d9]] on $\set{0, \tfrac12, 1}$.
We show that the constant function $\tfrac12$ is not a term function.

1. Claim: every term $t(x_1, \dots, x_n)$ maps $\set{0, 1}^n$ into $\set{0, 1}$. We use structural induction on $t$.
2. A variable $x_i$ takes a value in $\set{0, 1}$ on $\set{0, 1}^n$.
3. If $u \in \set{0, 1}$, then $\neg u = 1 - u \in \set{0, 1}$.
4. If $u, w \in \set{0, 1}$, then $1 - u + w \in \set{0, 1, 2}$, so $\min(1, 1 - u + w) \in \set{0, 1}$.
5. So the claim holds, and a term in $x_1$ has a value in $\set{0, 1}$ at $x_1 = 0$.
6. The constant $\tfrac12$ is therefore not a term function, so $\set{\neg, \to}$ is not functionally complete.

## Remarks

1. Adding $\land = \min$ and $\lor = \max$ does not help, since they are terms in $\neg$ and $\to$.
2. By contrast, [[Post's connectives|~fbe0fcc9]] preserve no nonempty proper subset of values, and they are complete.
3. The Wikipedia article, after Malinowski, states that no Łukasiewicz logic is functionally complete.
4. Słupecki showed in 1936 that adding a constant connective $T$ with value $\tfrac12$ makes all three-valued connectives definable, as the SEP entry on Łukasiewicz reports.

## Explanations

### L1 human

Łukasiewicz's "not" and "if" send true and false to true and false.
So a formula fed with only true and false never outputs the middle value.
That means some tables, for example "always $\tfrac12$", cannot be written.

### L2 human

1. Find a subset of values that every connective maps into itself.
2. Check that some function leaves this subset.
3. Conclude that the function is not a term.

The typical use is this invariant-subset test for incompleteness.
A trap: Post's negation has no such subset, since it moves every value in one cycle.
