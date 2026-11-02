---
tag: NCZZ90R5Y6
kind: definition
name: Fourier–Motzkin elimination
msc: [90C05, 15A39, 52B55]
defines: MJQARBFG10
uses: [033DA1WE8Y]
sources:
  - url: https://en.wikipedia.org/wiki/Fourier%E2%80%93Motzkin_elimination
---

## Definition

Let a system $S$ of $m$ linear inequalities in real variables $x_1, \dots, x_n$ be given by
$$\sum_{j=1}^{n} a_{ij} x_j \le b_i, \qquad i = 1, \dots, m,$$
with $a_{ij}, b_i \in \R$.
Split the indices into $I_+ = \set{i : a_{in} > 0}$, $I_- = \set{i : a_{in} < 0}$ and $I_0 = \set{i : a_{in} = 0}$.
The *Fourier–Motzkin elimination* of $x_n$ from $S$ is the system $S'$ in $x_1, \dots, x_{n-1}$ consisting of:

1. the inequalities of $S$ with index in $I_0$;
2. for each pair $(i, k) \in I_+ \times I_-$, the inequality
$$\sum_{j=1}^{n-1} \left(a_{in} a_{kj} - a_{kn} a_{ij}\right) x_j \le a_{in} b_k - a_{kn} b_i,$$
obtained by adding $a_{in}$ times inequality $k$ to $-a_{kn}$ times inequality $i$, so that $x_n$ cancels.

## Remarks

The main property: $(x_1, \dots, x_{n-1})$ satisfies $S'$ if and only if there is $x_n \in \R$ such that $(x_1, \dots, x_n)$ satisfies $S$.
Indeed, inequalities in $I_+$ give upper bounds on $x_n$ and those in $I_-$ give lower bounds, and $S'$ says exactly that each lower bound is at most each upper bound.
So the solution set of $S'$ is the [[projection|033DA1WE8Y]] of the solution set of $S$ forgetting $x_n$.

Example: for $-x \le 0$, $-y \le 0$, $x + y \le 1$, eliminating $y$ pairs $x + y \le 1$ (in $I_+$) with $-y \le 0$ (in $I_-$) and gives $x \le 1$.
With $-x \le 0$ from $I_0$, the result is $0 \le x \le 1$, the projection of the triangle onto the $x$-axis.

Non-example: the method does not work for integer solutions.
The system $x - 2y \le 0$, $-x + 2y \le 0$ with $x = 1$ has the real solution $y = 1/2$, but no integer solution $y$, while elimination of $y$ gives no condition that excludes $x = 1$.

The new system can have up to $\abs{I_0} + \abs{I_+} \cdot \abs{I_-}$ inequalities, at most $m^2/4$ when $I_0$ is empty, so repeated elimination can blow up quickly.
