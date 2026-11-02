---
tag: S5HVHEPSMA
kind: definition
name: Period-doubling bifurcation
msc: ["37G15", "37E05", "34C23"]
defines: NQDTTZ59X8
uses: [R6QVS6P21N, T75CZ5H47N, MAP5J6HK0T]
sources:
  - url: https://en.wikipedia.org/wiki/Period-doubling_bifurcation
---

## Definition

Let $I, J \subseteq \R$ be open intervals and let $(x, \mu) \mapsto f_\mu(x)$ be a map $I \times J \to \R$ of class $C^3$.
Write $f_x, f_{xx}, f_{xxx}$ for the partial derivatives in $x$.
The family $(f_\mu)$ has a *period-doubling bifurcation* (or *flip bifurcation*) at $(x_0, \mu_0) \in I \times J$ if the following hold:

1. $f_{\mu_0}(x_0) = x_0$, so $x_0$ is a [[fixed point|R6QVS6P21N]] of $f_{\mu_0}$.
2. $f_x(x_0, \mu_0) = -1$.
3. Let $x(\mu)$ be the branch of fixed points through $x_0$, given by the implicit function theorem. Then $\mu \mapsto f_x(x(\mu), \mu)$ has a nonzero derivative at $\mu_0$.
4. $\frac{1}{2} f_{xx}(x_0, \mu_0)^2 + \frac{1}{3} f_{xxx}(x_0, \mu_0) \neq 0$.

## Remarks

Under these conditions, for $\mu$ near $\mu_0$ on one side of $\mu_0$ there is exactly one orbit of [[period|T75CZ5H47N]] $2$ near $x_0$.
On the other side there is none, and the period-$2$ orbit tends to $x_0$ as $\mu \to \mu_0$.
The sign of the quantity in clause 4 decides whether the bifurcation is supercritical, with an attracting period-$2$ orbit, or subcritical, with a repelling one.

Example: the logistic family $f_r(x) = r x (1 - x)$ at $r_0 = 3$ and $x_0 = 2/3$.
Clause 1: $3 \cdot \frac{2}{3} \cdot \frac{1}{3} = \frac{2}{3}$.
Clause 2: $f_x = r(1 - 2x) = 3 \cdot (-\frac{1}{3}) = -1$.
Clause 3: on the branch $x(r) = 1 - 1/r$ one has $f_x = 2 - r$, with derivative $-1$ in $r$.
Clause 4: $f_{xx} = -2r = -6$ and $f_{xxx} = 0$, so the quantity is $18 \neq 0$.
For $r > 3$ the period-$2$ orbit is $\frac{r + 1 \pm \sqrt{(r - 3)(r + 1)}}{2r}$.

Non-example: the family $f_\mu(x) = \mu - x$ satisfies clauses 1 and 2 at $(x_0, \mu_0) = (0, 0)$, but $f_x = -1$ for every $\mu$, so clause 3 fails.
Here every point other than the fixed point $\mu/2$ has period $2$ for every $\mu$, and no isolated orbit is born.

A fixed point with derivative $+1$ instead of $-1$ gives a [[saddle-node bifurcation|MAP5J6HK0T]] or one of its degenerate relatives.
