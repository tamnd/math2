---
tag: TPSH4ETK67
kind: statement
role: theorem
name: Hörmander's L2 estimates
msc: [32W05, 35N15, 32T05]
uses: [AHYZMSBBNH, FF2P7ER3QT, M1VKCW3RFW, DC81TCR98Y, SASP14MA1Z]
about: [M1VKCW3RFW]
sources:
  - url: https://en.wikipedia.org/wiki/Dolbeault_cohomology
---

## Statement

Let $\Omega \subseteq \C^n$ be a [[pseudoconvex|AHYZMSBBNH]] open set.
Let $\varphi \in C^2(\Omega)$ be a real function, and let $c \colon \Omega \to (0, \infty)$ be a continuous function such that
$$\sum_{j,k=1}^n \frac{\partial^2 \varphi}{\partial z_j \partial \bar z_k}(z)\, w_j \bar w_k \ge c(z) \abs{w}^2 \quad \text{for all } z \in \Omega,\ w \in \C^n,$$
so that $\varphi$ is strictly [[plurisubharmonic|FF2P7ER3QT]].
Let $g = \sum_{j=1}^n g_j \, d\bar z_j$ be a [[(0,1)-form|DC81TCR98Y]] with coefficients $g_j$ in $L^2_{\mathrm{loc}}(\Omega)$.
Suppose that $\bar\partial g = 0$ in the sense of distributions and
$$\int_\Omega \frac{\abs{g}^2}{c}\, e^{-\varphi}\, d\lambda < \infty,$$
where $\abs{g}^2 = \sum_j \abs{g_j}^2$ and $\lambda$ is Lebesgue measure on $\C^n = \R^{2n}$.
Then there is a function $u \in L^2_{\mathrm{loc}}(\Omega)$ with $\bar\partial u = g$ in the sense of distributions and
$$\int_\Omega \abs{u}^2 e^{-\varphi}\, d\lambda \le \int_\Omega \frac{\abs{g}^2}{c}\, e^{-\varphi}\, d\lambda.$$

## Remarks

The proof is a duality argument in weighted [[L2 spaces|SASP14MA1Z]].
One views $\bar\partial$ as a closed, densely defined operator between $L^2$ spaces with weight $e^{-\varphi}$.
The key step is the a priori inequality $\norm{\bar\partial^* f}^2 + \norm{\bar\partial f}^2 \ge \int c \abs{f}^2 e^{-\varphi}$ for forms $f$ in the domains of both operators.
This Bochner–Kodaira–Morrey–Kohn type identity is where the plurisubharmonicity of $\varphi$ enters.
The Riesz representation theorem then gives the solution $u$ together with the bound; pseudoconvexity is used to exhaust $\Omega$ by sets on which the argument applies.
There is a version for any plurisubharmonic weight $\varphi$ on a pseudoconvex $\Omega$.
For every $\bar\partial$-closed $(0,1)$-form $g$ with $\int \abs{g}^2 e^{-\varphi} < \infty$ there is $u$ with $\bar\partial u = g$ and $\int \abs{u}^2 e^{-\varphi} (1 + \abs{z}^2)^{-2} \le \int \abs{g}^2 e^{-\varphi}$.
Similar statements hold for $(p,q)$-forms and on Stein and complete Kähler manifolds with Hermitian line bundles.
Example: for $\varphi(z) = \abs{z}^2$ one may take $c = 1$, so every $\bar\partial$-closed $g$ with $\int \abs{g}^2 e^{-\abs{z}^2} < \infty$ is $\bar\partial u$ for some $u$ with $\int \abs{u}^2 e^{-\abs{z}^2} \le \int \abs{g}^2 e^{-\abs{z}^2}$.
Pseudoconvexity cannot be dropped: an open set $\Omega \subseteq \C^n$ on which every smooth $\bar\partial$-closed $(0,q)$-form, $1 \le q \le n - 1$, is $\bar\partial$ of a smooth form is pseudoconvex.

## Explanations

### L1 human

The equation $\bar\partial u = g$ asks for a function whose failure to be holomorphic is prescribed.
Hörmander's theorem says that on a pseudoconvex domain this equation always has a solution, and that the size of the solution is controlled by the size of the data.
Size is measured by integrals with a weight $e^{-\varphi}$, and choosing the weight cleverly is the art of using the theorem.

### L2 human

The estimates turn the main existence problems of several complex variables into a single analytic tool.
To build a holomorphic function with given properties, one first builds a smooth function with these properties.
Then one corrects it by a solution of a $\bar\partial$-equation whose weighted $L^2$ norm is small.
In this way one obtains Oka's solution of the Levi problem, the Cousin problems on pseudoconvex domains, and Cartan's theorem B for the structure sheaf.
The method is the basis of the Ohsawa–Takegoshi extension theorem and of the theory of multiplier ideals.
