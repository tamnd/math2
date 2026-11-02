---
tag: AGRKRG1TMJ
kind: statement
role: theorem
name: Riesz–Thorin theorem
msc: [46B70, "46E30", 47A30]
uses: [SASP14MA1Z, WEBBT18D4X, 06EKW1AKXF]
about: [SASP14MA1Z, VX1R6FN6PS]
sources:
  - url: https://en.wikipedia.org/wiki/Riesz%E2%80%93Thorin_theorem
same_as:
  wikidata: Q245902
  wikipedia: Riesz–Thorin theorem
---

## Statement

Let $(X, \mu)$ and $(Y, \nu)$ be [[σ-finite|WEBBT18D4X]] measure spaces, and consider [[Lp spaces|SASP14MA1Z]] of complex-valued functions.
Let $1 \le p_0, p_1, q_0, q_1 \le \infty$.
Let $T$ be a linear map from $L^{p_0}(\mu) + L^{p_1}(\mu)$ to $L^{q_0}(\nu) + L^{q_1}(\nu)$.
Assume that there are constants $M_0, M_1 \ge 0$ with
$$\norm{T f}_{q_0} \le M_0 \norm{f}_{p_0} \text{ for } f \in L^{p_0}(\mu), \qquad \norm{T f}_{q_1} \le M_1 \norm{f}_{p_1} \text{ for } f \in L^{p_1}(\mu).$$
Let $0 < \theta < 1$, and define $p$ and $q$ by
$$\frac{1}{p} = \frac{1 - \theta}{p_0} + \frac{\theta}{p_1}, \qquad \frac{1}{q} = \frac{1 - \theta}{q_0} + \frac{\theta}{q_1}.$$
Then $T$ maps $L^p(\mu)$ into $L^q(\nu)$, and
$$\norm{T f}_q \le M_0^{1 - \theta} M_1^{\theta} \norm{f}_p \quad \text{for all } f \in L^p(\mu).$$

## Remarks

The proof is Thorin's complex-variable argument.
By [[density of simple functions|B6RYM7QTYZ]] and duality, it suffices to bound $\int (T f) g \, d\nu$ for simple $f$ and $g$.
One embeds $f$ and $g$ in analytic families $f_z$, $g_z$ for $z$ in the strip $0 \le \operatorname{Re} z \le 1$, with $f_\theta = f$ and $g_\theta = g$.
The function $z \mapsto \int (T f_z) g_z \, d\nu$ is bounded and analytic, and the [[Hadamard three-lines theorem|WHS58R43N0]] interpolates the bounds on the two edges.

Example: the Fourier transform satisfies $\norm{\hat f}_\infty \le \norm{f}_1$ and, by Plancherel, $\norm{\hat f}_2 = \norm{f}_2$ on $\R^n$ with suitable normalisation.
Riesz–Thorin with $p_0 = 1$, $q_0 = \infty$, $p_1 = q_1 = 2$ gives the Hausdorff–Young inequality $\norm{\hat f}_{p'} \le \norm{f}_p$ for $1 \le p \le 2$, where $1/p + 1/p' = 1$.

Complex scalars matter for the constant.
For spaces of real-valued functions the conclusion still holds, but the constant $M_0^{1-\theta} M_1^\theta$ may need an extra factor of at most $2$.

## Explanations

### L1 human

Suppose an operation on functions is under control in two ways of measuring size, say $L^1$ and $L^2$.
The theorem says that it is then also under control in every way of measuring size in between, such as $L^{4/3}$.
The bound in between is a weighted geometric mean of the two end bounds.

### L2 human

Riesz–Thorin is the basic tool for proving $L^p$ bounds from two easy endpoint bounds.
Typical uses are the Hausdorff–Young inequality, [[Young's convolution inequality|JXDKJCBXJ8]] and bounds for integral operators.
It needs linear operators and strong-type bounds at the endpoints.
The [[Marcinkiewicz interpolation theorem|R1PHMVBJ9J]] allows sublinear operators and weak-type endpoint bounds, at the cost of a worse constant and, in its basic form, only on the diagonal $p = q$.
Both are the starting points of abstract [[interpolation space|VX1R6FN6PS]] theory, the complex and the real method.
