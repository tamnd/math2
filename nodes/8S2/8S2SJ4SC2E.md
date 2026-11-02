---
tag: 8S2SJ4SC2E
kind: definition
name: Kurosh–Amitsur radical theory
msc: [16N80]
defines: A72J7ZVNR5
uses: [MBK7NFE74S, 0DDA6CY7GJ]
sources:
  - url: https://en.wikipedia.org/wiki/Radical_of_a_ring
---

## Definition

Work with associative [[rings that need not have an identity|MBK7NFE74S]].
A class $\mathcal{R}$ of such rings, closed under isomorphism, is a *radical class* in the sense of Kurosh and Amitsur if the following hold.

1. If $A \in \mathcal{R}$ and $B$ is a homomorphic image of $A$, then $B \in \mathcal{R}$.
2. Every ring $A$ has a [[two-sided ideal|0DDA6CY7GJ]] $\mathcal{R}(A)$ that belongs to $\mathcal{R}$ and contains every ideal of $A$ that belongs to $\mathcal{R}$.
3. For every ring $A$, the quotient $A/\mathcal{R}(A)$ has no nonzero ideal in $\mathcal{R}$, that is, $\mathcal{R}(A/\mathcal{R}(A)) = 0$.

The ideal $\mathcal{R}(A)$ is the *$\mathcal{R}$-radical* of $A$.
A ring $A$ is *$\mathcal{R}$-semisimple* if $\mathcal{R}(A) = 0$.

## Remarks

Example: the class of nil rings is a radical class.
Homomorphic images of nil rings are nil.
The sum of all nil ideals of $A$ is the largest nil ideal, the [[upper nilradical|3G2JQEYBEK]] $N$.
If $I/N$ is a nil ideal of $A/N$, then every $x \in I$ has a power in $N$, so $I$ is nil and $I/N = 0$.
Non-example: the class of nilpotent rings satisfies clause 1 but not clause 2, since a ring can have an infinite family of nilpotent ideals whose sum is not nilpotent.
Other radical classes are the Jacobson radical rings (rings equal to their [[Jacobson radical|XA0DCNH7WY]]), the locally nilpotent rings, which give the [[Levitzki radical|9DD8M9R868]], and the class giving the [[prime radical|WF117EJ2HF]].
