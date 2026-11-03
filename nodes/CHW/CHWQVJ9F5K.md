---
tag: CHWQVJ9F5K
kind: statement
role: theorem
name: Gale–Shapley algorithm
msc: [91B68, 05C70, 68W40]
uses: [X201T4TP0Y]
about: [X201T4TP0Y]
sources:
  - url: https://en.wikipedia.org/wiki/Gale%E2%80%93Shapley_algorithm
same_as:
  wikidata: Q65123731
  wikipedia: Gale–Shapley algorithm
---

## Statement

Consider an instance of the [[stable marriage problem|X201T4TP0Y]] with $n$ men and $n$ women.
Each person has a strict ranking of all members of the other side.
The *men-proposing deferred acceptance algorithm* runs as follows.
While some man is unmatched, such a man proposes to his favourite among the women who have not yet rejected him.
If she is unmatched, she accepts.
If she prefers the proposer to her current partner, she accepts and rejects her partner.
Otherwise she rejects the proposer.
Then:

1. the algorithm stops after at most $n^2$ proposals, and its output is a stable matching;
2. in this matching every man is matched to the best partner he has in any stable matching;
3. in this matching every woman is matched to the worst partner she has in any stable matching.

## Remarks

Each man proposes to each woman at most once, which bounds the number of proposals.
A woman, once matched, stays matched and only trades up, so at the end all are matched.
If $(m, w)$ blocked the result, then $m$ would have proposed to $w$ before his final partner, and $w$ would have kept someone she prefers to $m$.
For part 2 one shows that no man is ever rejected by a woman who is his partner in some stable matching.
Example: let $m_1$ rank $w_1 > w_2$, $m_2$ rank $w_2 > w_1$, $w_1$ rank $m_2 > m_1$, and $w_2$ rank $m_1 > m_2$.
The men-proposing algorithm gives $\set{(m_1, w_1), (m_2, w_2)}$, the women-proposing one gives $\set{(m_1, w_2), (m_2, w_1)}$, and both are stable.
In particular, a stable matching exists for every instance.

## Explanations

### L1 human

Men propose in order of their preferences, and women hold on to the best proposal so far, letting it go if a better one arrives.
The process always ends in a stable pairing, so no man and woman would both rather be together.
The side that proposes gets its best possible stable outcome.

### L2 human

The algorithm is the basis of real assignment systems, such as the matching of medical residents to hospitals and of students to schools.
It extends to the many-to-one case of hospitals with several positions and to incomplete preference lists.
For the proposing side, reporting true preferences is a dominant strategy, but not for the receiving side.
Comparing the man-optimal and woman-optimal outcomes leads to the lattice of stable matchings.
