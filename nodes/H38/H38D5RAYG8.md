---
tag: H38D5RAYG8
kind: definition
name: Geometric optics
msc: [78A05, 35L05, 35B40]
defines: 90F3NWRHVD
uses: [5EHD2XBQDG, HGMX1QGTAZ, PVD7VZJZ9B, 0ABK9V9Y64]
sources:
  - url: https://en.wikipedia.org/wiki/Geometrical_optics
---

## Definition

Let $\Omega \subseteq \R^n$ be open and let $c \colon \Omega \to (0, \infty)$ be smooth.
Consider the reduced [[wave equation|5EHD2XBQDG]] $\Delta u + \frac{\omega^2}{c(x)^2} u = 0$ at a high frequency $\omega = 1/\varepsilon$.
The *geometric optics ansatz* is a formal series
$$u(x) = e^{i\varphi(x)/\varepsilon} \sum_{k=0}^{\infty} \varepsilon^k a_k(x),$$
with a real phase $\varphi$ and amplitudes $a_k$.
Inserting it into the equation and setting the coefficient of each power of $\varepsilon$ to zero gives:

1. the [[eikonal equation|HGMX1QGTAZ]] $\abs{\nabla \varphi}^2 = c(x)^{-2}$, from the power $\varepsilon^{-2}$;
2. the [[transport equation|PVD7VZJZ9B]] $2\nabla\varphi \cdot \nabla a_0 + (\Delta\varphi)\, a_0 = 0$, from the power $\varepsilon^{-1}$;
3. the transport equations $2\nabla\varphi \cdot \nabla a_k + (\Delta\varphi)\, a_k = i\, \Delta a_{k-1}$ for $k \ge 1$.

*Geometric optics* is the approximation of $u$ by such a series, with $\varphi$ and the $a_k$ solving these equations.
The rays are the integral curves of the [[gradient|0ABK9V9Y64]] $\nabla\varphi$.

## Remarks

Example: with $c \equiv 1$, the phase $\varphi(x) = e \cdot x$ with a unit vector $e$ satisfies the eikonal equation, and $a_0 = 1$, $a_k = 0$ for $k \ge 1$ satisfy the transport equations.
The series reduces to the exact solution $e^{i e \cdot x/\varepsilon}$, a plane wave whose rays are straight lines in the direction $e$.
Non-example: $\varphi(x) = 2\, e \cdot x$ with $c \equiv 1$ and $\abs{e} = 1$ fails clause 1, since $\abs{\nabla \varphi}^2 = 4$.
The eikonal equation usually has smooth solutions only locally; where rays cross, at caustics, the approximation breaks down and other ansätze are needed.
The same procedure applies to time-dependent hyperbolic equations, with phases $\varphi(x, t)$.
