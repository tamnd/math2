---
tag: WE8WMBM9SM
kind: statement
role: theorem
name: No-trade theorem
msc: [91A27, 91B26]
uses: [7BCMKF2P7X, 08QMKTWF9T, 00NBBSXRQS, 0TTDGTEFMN, 0DKRR22AEQ, DA0W4GM6B3]
about: [7BCMKF2P7X]
sources:
  - url: https://en.wikipedia.org/wiki/No-trade_theorem
same_as:
  wikidata: Q7042801
  wikipedia: No-trade theorem
---

## Statement

Let $\Omega$ be a finite set of states and let $P$ be a [[prior|00NBBSXRQS]] probability on $\Omega$ with $P(\set{\omega}) > 0$ for every $\omega \in \Omega$.
Let $\mathcal{P}_1$ and $\mathcal{P}_2$ be [[partitions|08QMKTWF9T]] of $\Omega$ describing the information of two agents.
Let $X \colon \Omega \to \R$ be a [[random variable|0DKRR22AEQ]], the net payment from agent 2 to agent 1 under a proposed bet.
For $\omega' \in \Omega$, let $e_i(\omega') = E[X \mid \mathcal{P}_i(\omega')]$ be the [[conditional expectation|0TTDGTEFMN]] of $X$ given the block of $\mathcal{P}_i$ that contains $\omega'$.
Let $\omega \in \Omega$, and suppose that the event $\set{\omega' : e_1(\omega') \ge 0 \text{ and } e_2(\omega') \le 0}$, in which both agents weakly want the bet, is [[common knowledge|7BCMKF2P7X]] at $\omega$.
Let $M$ be the block of the meet of $\mathcal{P}_1$ and $\mathcal{P}_2$ that contains $\omega$.
Then $e_1(\omega') = e_2(\omega') = 0$ for every $\omega' \in M$.
In particular, it is never common knowledge that both agents strictly want the bet.

## Remarks

Common knowledge at $\omega$ means that $e_1 \ge 0$ and $e_2 \le 0$ on all of $M$.
Since $M$ is a disjoint union of blocks of $\mathcal{P}_1$, the average $E[X \mid M]$ is a weighted average of the values of $e_1$ on $M$, so $E[X \mid M] \ge 0$.
In the same way $E[X \mid M] \le 0$, so $E[X \mid M] = 0$, and a weighted average of non-negative numbers with positive weights is $0$ only if all of them are $0$.

Example: two traders with a common prior hold different private information about the value of an asset.
If one offers to buy at a given price and the other accepts, the acceptance itself is information that makes the buyer less eager.
The theorem says that, once willingness to trade is common knowledge, neither expects a strict gain.

The common prior is essential: with different priors, two agents can both strictly expect to win the same bet.
Milgrom and Stokey proved a general version in 1982 for trades among agents starting from a Pareto efficient allocation.

## Explanations

### L1 human

If someone eagerly offers you a bet, you should ask what they know that you do not.
The theorem turns this into mathematics.
If both sides are rational, share the same starting beliefs, and it is common knowledge that both accept the bet, then neither can expect to gain from it.
So purely speculative trade between such agents cannot happen.

### L2 human

The result is the betting form of [[Aumann's agreement theorem|DA0W4GM6B3]], with the same averaging proof over the block of the meet.
It shows that a large volume of speculative trade in real markets must come from something outside the model, such as different priors, liquidity needs, risk sharing or irrational traders.
The general version of Milgrom and Stokey replaces the bet by any trade that agents accept starting from an efficient allocation.
