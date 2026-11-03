---
tag: WV2N01B4YV
kind: problem
name: True quantified Boolean formula
msc: [68Q17, 68Q15, 03B70]
uses: [YAVW1XHNFH, QN7M1JCGT9]
about: [T9NTRY93ZT]
sources:
  - url: https://en.wikipedia.org/wiki/True_quantified_Boolean_formula
same_as:
  wikidata: Q1350285
  wikipedia: True quantified Boolean formula
history:
  posed_by: "Larry Stockmeyer and Albert Meyer"
  first_stated: "1973"
---

## Problem

Let $n \ge 1$.
A *fully quantified Boolean formula* has the form
$$Q_1 x_1 \, Q_2 x_2 \cdots Q_n x_n \; \varphi(x_1, \ldots, x_n).$$
Here each $Q_i$ is $\exists$ or $\forall$, and the variables $x_i$ range over $\set{0, 1}$.
The body $\varphi$ is a propositional formula in the variables $x_1, \ldots, x_n$.
Such a formula has no free variables, so it is either true or false.
The [[decision problem|YAVW1XHNFH]] TQBF asks, given a fully quantified Boolean formula, whether it is true.

## Remarks

Larry Stockmeyer and Albert Meyer showed in 1973 that TQBF is complete for [[PSPACE|T9NTRY93ZT]] under polynomial-time many-one reductions.
It is in PSPACE because a recursive evaluation needs to store only one value per quantifier at a time, so it uses space polynomial in the length of the formula.
When all quantifiers are $\exists$, the problem is the [[satisfiability|QN7M1JCGT9]] problem for $\varphi$, which is NP-complete.
When the quantifier prefix has at most $k$ blocks and starts with $\exists$, the restricted problem is complete for the level $\Sigma_k^p$ of the [[polynomial hierarchy|TDQ7AXGM6P]].
TQBF can be seen as a game: one player chooses the existential variables and the other the universal ones.
The formula is true when the first player has a winning strategy.

## Explanations

### L1 human

A quantified Boolean formula asks a question like "is there a value of $x$ such that for every value of $y$ the statement $\varphi(x, y)$ holds?".
With only "there is" quantifiers, this is the satisfiability puzzle.
Allowing "for every" as well makes the problem harder: it captures every problem that can be solved with a polynomial amount of memory.
For example, $\forall x \, \exists y \, (x \ne y)$ is true, since $y$ can be chosen as the opposite of $x$, while $\exists y \, \forall x \, (x \ne y)$ is false.
