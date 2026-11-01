---
tag: J3CT5D7FSZ
kind: statement
role: theorem
name: Janson inequality
msc: [05D40, 60C05, 05C80]
uses: [0NFPJVJJHX, 031TPJVS74]
about: [3B55HNS754]
sources:
  - url: https://en.wikipedia.org/wiki/Janson_inequality
same_as:
  wikidata: Q96384187
  wikipedia: Janson inequality
---

## Statement

Let $\Gamma$ be a finite set, and let $R \subseteq \Gamma$ be a random subset that contains each $r \in \Gamma$ independently with probability $p_r$.
Let $A_1, \dots, A_n$ be subsets of $\Gamma$, and let $B_i$ be the [[event|031TPJVS74]] that $A_i \subseteq R$.
Write $i \sim j$ if $i \ne j$ and $A_i \cap A_j \ne \emptyset$.
Let
$$\mu = \sum_{i=1}^n \Pr(B_i), \qquad \Delta = \sum_{(i, j) : i \sim j} \Pr(B_i \cap B_j),$$
where the second sum runs over ordered pairs.
Then
$$\Pr\Big(\bigcap_{i=1}^n \overline{B_i}\Big) \le e^{-\mu + \Delta/2}.$$

## Remarks

If moreover $\Delta \ge \mu$, a further argument gives the bound $e^{-\mu^2/(2\Delta)}$.
In the other direction, the [[Harris inequality|W1YH3YD3S4]] gives $\Pr\big(\bigcap_i \overline{B_i}\big) \ge \prod_i (1 - \Pr(B_i))$.
So when $\Delta$ is small and each $\Pr(B_i)$ is small, the probability that no $B_i$ occurs is close to $e^{-\mu}$, as for independent events.
For example, in the [[random graph|TNT3DG0HRJ]] $G(n, p)$, take $\Gamma$ to be the set of edges of $K_n$ and the $A_i$ to be the edge sets of triangles.
Then $\mu = \binom{n}{3} p^3$.
When $p = c/n$ for a constant $c > 0$, one has $\mu \to c^3/6$ and $\Delta \to 0$ as $n \to \infty$.
With the lower bound, the probability that $G(n, p)$ has no triangle tends to $e^{-c^3/6}$.
The proof writes the probability as a product of the factors $\Pr\big(\overline{B_i} \mid \bigcap_{j < i} \overline{B_j}\big)$.
It bounds each conditional probability of $B_i$ from below, using the Harris inequality for increasing events.

## Explanations

### L1 human

Many small "bad" patterns may appear in a random set.
If the patterns rarely overlap, the chance that none of them appears is close to what it would be if they were independent.
The Janson inequality makes this precise, with an error term that measures the overlaps.

### L2 human

The Janson inequality is a standard tool in the theory of random graphs and the [[probabilistic method|3B55HNS754]].
It gives exponentially small upper bounds on the probability that a random graph contains no copy of a given subgraph.
Compared with the second moment method, it gives a much sharper bound on the probability of the lower tail.
