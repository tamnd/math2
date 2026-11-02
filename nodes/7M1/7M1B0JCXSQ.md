---
tag: 7M1B0JCXSQ
kind: example
name: KdV equation as an integrable system
msc: [37K10, 35Q53, 37K15]
illustrates: [N0N7CMRCMH]
uses: [KTT75QC72Z, G3A4S7CSB3, 63D4AXYCT4, W6QS1ME39J]
sources:
  - url: https://en.wikipedia.org/wiki/Korteweg–De_Vries_equation
---

## Example

The [[Korteweg–De Vries equation|KTT75QC72Z]], written here as
$$u_t + u_{xxx} + 6 u u_x = 0$$
for a real function $u(x, t)$ that decays fast as $\abs{x} \to \infty$, is an infinite-dimensional [[integrable system|N0N7CMRCMH]].

It is Hamiltonian: with
$$\mathcal{H}(u) = \int_{\R} \left( \tfrac{1}{2} u_x^2 - u^3 \right) dx,$$
the variational derivative is $\delta \mathcal{H} / \delta u = -u_{xx} - 3 u^2$, and the equation reads $u_t = \partial_x \left( \delta \mathcal{H} / \delta u \right)$.

It has infinitely many conserved quantities.
The first ones are $\int u \, dx$, $\int u^2 \, dx$ and $\int \left( u^3 - \tfrac{1}{2} u_x^2 \right) dx$.
For the third one, integration by parts gives $\frac{d}{dt} \int u^3 \, dx = -3 \int u_x^3 \, dx$ and $\frac{d}{dt} \int \tfrac{1}{2} u_x^2 \, dx = -3 \int u_x^3 \, dx$, so the difference is constant.

It has a [[Lax pair|G3A4S7CSB3]]: with the [[Schrödinger operator|W6QS1ME39J]] $L = -\partial_x^2 - u$, there is a third-order differential operator $B$ such that the equation is equivalent to $L_t = [B, L]$.
Hence the spectrum of $L$ does not change in time.

## Remarks

Gardner, Greene, Kruskal and Miura solved the equation in 1967 by the inverse scattering transform.
The scattering data of $L$ evolve by explicit linear equations, and $u$ is recovered from them.
Each eigenvalue of $L$ corresponds to a [[soliton|63D4AXYCT4]], and a general decaying solution splits for large time into solitons and a dispersing tail.
Zakharov and Faddeev showed in 1971 that the scattering data give action-angle variables, in analogy with the [[Liouville–Arnold theorem|PNQCW85HTJ]].

## Explanations

### L1 human

The KdV equation describes long waves in shallow water.
It behaves like a mechanical system with infinitely many degrees of freedom, and it has infinitely many conserved quantities.
That is why it can be solved exactly, and why its solitary waves pass through each other and keep their shape.
