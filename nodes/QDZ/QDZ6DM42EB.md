---
tag: QDZ6DM42EB
kind: statement
role: theorem
name: Allard regularity theorem
msc: [49Q15, 49Q05, 53A10]
uses: [N3QA80M44M, PA78NFEPCF, 012PBA0FMD]
about: [N3QA80M44M]
sources:
  - url: https://en.wikipedia.org/wiki/Varifold
---

## Statement

Let $1 \le m < n$ be integers and let $p > m$.
Then there are constants $\varepsilon > 0$ and $\gamma \in (0, 1)$, depending only on $n$, $m$ and $p$, with the following property.
Let $\rho > 0$, let $U \supseteq B_\rho(0)$ be an open subset of $\R^n$, and let $V$ be an $m$-dimensional rectifiable [[varifold|N3QA80M44M]] in $U$ with weight measure $\norm{V}$.
Suppose that:

1. the density of $V$ is at least $1$ at $\norm{V}$-almost every point;
2. $V$ has generalized [[mean curvature|PA78NFEPCF]] $H$ in $U$, with $H \in L^p(\norm{V})$;
3. $0$ lies in the support of $\norm{V}$;
4. $\dfrac{\norm{V}(B_\rho(0))}{\omega_m \rho^m} \le 1 + \varepsilon$, where $\omega_m$ is the volume of the unit ball of $\R^m$;
5. $\rho^{1 - m/p} \left( \int_{B_\rho(0)} \abs{H}^p \, d\norm{V} \right)^{1/p} \le \varepsilon$.

Let $\alpha = 1 - m/p$.
Then there are an $m$-dimensional linear subspace $T \subseteq \R^n$ and a $C^{1, \alpha}$ map $u$ from an open subset of $T$ to $T^\perp$ with this property.
The support of $\norm{V}$ inside $B_{\gamma\rho}(0)$ is the graph of $u$ intersected with $B_{\gamma\rho}(0)$.

## Remarks

The theorem is due to William Allard (1972).
Hypothesis 4 says that, at scale $\rho$, $V$ has nearly the area of a single flat $m$-disc; hypothesis 5 says that its mean curvature is small at that scale.
The proof shows that $V$ is close to a plane in a scale-invariant tilt-excess sense.
It then approximates $V$ by the graph of a Lipschitz function and shows that this function is nearly harmonic.
An iteration over smaller and smaller balls then gives a [[Hölder continuous|012PBA0FMD]] tangent plane, and the graph is $C^{1,\alpha}$.
The density bound in hypothesis 4 cannot be dropped.
Two planes crossing at the origin, or one plane with multiplicity $2$, are stationary varifolds with density $2$ at $0$.
Neither is the graph of a single function near $0$.
A main corollary concerns a stationary $V$ with density at least $1$.
The set of points near which its support is a smooth embedded submanifold is open and dense in the support.

## Explanations

### L1 human

A varifold is a very general kind of surface, possibly with folds, crossings and corners.
Suppose such a surface is almost balanced, in the sense of small mean curvature, and looks almost like a single flat sheet in a ball.
Allard's theorem says that it is then a smooth sheet in a smaller ball.
So roughness cannot hide inside a region where the surface has nearly the area of a flat disc.

### L2 human

The theorem is the basic $\varepsilon$-regularity result for stationary and almost stationary varifolds.
It plays the role for varifolds that De Giorgi's regularity theorem plays for perimeter minimizers.
Combined with the monotonicity formula, it gives regularity at every point where the density is close to $1$.
It does not decide what happens at points of higher density, which is where branch points and crossings can occur.
