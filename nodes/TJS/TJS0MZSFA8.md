---
tag: TJS0MZSFA8
kind: definition
name: Differential game
msc: [91A23, 49N70]
defines: THSHGNJNPS
uses: [ZPDTVZQN5K, 0JW6MDHAZD, 0QNVQ4VD9T]
sources:
  - url: https://en.wikipedia.org/wiki/Differential_game
---

## Definition

Let $N \ge 2$ and $T > 0$.
For each player $i = 1, \dots, N$, let $U_i \subseteq \R^{m_i}$ be a nonempty compact set.
Let $f \colon [0, T] \times \R^n \times U_1 \times \cdots \times U_N \to \R^n$ be continuous and [[Lipschitz|0QNVQ4VD9T]] in its second variable.
For each $i$, let $L_i \colon [0, T] \times \R^n \times U_1 \times \cdots \times U_N \to \R$ and $g_i \colon \R^n \to \R$ be continuous.
A *differential game* on $[0, T]$ with initial state $x_0 \in \R^n$ consists of these data, used as follows.

1. Each player $i$ chooses a measurable control $u_i \colon [0, T] \to U_i$.
2. The controls drive the state by the [[control system|ZPDTVZQN5K]] $x'(t) = f(t, x(t), u_1(t), \dots, u_N(t))$ with $x(0) = x_0$.
3. Player $i$ wants to minimise its cost $J_i(u_1, \dots, u_N) = \int_0^T L_i(t, x(t), u_1(t), \dots, u_N(t)) \, dt + g_i(x(T))$.

The game is *two-player zero-sum* if $N = 2$ and $J_2 = -J_1$; then player $1$ minimises $J = J_1$ and player $2$ maximises it.

## Remarks

A full definition also says what information each player uses.
In open-loop play each player picks a control as a function of time alone.
In feedback play each player picks $u_i(t)$ as a function of $(t, x(t))$.
In the zero-sum case one often uses nonanticipating strategies, which choose the present control from the opponent's past controls.
A solution concept is a Nash equilibrium, a tuple of strategies from which no player gains by deviating alone.
In the zero-sum case this is a [[saddle point|0JW6MDHAZD]] of $J$, and its value is the value of the game.

Example: $n = 2$, $U_1$ the closed disc of radius $2$, $U_2$ the closed unit disc, $f(t, x, u_1, u_2) = u_2 - u_1$, $L_1 = 0$ and $g_1(x) = \abs{x}$, with $g_2 = -g_1$.
Here $x$ is the position of player $2$ relative to player $1$, and player $1$ wants to end close to player $2$.
All clauses hold: $f$ is continuous and does not depend on $x$, and the sets $U_i$ are compact.

Non-example: in a game where the state changes only at the times $0, 1, 2, \dots$ by a recurrence $x_{k+1} = F(x_k, u_{1,k}, u_{2,k})$, clause 2 fails.
It is a dynamic game in discrete time, not a differential game.

## Explanations

### L1 human

Several players steer the same system at the same time, each with its own goal.
The rules of motion are a differential equation, so the game is played in continuous time.
