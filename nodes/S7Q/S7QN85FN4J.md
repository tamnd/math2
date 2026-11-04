---
tag: S7QN85FN4J
kind: proof
name: Proof of the law of total expectation
msc: [60A10]
proves: 04RRB6HM00
uses: [0YAMJRK04E, 0DCT0QZVQ1, 04WSW8T3SY]
sources:
  - url: https://en.wikipedia.org/wiki/Law_of_total_expectation
    locator: Proof in the general case
---

## Proof

We apply the defining property of the conditional expectation to the whole space.

1. Let $Z = E[X \mid \mathcal{G}]$ be a [[conditional expectation|0YAMJRK04E]] of $X$ given $\mathcal{G}$. By definition, $Z$ is integrable and $\mathcal{G}$-measurable.
2. The definition also gives $E[Z \, 1_G] = E[X \, 1_G]$ for each $G \in \mathcal{G}$.
3. A [[σ-algebra|04WSW8T3SY]] on $\Omega$ contains $\Omega$. So $\Omega \in \mathcal{G}$, and step 2 applies with $G = \Omega$.
4. The indicator $1_\Omega$ is the constant $1$. So step 3 reads $E[Z] = E[X]$, where $E$ is the [[expected value|0DCT0QZVQ1]].
5. Two versions of $E[X \mid \mathcal{G}]$ are equal almost surely, so they have the same expectation. Thus step 4 does not depend on the choice of $Z$, and $E[E[X \mid \mathcal{G}]] = E[X]$.
6. Let $Y$ be a random variable on the same space. By definition, $E[X \mid Y] = E[X \mid \sigma(Y)]$, and $\sigma(Y) \subseteq \mathcal{F}$ is a σ-algebra.
7. Step 5 with $\mathcal{G} = \sigma(Y)$ gives $E[E[X \mid Y]] = E[X]$.

## Idea

The conditional expectation is built so that it has the same average as $X$ on every event of $\mathcal{G}$. The whole space $\Omega$ is one of these events, and the average over $\Omega$ is the ordinary expectation.
