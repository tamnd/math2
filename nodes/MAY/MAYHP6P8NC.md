---
tag: MAYHP6P8NC
kind: example
name: Suszko's two-valued semantics for Ł3 is not truth-functional
msc: ["03B50"]
topics: [WZP584JQ06]
audience: grad
instance_of: [DWYCKAKXZD]
illustrates: [2FQB3NQF8A]
uses: [2FQB3NQF8A, 66NMTCQNQV]
sources:
  - url: https://plato.stanford.edu/entries/logic-manyvalued/
    locator: 4.3 Are many-valued logics actually bivalent?
  - url: https://en.wikipedia.org/wiki/%C5%81ukasiewicz_logic
    locator: Three-valued logic
---

## Example

Let $\mathrm{Ł}_3$ have the values $\{0, \tfrac12, 1\}$, the designated set $D = \{1\}$ and the negation $\neg x = 1 - x$.
For each valuation $v$ of $\mathrm{Ł}_3$, define a two-valued map $b_v$ on formulas by $b_v(\varphi) = 1$ if $v(\varphi) = 1$, and $b_v(\varphi) = 0$ otherwise.
We show that the maps $b_v$ give the consequence of $\mathrm{Ł}_3$, and that negation is not truth-functional for them.

1. Each $b_v$ takes only the values $0$ and $1$.
   By the [[definition of matrix consequence|66NMTCQNQV]], $\Gamma \models \varphi$ holds iff every $b_v$ that is $1$ on all of $\Gamma$ is $1$ on $\varphi$, since $b_v(\psi) = 1$ means exactly $v(\psi) \in D$.
2. Take $v_1(p) = \tfrac12$.
   Then $v_1(\neg p) = 1 - \tfrac12 = \tfrac12$, so $b_{v_1}(p) = 0$ and $b_{v_1}(\neg p) = 0$.
3. Take $v_2(p) = 0$.
   Then $v_2(\neg p) = 1 - 0 = 1$, so $b_{v_2}(p) = 0$ and $b_{v_2}(\neg p) = 1$.
4. Steps 2 and 3 have the same input $b(p) = 0$ and different outputs $b(\neg p)$.
   So no function $g \colon \{0, 1\} \to \{0, 1\}$ satisfies $b(\neg p) = g(b(p))$ for all the maps $b_v$.

So $\mathrm{Ł}_3$ has an adequate two-valued semantics, as [[Suszko's reduction|2FQB3NQF8A]] predicts, but negation is not computed by a two-valued table in it.

## Remarks

The example shows what Suszko's reduction keeps and what it loses.
It keeps the consequence relation exactly, and it loses compositionality, the rule that the value of a compound is a function of the values of its parts.

Change the designated set to $D = \{\tfrac12, 1\}$ and the same thing happens with other valuations.
Take $v_1(p) = \tfrac12$ and $v_2(p) = 1$: both give $b(p) = 1$, but $b(\neg p)$ is $1$ for $v_1$ and $0$ for $v_2$.
In classical logic the map $b_v$ is the valuation $v$ itself, and there negation is truth-functional.
So the failure comes from the middle value, which the two-valued map merges with one of the classical values.

## Explanations

### L1 human

In three-valued logic, call a sentence "good" when its value is $1$, and "bad" otherwise.
A sentence with value $\tfrac12$ is bad, and so is its negation.
A sentence with value $0$ is also bad, but its negation is good.
So if you only know that a sentence is bad, you cannot tell whether its negation is good.

### L2 human

List the three values of $p$ and compute both maps.
For $p = 0, \tfrac12, 1$ the values of $\neg p$ are $1, \tfrac12, 0$.
Then $b(p)$ is $0, 0, 1$, and $b(\neg p)$ is $1, 0, 0$.
The first two rows have the same $b(p)$ and different $b(\neg p)$, and that is the whole argument.
The typical use of the example is to explain why the reduction does not make $\mathrm{Ł}_3$ classical.
Watch out: $p \lor \neg p$ is still not valid in $\mathrm{Ł}_3$, because the two-valued maps are not the classical valuations.
