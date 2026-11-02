---
tag: CN91KKNSQK
kind: definition
name: Iterative method
msc: [65F10, 65H10]
defines: 2RPE77ACER
uses: [03J5RAKB30, 090AA928Y7, K6ZF91051B, 0GT4WWGWH2, 9V7YQA85PC, 0EB9N0S33C]
sources:
  - url: https://en.wikipedia.org/wiki/Iterative_method
---

## Definition

Let $X$ be a [[normed vector space|03J5RAKB30]], let $D \subseteq X$, and let $x^* \in X$ be a solution of a given problem.
An *iterative method* is a sequence of maps $\Phi_k \colon D^{k+1} \to D$ for $k \ge 0$.
From an initial guess $x_0 \in D$, it produces the iterates $x_{k+1} = \Phi_k(x_0, \dots, x_k)$.
The method is *convergent* for $x_0$ if the iterates [[converge|090AA928Y7]] to $x^*$.
It is *stationary* if there is one map $\Phi \colon D \to D$ with $\Phi_k(x_0, \dots, x_k) = \Phi(x_k)$ for all $k$.

## Remarks

A stationary method is a [[fixed-point iteration|K6ZF91051B]] for $\Phi$.
For a [[linear system|0GT4WWGWH2]] $A x = b$ with $A$ invertible, a *stationary linear method* has the form $x_{k+1} = G x_k + c$.
It is *consistent* if $x^* = A^{-1} b$ satisfies $x^* = G x^* + c$.
Then the error $e_k = x_k - x^*$ satisfies $e_{k+1} = G e_k$.
So the method converges for every $x_0$ if and only if the [[spectral radius|9V7YQA85PC]] of $G$ is less than $1$.
Example: $x_{k+1} = x_k / 2 + 1$ on $\R$ is stationary and consistent for $x / 2 = 1$, with $x^* = 2$.
Its error halves at each step, so it converges for every $x_0$.
Non-example: $x_{k+1} = 2 x_k - 2$ has the fixed point $2$, but the error doubles at each step.
It is not convergent for any $x_0 \ne 2$.
Krylov subspace methods are nonstationary: each iterate depends on all earlier ones, or on several of them.
