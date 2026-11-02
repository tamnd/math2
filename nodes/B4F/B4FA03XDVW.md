---
tag: B4FA03XDVW
kind: statement
role: theorem
name: Multilevel Monte Carlo method
msc: [65C05, 65C30]
uses: [HWP11G3HTN, A01GEGWKVB, 0WQNRCNY3M, 0477R9PYAE, 05NZ1HHQMV]
about: [HWP11G3HTN]
sources:
  - url: https://en.wikipedia.org/wiki/Multilevel_Monte_Carlo_method
same_as:
  wikidata: Q48998192
  wikipedia: Multilevel Monte Carlo method
---

## Statement

Let $P$ be a random variable with finite [[expected value|0WQNRCNY3M]].
Let $P_0, P_1, P_2, \ldots$ be random variables on the same probability space, the approximations of $P$ at levels $\ell = 0, 1, 2, \ldots$, and set $P_{-1} = 0$.
For each level $\ell$ let $Y_\ell$ be an estimator of $\mathbb E[P_\ell - P_{\ell - 1}]$ built from $N_\ell$ independent samples, with total cost $C_\ell$.
Let the $Y_\ell$ be independent.
Suppose there are positive constants $\alpha, \beta, \gamma, c_1, c_2, c_3$ with $\alpha \ge \frac12 \min(\beta, \gamma)$ such that for all $\ell \ge 0$:

1. $\abs{\mathbb E[P_\ell - P]} \le c_1 2^{-\alpha \ell}$;
2. $\mathbb E Y_\ell = \mathbb E[P_\ell - P_{\ell - 1}]$;
3. $\operatorname{Var} Y_\ell \le c_2 N_\ell^{-1} 2^{-\beta \ell}$;
4. $\mathbb E C_\ell \le c_3 N_\ell 2^{\gamma \ell}$.

Then there is a constant $c_4$ with the following property.
For every $0 < \varepsilon < e^{-1}$ there are a level $L$ and sample sizes $N_0, \ldots, N_L$ such that the estimator $Y = \sum_{\ell = 0}^{L} Y_\ell$ satisfies the following.
Its [[mean squared error|05NZ1HHQMV]] is $\mathbb E[(Y - \mathbb E P)^2] < \varepsilon^2$, and its expected total cost is
$$\mathbb E \sum_{\ell=0}^{L} C_\ell \le \begin{cases} c_4\, \varepsilon^{-2} & \text{if } \beta > \gamma, \\ c_4\, \varepsilon^{-2} (\ln \varepsilon)^2 & \text{if } \beta = \gamma, \\ c_4\, \varepsilon^{-2 - (\gamma - \beta)/\alpha} & \text{if } \beta < \gamma. \end{cases}$$

## Remarks

The telescoping sum $\mathbb E P_L = \sum_{\ell=0}^{L} \mathbb E[P_\ell - P_{\ell-1}]$ shows that $Y$ estimates $\mathbb E P_L$ without bias, so its mean squared error is the squared bias $(\mathbb E[P_L - P])^2$ plus $\sum_\ell \operatorname{Var} Y_\ell$.
One chooses $L$ by clause 1 so that the bias is below $\varepsilon/\sqrt2$.
The $N_\ell$ then minimise the cost under the constraint $\sum_\ell \operatorname{Var} Y_\ell \le \varepsilon^2/2$.
A Lagrange multiplier gives $N_\ell$ proportional to $\sqrt{V_\ell / c_\ell}$, where $V_\ell$ and $c_\ell$ are the variance and cost of one sample on level $\ell$.
The variance decay in clause 3 comes from coupling: $P_\ell$ and $P_{\ell-1}$ are computed from the same random input, so their difference is small.
Example: consider $\mathbb E\, \varphi(S_T)$, where $S$ solves a stochastic differential equation and $\varphi$ is Lipschitz.
Under standard conditions, the Euler–Maruyama scheme with $2^\ell$ time steps gives $\alpha = 1$, $\beta = 1$ and $\gamma = 1$.
So the cost is $O(\varepsilon^{-2} (\ln \varepsilon)^2)$, against $O(\varepsilon^{-3})$ for plain Monte Carlo with the same scheme.
In the case $\beta > \gamma$ the cost has the same order $\varepsilon^{-2}$ as plain Monte Carlo with exact samples of $P$ at unit cost.

## Explanations

### L1 human

Plain Monte Carlo with an approximate model must use a fine and expensive model for every sample.
The multilevel method uses many cheap samples of a coarse model and only a few expensive samples of the fine model, to correct the coarse answer.
The corrections have small variance, because the fine and coarse models are run with the same random input, so few samples are needed for them.
Overall the work can drop from $\varepsilon^{-3}$ to about $\varepsilon^{-2}$ for accuracy $\varepsilon$.

### L2 human

The method, introduced by Giles for stochastic differential equations, is related to earlier multilevel work of Heinrich on parametric integration.
It is a recursive [[variance reduction|A01GEGWKVB]]: each level acts as a control variate for the next.
The three regimes of the theorem say whether the cost is dominated by the coarsest levels ($\beta > \gamma$), spread evenly ($\beta = \gamma$), or dominated by the finest level ($\beta < \gamma$).
The Milstein scheme improves the strong convergence and gives $\beta = 2$ in many scalar problems, which moves the Euler–Maruyama case $\beta = \gamma$ to the optimal regime $\beta > \gamma$.
The same framework applies to partial differential equations with random coefficients, where the levels are finite element meshes.
