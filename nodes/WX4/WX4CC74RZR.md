---
tag: WX4CC74RZR
kind: definition
name: Fictitious play
msc: [91A26, 91A10]
defines: QBA1NK6YCH
uses: [5MZTZRC3CZ, P01KKHB155, QS6VCNJK60, 8PC5CFGMAD, 745WYP9YJ0, K6M193GE4X]
sources:
  - url: https://en.wikipedia.org/wiki/Fictitious_play
---

## Definition

Let $G$ be a finite two-player [[normal-form game|5MZTZRC3CZ]] with action sets $A_1, A_2$ and payoff functions $u_1, u_2$.
A *fictitious play process* is a sequence of action profiles $(a^t)_{t \ge 0} = (a^t_1, a^t_2)_{t \ge 0}$ such that:

1. $a^0 \in A_1 \times A_2$ is arbitrary;
2. for $t \ge 1$ and $j \in \set{1, 2}$, let $\bar a^t_j$ be the [[mixed strategy|P01KKHB155]] giving each $b \in A_j$ the probability $\frac{1}{t} \abs{\set{s < t : a^s_j = b}}$;
3. for $t \ge 1$ and each player $i$, the action $a^t_i$ is a [[best response|QS6VCNJK60]] of player $i$ to $\bar a^t_j$, where $j$ is the other player.

Ties between best responses may be broken by any rule.
The mixed strategies $\bar a^t_1, \bar a^t_2$ are the *empirical frequencies* of the process.

## Remarks

The same rule makes sense for games with more than two players.
Each player then best responds to the product of the empirical frequencies of the others, or to their joint empirical distribution.
If the empirical frequencies converge, their limit is a [[Nash equilibrium|745WYP9YJ0]] in mixed strategies.
Robinson proved that in every two-player [[zero-sum game|8PC5CFGMAD]] the empirical frequencies converge to the set of optimal strategy pairs.
Shapley gave a two-player game with three actions each in which they do not converge.

Example: in [[matching pennies|K6M193GE4X]], player 1 wins if the two coins match and player 2 wins otherwise.
Each player switches only when the tally of the opponent's past choices tips the other way, so play runs through longer and longer cycles of the four action profiles.
Since the game is zero-sum, Robinson's theorem gives that both empirical frequencies tend to $(1/2, 1/2)$.

Non-example: let each player play a best response to the opponent's last action $a^{t-1}_j$ only.
This process is not fictitious play.
It fails clause 3, since the last action is in general not the empirical frequency of all past actions.
