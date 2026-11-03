---
tag: 5ZRQC3DG7W
kind: conjecture
name: Exponential time hypothesis
msc: [68Q17, 68Q25, 68Q27]
uses: [3QKF32ZAKN, 0TGV80E6A4]
about: [3QKF32ZAKN]
sources:
  - url: https://en.wikipedia.org/wiki/Exponential_time_hypothesis
history:
  posed_by: Russell Impagliazzo and Ramamohan Paturi
  first_stated: "1999"
---

## Statement

Let $k \ge 3$ be an integer.
The problem $k$-SAT asks whether a Boolean formula in conjunctive normal form with at most $k$ literals per clause is satisfiable.
Let $n$ be the number of variables of the formula.
Let $s_k$ be the infimum of the real numbers $\delta$ such that $k$-SAT can be solved by an algorithm in time $O(2^{\delta n})$.

**Hypothesis.**
$$s_3 > 0.$$
That is, there is a constant $c > 0$ such that no algorithm solves 3-SAT in time $O(2^{c n})$.

## Remarks

The hypothesis is open, and it implies $\mathrm{P} \ne \mathrm{NP}$.
Here time is measured in [[big O notation|0TGV80E6A4]] in the number of variables, which is a natural measure since brute force takes about $2^n$ steps.
The best known algorithms for 3-SAT run in time $O(c^n)$ for constants $c$ somewhat below $1.33$, which is consistent with the hypothesis.

Impagliazzo, Paturi and Zane proved the sparsification lemma.
With it, the hypothesis is equivalent to the same statement with $n$ replaced by the number of clauses.
It then implies that many NP-complete problems, such as finding a $k$-clique or a vertex cover, need time $2^{\Omega(n)}$ or $n^{\Omega(k)}$ in suitable forms.

The *strong exponential time hypothesis* says that $s_k \to 1$ as $k \to \infty$.
It implies the exponential time hypothesis.

## Explanations

### L1 human

Satisfiability of logical formulas can always be decided by trying all $2^n$ ways to set $n$ true-or-false variables.
Clever algorithms do better, but all known ones still take exponential time.
The hypothesis says that this is unavoidable: no algorithm runs in time growing like $2^{o(n)}$.
It is stronger than "P is not NP", and it gives precise lower bounds for many problems.
