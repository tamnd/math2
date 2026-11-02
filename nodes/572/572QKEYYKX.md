---
tag: 572QKEYYKX
kind: statement
role: theorem
name: Lieb–Thirring inequality
msc: [35P15, 81Q10, 47A75]
uses: [89AA6XJY5K, 0BQAA2BK3Q]
about: [89AA6XJY5K]
sources:
  - url: https://en.wikipedia.org/wiki/Lieb%E2%80%93Thirring_inequality
same_as:
  wikidata: Q25303678
  wikipedia: Lieb–Thirring inequality
---

## Statement

Let $n \ge 1$ be an integer and let $\gamma$ be a real number with
$$\gamma \ge \tfrac{1}{2} \text{ if } n = 1, \qquad \gamma > 0 \text{ if } n = 2, \qquad \gamma \ge 0 \text{ if } n \ge 3.$$
Then there is a constant $L_{\gamma,n}$, depending only on $\gamma$ and $n$, with the following property.
Let $V \colon \R^n \to \R$ be measurable with positive part $V_+ = \max(V, 0)$ locally integrable and negative part $V_- = \max(-V, 0)$ in the Lebesgue space $L^{\gamma + n/2}(\R^n)$.
Let $E_1 \le E_2 \le \cdots < 0$ be the negative [[eigenvalues|0BQAA2BK3Q]], counted with multiplicity, of the [[Schrödinger operator|89AA6XJY5K]] $-\Delta + V$ on $L^2(\R^n)$, defined through its quadratic form.
Then
$$\sum_j \abs{E_j}^\gamma \le L_{\gamma,n}\int_{\R^n} V_-(x)^{\gamma + n/2} \, dx,$$
where for $\gamma = 0$ the left side is the number of negative eigenvalues.

## Remarks

The right side is, up to a constant, the semiclassical value: counting phase-space volume gives $\sum_j \abs{E_j}^\gamma \approx L^{\mathrm{cl}}_{\gamma,n}\int V_-^{\gamma + n/2} \, dx$ for large potentials.
Lieb and Thirring proved the inequality for $\gamma > 1/2$ when $n = 1$ and $\gamma > 0$ when $n \ge 2$.
The case $\gamma = 0$, $n \ge 3$ is the Cwikel–Lieb–Rozenblum bound, and the endpoint $\gamma = 1/2$, $n = 1$ is due to Weidl.
The restrictions on $\gamma$ are needed.
For $n = 1, 2$, every nonzero $V \le 0$ produces a negative eigenvalue, so no bound with $\gamma = 0$ is possible there.
For $n = 1$ the bound also fails for $0 < \gamma < 1/2$.

For $\gamma = 1$, a duality argument turns the inequality into a lower bound on kinetic energy.
For an $N$-fermion wave function with one-particle density $\rho$, the kinetic energy is at least $K_n\int \rho(x)^{1 + 2/n} \, dx$ for a constant $K_n > 0$.

## Explanations

### L1 human

The negative eigenvalues of $-\Delta + V$ are the bound states of a quantum particle in a potential well $V$.
The inequality says that a shallow or small well cannot hold many deep bound states.
The total, measured by the sum of powers of the binding energies, is controlled by a single integral of the well depth.

### L2 human

Lieb and Thirring found the inequality to give a short proof of the stability of matter.
This says that the energy of $N$ electrons and $N$ nuclei is at least $-CN$ for a constant $C$ independent of $N$.
The case $\gamma = 1$ is the key, through the kinetic energy bound, which resembles the Thomas–Fermi model.
The sharp constants are an active topic; for $n = 1$ and $\gamma = 3/2$ the sharp constant equals the semiclassical one.
The inequality is a quantitative version of the fact that $-\Delta + V$ has finitely many negative eigenvalues when $V_-$ is small at infinity.
