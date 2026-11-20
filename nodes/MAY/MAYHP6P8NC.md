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

Let $\mathrm{Ł}_3$ have the values $\set{0, \tfrac12, 1}$, the designated set $D = \set{1}$ and the negation $\neg x = 1 - x$.
For each valuation $v$ of $\mathrm{Ł}_3$, define $b_v(\varphi) = 1$ if $v(\varphi) = 1$, and $b_v(\varphi) = 0$ otherwise.

1. Two-valued and adequate. Each $b_v$ takes only the values $0$ and $1$. By the [[definition of matrix consequence|66NMTCQNQV]], $\Gamma \models \varphi$ iff every $b_v$ that is $1$ on $\Gamma$ is $1$ on $\varphi$.
2. Take $v_1(p) = \tfrac12$. Then $v_1(\neg p) = \tfrac12$, so $b_{v_1}(p) = 0$ and $b_{v_1}(\neg p) = 0$.
3. Take $v_2(p) = 0$. Then $v_2(\neg p) = 1$, so $b_{v_2}(p) = 0$ and $b_{v_2}(\neg p) = 1$.
4. Steps 2 and 3 have the same input $b(p) = 0$ and different outputs $b(\neg p)$. So no function $g \colon \set{0, 1} \to \set{0, 1}$ satisfies $b(\neg p) = g(b(p))$ for all these $b$.

So $\mathrm{Ł}_3$ has an adequate two-valued semantics, as [[Suszko's reduction|2FQB3NQF8A]] predicts, but negation is not truth-functional in it.

## Remarks

The example shows what Suszko's reduction keeps and what it loses: it keeps the consequence relation and loses compositionality.
With $D = \set{\tfrac12, 1}$ the same steps work with $v_1(p) = \tfrac12$ and $v_2(p) = 1$: then $b(p) = 1$ in both, and $b(\neg p)$ is $1$ and $0$.
In classical logic the map $b_v$ is the valuation $v$ itself, and negation is truth-functional.

## Explanations

### L1 human

In three-valued logic, call a sentence "good" when its value is $1$, and "bad" otherwise.
A sentence with value $\tfrac12$ is bad, and so is its negation.
A sentence with value $0$ is also bad, but its negation is good.
So knowing that a sentence is bad does not tell us whether its negation is good.

### L2 human

1. List the three valuations of $p$: $0$, $\tfrac12$, $1$.
2. Compute $b(p)$: $0$, $0$, $1$.
3. Compute $b(\neg p)$: $1$, $0$, $0$.
4. The first two rows have the same $b(p)$ and different $b(\neg p)$.

The typical use is to explain why the reduction does not make $\mathrm{Ł}_3$ classical.
A trap: the reduction does not say that $\mathrm{Ł}_3$ equals classical logic; $p \lor \neg p$ is still not valid.
