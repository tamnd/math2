---
tag: 4PDKJ8N1S9
kind: statement
role: theorem
name: Strichartz estimate
msc: [35Q41, 35B45, 35Q55]
uses: [EPZR6H2WJN, DPVM34ADZV, SASP14MA1Z]
about: [EPZR6H2WJN, AYMJ2NFR4W]
sources:
  - url: https://en.wikipedia.org/wiki/Strichartz_estimate
same_as:
  wikidata: Q18393075
  wikipedia: Strichartz estimate
---

## Statement

Let $n \ge 1$.
For $f \in L^2(\R^n)$ and $t \in \R$, let $e^{it\Delta} f$ be the solution at time $t$ of the free [[Schrödinger equation|EPZR6H2WJN]] $i u_t + \Delta u = 0$ with $u(0) = f$.
It is given by the [[Fourier transform|DPVM34ADZV]] as $\widehat{e^{it\Delta} f}(\xi) = e^{-it\abs{\xi}^2} \hat f(\xi)$.
Call a pair $(q, r)$ admissible if $2 \le q \le \infty$, $2 \le r \le \infty$,
$$\frac{2}{q} + \frac{n}{r} = \frac{n}{2},$$
and $(q, r, n) \ne (2, \infty, 2)$.
Let $(q, r)$ be admissible, and let $L^r$ denote the [[Lebesgue space|SASP14MA1Z]].
Then there is a constant $C = C(n, q, r)$ with
$$\Big( \int_{\R} \norm{e^{it\Delta} f}_{L^r(\R^n)}^q \, dt \Big)^{1/q} \le C \norm{f}_{L^2(\R^n)} \quad \text{for all } f \in L^2(\R^n).$$
For $q = \infty$ the left side means $\sup_{t} \norm{e^{it\Delta} f}_{L^r(\R^n)}$.

## Remarks

The proof combines two facts.
The first is the dispersive estimate $\norm{e^{it\Delta} f}_{L^\infty} \le (4\pi\abs{t})^{-n/2} \norm{f}_{L^1}$, which follows from the explicit kernel of $e^{it\Delta}$; interpolation with the conservation of the $L^2$ norm gives the $L^{r'} \to L^r$ bounds.
The second is the $TT^*$ argument, which reduces the estimate to a bound for a time convolution handled by the Hardy–Littlewood–Sobolev inequality when $q > 2$.
The endpoint $q = 2$, $r = \frac{2n}{n - 2}$ for $n \ge 3$ was proved by Keel and Tao in 1998.
The relation $\frac{2}{q} + \frac{n}{r} = \frac{n}{2}$ is forced by scaling: if $f_\lambda(x) = f(\lambda x)$, then $e^{it\Delta} f_\lambda (x) = (e^{i\lambda^2 t\Delta} f)(\lambda x)$, and comparing powers of $\lambda$ on both sides gives the relation.
Example: for $n = 1$ the pair $(q, r) = (4, \infty)$ is admissible, and for $n = 2$ the pair $(4, 4)$ is admissible, the case first proved by Strichartz.

## Explanations

### L1 human

Waves of the Schrödinger equation spread out, so the solution cannot stay concentrated for long.
The Strichartz estimate measures this: although the total mass $\norm{u(t)}_{L^2}$ never changes, the solution is small in other norms for most times.
Averaged in time, the solution is more integrable in space than the initial data alone would suggest.
This extra integrability is what makes nonlinear equations tractable.

### L2 human

Strichartz estimates are the basic tool for the local and global well-posedness of nonlinear [[dispersive equations|AYMJ2NFR4W]], such as the nonlinear Schrödinger equation $i u_t + \Delta u = \pm\abs{u}^{p-1} u$.
One writes the equation in Duhamel form and runs a fixed point argument in the spaces $L^q_t L^r_x$, using the inhomogeneous version of the estimate.
Similar estimates hold for the wave and Klein–Gordon equations, with different admissibility conditions and a loss of derivatives.
Abstract versions, due to Keel and Tao, need only an energy bound and a dispersive decay estimate for the evolution.
