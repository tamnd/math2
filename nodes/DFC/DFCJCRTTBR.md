---
tag: DFCJCRTTBR
kind: definition
name: Mixing
msc: [37A25, 28D05]
defines: S3RJQ9CX2P
uses: [0NFPJVJJHX, 556WBDAHNP]
sources:
  - url: https://en.wikipedia.org/wiki/Mixing_(mathematics)
---

## Definition

Let $(X, \mathcal{B}, \mu)$ be a [[probability space|0NFPJVJJHX]] and let $T \colon X \to X$ be a [[measure-preserving transformation|556WBDAHNP]].
The map $T$ is *mixing*, or *strongly mixing*, if for all $A, B \in \mathcal{B}$,
$$\lim_{n \to \infty} \mu(T^{-n} A \cap B) = \mu(A) \, \mu(B).$$

## Remarks

Example: let $T(x) = 2x \bmod 1$ on $[0,1)$ with Lebesgue measure $\mu$.
Let $A$ and $B$ be dyadic intervals of length $2^{-k}$, that is, of the form $[j 2^{-k}, (j+1) 2^{-k})$.
For $n \ge k$, the set $T^{-n} A$ is a union of $2^n$ intervals of length $2^{-n-k}$, one in each interval $[i 2^{-n}, (i+1) 2^{-n})$.
Exactly $2^{n-k}$ of them lie in $B$, so $\mu(T^{-n} A \cap B) = 2^{-2k} = \mu(A) \mu(B)$.
Dyadic intervals generate the Borel sets, and an approximation argument gives the limit for all $A$ and $B$.

Non-example: let $T(x) = x + \alpha \bmod 1$ with $\alpha$ irrational, and let $A = B = [0, 1/4)$.
The numbers $n \alpha \bmod 1$ come arbitrarily close to $0$ for infinitely many $n$, and for those $n$ the measure $\mu(T^{-n} A \cap A)$ is close to $1/4$.
So it does not tend to $1/16$, and the rotation is not mixing, although it is ergodic.

Taking $A = B$ with $T^{-1} A = A$ shows that a mixing map is ergodic: then $\mu(A) = \mu(A)^2$, so $\mu(A) \in \set{0, 1}$.
In terms of functions, $T$ is mixing if and only if $\int (f \circ T^n) \, g \, d\mu \to \int f \, d\mu \int g \, d\mu$ for all $f, g \in L^2(\mu)$.
