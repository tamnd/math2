---
tag: RQVB74V0AS
kind: definition
name: Nucleolus
msc: [91A12]
defines: DWA0FP9FC9
uses: [39HGM44CFZ, CBP13S0ETD]
sources:
  - url: https://en.wikipedia.org/wiki/Nucleolus_(game_theory)
---

## Definition

Let $(N, v)$ be a [[cooperative game with transferable utility|39HGM44CFZ]] with $n = \abs{N}$ players, and write $x(S) = \sum_{i \in S} x_i$ for $x \in \R^N$.
An *imputation* is a vector $x \in \R^N$ with $x(N) = v(N)$ and $x_i \ge v(\set{i})$ for every $i \in N$.
The *excess* of a coalition $S$ at $x$ is $e(S, x) = v(S) - x(S)$.
Let $\theta(x) \in \R^{2^n - 2}$ list the excesses $e(S, x)$ of all nonempty proper coalitions $S \subsetneq N$ in weakly decreasing order.
The *nucleolus* is the set of imputations $x$ such that $\theta(x)$ is lexicographically minimal among the vectors $\theta(y)$, $y$ an imputation.

## Remarks

If the set of imputations is nonempty, the nucleolus consists of exactly one imputation, and one speaks of the nucleolus as a point.
Example: in the three-player majority game, where $v(S) = 1$ if $\abs{S} \ge 2$ and $v(S) = 0$ otherwise, the nucleolus is $(1/3, 1/3, 1/3)$.
At this point every pair has excess $1 - 2/3 = 1/3$; at any other imputation some pair $S$ has $x(S) < 2/3$, so the largest excess exceeds $1/3$.
Non-example: $(1/2, 1/2, 0)$ is an imputation of this game, but the pair $\set{1, 3}$ has excess $1/2 > 1/3$, so it is not the nucleolus.
If the [[core|CBP13S0ETD]] is nonempty, the nucleolus lies in the core, because core points are exactly the imputations whose largest excess is at most $0$.
The nucleolus can be computed by solving a finite sequence of linear programs.

## Explanations

### L1 human

The excess of a group measures how unhappy it is with a split.
The nucleolus is the split that makes the unhappiest group as happy as possible, breaking ties by looking at the next unhappiest group.
