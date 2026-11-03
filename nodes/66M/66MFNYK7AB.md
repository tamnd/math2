---
tag: 66MFNYK7AB
kind: definition
name: Trembling hand perfect equilibrium
msc: [91A11, 91A10]
defines: GTKFGTX0B3
uses: [5MZTZRC3CZ, P01KKHB155, QS6VCNJK60, 745WYP9YJ0, 05M5SWSZZD]
sources:
  - url: https://en.wikipedia.org/wiki/Trembling_hand_perfect_equilibrium
---

## Definition

Let $G$ be a finite [[normal-form game|5MZTZRC3CZ]] with players $i = 1, \dots, n$ and finite pure strategy sets $S_1, \dots, S_n$.
A [[mixed strategy|P01KKHB155]] profile is *completely mixed* if every player gives positive probability to each of her pure strategies.
For a profile $\tau$, write $\tau_{-i}$ for the strategies of the players other than $i$.
A mixed strategy profile $\sigma = (\sigma_1, \dots, \sigma_n)$ is a *trembling hand perfect equilibrium* if there is a sequence $(\sigma^k)_{k \ge 1}$ of completely mixed strategy profiles such that:

1. $\sigma^k \to \sigma$ as $k \to \infty$, and
2. for every $k$ and every player $i$, the strategy $\sigma_i$ is a [[best response|QS6VCNJK60]] to $\sigma^k_{-i}$.

## Remarks

Letting $k \to \infty$ in clause 2 and using the continuity of expected payoffs shows that every trembling hand perfect equilibrium is a [[Nash equilibrium|745WYP9YJ0]].
Selten proved that every finite normal-form game has a trembling hand perfect equilibrium.
In a two-player game, a mixed profile is trembling hand perfect if and only if it is a Nash equilibrium in which neither player uses a weakly dominated strategy.

Example: player 1 chooses $U$ or $D$, player 2 chooses $L$ or $R$, and both get $1$ at $(U, L)$ and $0$ otherwise.
Let $\sigma^k$ be the profile where player 1 plays $U$ with probability $1 - 1/k$ and player 2 plays $L$ with probability $1 - 1/k$.
Against any completely mixed strategy of player 2, $U$ earns the positive probability of $L$ and $D$ earns $0$, so $U$ is the unique best response.
By symmetry $L$ is the unique best response of player 2, so $(U, L)$ is trembling hand perfect.

Non-example: $(D, R)$ is a Nash equilibrium of the same game, but it fails clause 2.
Against any completely mixed strategy of player 2, $D$ earns $0$ and $U$ earns a positive amount, so $D$ is never a best response to a completely mixed profile.

An equivalent form uses $\varepsilon$-perfect equilibria: completely mixed profiles in which every pure strategy that is not a best response gets probability at most $\varepsilon$.
The trembling hand perfect equilibria are exactly the limits of $\varepsilon_k$-perfect equilibria with $\varepsilon_k \to 0$.
