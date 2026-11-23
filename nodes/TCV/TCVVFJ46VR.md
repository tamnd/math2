---
tag: TCVVFJ46VR
kind: example
name: Łukasiewicz's three-valued connectives are not functionally complete
msc: ["03B50"]
topics: [WZP584JQ06]
audience: research
instance_of: [1CE2TGM6MQ]
not_instance_of:
  - target: TDZVCWYJ9F
    note: the many-valued analog fails, since the terms preserve the set {0, 1}
  - target: YHYSGRE7JV
    note: unlike Post's connectives, they do not define every three-valued function
uses: [F9NDCFY3GS, PHGRJ2D97H]
sources:
  - url: https://en.wikipedia.org/wiki/Many-valued_logic
    locator: Functional completeness of many-valued logics
  - url: https://plato.stanford.edu/entries/lukasiewicz/
    locator: 5.4 Axioms and Definitions
---

## Example

Take the connectives $\neg x = 1 - x$ and $x \to y = \min(1, 1 - x + y)$ of [[Łukasiewicz's three-valued logic|F9NDCFY3GS]] on $\{0, \tfrac12, 1\}$.
We show that the constant function with value $\tfrac12$ is not a term function, so the connectives are not [[functionally complete|TDZVCWYJ9F]].

1. We claim that every term $t(x_1, \dots, x_n)$ maps $\{0, 1\}^n$ into $\{0, 1\}$, and we prove it by structural induction on $t$.
2. A variable $x_i$ takes a value in $\{0, 1\}$ on $\{0, 1\}^n$.
3. If $u \in \{0, 1\}$, then $\neg u = 1 - u \in \{0, 1\}$.
4. If $u, w \in \{0, 1\}$, then $1 - u + w \in \{0, 1, 2\}$, so $\min(1, 1 - u + w) \in \{0, 1\}$.
5. So the claim holds, and every term in $x_1$ takes a value in $\{0, 1\}$ at $x_1 = 0$.
6. The constant $\tfrac12$ takes the value $\tfrac12$ there, so it is not a term function.

## Remarks

The example shows the invariant-subset test for incompleteness: find a set of values that every connective maps into itself, and a function that leaves it.
Adding $\land = \min$ and $\lor = \max$ does not help, since they are terms in $\neg$ and $\to$ and also preserve $\{0, 1\}$.
The same argument works for every Łukasiewicz logic $\mathrm{Ł}_n$, and for the logic on $[0, 1]$, so none of them is functionally complete.

The picture changes when the obstacle is removed.
[[Post's connectives|PHGRJ2D97H]] include a cyclic negation that sends $0$ to $1$, $1$ to $\tfrac12$ and $\tfrac12$ to $0$, so no proper nonempty subset of values is preserved, and they are complete.
Słupecki showed in 1936 that adding to $\neg$ and $\to$ a constant connective with value $\tfrac12$ makes every three-valued function definable.

## Explanations

### L1 human

Łukasiewicz's "not" and "if" send true and false to true and false.
So a formula fed with only true and false never outputs the middle value.
That means some tables, for example "always $\tfrac12$", cannot be written with these connectives.

### L2 human

The test has three steps.
First find a subset of values that every connective maps into itself, here $\{0, 1\}$.
Then check that some function leaves this subset, here the constant $\tfrac12$.
Then conclude that the function is not a term, by induction on terms.
The typical use is to prove incompleteness quickly.
Watch out: the test only proves incompleteness, and Post's negation shows that a single connective can destroy every invariant subset.
