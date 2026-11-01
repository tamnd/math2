---
tag: YE52MQ13MV
kind: statement
role: theorem
name: Going-down theorem
msc: [13B21]
uses: [B7X0KFY1S1, H20P600HQS, 0QVD7WBFGN, 00MHHZ9SNE]
about: [B7X0KFY1S1, 00MHHZ9SNE]
sources:
  - url: https://en.wikipedia.org/wiki/Going_up_and_going_down
---

## Statement

Let $A \subseteq B$ be [[integral domains|0QVD7WBFGN]] such that $A$ is [[integrally closed|H20P600HQS]] and $B$ is [[integral over|B7X0KFY1S1]] $A$.
Let $\mathfrak{p}_1 \supseteq \mathfrak{p}_2$ be [[prime ideals|00MHHZ9SNE]] of $A$, and let $\mathfrak{q}_1$ be a prime ideal of $B$ with $\mathfrak{q}_1 \cap A = \mathfrak{p}_1$.
Then there is a prime ideal $\mathfrak{q}_2$ of $B$ with $\mathfrak{q}_2 \subseteq \mathfrak{q}_1$ and $\mathfrak{q}_2 \cap A = \mathfrak{p}_2$.

## Remarks

The proof shows that $\mathfrak{p}_2 B_{\mathfrak{q}_1} \cap A = \mathfrak{p}_2$; a prime of $B_{\mathfrak{q}_1}$ over $\mathfrak{p}_2$ then exists, and it contracts to the wanted $\mathfrak{q}_2$ in $B$.
The key step uses that $A$ is integrally closed.
If an element of $B$ is integral over the ideal $\mathfrak{p}_2$, then the coefficients of its minimal polynomial over the fraction field of $A$ lie in $\mathfrak{p}_2$.
Here one also uses that $B$ is a domain, so that nonzero elements of $A$ are not zero divisors on $B$.

Example: $\Z \subseteq \Z[i]$ satisfies the hypotheses, and for $\mathfrak{p}_1 = 5\Z \supseteq \mathfrak{p}_2 = 0$ and $\mathfrak{q}_1 = (2 + i)$, the prime $\mathfrak{q}_2 = 0$ works.

The hypothesis that $A$ is integrally closed cannot be dropped: there are integral extensions of domains in which going-down fails.
A different sufficient condition is flatness: going-down holds for every flat ring extension.

## Explanations

### L1 human

Going-down is the reverse of [[going-up|GHKYR5PBQC]]: given a prime upstairs, one wants to descend along a chain of smaller primes downstairs.
Unlike going-up, this needs the small ring to be integrally closed.

### L2 human

Going-down is used to prove that heights behave well in integral extensions over a normal base: $\operatorname{ht} \mathfrak{q} = \operatorname{ht}(\mathfrak{q} \cap A)$ for every prime $\mathfrak{q}$ of $B$.
It is a key ingredient in dimension theory of finitely generated algebras over a field, for example to show that such domains are catenary.
In geometry it gives that a finite surjective map from an irreducible variety onto a normal variety is an open map.
