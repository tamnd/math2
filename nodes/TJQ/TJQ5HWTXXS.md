---
tag: TJQ5HWTXXS
kind: definition
name: Hahn series
msc: ["13F25", "12J10"]
defines: YQP8V1KKMW
uses: [0QA8CHH8MG, 1P8087YGYQ, 071DDFVG4J, 0F1D6PK9RZ, 2S4K8FA8QY, SVY882HKSJ]
sources:
  - url: https://en.wikipedia.org/wiki/Hahn_series
---

## Definition

Let $K$ be a [[field|0QA8CHH8MG]] and let $\Gamma$ be an [[abelian group|071DDFVG4J]] with a total order making it a [[linearly ordered group|1P8087YGYQ]].
A *Hahn series* over $K$ with exponents in $\Gamma$ is a map $f \colon \Gamma \to K$, written $f = \sum_{\gamma \in \Gamma} f(\gamma) t^\gamma$, whose support $\set{\gamma \in \Gamma : f(\gamma) \ne 0}$ is [[well-ordered|0F1D6PK9RZ]].
The set of Hahn series is written $K((t^\Gamma))$.
Addition is pointwise, and multiplication is
$$(fg)(\gamma) = \sum_{\alpha + \beta = \gamma} f(\alpha) g(\beta).$$

## Remarks

For each $\gamma$ the sum defining $(fg)(\gamma)$ has finitely many nonzero terms, and the support of $fg$ is again well-ordered.
With these operations $K((t^\Gamma))$ is a field, as Hahn showed.
Example: for $\Gamma = \Z$, the well-ordered subsets are the subsets bounded below, so $K((t^\Z))$ is the [[field of formal Laurent series|2S4K8FA8QY]] $K((t))$.
Example: for $\Gamma = \Q$, the series $\sum_{n \ge 1} t^{1 - 1/n}$ is a Hahn series, since its support $\set{0, 1/2, 2/3, \dots}$ is well-ordered.
Non-example: for $\Gamma = \Z$, the formal sum $\sum_{n \ge 1} t^{-n}$ is not a Hahn series, since its support $\set{-1, -2, \dots}$ has no least element.
The map $v(f) = \min \set{\gamma : f(\gamma) \ne 0}$ for $f \ne 0$ is a [[valuation|SVY882HKSJ]] on $K((t^\Gamma))$ with value group $\Gamma$.
