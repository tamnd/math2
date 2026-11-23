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

Let $\mathbf{K}$ be the algebra on $\{0, \tfrac12, 1\}$ with $\neg x = 1 - x$, $x \land y = \min(x, y)$ and $x \lor y = \max(x, y)$.
Consider the two [[logical matrices|AJEJS6TFWP]] $\mathsf{K}_3 = \langle \mathbf{K}, \{1\} \rangle$ and $\mathsf{LP} = \langle \mathbf{K}, \{\tfrac12, 1\} \rangle$.

1. Both are logical matrices, because $\mathbf{K}$ is an algebra for $\neg, \land, \lor$ and each designated set is a subset of $\{0, \tfrac12, 1\}$.
2. Explosion $p \land \neg p \models q$ holds in $\mathsf{K}_3$.
   The premise has the value $\min(x, 1 - x)$, which is $0$ at $x = 0$ or $x = 1$ and $\tfrac12$ at $x = \tfrac12$, so it is never $1$.
3. Explosion fails in $\mathsf{LP}$.
   At $p = \tfrac12$ and $q = 0$ the premise has the designated value $\tfrac12$, and the conclusion $0$ is not designated.
4. The inference $p \models q \lor \neg q$ holds in $\mathsf{LP}$.
   The conclusion has the value $\max(y, 1 - y)$, which is $1$ or $\tfrac12$, so it is always designated.
5. The inference $p \models q \lor \neg q$ fails in $\mathsf{K}_3$.
   At $p = 1$ and $q = \tfrac12$ the premise is designated, and the conclusion has the value $\tfrac12$, which is not.

So one algebra with two designated sets gives two different logics.

## Remarks

Steps 2 to 5 show a duality.
$\mathsf{K}_3$ keeps explosion and loses excluded middle, and $\mathsf{LP}$ does the reverse.
$\mathsf{LP}$ is Priest's [[logic of paradox|BXJZG67PX3]], a [[paraconsistent logic|C7YWCR87QJ]].
[[Strong Kleene logic|SZHA10A9X7]] has no tautologies, while $\mathsf{LP}$ has the tautology $p \lor \neg p$ by step 4.
In fact a formula is a tautology of $\mathsf{LP}$ exactly when it is a classical tautology.

Both logics extend [[first-degree entailment|KXTP4P3GHT]], whose four values separate the two readings of the middle value: "neither true nor false" for $\mathsf{K}_3$ and "both true and false" for $\mathsf{LP}$.
If you designate only $\tfrac12$, the matrix is no longer useful, since then $p \land q \models p$ fails at $p = 1$, $q = \tfrac12$.

## Explanations

### L1 human

Take three values: true, false and a middle value.
In one logic the middle value counts as "not true", and in the other it counts as "true enough".
The tables are the same, but different arguments become valid.
For example, "$p$ and not $p$, so anything" is valid in the first logic and invalid in the second.

### L2 human

To separate two logics on one algebra, fix the algebra and list the valuations of the variables of an inference.
Mark the rows in which all premises are designated, and check the conclusion in these rows only.
For explosion in $\mathsf{LP}$, the marked rows are those with $p = \tfrac12$, and the row with $q = 0$ fails.
For explosion in $\mathsf{K}_3$, no row is marked, so the inference holds with nothing to check.
Watch out: a valuation that refutes an inference in one matrix can satisfy it in the other, so fix the designated set before the check.
