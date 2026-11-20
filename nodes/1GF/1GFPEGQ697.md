---
tag: 1GFPEGQ697
kind: example
name: Excluded middle in LP and in K3
msc: ["03B53", "03B50"]
topics: [NJB94B39QK]
audience: ug2
instance_of: [BXJZG67PX3]
uses: [W28EY7C3FA, 0RYYK8PG4S, MP4R7T546Z, SZHA10A9X7]
sources:
  - url: https://en.wikipedia.org/wiki/Three-valued_logic
    locator: Kleene and Priest logics
  - book: isbn:9780521670265
---

## Example

We compute $v(p \lor \neg p)$ for each value of $p$, with the tables of the [[logic of paradox|W28EY7C3FA]].

| $v(p)$ | $v(\neg p)$ | $v(p \lor \neg p)$ |
|---|---|---|
| $1$ | $0$ | $1$ |
| $\tfrac12$ | $\tfrac12$ | $\tfrac12$ |
| $0$ | $1$ | $1$ |

1. In LP, the designated values are $1$ and $\tfrac12$. Every row is designated, so the [[law of excluded middle|0RYYK8PG4S]] $p \lor \neg p$ is an LP tautology.
2. In [[strong Kleene logic|SZHA10A9X7]] K3, only $1$ is designated. The middle row is not designated, so $p \lor \neg p$ is not a K3 tautology.

The same table, with $\neg(p \land \neg p)$ in place of $p \lor \neg p$, gives the values $1$, $\tfrac12$, $1$.
So the [[law of non-contradiction|MP4R7T546Z]] is also an LP tautology and not a K3 tautology.

## Remarks

The example illustrates both parts 1 and 2 of the theorem on LP and K3 tautologies.
The middle row is the all-$\tfrac12$ valuation of part 2.
LP keeps the law of non-contradiction as a tautology, and still rejects explosion; a tautology is not the same as a rule.

## Explanations

### L1 human

"$p$ or not $p$" is accepted in LP for every value of $p$.
In K3, it fails when $p$ has no truth value, since then "$p$ or not $p$" has no truth value either.
So the two logics, with the same tables, disagree about this law.

### L2 human

Read the middle row.
With $v(p) = \tfrac12$, both disjuncts are $\tfrac12$, and so is the disjunction.
LP counts $\tfrac12$ as designated and K3 does not.
A trap is to think that LP rejects non-contradiction because a contradiction can be designated; the formula $\neg(p \land \neg p)$ is still designated in every row.
