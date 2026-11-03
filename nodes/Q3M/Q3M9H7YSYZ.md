---
tag: Q3M9H7YSYZ
kind: problem
name: Gelfand–Bratu problem
msc: [35J61, 35B32, "80A25"]
uses: [0XQ2ZVN1PZ, G3XFT0MWKH, X3P4TQZ9X2]
about: [RCNY89A4NY]
sources:
  - url: https://en.wikipedia.org/wiki/Liouville%E2%80%93Bratu%E2%80%93Gelfand_equation
same_as:
  wikidata: Q30693537
  wikipedia: Liouville–Bratu–Gelfand equation
history:
  posed_by: "Gheorghe Bratu"
  first_stated: "1914"
---

## Problem

Let $n \ge 1$, let $\Omega \subseteq \R^n$ be a bounded domain with smooth boundary, and let $\lambda > 0$ be a parameter.
Find all functions $u \in C^2(\Omega) \cap C(\overline{\Omega})$ such that
$$-\Delta u = \lambda e^{u} \text{ in } \Omega, \qquad u = 0 \text{ on } \partial \Omega,$$
where $\Delta$ is the [[Laplacian|0XQ2ZVN1PZ]].
In particular, determine for which $\lambda$ solutions exist and how many there are.

## Remarks

This is a [[semilinear|X3P4TQZ9X2]] elliptic problem with a [[Dirichlet boundary condition|G3XFT0MWKH]]; the exponential nonlinearity makes it a standard test case for bifurcation theory and numerical continuation.
By the maximum principle every solution is positive in $\Omega$.
There is a number $\lambda^* \in (0, \infty)$, depending on $\Omega$, such that a minimal solution exists for $0 < \lambda < \lambda^*$ and no solution exists for $\lambda > \lambda^*$.
For $n = 1$ and $\Omega = (0, 1)$ the solutions are $u(x) = -2 \ln\big(\cosh(\vartheta (x - \tfrac12)/2) / \cosh(\vartheta/4)\big)$, where $\vartheta > 0$ solves $\vartheta = \sqrt{2 \lambda} \cosh(\vartheta/4)$.
This equation has two roots for $\lambda < \lambda^*$, one for $\lambda = \lambda^*$ and none for $\lambda > \lambda^*$, with $\lambda^* \approx 3.5138$.
On the unit ball of $\R^n$ with $n \ge 3$, the function $u = -2 \ln \abs{x}$ is a singular solution with $\lambda = 2(n-2)$.
Joseph and Lundgren (1973) showed that on the unit ball with $3 \le n \le 9$ there are infinitely many solutions for $\lambda = 2(n - 2)$.
In thermal explosion theory, the problem gives the steady states of the Frank-Kamenetskii model.
In 1853 Liouville found the general solution of $\Delta u + \lambda e^{u} = 0$ in the plane, without boundary condition; this is a form of [[Liouville's equation|C8E0TWY3WT]].

## Explanations

### L1 human

The problem asks for a steady temperature profile in a body that heats itself.
The heat source grows exponentially with the temperature, while the surface is kept at temperature zero.
The parameter $\lambda$ measures how strong the heating is compared with the cooling by conduction.
For small $\lambda$ the body has a gentle steady profile, and in simple cases such as a rod there is also a second, hotter one.
Beyond a critical value no steady profile exists at all, which in combustion means the body explodes.
