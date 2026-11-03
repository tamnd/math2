---
tag: J02XAHCZ1W
kind: statement
role: theorem
name: Brunovsky normal form
msc: [93B10, 93B17, 93B52]
uses: [A9WFM77Z4P, 9NSCZ2KBEB, 0ZC9YTXZRY, 0EB9N0S33C, 0JV30XN73Z, 7NYES2D0Z4, VZACRS73RY]
about: [A9WFM77Z4P]
sources:
  - url: https://en.wikipedia.org/wiki/Controllability
---

## Statement

Let $1 \le m \le n$, let $A$ be a real $n \times n$ matrix and let $B$ be a real $n \times m$ matrix of [[rank|0ZC9YTXZRY]] $m$ such that $x' = Ax + Bu$ is [[controllable|A9WFM77Z4P]].
For $k \ge 1$ let $J_k$ be the $k \times k$ matrix with ones on the superdiagonal and zeros elsewhere.
Let $e_k$ be the last standard basis vector of $\R^k$.
For $k \ge 0$ let $r_k$ be the rank of $\begin{pmatrix} B & AB & \cdots & A^{k-1} B \end{pmatrix}$, with $r_0 = 0$.
Then:

1. There are integers $\kappa_1 \ge \kappa_2 \ge \cdots \ge \kappa_m \ge 1$ with sum $n$, the *controllability indices*, determined as follows. For each $k \ge 1$, the number of $i$ with $\kappa_i \ge k$ equals $r_k - r_{k-1}$.
2. There are [[invertible|0EB9N0S33C]] real matrices $T \in \R^{n \times n}$ and $G \in \R^{m \times m}$ and a real matrix $F \in \R^{m \times n}$ with
$$T^{-1} (A + BF) T = \operatorname{diag}(J_{\kappa_1}, \ldots, J_{\kappa_m}), \qquad T^{-1} B G = \operatorname{diag}(e_{\kappa_1}, \ldots, e_{\kappa_m}),$$
with block diagonal right-hand sides.
3. Two such pairs $(A, B)$ and $(A', B')$ of the same sizes are related in this way if and only if they have the same controllability indices.

## Remarks

The transformation in part 2 is the change of state $x = Tz$, together with the [[feedback|7NYES2D0Z4]] and input change $u = Fx + Gv$; it gives $z' = T^{-1}(A + BF) T z + T^{-1} B G v$.
The normal form consists of $m$ independent chains of integrators $z' = J_{\kappa_i} z + e_{\kappa_i} v_i$, of lengths $\kappa_1, \ldots, \kappa_m$.
For this normal form, $r_k = \sum_i \min(\kappa_i, k)$, so $r_k - r_{k-1}$ counts the chains of length at least $k$; the ranks $r_k$ do not change under the transformations, which gives part 3.
By part 1 the indices form an [[integer partition|0JV30XN73Z]] of $n$, the conjugate of the partition $(r_1 - r_0, r_2 - r_1, \ldots)$.
For $m = 1$ there is a single chain of length $n$; it is the [[controllable canonical form|VZACRS73RY]] with all coefficients $a_i$ removed by feedback.
Example: for $n = 3$, $m = 2$, $A = J_3$ and $B = \begin{pmatrix} 0 & 1 \\ 0 & 0 \\ 1 & 0 \end{pmatrix}$ one gets $r_1 = 2$, $r_2 = 3$, so the indices are $\kappa = (2, 1)$.

## Explanations

### L1 human

A controllable linear system with several inputs looks complicated, but up to a change of variables and a feedback it is very simple.
It is a set of separate chains, each driven by one input, in which each variable is the derivative of the next one.
The only thing that remains of the original system is the list of chain lengths.
So controllable linear systems are classified by a few whole numbers.

### L2 human

The result classifies controllable pairs $(A, B)$ under the feedback group: state changes, input changes and state feedback.
The controllability indices are computed from the ranks of the blocks of the Kalman matrix used in the [[Kalman rank condition|9NSCZ2KBEB]].
The form is the linear model case of differential flatness: the first variable of each chain is a flat output, and the state and input are its derivatives.
It is also the starting point of exact feedback linearization, which asks when a nonlinear system can be brought to this form.
