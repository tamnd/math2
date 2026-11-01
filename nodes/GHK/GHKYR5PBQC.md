---
tag: GHKYR5PBQC
kind: statement
role: theorem
name: Going-up theorem
msc: [13B21]
uses: [B7X0KFY1S1, 00MHHZ9SNE, YZ97GKYY3P]
about: [B7X0KFY1S1, 00MHHZ9SNE]
sources:
  - url: https://en.wikipedia.org/wiki/Going_up_and_going_down
---

## Statement

Let $A \subseteq B$ be commutative rings with $B$ [[integral over|B7X0KFY1S1]] $A$.
Let $\mathfrak{p}_1 \subseteq \mathfrak{p}_2$ be [[prime ideals|00MHHZ9SNE]] of $A$, and let $\mathfrak{q}_1$ be a prime ideal of $B$ with $\mathfrak{q}_1 \cap A = \mathfrak{p}_1$.
Then there is a prime ideal $\mathfrak{q}_2$ of $B$ with $\mathfrak{q}_1 \subseteq \mathfrak{q}_2$ and $\mathfrak{q}_2 \cap A = \mathfrak{p}_2$.

## Remarks

The ring $B/\mathfrak{q}_1$ is integral over its subring $A/\mathfrak{p}_1$.
The [[lying over theorem|YZ97GKYY3P]] gives a prime of $B/\mathfrak{q}_1$ over $\mathfrak{p}_2/\mathfrak{p}_1$, and its preimage in $B$ is $\mathfrak{q}_2$.

By induction, every chain $\mathfrak{p}_1 \subseteq \cdots \subseteq \mathfrak{p}_n$ of primes of $A$ lifts to a chain $\mathfrak{q}_1 \subseteq \cdots \subseteq \mathfrak{q}_n$ of primes of $B$ with $\mathfrak{q}_i \cap A = \mathfrak{p}_i$.
So the [[Krull dimension|MVGBS3J1P7]] of $B$ is at least that of $A$.

Example: for $\Z \subseteq \Z[i]$, the chain $0 \subseteq 5\Z$ lifts to $0 \subseteq (2 + i)$.

Integrality is needed: for $k[x] \subseteq k[x, x^{-1}]$, the prime $0$ lies under $0$, but no prime of $k[x, x^{-1}]$ lies over $(x)$, since $x$ is a unit there.

## Explanations

### L1 human

If a prime of the big ring sits over a prime of the small ring, then one can climb up along any longer chain downstairs and stay above it upstairs.
In geometry: the image of a closed subset under an integral map is closed, and specializations of points can be followed upstairs.

### L2 human

Going-up and [[incomparability|Q2XBHJ96GV]] together give $\dim B = \dim A$ for every integral extension $A \subseteq B$.
This is the key step in computing the dimension of a finitely generated algebra over a field through [[Noether normalization|7Z28JY8QW4]].
The companion result in the other direction, [[going-down|YE52MQ13MV]], needs extra hypotheses.
