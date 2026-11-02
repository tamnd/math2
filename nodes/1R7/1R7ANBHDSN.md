---
tag: 1R7ANBHDSN
kind: definition
name: Riemannian metric
msc: [53B20, 53C20]
defines: Q61VFHCH2J
uses: [F45VQ47GPV, WY6K3P4YCG, 0NB0AWGJBW, WX302T93TW, NH739XXVXK]
sources:
  - url: https://en.wikipedia.org/wiki/Metric_tensor
---

## Definition

Let $M$ be a smooth manifold with [[tangent bundle|WY6K3P4YCG]] $TM$.
A *Riemannian metric* on $M$ is a family $g = (g_p)_{p \in M}$ such that:

1. for each $p \in M$, $g_p$ is an [[inner product|0NB0AWGJBW]] on $T_pM$, that is, a symmetric positive definite bilinear form;
2. for all smooth vector fields $X, Y$ on $M$, the function $p \mapsto g_p(X_p, Y_p)$ is smooth.

## Remarks

Equivalently, $g$ is a smooth symmetric [[tensor field|WX302T93TW]] of type $(0, 2)$ that is positive definite at every point.
In a chart, $g = \sum_{i,j} g_{ij} \, dx^i \otimes dx^j$ where $(g_{ij}(p))$ is a symmetric positive definite matrix depending smoothly on $p$; one often writes $ds^2 = g_{ij} \, dx^i dx^j$.
Example: on the upper half-plane $\set{(x, y) : y > 0}$, $g = (dx^2 + dy^2)/y^2$ is a Riemannian metric; its matrix $y^{-2} I$ is symmetric and positive definite because $y > 0$, and its entries are smooth.
Non-example: on $\R^2$, $g = x^2 (dx^2 + dy^2)$ fails clause 1 on the line $x = 0$, where $g_p = 0$ is not positive definite.
The length of a piecewise smooth curve $\gamma : [a, b] \to M$ is $\int_a^b \sqrt{g(\gamma'(t), \gamma'(t))} \, dt$.
Every smooth manifold (Hausdorff and second countable) has a Riemannian metric: glue Euclidean metrics of charts with a [[partition of unity|NH739XXVXK]]; positive definiteness survives convex combinations.
