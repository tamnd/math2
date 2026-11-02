---
tag: SNDSAJ8G8F
kind: definition
name: Delta derivative on a time scale
msc: ["26E70", 39A12]
defines: XXQ92H7T83
uses: [C4B1FA1H0J, 0G5AV9Q4RR]
sources:
  - url: https://en.wikipedia.org/wiki/Time-scale_calculus
---

## Definition

Let $\mathbb{T}$ be a time scale, that is, a nonempty [[closed subset|0G5AV9Q4RR]] of $\R$.
Let $\sigma(t) = \inf \set{s \in \mathbb{T} : s > t}$ for $t \in \mathbb{T}$, with $\sigma(t) = t$ when $t = \max \mathbb{T}$.
Let $\mathbb{T}^\kappa$ be $\mathbb{T}$ without $m = \max \mathbb{T}$ if this maximum exists and $\sup \set{s \in \mathbb{T} : s < m} < m$, and $\mathbb{T}^\kappa = \mathbb{T}$ otherwise.
Let $f \colon \mathbb{T} \to \R$ and $t \in \mathbb{T}^\kappa$.
A number $f^\Delta(t) \in \R$ is the *delta derivative* of $f$ at $t$ if the following holds.
For every $\varepsilon > 0$ there is $\delta > 0$ such that
$$\abs{f(\sigma(t)) - f(s) - f^\Delta(t)\,(\sigma(t) - s)} \le \varepsilon \abs{\sigma(t) - s}$$
for all $s \in \mathbb{T}$ with $\abs{t - s} < \delta$.
Then $f$ is called *delta differentiable* at $t$.

## Remarks

This is the derivative of [[time-scale calculus|C4B1FA1H0J]]; when it exists it is unique.
Example: on $\mathbb{T} = \Z$, $\sigma(t) = t + 1$; with $\delta = \tfrac{1}{2}$ the only admissible $s$ is $t$, and the condition holds exactly for $f^\Delta(t) = f(t+1) - f(t)$.
Non-example: on $\mathbb{T} = \R$, $\sigma(t) = t$ and the condition says that $f$ is differentiable at $t$ with $f^\Delta(t) = f'(t)$; so $f(t) = \abs{t}$ has no delta derivative at $0$.
If $\sigma(t) > t$ and $f$ is continuous at $t$, then $f^\Delta(t) = \frac{f(\sigma(t)) - f(t)}{\sigma(t) - t}$.
If $\sigma(t) = t$ and $t$ is not isolated from the right, then $f^\Delta(t) = \lim_{s \to t,\, s \in \mathbb{T}} \frac{f(t) - f(s)}{t - s}$ when this limit exists.
