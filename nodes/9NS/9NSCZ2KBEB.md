---
tag: 9NSCZ2KBEB
kind: statement
role: theorem
name: Kalman rank condition
msc: [93B05, 93C05]
uses: [ZPDTVZQN5K, A9WFM77Z4P, 0ZC9YTXZRY, 020M04FN1H, 0F765KFC2J, C4HN3EAQWM]
about: [A9WFM77Z4P]
sources:
  - url: https://en.wikipedia.org/wiki/Controllability
---

## Statement

Let $n, m \ge 1$, let $A$ be a real $n \times n$ matrix and let $B$ be a real $n \times m$ matrix.
Consider the linear [[control system|ZPDTVZQN5K]] $x' = A x + B u$ with control set $\R^m$.
The system is [[controllable|A9WFM77Z4P]] if and only if the $n \times nm$ matrix
$$\mathcal{C} = \begin{pmatrix} B & AB & A^2 B & \cdots & A^{n-1} B \end{pmatrix}$$
has [[rank|0ZC9YTXZRY]] $n$.
In that case every state can be steered to every other state in any prescribed time $T > 0$.

## Remarks

The proof uses the controllability Gramian $W_T = \int_0^T e^{-As} B B^T e^{-A^T s} \, ds$, built from the [[matrix exponential|020M04FN1H]].
A vector $v$ lies in the kernel of $W_T$ exactly when $v^T e^{-As} B = 0$ for all $s \in [0, T]$, and by Taylor expansion and the [[Cayley–Hamilton theorem|0F765KFC2J]] this holds exactly when $v^T A^k B = 0$ for $k = 0, \ldots, n - 1$.
So $W_T$ is invertible if and only if $\rank \mathcal{C} = n$.
If $W_T$ is invertible, the control $u(s) = B^T e^{-A^T s} W_T^{-1} (e^{-AT} x_1 - x_0)$ steers $x_0$ to $x_1$ in time $T$.
If $\rank \mathcal{C} < n$, every trajectory from $0$ stays in the column space of $\mathcal{C}$, so the states outside it are not reachable from $0$.
Example: for the double integrator, $A = \begin{pmatrix} 0 & 1 \\ 0 & 0 \end{pmatrix}$ and $B = \begin{pmatrix} 0 \\ 1 \end{pmatrix}$ give $\mathcal{C} = \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}$, of rank $2$, so the system is controllable.

## Explanations

### L1 human

The control pushes the state in the directions of the columns of $B$.
The dynamics then turns these directions by $A$, then by $A$ again, and so on.
The test says that the system can be steered anywhere exactly when all these directions together span the whole state space.
It turns a question about all possible control functions into the rank of one matrix.

### L2 human

The condition is purely algebraic and easy to check by hand or by computer.
By duality, the system $x' = A x$, $y = C x$ is [[observable|C4HN3EAQWM]] if and only if the matrix with block rows $C, CA, \ldots, CA^{n-1}$ has rank $n$.
This is the Kalman condition for the pair $(A^T, C^T)$.
When the condition fails, a linear change of coordinates splits the state into a controllable part and a part on which the control has no effect.
Controllability of $(A, B)$ is also equivalent to the possibility of placing the eigenvalues of $A + BK$ anywhere, symmetric under complex conjugation, by a choice of the feedback matrix $K$.
