---
tag: D2V617HTVA
kind: definition
name: Flux balance analysis
msc: [92C42, 90C05]
defines: ADAQK6EKYV
uses: [VNMXB0J2KA, 0PHDYNR24D, 0VD9ZSWWJG]
sources:
  - url: https://en.wikipedia.org/wiki/Flux_balance_analysis
---

## Definition

Consider a metabolic network with $m$ internal metabolites and $n$ reactions, with stoichiometric [[matrix|0VD9ZSWWJG]] $S \in \R^{m \times n}$.
The entry $S_{ik}$ is the net number of molecules of metabolite $i$ produced by one unit of reaction $k$.
Let $\ell, u \in (\R \cup \set{\pm\infty})^n$ with $\ell \le u$ be lower and upper bounds on the fluxes, and let $c \in \R^n$ be an objective vector.
*Flux balance analysis* is the [[linear program|VNMXB0J2KA]]
$$\text{maximize } c^T v \quad \text{subject to} \quad S v = 0, \quad \ell \le v \le u,$$
over flux vectors $v \in \R^n$; an optimal $v$ is a predicted steady-state flux distribution.

## Remarks

The condition $S v = 0$ says that $v$ lies in the [[null space|0PHDYNR24D]] of $S$, so each internal metabolite is produced and consumed at the same rate.
Irreversible reactions have $\ell_k = 0$, and exchange reactions with the medium carry the bounds on uptake.
Example: the chain uptake $\to A$, $A \to B$, $B \to$ out, with fluxes $v_1, v_2, v_3$, has $S = \begin{pmatrix} 1 & -1 & 0 \\ 0 & 1 & -1 \end{pmatrix}$, so $S v = 0$ forces $v_1 = v_2 = v_3$; with bounds $0 \le v_k \le 10$ and $c = (0, 0, 1)$, the optimum is $v = (10, 10, 10)$.
Non-example: a flux vector with $v_1 = 10$, $v_2 = 5$, $v_3 = 5$ is not feasible, since metabolite $A$ would accumulate at rate $5$.
When an optimum exists, the optimal value is unique, but the optimal flux vector often is not; flux variability analysis computes the range of each $v_k$ over all optimal solutions.
