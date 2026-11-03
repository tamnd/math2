---
tag: FEFSCJ8VQS
kind: statement
role: theorem
name: Regret matching converges to correlated equilibria
msc: [91A26, 91A10]
uses: [5MZTZRC3CZ, F4GH3T905G, 0DVDCMA2DK, 0ST21PGDAP, QBA1NK6YCH]
about: [F4GH3T905G]
sources:
  - url: https://en.wikipedia.org/wiki/Correlated_equilibrium
---

## Statement

Let $G$ be a finite [[normal-form game|5MZTZRC3CZ]] with players $i = 1, \dots, n$, action sets $A_i$, payoff functions $u_i$, and $A = A_1 \times \cdots \times A_n$.
Let $M > 0$ satisfy $\abs{u_i(a)} \le M$ for all $i$ and $a \in A$, and let $m_i = \abs{A_i}$.
The game is played repeatedly at times $t = 1, 2, \dots$, and $a^t \in A$ is the action profile at time $t$.
For player $i$, distinct actions $j, k \in A_i$ and time $t$, define the regret
$$R^t_i(j, k) = \max\Big( 0, \ \frac{1}{t} \sum_{s \le t, \ a^s_i = j} \big( u_i(k, a^s_{-i}) - u_i(a^s) \big) \Big).$$
Each player $i$ fixes $\mu_i > 2 M (m_i - 1)$ and uses *regret matching*.
At time $1$ she plays an arbitrary action.
If $j = a^t_i$, then at time $t + 1$ she plays each $k \ne j$ with probability $R^t_i(j, k) / \mu_i$ and plays $j$ with the remaining probability.
The players randomize independently.
Let $z^t$ be the empirical [[distribution|0DVDCMA2DK]] of play, which gives each $a \in A$ the weight $\frac{1}{t} \abs{\set{s \le t : a^s = a}}$.
Then [[almost surely|0ST21PGDAP]], the distance from $z^t$ to the set of [[correlated equilibria|F4GH3T905G]] of $G$ tends to $0$ as $t \to \infty$.

## Remarks

The bound $\mu_i > 2 M (m_i - 1)$ guarantees that the probabilities are well defined, since each regret is at most $2M$.
A distribution $z$ on $A$ is a correlated equilibrium exactly when all its conditional regrets $\sum_{a : a_i = j} z(a) (u_i(k, a_{-i}) - u_i(a))$ are at most $0$.
The proof shows that all regrets $R^t_i(j, k)$ tend to $0$ almost surely, using Blackwell's approachability theorem.
Since the regrets of $z^t$ are the averages $R^t_i(j, k)$ before truncation at $0$, this gives the conclusion.

The theorem gives convergence of the empirical distribution to a set, not convergence of play to a single equilibrium.
The players need to know only their own payoffs and the history of play, not the payoffs of the others.

## Explanations

### L1 human

After each round, a player asks: "Each time I played $j$, how much better would I have done by playing $k$ instead?"
Regret matching switches to $k$ with probability proportional to that regret.
It is a very simple and natural rule of thumb.
The theorem, due to Sergiu Hart and Andreu Mas-Colell (2000), says that if everyone uses it, the long-run pattern of play looks like a correlated equilibrium.

### L2 human

Unlike [[fictitious play|QBA1NK6YCH]], which need not converge in general games, regret matching leads to the set of correlated equilibria in every finite game.
The price is that the target is correlated equilibrium, a weaker notion than Nash equilibrium, and only the time averages converge.
A simpler unconditional version, which compares the payoff obtained with that of each fixed action, leads to the larger set of coarse correlated equilibria.
Such no-regret dynamics are used in computational game theory, for example to solve large poker games.
