---
tag: VXB4G47Z3T
kind: statement
role: theorem
name: Kigami's construction of Laplacians on post-critically finite fractals
msc: ["31E05", "28A80", "31C25"]
uses: [75B8VHDGSA, TN6M6DVZRP, THCM7DWHNY, MH20Q2N1AH]
about: [YY46TGRVBG, THCM7DWHNY]
sources:
  - url: https://en.wikipedia.org/wiki/Analysis_on_fractals
---

## Statement

Let $K \subset \R^d$ be the attractor of an [[iterated function system|75B8VHDGSA]] of contracting similitudes $F_1, \dots, F_N$, and assume that $K$ is connected and post-critically finite.
Let $V_0 \subset K$ be its finite boundary set, let $V_{m+1} = \bigcup_{i=1}^N F_i(V_m)$, and for a word $w = w_1 \cdots w_m$ write $F_w = F_{w_1} \circ \cdots \circ F_{w_m}$ and $r_w = r_{w_1} \cdots r_{w_m}$.
Let $\mathcal{E}_0(u) = \sum_{\set{p, q} \subset V_0} c_{pq} (u(p) - u(q))^2$ be the energy of an electrical network on $V_0$ with conductances $c_{pq} = c_{qp} \ge 0$ that connect $V_0$, and let $r_1, \dots, r_N \in (0, 1)$.
For $u \colon V_m \to \R$ set
$$\mathcal{E}_m(u) = \sum_{\abs{w} = m} r_w^{-1} \, \mathcal{E}_0(u \circ F_w|_{V_0}).$$
Assume the renormalization condition: for every $u \colon V_0 \to \R$, the minimum of $\mathcal{E}_1(v)$ over all $v \colon V_1 \to \R$ with $v|_{V_0} = u$ equals $\mathcal{E}_0(u)$.
Then:

1. For every function $u \colon K \to \R$, the sequence $\mathcal{E}_m(u|_{V_m})$ is nondecreasing in $m$; let $\mathcal{E}(u)$ be its limit in $[0, \infty]$.
2. Let $\mathcal{F} = \set{u \colon K \to \R : u \text{ continuous}, \ \mathcal{E}(u) < \infty}$, and define $\mathcal{E}(u, v)$ from $\mathcal{E}$ by polarization. Then $(\mathcal{E}, \mathcal{F})$ is a [[resistance form|THCM7DWHNY]] on $K$, and its resistance metric induces the usual topology of $K$.
3. For every finite Borel measure $\mu$ on $K$ whose support is $K$, $(\mathcal{E}, \mathcal{F})$ is a local regular [[Dirichlet form|MH20Q2N1AH]] on $L^2(K, \mu)$.
4. The Laplacian $\Delta_\mu$ is defined by: $\Delta_\mu u = f$, with $u \in \mathcal{F}$ and $f$ continuous, if $\mathcal{E}(u, v) = -\int_K f v \, d\mu$ for every $v \in \mathcal{F}$ that vanishes on $V_0$.

## Remarks

The renormalization condition says that $\mathcal{E}_0$ is the trace of $\mathcal{E}_1$ on $V_0$, and by self-similarity $\mathcal{E}_m$ is then the trace of $\mathcal{E}_{m+1}$ on $V_m$ for every $m$.
This gives the monotonicity in clause 1 and shows that each $u$ on $V_m$ has a unique extension to $V_{m+1}$ with the same energy, the harmonic extension.
The bound $(u(x) - u(y))^2 \le R(x, y) \, \mathcal{E}(u)$ with a resistance $R$ that is small on small cells gives the continuity of functions of finite energy; this uses $r_i < 1$.
For the Sierpiński gasket, with $\mathcal{E}_0$ the unit-conductance triangle and all $r_i = 3/5$, the renormalization condition is the computation of the "$1/5$–$2/5$ rule", as in [[Laplacian on the Sierpiński gasket|W9V9JSAWYK]].
Finding $\mathcal{E}_0$ and $r_i$ that satisfy the renormalization condition is a nonlinear fixed-point problem, and the theorem takes a solution as given.
A pair $(\mathcal{E}_0, (r_i))$ that satisfies the renormalization condition is called a harmonic structure, and it is called regular when all $r_i < 1$.
The construction is due to Kigami.

## Explanations

### L1 human

Many fractals can be cut into finitely many small copies of themselves which touch each other at only finitely many points.
On such a fractal, one can put a finite electrical network on the touching points at each level of detail.
The theorem says that if the network at level $0$ is chosen so that it agrees with the network at level $1$, then the energies of all levels fit together.
Their limit is an energy on the whole fractal, and from the energy and a measure one gets a Laplacian, much as the usual Laplacian comes from the energy $\int \abs{\nabla u}^2$.

### L2 human

The result turns the analysis of a fractal into linear algebra on a sequence of finite graphs, each step governed by the same [[Laplacian matrix|TN6M6DVZRP]].
Harmonic functions are determined by their values on $V_0$ and are computed level by level through fixed harmonic extension matrices.
Once the Laplacian exists, one studies its spectrum, the heat equation $\partial_t u = \Delta_\mu u$ and its heat kernel, and the diffusion process attached to the Dirichlet form by the Fukushima correspondence.
The resistance metric is the natural metric for these estimates.
The approach complements the probabilistic one, in which Brownian motion on the gasket is built as a limit of random walks on the graphs $\Gamma_m$.
