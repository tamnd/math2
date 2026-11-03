---
tag: XHK1K3RM0X
kind: statement
role: theorem
name: Johnson's rule
msc: [90B35, 68M20]
uses: [TKNK10024E, 2M8CRHVZA0]
about: [TKNK10024E]
sources:
  - url: https://en.wikipedia.org/wiki/Johnson's_rule
same_as:
  wikidata: Q1662347
  wikipedia: Johnson's rule
---

## Statement

Consider a two-machine [[flow shop|TKNK10024E]] with $n$ jobs and no preemption.
Each job $j$ must be processed first on machine $1$ for a time $a_j \ge 0$, then on machine $2$ for a time $b_j \ge 0$.
Order the jobs as follows: first the jobs with $a_j \le b_j$, in nondecreasing order of $a_j$; then the jobs with $a_j > b_j$, in nonincreasing order of $b_j$.
Process the jobs in this order on both machines, each job as early as possible.
Then this schedule minimizes the makespan among all feasible schedules.

## Remarks

First, an exchange argument shows that one may use the same order on both machines without loss.
For a fixed order, the makespan equals $\max_{1 \le k \le n} \big( \sum_{j \le k} a_{\sigma(j)} + \sum_{j \ge k} b_{\sigma(j)} \big)$.
Swapping two adjacent jobs $u$ before $v$ never increases this maximum when $\min(a_u, b_v) \le \min(a_v, b_u)$, and Johnson's order satisfies this condition for every adjacent pair.
Example: jobs with $(a_j, b_j) = (3, 6), (5, 2), (1, 2), (6, 6), (7, 5)$.
The first group, sorted by $a$, is $(1, 2), (3, 6), (6, 6)$; the second group, sorted by decreasing $b$, is $(7, 5), (5, 2)$.
The makespan of this order is $24$, and the lower bound $\sum a_j + \min_j b_j = 22 + 2 = 24$ shows that it is optimal.
The rule does not extend to three or more machines in general, where the problem is NP-hard.

## Explanations

### L1 human

Two workers form a line: the first prepares each job, the second finishes it.
Jobs that are quick to prepare should go first, so the second worker starts soon.
Jobs that are quick to finish should go last, so the second worker does not have much left after the first one stops.
Johnson's rule turns this intuition into an exact recipe.

### L2 human

The rule is due to Selmer Johnson (1954) and is one of the first exact results in [[scheduling|GP8CM94ST5]].
It shows that $F_2 \| C_{\max}$ is solvable in time $O(n \log n)$, in contrast with $F_3 \| C_{\max}$, which is strongly NP-hard.
It also solves some special three-machine cases, when the middle machine is dominated, by applying the rule to the sums $a_j + b_j$ and $b_j + c_j$.
It is a common building block of heuristics for larger flow shops.
