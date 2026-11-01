---
tag: PA7ZQ6C6SP
kind: statement
role: theorem
name: Löwner's theorem
msc: [47A63, 15A45, "30E20"]
uses: [N155BSJ2DN, 0Q1D85B8G6, 0P17NGQQMQ, 9G9S92T1VJ]
about: [N155BSJ2DN]
sources:
  - url: https://en.wikipedia.org/wiki/Operator_monotone_function
---

## Statement

Let $a < b$ be real numbers, possibly $a = -\infty$ or $b = \infty$, and let $f \colon (a, b) \to \R$.
Let $\mathbb{H} = \set{z \in \C : \operatorname{Im} z > 0}$ be the upper half-plane.
Then $f$ is [[operator monotone|N155BSJ2DN]] on $(a, b)$ if and only if there is a holomorphic function $F$ on $\C \setminus \bigl( (-\infty, a] \cup [b, \infty) \bigr)$ such that:

1. $F(t) = f(t)$ for all $t \in (a, b)$;
2. $F(\bar z) = \overline{F(z)}$ for all $z$ in the domain of $F$;
3. $\operatorname{Im} F(z) \ge 0$ for all $z \in \mathbb{H}$.

## Remarks

So an operator monotone function is real analytic, and it extends to a holomorphic map from $\mathbb{H}$ into the closed upper half-plane, a so-called Pick function.
Example: for $0 < p < 1$, the function $t^p$ on $(0, \infty)$ extends to $z^p$ with the principal branch.
It maps $\mathbb{H}$ into the sector of arguments between $0$ and $p\pi$, which lies in $\mathbb{H}$, so $t^p$ is operator monotone.
In the same way $\log t$ is operator monotone on $(0, \infty)$, since $\log z$ maps $\mathbb{H}$ into the strip $0 < \operatorname{Im} w < \pi$.
In contrast, $z^2$ maps $-1 + i \in \mathbb{H}$ to $-2i$, so $t^2$ is not operator monotone on $(0, \infty)$.
One route to the proof goes through divided differences.
A function $f$ of class $C^1$ is operator monotone if and only if the following holds for all points $t_1, \dots, t_n$ of $(a, b)$.
The matrix with entries $(f(t_i) - f(t_j)) / (t_i - t_j)$ off the diagonal and $f'(t_i)$ on the diagonal is [[positive semidefinite|01MMVW8CKC]].

## Explanations

### L1 human

Keeping the order of Hermitian matrices of every size is a very strong demand on a function.
Löwner's theorem says that exactly the functions that extend to the complex upper half-plane and send it into itself meet this demand.
This turns a question about matrices into a question about holomorphic functions.

### L2 human

The theorem gives integral representations of operator monotone functions, through the Nevanlinna representation of Pick functions.
It explains at once why $t^p$ is operator monotone on $(0, \infty)$ exactly for $0 \le p \le 1$.
Operator monotone functions appear in matrix inequalities, in the theory of operator means and in quantum information.
