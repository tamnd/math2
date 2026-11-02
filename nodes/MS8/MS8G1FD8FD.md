---
tag: MS8G1FD8FD
kind: definition
name: Ruelle zeta function
msc: ["37C30", "11M41"]
defines: ENYXKW76AA
uses: [2A5Z21CE4P, R6QVS6P21N, 033WGN00BF, 624XDXX8FN]
sources:
  - url: https://en.wikipedia.org/wiki/Ruelle_zeta_function
---

## Definition

Let $X$ be a set and let $f \colon X \to X$ be a map.
Assume that the set $\operatorname{Fix}(f^n)$ of [[fixed points|R6QVS6P21N]] of $f^n$ is finite for every $n \ge 1$.
Let $\varphi \colon X \to \C$ be a function, called the weight.
The *Ruelle zeta function* of $(f, \varphi)$ is the [[formal power series|033WGN00BF]]
$$\zeta_{f, \varphi}(z) = \exp\left( \sum_{n=1}^{\infty} \frac{z^n}{n} \sum_{x \in \operatorname{Fix}(f^n)} \prod_{k=0}^{n-1} \varphi(f^k x) \right).$$

## Remarks

Example: let $f$ be the shift on the full shift $\set{0, 1}^{\N}$ and let $\varphi = c$ be a constant.
The shift $f^n$ has $2^n$ fixed points, each of weight $c^n$, so $\zeta_{f, \varphi}(z) = \exp \sum_{n \ge 1} (2cz)^n / n = 1/(1 - 2cz)$.

Non-example: for the identity map of the circle the set $\operatorname{Fix}(f)$ is infinite, so the inner sum is not defined.

With $\varphi = 1$ one gets the [[Artin–Mazur zeta function|2A5Z21CE4P]] of $f$.
More generally the weight may take values in $d \times d$ matrices, and then the product is replaced by the trace of the ordered product $\varphi(f^{n-1} x) \cdots \varphi(x)$.
If $f$ is the shift on a [[subshift of finite type|624XDXX8FN]] with transition matrix $A$ and $\varphi(x) = w(x_0, x_1)$ depends only on the first two symbols, then $\zeta_{f, \varphi}(z) = 1/\det(I - z B)$, where $B_{ij} = A_{ij} w(i, j)$.
