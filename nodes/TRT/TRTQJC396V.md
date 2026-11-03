---
tag: TRTQJC396V
kind: definition
name: Wardrop equilibrium
msc: [90B20, 91A14, 90C35]
defines: F2SMTMBDP0
uses: [0KFYGSHHF5, 03NAMV1DHJ]
sources:
  - url: https://en.wikipedia.org/wiki/Wardrop_equilibrium
---

## Definition

Let $(V, E)$ be a finite [[directed graph|0KFYGSHHF5]].
Each edge $e$ has a latency function $\ell_e \colon [0, \infty) \to [0, \infty)$ that is continuous and nondecreasing.
There are pairs $(s_1, t_1), \dots, (s_k, t_k)$ of vertices with traffic rates $r_1, \dots, r_k > 0$.
Let $\mathcal{P}_i$ be the set of directed [[paths|03NAMV1DHJ]] from $s_i$ to $t_i$, assumed nonempty, and let $\mathcal{P} = \bigcup_i \mathcal{P}_i$.
A *feasible flow* is a function $f \colon \mathcal{P} \to [0, \infty)$ with $\sum_{P \in \mathcal{P}_i} f_P = r_i$ for each $i$.
Its edge flow is $f_e = \sum_{P \ni e} f_P$, and the latency of a path $P$ is $\ell_P(f) = \sum_{e \in P} \ell_e(f_e)$.

A feasible flow $f$ is a *Wardrop equilibrium* if, for every $i$ and all $P, Q \in \mathcal{P}_i$ with $f_P > 0$,
$$\ell_P(f) \le \ell_Q(f).$$

## Remarks

Equivalently, all paths of $\mathcal{P}_i$ that carry flow have the same latency, and it is the least latency over $\mathcal{P}_i$.
A Wardrop equilibrium always exists: the feasible flows that minimize the potential $\sum_{e \in E} \int_0^{f_e} \ell_e(x)\, dx$ are exactly the equilibria.
An equilibrium need not minimize the total travel time $\sum_e f_e \ell_e(f_e)$; see [[Braess's paradox|VTPMBJAHD7]].

Example (Pigou's network): two parallel edges from $s$ to $t$ with $\ell_1(x) = 1$ and $\ell_2(x) = x$, and rate $r = 1$.
The flow with $f_2 = 1$ and $f_1 = 0$ is an equilibrium, since the used path has latency $\ell_2(1) = 1 \le \ell_1 = 1$.

Non-example: in the same network, the split $f_1 = f_2 = 1/2$ is not an equilibrium.
The first edge carries flow and has latency $1$, but the second has latency $1/2 < 1$.
