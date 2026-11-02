---
tag: 18ZNC2R6AX
kind: definition
name: Resolvent set
msc: [47A10, 46H05]
defines: X0243CZD9D
uses: [EH0CZ19RKP, 0XVEZDE9J8, 06GZ956657]
sources:
  - url: https://en.wikipedia.org/wiki/Resolvent_set
---

## Definition

Let $\mathbb{K}$ be a field, let $A$ be an associative algebra over $\mathbb{K}$ with unit $1$, and let $a \in A$.
The *resolvent set* of $a$ is
$$\rho(a) = \set{\lambda \in \mathbb{K} : a - \lambda 1 \text{ is invertible in } A} = \mathbb{K} \setminus \sigma(a),$$
where invertible means being a [[unit|0XVEZDE9J8]] of $A$, and $\sigma(a)$ is the [[spectrum|EH0CZ19RKP]] of $a$.
For $\lambda \in \rho(a)$, the element $R(\lambda) = (a - \lambda 1)^{-1}$ is the *resolvent* of $a$ at $\lambda$.

Let $T$ be a closed linear operator with domain $D(T)$ in a complex [[Banach space|06GZ956657]] $X$.
The resolvent set of $T$ is the set of $\lambda \in \C$ such that $T - \lambda$ maps $D(T)$ bijectively onto $X$ with bounded inverse.

## Remarks

Some authors use $(\lambda 1 - a)^{-1}$ as the resolvent; this changes its sign only.
The resolvent satisfies the resolvent identity $R(\lambda) - R(\mu) = (\lambda - \mu) R(\lambda) R(\mu)$ for $\lambda, \mu \in \rho(a)$.
It follows from $R(\lambda) - R(\mu) = R(\lambda) \big( (a - \mu 1) - (a - \lambda 1) \big) R(\mu)$.

Example: in $C([0,1])$ with complex values, let $f(t) = t$.
Then $\rho(f) = \C \setminus [0,1]$, and $R(\lambda)(t) = 1/(t - \lambda)$.

Non-example: for the same $f$, the number $\lambda = 1/2$ is not in $\rho(f)$, because $f - 1/2$ vanishes at $t = 1/2$ and has no continuous inverse.
