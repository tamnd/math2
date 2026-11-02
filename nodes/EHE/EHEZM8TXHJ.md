---
tag: EHEZM8TXHJ
kind: definition
name: Continuous dual space
msc: [46A20]
defines: 4A82S5FVRT
uses: [07YQ1C78G0, 03TM135G0N, 07JBSZE0V4]
sources:
  - url: https://en.wikipedia.org/wiki/Dual_space
    locator: Continuous dual space
---

## Definition

Let $\mathbb{K}$ be $\R$ or $\C$, and let $E$ be a [[topological vector space|T32W553W95]] over $\mathbb{K}$.
The *continuous dual space* of $E$ is the set $E'$ of all [[continuous linear maps|03TM135G0N]] $f \colon E \to \mathbb{K}$, that is, of all continuous [[linear forms|07YQ1C78G0]] on $E$.
With pointwise addition and scalar multiplication, $E'$ is a linear subspace of the algebraic [[dual space|07JBSZE0V4]] of $E$.

## Remarks

The notations $E^*$ and $E'$ are both common; some texts reserve $E^*$ for the algebraic dual.
A linear form $f$ is continuous if and only if it is bounded on some neighbourhood of $0$.
For a normed space $E$, $f$ is continuous if and only if $\norm{f} = \sup_{\norm{x} \le 1} \abs{f(x)} < \infty$, and $E'$ with this norm is a Banach space.
Example: on $\ell^2$, for fixed $y \in \ell^2$, the form $f(x) = \sum_n x_n y_n$ is in $(\ell^2)'$, since $\abs{f(x)} \le \norm{y} \norm{x}$ by the Cauchy–Schwarz inequality.
Non-example: on the space $c_{00}$ of finitely supported sequences with the sup norm, $f(x) = \sum_n x_n$ is linear but not continuous, since $x = e_1 + \cdots + e_k$ has norm $1$ and $f(x) = k$.
For a Hausdorff locally convex space $E$, the Hahn–Banach theorem gives that $E'$ separates the points of $E$; for $L^p([0, 1])$ with $0 < p < 1$, by contrast, $E' = \set{0}$.
