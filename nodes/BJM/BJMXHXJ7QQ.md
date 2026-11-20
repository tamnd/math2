---
tag: BJMXHXJ7QQ
kind: example
name: Strong Kleene logic and the logic of paradox share one algebra
msc: ["03B50", "03B53"]
topics: [WZP584JQ06]
audience: grad
instance_of: [P7E926JK13]
uses: [AJEJS6TFWP, SZHA10A9X7]
sources:
  - url: https://en.wikipedia.org/wiki/Three-valued_logic
    locator: Kleene and Priest logics
  - url: https://plato.stanford.edu/entries/logic-manyvalued/
    locator: 3.2 Logical matrices and the designation-based notion of entailment
---

## Example

Let $\mathbf{K}$ be the algebra on $\set{0, \tfrac12, 1}$ with $\neg x = 1 - x$, $x \land y = \min(x, y)$ and $x \lor y = \max(x, y)$.
Consider the two [[logical matrices|AJEJS6TFWP]] $\mathsf{K}_3 = \langle \mathbf{K}, \set{1} \rangle$ and $\mathsf{LP} = \langle \mathbf{K}, \set{\tfrac12, 1} \rangle$.

1. Both are logical matrices: $\mathbf{K}$ is an algebra for $\neg, \land, \lor$, and each designated set is a subset of $\set{0, \tfrac12, 1}$.
2. Explosion $p \land \neg p \models q$ holds in $\mathsf{K}_3$. The value $\min(x, 1 - x)$ is at most $\tfrac12$, so the premise is never designated.
3. Explosion fails in $\mathsf{LP}$. Take $p = \tfrac12$ and $q = 0$: the premise has value $\tfrac12$, which is designated, and $q$ is not.
4. $p \models q \lor \neg q$ holds in $\mathsf{LP}$. The value $\max(y, 1 - y)$ is at least $\tfrac12$, so the conclusion is always designated.
5. $p \models q \lor \neg q$ fails in $\mathsf{K}_3$. Take $p = 1$ and $q = \tfrac12$: the conclusion has value $\tfrac12$, which is not designated.

So one algebra with two designated sets gives two different logics.

## Remarks

Steps 2 to 5 show a duality: $\mathsf{K}_3$ keeps explosion and loses excluded middle, and $\mathsf{LP}$ does the reverse.
$\mathsf{LP}$ is Priest's logic of paradox, a [[paraconsistent logic|C7YWCR87QJ]].
[[Strong Kleene logic|SZHA10A9X7]] has no tautologies, while $\mathsf{LP}$ has tautologies, for example $p \lor \neg p$ by step 4.
Both are extensions of [[first-degree entailment|KXTP4P3GHT]], whose four values combine the two readings of the middle value.

## Explanations

### L1 human

Take three values: true, false and a middle value.
In one logic the middle value counts as "not true", and in the other it counts as "true enough".
The tables are the same, but different arguments become valid.
For example, "$p$ and not $p$, so anything" is valid in the first logic and invalid in the second.

### L2 human

1. Fix the algebra and list the valuations of the variables of the inference.
2. Mark the rows in which all premises are designated.
3. Check the conclusion in these rows only.

The typical use is to separate two logics by one inference.
A trap: a valuation that refutes an inference in one matrix can satisfy it in the other, so the designated set must be fixed before the check.
