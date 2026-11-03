---
tag: XRDA4Y561H
kind: definition
name: Time-variant system
msc: [93A10, 93C05]
defines: S4THJVE1AJ
uses: [21FN2KSTJZ]
sources:
  - url: https://en.wikipedia.org/wiki/Time-variant_system
---

## Definition

Let $\mathcal{T}$ be $\R$ or $\Z$, and let $\mathcal{U}$ and $\mathcal{Y}$ be sets of functions on $\mathcal{T}$ that are closed under time shifts.
For $\tau \in \mathcal{T}$ and a signal $v$, the *shift* $S_\tau v$ is the signal $(S_\tau v)(t) = v(t - \tau)$.
A system $H \colon \mathcal{U} \to \mathcal{Y}$ is *time-invariant* if
$$H(S_\tau u) = S_\tau (H u)$$
for all $u \in \mathcal{U}$ and all $\tau \in \mathcal{T}$.
The system is *time-variant* if it is not time-invariant, that is, if this equation fails for some $u$ and some $\tau$.

## Remarks

Example: $(Hu)(t) = t \, u(t)$ on real signals over $\R$ is time-variant.
For the constant input $u = 1$ one has $S_\tau u = 1$, so $H(S_\tau u)(t) = t$, while $(S_\tau H u)(t) = t - \tau$; these differ for $\tau \ne 0$.
Non-example: the delay $(Hu)(t) = u(t - 1)$ is time-invariant, since both $H(S_\tau u)(t)$ and $(S_\tau Hu)(t)$ equal $u(t - \tau - 1)$.
The state-space system $x' = A(t) x + B(t) u$, $y = C(t) x + D(t) u$ with zero initial state in the far past is time-invariant when the matrices $A, B, C, D$ are constant.
The definition does not need [[linearity|21FN2KSTJZ]]; a time-variant linear system is often called a linear time-varying system.
