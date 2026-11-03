---
tag: 2M8CRHVZA0
kind: definition
name: Optimal job scheduling
msc: [90B35, 68M20, 90C27]
defines: GP8CM94ST5
uses: [NS0Q42Y3FX]
sources:
  - url: https://en.wikipedia.org/wiki/Optimal_job_scheduling
---

## Definition

A *scheduling problem* has a finite set $M$ of machines and a finite set $J$ of jobs.
Each job $j$ has a processing time $p_{ij} \ge 0$ on each machine $i$.
The problem also fixes the admissible schedules and an objective.
A *schedule* assigns to each job $j$ a finite set of pairs $(i, I)$ of a machine $i$ and a time interval $I \subseteq [0, \infty)$ such that:

1. no machine processes two jobs at the same time;
2. no job is processed on two machines at the same time;
3. each job gets the processing its environment requires, such as $p_{ij}$ units on one chosen machine $i$, or on every machine in a fixed order;
4. the extra constraints of the problem hold, such as release dates, precedence constraints between jobs, or the ban on preemption.

The *completion time* $C_j$ of job $j$ is the end of its last interval.
*Optimal job scheduling* asks for an admissible schedule that minimizes the objective, a nondecreasing function of $(C_j)_{j \in J}$.
Standard objectives are the makespan $C_{\max} = \max_j C_j$ and the total completion time $\sum_j C_j$.

## Remarks

Example: one machine and jobs with times $3, 1, 2$, without preemption, objective $\sum_j C_j$.
Processing them in the order of times $1, 2, 3$ (shortest first) gives completion times $1, 3, 6$ and total $10$.
All four clauses hold, and this shortest-first rule is optimal for this problem.

Non-example: on one machine, run the job of time $3$ during $[0, 3]$ and the job of time $1$ during $[2, 3]$.
This fails clause 1, since both jobs run on the machine during $[2, 3]$.

The three-field notation $\alpha \mid \beta \mid \gamma$ records the machine environment $\alpha$, the job constraints $\beta$ and the objective $\gamma$.
For $\alpha$, the symbol $1$ means one machine, $P_m$ means $m$ identical parallel machines, $F_m$ a flow shop and $J_m$ a job shop.
For $\beta$, typical entries are $r_j$ (release dates), $\mathrm{prec}$ (precedence) and $\mathrm{pmtn}$ (preemption).
For example, $P_m \| C_{\max}$ is makespan minimization on $m$ identical machines.
