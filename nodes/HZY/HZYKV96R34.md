---
tag: HZYKV96R34
kind: statement
role: theorem
name: Friendship paradox
msc: [91D30, 05C07]
uses: [00C0BR7D7H, 0KS0KRDV4Y, 0477R9PYAE]
about: [0KS0KRDV4Y]
sources:
  - url: https://en.wikipedia.org/wiki/Friendship_paradox
same_as:
  wikidata: Q1455885
  wikipedia: Friendship paradox
---

## Statement

Let $G = (V, E)$ be a finite simple [[graph|00C0BR7D7H]] with at least one edge, and let $d(v)$ denote the [[degree|0KS0KRDV4Y]] of a vertex $v$.
Let $\mu = \frac{1}{\abs{V}} \sum_{v \in V} d(v)$ be the mean degree and $\sigma^2 = \frac{1}{\abs{V}} \sum_{v \in V} (d(v) - \mu)^2$ the variance of the degrees.
Let $\nu$ be the mean degree of a friend, averaged over all ordered pairs $(u, w)$ with $\set{u, w} \in E$ of the degree $d(w)$.
Then
$$\nu = \frac{\sum_{v} d(v)^2}{\sum_{v} d(v)} = \mu + \frac{\sigma^2}{\mu} \ge \mu,$$
with equality if and only if all vertices of $G$ have the same degree.

## Remarks

Each vertex $w$ appears as the second entry of exactly $d(w)$ ordered pairs, so $\nu = \sum_w d(w) \cdot d(w) / \sum_w d(w)$.
Dividing numerator and denominator by $\abs{V}$ gives $(\sigma^2 + \mu^2)/\mu$, using the formula for the [[variance|0477R9PYAE]].
Example: in the star with one centre and $3$ leaves, $\mu = 6/4 = 3/2$, while $\nu = (9 + 1 + 1 + 1)/6 = 2$.
The hypothesis of at least one edge is needed so that $\mu > 0$ and $\nu$ is defined.
The paradox concerns the average over pairs of friends; it does not say that most people have fewer friends than each of their friends.

## Explanations

### L1 human

On average, your friends have more friends than you do.
The reason is not that you are unpopular.
Popular people appear in many friend lists, so when you average over friend lists, popular people are counted many times.
That pulls the average up, unless everyone has exactly the same number of friends.

### L2 human

The result is a size-biased sampling effect: picking a random end of a random edge picks a vertex with probability proportional to its degree.
The gap $\sigma^2/\mu$ is large in networks with very unequal degrees, such as many social networks.
The same effect is used in practice: sampling friends of random people finds well-connected people, which helps for early detection of epidemics.
Scott Feld described the paradox for social networks in 1991.
