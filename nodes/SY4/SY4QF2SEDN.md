---
tag: SY4QF2SEDN
kind: statement
role: theorem
name: List scheduling and Graham's bound
msc: [90B35, 68W25, 68M20]
uses: [2M8CRHVZA0, 4WEVBDQ8SR, PSM6NKYJB8]
about: [GP8CM94ST5]
sources:
  - url: https://en.wikipedia.org/wiki/List_scheduling
same_as:
  wikidata: Q6646016
  wikipedia: List scheduling
---

## Statement

Let $m \ge 1$ identical machines and $n$ jobs with processing times $p_1, \dots, p_n > 0$ be given, without preemption.
*List scheduling* takes the jobs in a given order.
It assigns each job, in turn, to a machine that becomes free earliest, and starts it at that time.
Let $C$ be the makespan of the resulting schedule and $C^*$ the minimal makespan over all schedules.
Then
$$C \le \Big(2 - \frac{1}{m}\Big) C^*,$$
for every order of the list, and the factor $2 - 1/m$ cannot be lowered.

## Remarks

Let job $k$ finish last, at time $C$, and let $s_k = C - p_k$ be its start time.
Before $s_k$ all machines are busy, so $m s_k \le \sum_{j \ne k} p_j$, and $C \le \frac1m \sum_j p_j + \big(1 - \frac1m\big) p_k$.
Both $\frac1m \sum_j p_j$ and $p_k$ are at most $C^*$, which gives the bound.
Tightness: take $m(m - 1)$ jobs of time $1$ followed by one job of time $m$; list scheduling gives $C = 2m - 1$, while $C^* = m$.
The same bound holds when the jobs have precedence constraints and a job is started only once its predecessors are done.
Sorting the list by nonincreasing processing time (the LPT rule) improves the factor to $\frac43 - \frac{1}{3m}$.

## Explanations

### L1 human

Hand out jobs one by one, always to the worker who is free first.
This simple greedy method never takes more than about twice as long as the best possible plan.
The reason is that every worker was busy until the last job started, and the last job itself is not longer than the best plan.

### L2 human

Ronald Graham proved the bound in 1966, in one of the first worst-case analyses of an [[approximation algorithm|4WEVBDQ8SR]].
It is also an early example of what is now called competitive analysis, since list scheduling assigns jobs online without knowing future ones.
The problem $P_m \| C_{\max}$ itself is NP-hard, even for $m = 2$, so a fast algorithm with a guaranteed factor is the natural goal.
