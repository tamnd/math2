---
tag: KGQSYD1G5V
kind: definition
name: Value iteration and policy iteration
msc: [90C40, 90C39]
defines: NPM6VD9TZ1
uses: [EC0HKSBVQ7, Z94Z6BY8JG]
sources:
  - url: https://en.wikipedia.org/wiki/Markov_decision_process
    locator: Algorithms
---

## Definition

Let $(S, A, P, r, \gamma)$ be a discounted [[Markov decision process|WCNHWTJXYD]] with finite $S$ and $A$ and $\gamma \in [0, 1)$.
For $V \colon S \to \R$ and $s \in S$, $a \in A$, put $Q_V(s, a) = r(s, a) + \gamma \sum_{s' \in S} P(s' \mid s, a) V(s')$, and let the *Bellman operator* be $(\mathcal{T} V)(s) = \max_{a \in A} Q_V(s, a)$.
A map $f \colon S \to A$ is *greedy* for $V$ if $Q_V(s, f(s)) = \max_{a} Q_V(s, a)$ for all $s$.
For a map $f \colon S \to A$, let $V^f$ be the value of the stationary policy $f$, the unique solution of the linear system $V(s) = r(s, f(s)) + \gamma \sum_{s'} P(s' \mid s, f(s)) V(s')$.

*Value iteration* starts from any $V_0 \colon S \to \R$, sets $V_{k+1} = \mathcal{T} V_k$ for $k \ge 0$, and after stopping at some $k$ returns a greedy map for $V_k$.

*Policy iteration* starts from any map $f_0 \colon S \to A$ and repeats the following steps for $k = 0, 1, 2, \dots$:

1. evaluation: compute $V^{f_k}$ by solving the linear system above;
2. improvement: choose $f_{k+1}$ greedy for $V^{f_k}$, keeping $f_{k+1}(s) = f_k(s)$ whenever $f_k(s)$ already attains the maximum;
3. stop when $f_{k+1} = f_k$ and return $f_k$.

## Remarks

Example: one state $s$ and two actions with rewards $r(s, a_1) = 1$ and $r(s, a_2) = 2$, and $\gamma = 1/2$.
Value iteration from $V_0 = 0$ gives $V_k = 4(1 - 2^{-k})$, which tends to $V^* = 4$, and the greedy action is $a_2$ from $k = 0$ on.
Policy iteration from $f_0 = a_1$ evaluates $V^{f_0} = 2$, improves to $f_1 = a_2$ with $V^{f_1} = 4$, and stops at the next step.

Non-example: if $\gamma = 1$, the linear system of the evaluation step may have no solution or many, so the definition of $V^f$ breaks down.
For instance, with one state and reward $1$ it reads $V = 1 + V$.

The operator $\mathcal{T}$ is a [[contraction mapping|0QN69YA357]] of modulus $\gamma$ in the maximum norm, so value iteration satisfies $\max_s \abs{V_k(s) - V^*(s)} \le \gamma^k \max_s \abs{V_0(s) - V^*(s)}$.
Policy iteration produces values $V^{f_0} \le V^{f_1} \le \cdots$, with strict improvement in some state until it stops, so it stops after at most $\abs{A}^{\abs{S}}$ rounds with an optimal policy.
