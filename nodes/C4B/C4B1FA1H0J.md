---
tag: C4B1FA1H0J
kind: definition
name: Time-scale calculus
msc: ["26E70", 39A12]
defines: 30G1M35TK1
uses: [0ZCK8DQYN1, 0V1EJCT8G6, AZBDB5F4M4]
sources:
  - url: https://en.wikipedia.org/wiki/Time-scale_calculus
---

## Definition

A *time scale* is a nonempty [[closed subset|0ZCK8DQYN1]] $\mathbb{T}$ of $\R$.
The forward jump operator $\sigma \colon \mathbb{T} \to \mathbb{T}$ is $\sigma(t) = \inf \set{s \in \mathbb{T} : s > t}$, with $\sigma(t) = t$ when $t$ is the largest element of $\mathbb{T}$.
The graininess is $\mu(t) = \sigma(t) - t$.
Let $\mathbb{T}^\kappa$ be $\mathbb{T}$ without its largest element $m$ if $m$ exists and $\sup \set{s \in \mathbb{T} : s < m} < m$; otherwise $\mathbb{T}^\kappa = \mathbb{T}$.
Let $f \colon \mathbb{T} \to \R$ and $t \in \mathbb{T}^\kappa$.
The function $f$ is *delta differentiable* at $t$, with *delta derivative* $f^\Delta(t) \in \R$, if for every $\varepsilon > 0$ there is $\delta > 0$ such that
$$\abs{f(\sigma(t)) - f(s) - f^\Delta(t) \, (\sigma(t) - s)} \le \varepsilon \abs{\sigma(t) - s} \quad \text{for all } s \in \mathbb{T} \text{ with } \abs{t - s} < \delta.$$
*Time-scale calculus* is the study of delta derivatives, of the matching integrals, and of dynamic equations built from them.

## Remarks

The delta derivative is unique when it exists.
Example: for $\mathbb{T} = \R$, $\sigma(t) = t$ and the condition says that $f$ is differentiable at $t$ with $f^\Delta(t) = f'(t)$, the ordinary [[derivative|0V1EJCT8G6]].
Example: for $\mathbb{T} = \Z$, $\sigma(t) = t + 1$, and with $\delta = \frac{1}{2}$ the only admissible $s$ is $t$, so the condition holds exactly for $f^\Delta(t) = f(t + 1) - f(t)$.
More generally, if $\mu(t) > 0$ and $f$ is continuous at $t$, then $f^\Delta(t) = \frac{f(\sigma(t)) - f(t)}{\mu(t)}$, a [[difference quotient|AZBDB5F4M4]].
Non-example: on $\mathbb{T} = \R$, the function $f(t) = \abs{t}$ is not delta differentiable at $0$, because it has no ordinary derivative there.
