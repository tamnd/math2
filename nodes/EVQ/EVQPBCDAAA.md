---
tag: EVQPBCDAAA
kind: definition
name: Liénard–Wiechert potential
msc: [78A25, 78A35, 35Q61]
defines: B6SKCGENY8
uses: [9Q1NE5EP37, 6XPSV47R56, SAEDXNM3Y1, 8PEMR2J7EF]
sources:
  - url: https://en.wikipedia.org/wiki/Li%C3%A9nard%E2%80%93Wiechert_potential
---

## Definition

Let $\varepsilon_0, \mu_0 > 0$ and $c = 1/\sqrt{\varepsilon_0 \mu_0}$.
Let a point [[charge|6XPSV47R56]] $q$ move along a continuously differentiable path $r_s \colon \R \to \R^3$ with velocity $v_s = \dot r_s$.
Assume that there is $\beta_0 < 1$ with $\abs{v_s(t)} \le \beta_0 c$ for all $t$.
For a point $r$ and a time $t$ with $r \neq r_s(t)$ the *retarded time* $t_r$ is the unique solution of
$$t_r = t - \frac{\abs{r - r_s(t_r)}}{c}.$$
Put $n = (r - r_s(t_r)) / \abs{r - r_s(t_r)}$ and $\beta = v_s(t_r) / c$.
The *Liénard–Wiechert potentials* of the charge are
$$\varphi(r, t) = \frac{1}{4 \pi \varepsilon_0} \, \frac{q}{(1 - n \cdot \beta) \, \abs{r - r_s(t_r)}}, \qquad A(r, t) = \frac{\beta}{c} \, \varphi(r, t).$$

## Remarks

The retarded time exists and is unique because $s \mapsto s + \abs{r - r_s(s)}/c$ is strictly increasing and tends to $\pm\infty$ as $s \to \pm\infty$ when the speed stays below $\beta_0 c$.
Without a uniform bound below $c$ it can fail to exist: for a charge in hyperbolic motion some points never receive a signal from it.
The potentials are the [[retarded potentials|9Q1NE5EP37]] of the densities $\rho = q \, \delta(r - r_s(t))$ and $J = q \, v_s(t) \, \delta(r - r_s(t))$.
The factor $1 / (1 - n \cdot \beta)$ comes from the integration of the delta function against the retarded time.
Written out, $A = \frac{\mu_0}{4 \pi} \frac{q \, v_s(t_r)}{(1 - n \cdot \beta) \abs{r - r_s(t_r)}}$, since $\mu_0 = 1/(\varepsilon_0 c^2)$.

Example: for a charge at rest at $r_0$, one has $\beta = 0$, so $\varphi = q / (4 \pi \varepsilon_0 \abs{r - r_0})$ is the Coulomb potential and $A = 0$.

Non-example: for a moving charge the function $q / (4 \pi \varepsilon_0 \abs{r - r_s(t_r)})$ is not the Liénard–Wiechert potential, since it lacks the factor $1/(1 - n \cdot \beta)$; the two agree only at points where $n \cdot \beta = 0$.

## Explanations

### L1 human

The scalar potential is the Coulomb potential of the charge at its retarded position, multiplied by $1 / (1 - n \cdot \beta)$.
This factor is larger than $1$ in front of a charge that comes toward the point and smaller than $1$ behind it.
The vector potential points along the velocity of the charge.
