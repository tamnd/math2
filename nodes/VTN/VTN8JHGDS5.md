---
tag: VTN8JHGDS5
kind: statement
role: theorem
name: Kodaira–Nirenberg–Spencer existence theorem
msc: [32G05]
uses: [JSGWAN2RJV, VKQSM3BCE4, EWZ1G10MAY, PQ6Q143ARJ]
about: [VKQSM3BCE4, EWZ1G10MAY]
sources:
  - url: https://en.wikipedia.org/wiki/Kodaira%E2%80%93Spencer_map
---

## Statement

Let $X$ be a compact [[complex manifold|JSGWAN2RJV]], and let $\Theta_X$ be the sheaf of holomorphic vector fields on $X$.
Assume that $H^2(X, \Theta_X) = 0$, and let $m = \dim_\C H^1(X, \Theta_X)$.
Then there is a [[deformation|VKQSM3BCE4]] $\varpi \colon \mathcal{X} \to B$ of $X$ with $X_0 \cong X$, over an open neighbourhood $B$ of $0$ in $\C^m$.
Its [[Kodaira–Spencer map|EWZ1G10MAY]] at $0$,
$$\rho_0 \colon T_0 B \to H^1(X, \Theta_X)$$
is an isomorphism.

## Remarks

The proof writes a deformed complex structure as a vector-valued $(0,1)$-form $\varphi(t)$ with $\varphi(0) = 0$.
Integrability of the new structure is the equation $\bar\partial \varphi + \tfrac12 [\varphi, \varphi] = 0$.
One solves it by a power series in $t$ whose linear term runs over harmonic representatives of $H^1(X, \Theta_X)$.
At each order the obstruction to the next step lies in $H^2(X, \Theta_X)$, which is zero, and estimates for elliptic operators give convergence.
The Newlander–Nirenberg theorem then turns the integrable almost complex structures into complex manifolds.

By the completeness theorem of Kodaira and Spencer, a family with surjective Kodaira–Spencer map at $0$ is complete there.
So the family of the theorem contains all small deformations of $X$.

Example: for a compact Riemann surface of genus $g \ge 2$, $H^2(X, \Theta_X) = 0$ for dimension reasons, and $\dim H^1(X, \Theta_X) = 3g - 3$ by Riemann–Roch and Serre duality.
So $X$ has a complete family with a smooth $(3g-3)$-dimensional base.

Without the hypothesis $H^2(X, \Theta_X) = 0$, the conclusion can fail: the base of a complete family with bijective Kodaira–Spencer map may have to be singular.

## Explanations

### L1 human

The space $H^1(X, \Theta_X)$ lists all the directions in which the complex structure of $X$ could move to first order.
The theorem says that, if a certain obstruction space vanishes, every such direction is realized by an actual family.
So the small deformations of $X$ are parametrized by a ball in $H^1(X, \Theta_X)$.

### L2 human

This is the first general existence result in the deformation theory of complex manifolds, from 1958.
Kuranishi later removed the hypothesis by allowing singular bases: his family lives over the zero set of an obstruction map from $H^1$ to $H^2$.
The theorem applies to curves and to many surfaces, and it is the local model behind moduli spaces of these objects.
It does not apply to complex tori of dimension at least $2$, where $H^2(X, \Theta_X) \ne 0$, although their deformations are still unobstructed.
