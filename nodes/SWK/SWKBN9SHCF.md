---
tag: SWKBN9SHCF
kind: statement
role: theorem
name: Pinsker's inequality
msc: [94A17, "60E15", 62B10]
uses: [059TJN0NZ1, 3SZESKX3N5, PQBW43X5RE, 04DXAFN2ES]
about: [3SZESKX3N5, PQBW43X5RE]
sources:
  - url: https://en.wikipedia.org/wiki/Pinsker%27s_inequality
same_as:
  wikidata: Q7196482
  wikipedia: Pinsker's inequality
---

## Statement

Let $P$ and $Q$ be [[probability measures|059TJN0NZ1]] on a measurable space $(\Omega, \mathcal{F})$.
Let $\delta(P, Q) = \sup_{A \in \mathcal{F}} \abs{P(A) - Q(A)}$ be their [[total variation distance|3SZESKX3N5]], and let $D(P \,\|\, Q)$ be the [[Kullback–Leibler divergence|PQBW43X5RE]] computed with the [[natural logarithm|04DXAFN2ES]].
Then
$$\delta(P, Q) \le \sqrt{\tfrac12 D(P \,\|\, Q)}.$$

## Remarks

Proof idea: let $A$ be the set on which the density of $P$ with respect to $P + Q$ exceeds that of $Q$.
Then $\delta(P, Q) = P(A) - Q(A)$.
By the data processing inequality for the divergence, it is enough to treat the two-point laws $(P(A), 1 - P(A))$ and $(Q(A), 1 - Q(A))$.
For two-point laws with parameters $p$ and $q$, the inequality $p \ln \frac{p}{q} + (1 - p) \ln \frac{1 - p}{1 - q} \ge 2 (p - q)^2$ follows from a one-variable calculus argument in $q$.

Example: for $P = (\frac12, \frac12)$ and $Q = (\frac14, \frac34)$ on two points, $\delta(P, Q) = \frac14$ and $D(P \,\|\, Q) = \frac12 \ln 2 + \frac12 \ln \frac23 = \frac12 \ln \frac43 \approx 0.144$, so the bound is $\sqrt{0.072} \approx 0.27 \ge 0.25$.

The bound is useless when $D(P \,\|\, Q) \ge 2$, since $\delta \le 1$ always; for large divergence, bounds such as $\delta \le \sqrt{1 - e^{-D}}$ are better.
The constant $\frac12$ is the best possible.
With logarithms in base $2$, the inequality reads $\delta(P, Q) \le \sqrt{\tfrac{\ln 2}{2} D_2(P \,\|\, Q)}$.

## Explanations

### L1 human

If two probability laws have small Kullback–Leibler divergence, then every event has nearly the same probability under both.
Pinsker's inequality makes this quantitative: the largest gap in probability is at most the square root of half the divergence.

### L2 human

The divergence is often easy to compute, because it adds over independent coordinates, while the total variation distance is what controls tests and estimates.
Pinsker's inequality transfers bounds from one to the other.
It is used in lower bounds for hypothesis testing and bandit problems, in concentration of measure through transport inequalities, and in proofs of mixing for [[Markov chains|0G48PYM96Q]].
It relates two members of the family of [[f-divergences|TC7SQFTN3A]].
