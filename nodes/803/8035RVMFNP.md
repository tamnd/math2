---
tag: 8035RVMFNP
kind: definition
name: Path integral formulation
msc: [81S40, 81Q30, 81T08]
defines: 1NYTFT5NPE
uses: [EPZR6H2WJN, T0WAGV4KP4, 0NEGN5CRSC, DT49GKR9AS, G686S8SEK0, W26MGR4DA3]
sources:
  - url: https://en.wikipedia.org/wiki/Path_integral_formulation
---

## Definition

Let $d \ge 1$, $m > 0$ and $\hbar > 0$, and let $V \colon \R^d \to \R$ be measurable.
Let $H_0 = -\frac{\hbar^2}{2m}\Delta$ on $L^2(\R^d)$, and assume that $H_0 + V$ is [[essentially self-adjoint|DT49GKR9AS]] on $D(H_0) \cap D(V)$, with closure $H$.
For a path through the points $x_0, x_1, \dots, x_N \in \R^d$ at the times $0, \varepsilon, \dots, N\varepsilon$, the time-sliced [[action|T0WAGV4KP4]] is
$$S_N(x_0, \dots, x_N) = \sum_{k=1}^{N} \varepsilon \left( \frac{m}{2} \abs{\frac{x_k - x_{k-1}}{\varepsilon}}^2 - V(x_{k-1}) \right).$$
The *path integral formulation* expresses the solution $\psi(t) = e^{-itH/\hbar}\psi_0$ of the [[Schrödinger equation|EPZR6H2WJN]] as a limit.
$$\psi(t)(x) = \lim_{N \to \infty} \left( \frac{m}{2\pi i \hbar \varepsilon} \right)^{Nd/2} \int_{\R^d} \cdots \int_{\R^d} e^{i S_N(x_0, \dots, x_{N-1}, x)/\hbar}\, \psi_0(x_0)\, dx_0 \cdots dx_{N-1}.$$
Here $\varepsilon = t/N$ and $\psi_0 \in L^1 \cap L^2(\R^d)$.
The integrals are iterated integrals, each read as an $L^2$ limit of integrals over balls when needed.
The limit in $N$ is taken in $L^2(\R^d)$.
Formally this is written $\psi(t)(x) = \int e^{iS[q]/\hbar}\, \psi_0(q(0))\, \mathcal{D}q$, an integral over all paths $q$ with $q(t) = x$, where $S[q] = \int_0^t \left( \frac{m}{2}\abs{\dot q}^2 - V(q) \right) ds$ is the classical action.

## Remarks

The limit exists by the Trotter product formula $e^{-itH/\hbar} = \lim_N \left( e^{-i\varepsilon H_0/\hbar} e^{-i\varepsilon V/\hbar} \right)^N$ in the strong sense, which holds under the stated hypothesis on $H_0 + V$.
Each factor $e^{-i\varepsilon H_0/\hbar}$ has the integral kernel $\left( \frac{m}{2\pi i\hbar\varepsilon} \right)^{d/2} \exp\!\left( \frac{i m \abs{x - y}^2}{2\hbar\varepsilon} \right)$ on $L^1 \cap L^2$, and multiplying these kernels with the phases $e^{-i\varepsilon V(x_{k-1})/\hbar}$ gives the integrand above.

Example: for $V = 0$ and $N = 1$ the formula is exact, and it is the free propagator.

The formal measure $\mathcal{D}q$ does not exist as a countably additive measure on paths, so the definition must go through a limit of this kind.
After the [[Wick rotation|G686S8SEK0]] $t = -i\tau$, the oscillating factors become Gaussian weights, and the limit becomes an integral against Wiener measure; this is the [[Feynman–Kac formula|W26MGR4DA3]].
The same form, with fields in place of paths, is the starting point of perturbative quantum field theory.
