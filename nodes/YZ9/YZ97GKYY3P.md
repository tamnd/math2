---
tag: YZ97GKYY3P
kind: statement
role: theorem
name: Lying over theorem
msc: [13B21]
uses: [B7X0KFY1S1, 00MHHZ9SNE, 5AFH94P4S3]
about: [B7X0KFY1S1, 00MHHZ9SNE]
sources:
  - url: https://en.wikipedia.org/wiki/Going_up_and_going_down
---

## Statement

Let $A \subseteq B$ be commutative rings with $B$ [[integral over|B7X0KFY1S1]] $A$.
Let $\mathfrak{p}$ be a [[prime ideal|00MHHZ9SNE]] of $A$.
Then there is a prime ideal $\mathfrak{q}$ of $B$ with $\mathfrak{q} \cap A = \mathfrak{p}$.

## Remarks

One [[localizes|4C1AE84N5N]] at $\mathfrak{p}$: the ring $B_{\mathfrak{p}}$ is integral over the [[local ring|MZ02BKPHJA]] $A_{\mathfrak{p}}$ and is not zero, since $A_{\mathfrak{p}} \subseteq B_{\mathfrak{p}}$.
Take a maximal ideal $\mathfrak{n}$ of $B_{\mathfrak{p}}$.
Then $B_{\mathfrak{p}}/\mathfrak{n}$ is a field integral over $A_{\mathfrak{p}}/(\mathfrak{n} \cap A_{\mathfrak{p}})$, so the latter is a field by [[integral extensions of fields|5GCANV7337]], and $\mathfrak{n} \cap A_{\mathfrak{p}}$ is the maximal ideal $\mathfrak{p} A_{\mathfrak{p}}$.
The [[contraction|5AFH94P4S3]] of $\mathfrak{n}$ to $B$ is the wanted $\mathfrak{q}$.

Example: for $\Z \subseteq \Z[i]$ and $\mathfrak{p} = 5\Z$, the prime $\mathfrak{q} = (2 + i)$ satisfies $\mathfrak{q} \cap \Z = 5\Z$, since $5 = (2 + i)(2 - i)$.

Integrality is needed: for $\Z \subseteq \Q$, the only prime ideal of $\Q$ is $0$, so no prime of $\Q$ lies over $2\Z$.
Injectivity is needed too: for the integral map $\Z \to \Z/2\Z$, no prime lies over $3\Z$.

## Explanations

### L1 human

The theorem says that every prime ideal of the small ring is the trace of a prime ideal of the big ring.
In geometry: the map of spaces given by an integral extension is surjective, every point downstairs has a point above it.

### L2 human

Lying over is the first of the Cohen–Seidenberg theorems; [[going-up|GHKYR5PBQC]], [[incomparability|Q2XBHJ96GV]] and [[going-down|YE52MQ13MV]] build on it.
In number theory it says that each prime number $p$ is divisible by some prime ideal of the ring of integers of a number field.
Together with going-up and incomparability it gives $\dim A = \dim B$ for an integral extension.
