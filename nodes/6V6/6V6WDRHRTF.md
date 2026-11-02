---
tag: 6V6WDRHRTF
kind: definition
name: Kobayashi hyperbolic manifold
msc: [32Q45, 32F45]
defines: HRPAX8V7HA
uses: [JSGWAN2RJV, DY8QQ5GTTX, 0VKD1TP7F3]
sources:
  - url: https://en.wikipedia.org/wiki/Kobayashi_metric
---

## Definition

Let $X$ be a connected [[complex manifold|JSGWAN2RJV]] with [[Kobayashi pseudodistance|DY8QQ5GTTX]] $k_X$.
The manifold $X$ is *Kobayashi hyperbolic* if $k_X(p, q) > 0$ for all $p, q \in X$ with $p \ne q$, that is, if $k_X$ is a [[distance|0VKD1TP7F3]] on $X$.

## Remarks

When $X$ is hyperbolic, $k_X$ induces the manifold topology of $X$, by a theorem of Barth.
Example: a bounded domain $\Omega \subseteq \C^n$ is hyperbolic.
Check: if $\abs{z} < R$ on $\Omega$ and $p \ne q$, choose a complex linear function $\ell$ with $\ell(p) \ne \ell(q)$ and $\abs{\ell(z)} < 1$ on $\Omega$; since $\ell \colon \Omega \to \mathbb{D}$ decreases Kobayashi distances, $k_\Omega(p, q) \ge k_{\mathbb{D}}(\ell(p), \ell(q)) > 0$.
Non-example: $\C^n$ is not hyperbolic, since $k_{\C^n} \equiv 0$.
More generally, if there is a nonconstant holomorphic map $f \colon \C \to X$, then $k_X(f(a), f(b)) \le k_\C(a, b) = 0$ with $f(a) \ne f(b)$ for some $a, b$, so $X$ is not hyperbolic.
Hence complex tori and complex projective spaces are not hyperbolic.
A Riemann surface is hyperbolic exactly when its universal covering is the unit disc.
