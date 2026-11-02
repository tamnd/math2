---
tag: J1SGNEWKWS
kind: definition
name: P-adic dynamics
msc: [37P20, 11S82]
defines: B6DFK8HCB7
uses: [BT6T702C28, 1H5F1BP6XS, ASMPNM7K0M, AYVTR2ES5B]
sources:
  - url: https://en.wikipedia.org/wiki/P-adic_analysis
---

## Definition

Let $p$ be a prime.
Let $K$ be a field that is complete for a [[non-Archimedean absolute value|1H5F1BP6XS]] $\abs{\cdot}$ extending the $p$-adic absolute value of $\Q$.
Examples are $\Q_p$, its finite extensions, and $\C_p$.
A *$p$-adic dynamical system* is a pair $(X, \varphi)$ in which:

1. $X$ is either the projective line $\mathbb{P}^1(K)$ or a subset of $K$, such as a closed disc;
2. $\varphi \colon X \to X$ is given by a rational function in $K(z)$ when $X = \mathbb{P}^1(K)$, or by a power series with coefficients in $K$ that converges on $X$ otherwise.

*$p$-adic dynamics* is the study of the [[iterates|AYVTR2ES5B]] $\varphi^n$ and of the orbits $\set{\varphi^n(x) : n \in \N}$ of such systems, with respect to the topology of $\abs{\cdot}$.

## Remarks

Example: let $X = \Z_p$ and $\varphi(x) = x + 1$.
It maps $\Z_p$ into $\Z_p$, and it is a polynomial, so $(\Z_p, \varphi)$ is a $p$-adic dynamical system.
It is an isometry, since $\abs{\varphi(x) - \varphi(y)} = \abs{x - y}$.
The orbit of $0$ is $\N$, which is dense in $\Z_p$.

Non-example: let $\varphi(x) = x / p$ on $X = \Z_p$.
Then $\varphi(1) = 1/p$ has absolute value $p > 1$, so $\varphi$ does not map $X$ into $X$, and clause 2 fails.

A second example: $\varphi(z) = z^2$ on the open unit disc $\set{x \in \C_p : \abs{x} < 1}$.
Since $\abs{\varphi^n(x)} = \abs{x}^{2^n}$, every orbit tends to the attracting fixed point $0$.
