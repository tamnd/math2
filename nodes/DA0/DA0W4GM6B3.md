---
tag: DA0W4GM6B3
kind: statement
role: theorem
name: Aumann's agreement theorem
msc: [91A27, 03B42, 62C10]
uses: [7BCMKF2P7X, 08QMKTWF9T, 00NBBSXRQS, 0990W5PN13]
about: [7BCMKF2P7X]
sources:
  - url: https://en.wikipedia.org/wiki/Aumann%27s_agreement_theorem
same_as:
  wikidata: Q4454919
  wikipedia: Aumann's agreement theorem
---

## Statement

Let $\Omega$ be a finite set of states and let $P$ be a [[prior|00NBBSXRQS]] probability on $\Omega$ with $P(\set{\omega}) > 0$ for every $\omega \in \Omega$.
Let $\mathcal{P}_1$ and $\mathcal{P}_2$ be [[partitions|08QMKTWF9T]] of $\Omega$ describing the information of two agents, and let $\mathcal{P}_i(\omega)$ be the block of $\mathcal{P}_i$ that contains $\omega$.
Let $A \subseteq \Omega$ be an event, and let $q_i(\omega) = P(A \mid \mathcal{P}_i(\omega))$ be the posterior [[conditional probability|0990W5PN13]] of $A$ for agent $i$ at $\omega$.
Let $a, b \in [0, 1]$ and $\omega \in \Omega$.
If the event $\set{\omega' \in \Omega : q_1(\omega') = a \text{ and } q_2(\omega') = b}$ is [[common knowledge|7BCMKF2P7X]] at $\omega$, then $a = b$.

## Remarks

Let $M$ be the block of the meet of $\mathcal{P}_1$ and $\mathcal{P}_2$ that contains $\omega$.
Common knowledge means that $q_1 = a$ and $q_2 = b$ on all of $M$.
The set $M$ is a disjoint union of blocks of $\mathcal{P}_1$, and on each of them the conditional probability of $A$ is $a$, so $P(A \mid M) = a$.
In the same way $P(A \mid M) = b$, so $a = b$.

Example: two agents share a prior over the outcome of a coin toss and get private evidence about it.
If they publicly announce their posteriors for "heads" back and forth, Geanakoplos and Polemarchakis showed that the announced posteriors become equal after finitely many rounds.

The common prior is essential: agents with different priors can hold different posteriors that are common knowledge, for instance if neither receives any information.

## Explanations

### L1 human

Two people who start with the same beliefs, are honest and rational, and openly know each other's opinions cannot "agree to disagree".
If they still disagree, then at least one of them has not fully taken in what the other's opinion reveals.
The private reasons may differ, but once the conclusions are common knowledge, the conclusions must coincide.

### L2 human

The theorem appeared in Aumann's 1976 paper "Agreeing to disagree", which also introduced the partition model of [[common knowledge|7BCMKF2P7X]].
The proof is a short averaging argument over the block of the meet.
The same argument gives the no-trade and no-betting theorems.
Two agents with a common prior cannot both strictly expect to gain from a zero-sum bet when its acceptance is common knowledge.
These results show how strong the common prior assumption is in economic models.
