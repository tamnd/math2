---
tag: NAJ9Y60PF6
kind: definition
name: Infinitesimal generator of a Markov process
msc: [60J35, 47D07, 47D06]
defines: VPA41PWRR1
uses: [4HS3C12472, 0XMEM406JM, 06GZ956657, KQMJ7M57ER]
sources:
  - url: https://en.wikipedia.org/wiki/Infinitesimal_generator_(stochastic_processes)
---

## Definition

Let $E$ be a locally compact Hausdorff space with a countable base.
Let $C_0(E)$ be the [[Banach space|06GZ956657]] of continuous functions on $E$ that vanish at infinity, with the sup norm.
Let $(X_t)_{t \ge 0}$ be a [[Feller process|4HS3C12472]] on $E$ with semigroup $T_t f(x) = \mathbb{E}_x[f(X_t)]$.
The *infinitesimal generator* of $X$ is the linear operator $A$ with domain
$$D(A) = \set{f \in C_0(E) : \lim_{t \downarrow 0} \frac{T_t f - f}{t} \text{ exists in } C_0(E)},$$
given by
$$Af = \lim_{t \downarrow 0} \frac{T_t f - f}{t} \quad \text{for } f \in D(A),$$
where the limit is in the sup norm.

## Remarks

Example: for a continuous-time Markov chain on a finite set $S$ with rate matrix $Q$, one has $T_t = e^{tQ}$, so $(T_t f - f)/t \to Qf$ for every $f$, and $A = Q$ with $D(A)$ the whole space.
Example: for Brownian motion on $\R^d$, every twice continuously differentiable $f$ with $f$, its first and its second derivatives in $C_0(\R^d)$ lies in $D(A)$, and $Af = \tfrac12 \Delta f$.
Non-example: for Brownian motion on $\R$, the function $f(x) = e^{-x^2} \abs{x}$ is in $C_0(\R)$ but not in $D(A)$, since it is not differentiable at $0$.
For $f \in D(A)$, Dynkin's formula says that $f(X_t) - f(X_0) - \int_0^t Af(X_s)\, ds$ is a martingale.
The semigroup satisfies $\frac{d}{dt} T_t f = A T_t f = T_t A f$ for $f \in D(A)$, the [[backward|KQMJ7M57ER]] and forward equations.
