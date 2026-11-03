---
tag: JQTTAK1242
kind: definition
name: Branch and price
msc: [90C57, 90C06, 90C10]
defines: 2A9PYZ3F4H
uses: [ZZ7C50WN56, X8JZFMSYT1, PYMHHM5Z6F, 9GX3WH5EQF]
sources:
  - url: https://en.wikipedia.org/wiki/Branch_and_price
---

## Definition

Let $N$ be a finite index set, too large to list, with columns $a_j \in \R^m$ and costs $c_j \in \R$ given implicitly through a pricing problem.
Let $b \in \R^m$, and consider the [[integer program|9GX3WH5EQF]]
$$\text{minimize } \sum_{j \in N} c_j x_j \quad \text{subject to} \quad \sum_{j \in N} a_j x_j = b, \quad x_j \in \Z_{\ge 0} \ (j \in N).$$
*Branch and price* is the [[branch and bound|ZZ7C50WN56]] method for this program with the following two features.

1. The bound at each subproblem is the optimal value of its [[linear programming relaxation|PYMHHM5Z6F]], computed by [[column generation|X8JZFMSYT1]]. The pricing problem is restricted to the columns allowed at that subproblem.
2. A subproblem whose relaxation optimum is fractional is split by a branching rule. The conditions of the rule must be expressible in the pricing problem.

## Remarks

Branching on a single variable, $x_j = 0$ or $x_j \ge 1$, is usually avoided: the branch $x_j = 0$ forbids one column, and the pricing problem may generate the same column again.
A common rule for set partitioning problems, due to Ryan and Foster, branches on a pair of rows $r, s$.
Either they are covered by the same column, or by different columns.

Example: in a vehicle routing problem, each column is a feasible route, and pricing is a shortest path problem with resource constraints.
Branching on whether customers $r$ and $s$ are on the same route changes only the graph of the pricing problem.

Non-example: [[branch and bound|ZZ7C50WN56]] on a formulation with a small, fixed set of variables, solving each relaxation directly by the simplex method, is not branch and price.
