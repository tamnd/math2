---
tag: EVFDAQTNDF
kind: definition
name: Proper equilibrium
msc: [91A11, 91A10]
defines: ZTKE3WXEJ2
uses: [5MZTZRC3CZ, P01KKHB155, GTKFGTX0B3, 05M5SWSZZD]
sources:
  - url: https://en.wikipedia.org/wiki/Proper_equilibrium
---

## Definition

Let $G$ be a finite [[normal-form game|5MZTZRC3CZ]] with players $i = 1, \dots, n$, finite pure strategy sets $S_i$ and payoff functions $u_i$.
For a [[mixed strategy|P01KKHB155]] profile $\sigma$, write $\sigma_{-i}$ for the strategies of the players other than $i$.
Write $u_i(s, \sigma_{-i})$ for the expected payoff of player $i$ when she plays the pure strategy $s \in S_i$ and the others play $\sigma_{-i}$.
Let $\varepsilon > 0$.
A mixed strategy profile $\sigma$ is *$\varepsilon$-proper* if:

1. every player gives positive probability to each of her pure strategies, and
2. for every player $i$ and all $s, s' \in S_i$, if $u_i(s, \sigma_{-i}) < u_i(s', \sigma_{-i})$, then $\sigma_i(s) \le \varepsilon \, \sigma_i(s')$.

A mixed strategy profile $\sigma$ is a *proper equilibrium* if there are numbers $\varepsilon_k > 0$ with $\varepsilon_k \to 0$ and $\varepsilon_k$-proper profiles $\sigma^k$ with $\sigma^k \to \sigma$.

## Remarks

Every proper equilibrium is a [[trembling hand perfect equilibrium|GTKFGTX0B3]].
Myerson proved that every finite normal-form game has a proper equilibrium.

Example: player 1 chooses $U$ or $D$, player 2 chooses $L$ or $R$, and both get $1$ at $(U, L)$ and $0$ otherwise.
Let player 1 play $D$ with probability $\varepsilon/2$ and player 2 play $R$ with probability $\varepsilon/2$, where $0 < \varepsilon \le 1$.
Then $D$ and $R$ are strictly worse than $U$ and $L$, and $\varepsilon/2 \le \varepsilon (1 - \varepsilon/2)$, so this profile is $\varepsilon$-proper.
Letting $\varepsilon \to 0$ shows that $(U, L)$ is a proper equilibrium.

Non-example: take the symmetric game with three strategies per player.
Player 1's payoffs are the entries of
$$\begin{pmatrix} 1 & 0 & -9 \\ 0 & 0 & -7 \\ -9 & -7 & -7 \end{pmatrix}$$
(row for player 1, column for player 2), and player 2's payoffs are given by the transpose.
The profile in which both players play the second strategy is trembling hand perfect, using trembles in which the third strategy is twice as likely as the first.
It is not proper.
Near this profile the third strategy is strictly the worst for player 2, so clause 2 gives $\sigma_2(3) \le \varepsilon \, \sigma_2(1)$.
Take $\varepsilon < 1/9$.
Then the first strategy gives player 1 the payoff $\sigma_2(1) - 9 \sigma_2(3) > 0$.
The second strategy gives her $-7 \sigma_2(3) < 0$.
So clause 2 gives $\sigma_1(2) \le \varepsilon \, \sigma_1(1)$, and $\sigma_1$ cannot be close to the second strategy.
