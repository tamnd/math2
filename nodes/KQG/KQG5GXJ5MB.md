---
tag: KQG5GXJ5MB
kind: statement
role: proposition
name: Parareal
msc: [65L05, 65Y05]
uses: [0FXDW992DS]
about: [0FXDW992DS]
sources:
  - url: https://en.wikipedia.org/wiki/Parareal
---

## Statement

Consider an [[initial value problem|0FXDW992DS]] with state space $\R^d$ on a time interval $[0, T]$, cut into $N$ slices by times $0 = T_0 < T_1 < \cdots < T_N = T$.
For $n = 0, \ldots, N - 1$, let $\mathcal{F}_n \colon \R^d \to \R^d$ (fine) and $\mathcal{G}_n \colon \R^d \to \R^d$ (coarse) be maps, called propagators.
They approximate the solution at $T_{n+1}$ of the problem started at $T_n$.
Let $Y_0 = y_0$ and $Y_{n+1} = \mathcal{F}_n(Y_n)$ be the sequential fine solution.
The Parareal iteration sets $U_0^k = y_0$ for all $k \ge 0$, $U_{n+1}^0 = \mathcal{G}_n(U_n^0)$, and
$$U_{n+1}^{k+1} = \mathcal{G}_n(U_n^{k+1}) + \mathcal{F}_n(U_n^k) - \mathcal{G}_n(U_n^k), \qquad k \ge 0,\ 0 \le n \le N - 1.$$
Then $U_n^k = Y_n$ for all $k \ge 0$ and $0 \le n \le k$.
In particular, after $N$ iterations the iterates equal the fine solution at every time $T_n$.

## Remarks

The proof is an induction on $k$.
For $k = 0$ only $n = 0$ is concerned, and $U_0^0 = y_0 = Y_0$.
If the claim holds for $k$, then $U_0^{k+1} = Y_0$, and if $U_n^{k+1} = Y_n$ with $n \le k$, then also $U_n^k = Y_n$, so the iteration gives $U_{n+1}^{k+1} = \mathcal{G}_n(Y_n) + \mathcal{F}_n(Y_n) - \mathcal{G}_n(Y_n) = Y_{n+1}$.
The result needs no property of $\mathcal{F}_n$ and $\mathcal{G}_n$; it guarantees termination but no speed-up.
In practice the iteration is stopped after $K$ iterations with $K$ much smaller than $N$, when $\mathcal{G}_n$ is accurate and stable enough for the iterates to converge fast.

## Explanations

### L1 human

Parareal is a way to use many processors on a problem that seems purely sequential: marching forward in time.
A cheap coarse solver first gives rough values at the start of each time slice.
Then all slices are solved accurately at the same time, in parallel, from these rough starting values.
A cheap sequential sweep corrects the starting values, and the process repeats.
The statement says that the correct values spread forward by at least one slice per iteration.
So the iteration reaches the fine solution after at most as many iterations as there are slices.

### L2 human

The expensive fine solves $\mathcal{F}_n(U_n^k)$ for all $n$ are independent, so they run in parallel; only the coarse sweep is sequential.
The parallel speed-up is bounded by about $N/K$, so the method pays off only when it converges in few iterations.
It works well for diffusive problems and less well for hyperbolic or highly oscillatory ones.
Parareal can be seen as a multiple shooting method in which a Newton step is approximated with the coarse propagator.
