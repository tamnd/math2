---
tag: FA0CD4SQZ5
kind: definition
name: Weak mixing
msc: [37A25, 28D05]
defines: 2MGZFRH5PX
uses: [0NFPJVJJHX, 556WBDAHNP, S3RJQ9CX2P, 37TRG5DBQC]
sources:
  - url: https://en.wikipedia.org/wiki/Mixing_(mathematics)
---

## Definition

Let $(X, \mathcal{B}, \mu)$ be a [[probability space|0NFPJVJJHX]] and let $T \colon X \to X$ be a [[measure-preserving transformation|556WBDAHNP]].
The map $T$ is *weakly mixing* if for all $A, B \in \mathcal{B}$,
$$\lim_{N \to \infty} \frac{1}{N} \sum_{n=0}^{N-1} \abs{\mu(T^{-n} A \cap B) - \mu(A) \, \mu(B)} = 0.$$

## Remarks

Example: every [[mixing|S3RJQ9CX2P]] map is weakly mixing, since the averages of a sequence that tends to $0$ also tend to $0$.
So the doubling map $x \mapsto 2x \bmod 1$ with Lebesgue measure is weakly mixing.

Non-example: let $T(x) = x + \alpha \bmod 1$ with $\alpha$ irrational, and let $f(x) = e^{2\pi i x}$.
Then $f \circ T = e^{2\pi i \alpha} f$, so $f$ is a nonconstant eigenfunction of the [[Koopman operator|37TRG5DBQC]].
By form 2 below, $T$ is not weakly mixing, although it is ergodic.

Equivalent forms, for $T$ as above:

1. The product map $T \times T$ is ergodic for the product measure $\mu \times \mu$.
2. Every $f \in L^2(\mu)$ with $f \circ T = \lambda f$ for some $\lambda \in \C$ is constant almost everywhere.
3. For all $A, B \in \mathcal{B}$ there is a set $J \subseteq \N$ of density zero such that $\mu(T^{-n} A \cap B) \to \mu(A)\mu(B)$ as $n \to \infty$ with $n \notin J$.

There are weakly mixing maps that are not mixing; Chacon's transformation is a classical example.
