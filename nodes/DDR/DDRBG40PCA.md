---
tag: DDRBG40PCA
kind: statement
role: theorem
name: Lax entropy condition
msc: [35L67, 35L65, 76L05]
uses: [XN081NCPF5, P3VXR8FW17, S4XMYJ3V42, JSDMGGTG7G]
about: [JSDMGGTG7G, 1A01A3EJRX]
sources:
  - url: https://en.wikipedia.org/wiki/Shock_wave
---

## Statement

Let $U \subseteq \R^m$ be open and let $f \colon U \to \R^m$ be smooth.
Assume the [[conservation law|XN081NCPF5]] $u_t + f(u)_x = 0$ is [[strictly hyperbolic|P3VXR8FW17]], with eigenvalues $\lambda_1(u) < \cdots < \lambda_m(u)$ of $Df(u)$ and right eigenvectors $r_1(u), \ldots, r_m(u)$.
Fix $k$ and assume the $k$-th field is genuinely nonlinear, normalized so that $\nabla \lambda_k(u) \cdot r_k(u) = 1$ on $U$.
A triple $(u_l, u_r, \sigma)$ satisfies the *Lax entropy condition* for the $k$-th family if
$$\lambda_k(u_r) < \sigma < \lambda_k(u_l) \quad \text{and} \quad \lambda_{k-1}(u_l) < \sigma < \lambda_{k+1}(u_r),$$
where the conditions with $\lambda_0$ or $\lambda_{m+1}$ are omitted.
Let $u_l \in U$.
Then there are $\varepsilon_0 > 0$, a smooth curve $\varepsilon \mapsto S_k(\varepsilon) \in U$ and a smooth function $\varepsilon \mapsto \sigma_k(\varepsilon)$ on $(-\varepsilon_0, \varepsilon_0)$ such that:

1. $S_k(0) = u_l$, $S_k'(0) = r_k(u_l)$ and $\sigma_k(0) = \lambda_k(u_l)$;
2. $f(S_k(\varepsilon)) - f(u_l) = \sigma_k(\varepsilon) \big( S_k(\varepsilon) - u_l \big)$ for all $\abs{\varepsilon} < \varepsilon_0$;
3. $\sigma_k(\varepsilon) = \tfrac12 \big( \lambda_k(u_l) + \lambda_k(S_k(\varepsilon)) \big) + O(\varepsilon^2)$;
4. for $0 < \abs{\varepsilon} < \varepsilon_0$, the triple $(u_l, S_k(\varepsilon), \sigma_k(\varepsilon))$ satisfies the Lax entropy condition for the $k$-th family if and only if $\varepsilon < 0$.

## Remarks

Clause 2 is the [[Rankine–Hugoniot condition|S4XMYJ3V42]], so the states $S_k(\varepsilon)$ can be joined to $u_l$ by a $k$-shock.
The curve is found by the implicit function theorem applied to $\big( \int_0^1 Df(u_l + s(u - u_l))\, ds - \sigma I \big)(u - u_l) = 0$ near the simple eigenvalue $\lambda_k(u_l)$.
By the normalization, $\lambda_k(S_k(\varepsilon)) = \lambda_k(u_l) + \varepsilon + O(\varepsilon^2)$, and clause 3 gives $\sigma_k(\varepsilon) = \lambda_k(u_l) + \varepsilon/2 + O(\varepsilon^2)$.
So $\lambda_k(S_k(\varepsilon)) < \sigma_k(\varepsilon) < \lambda_k(u_l)$ exactly when $\varepsilon < 0$, and the other two inequalities hold for small $\varepsilon$ by strict hyperbolicity.

Example: for Burgers' equation, $m = 1$ and $f(u) = u^2/2$, one has $\lambda_1(u) = u$ and $r_1 = 1$.
Then $S_1(\varepsilon) = u_l + \varepsilon$ and $\sigma_1(\varepsilon) = u_l + \varepsilon/2$ exactly, and the shock is admissible if and only if $u_r < u_l$.

Genuine nonlinearity is needed: if $\nabla\lambda_k \cdot r_k = 0$ identically, then $\lambda_k(u_l) = \sigma = \lambda_k(u_r)$ along the whole curve, and the strict inequalities never hold.
Such jumps are contact discontinuities.

## Explanations

### L1 human

A conservation law can have several solutions with jumps, and only some of them are physical.
Lax's rule keeps a jump when the waves of its own family run into it from both sides.
Then the jump is fed by the flow and does not create information.
The theorem says that, among the small jumps of one family allowed by the conservation laws, exactly half pass this test.
For Burgers' equation the allowed jumps are those where the value drops from left to right.

### L2 human

The Lax condition, together with the Rankine–Hugoniot conditions, defines the admissible shocks used to solve the [[Riemann problem|GJWKX22VVE]] for small data.
For each genuinely nonlinear family, the admissible half of the shock curve joins with the rarefaction curve to a single wave curve through $u_l$.
For weak shocks of systems with a convex entropy, the Lax condition agrees with the entropy inequality that defines [[entropy solutions|1A01A3EJRX]].
For the Euler equations of a polytropic gas, it is equivalent to the gas being compressed across the shock.
