---
tag: 08S7FDRS5Z
kind: definition
name: Differentiable on an open set
msc: [26B05]
defines: 0HHHDCXZV4
uses: [0135XZZQ8M]
sources:
  - url: https://en.wikipedia.org/wiki/Differentiable_function
    locator: Differentiability in higher dimensions
---

## Definition

Let $U \subseteq \mathbb{R}^n$ be an open set and let $f \colon U \to \mathbb{R}^m$.
The function $f$ is differentiable on $U$ when it is [[differentiable|0135XZZQ8M]] at each point $a \in U$.
Then the derivative of $f$ is the map $Df \colon U \to L(\mathbb{R}^n, \mathbb{R}^m)$, $a \mapsto Df(a)$, where $L(\mathbb{R}^n, \mathbb{R}^m)$ is the space of linear maps from $\mathbb{R}^n$ to $\mathbb{R}^m$.

## Remarks

The function $f$ is continuously differentiable, or of class $C^1$, on $U$ when it is differentiable on $U$ and $Df$ is continuous. Here $L(\mathbb{R}^n, \mathbb{R}^m)$ carries the topology of $m \times n$ matrices.
For a set $S$ that is not open, one uses derivatives within $S$ instead. On an open set the two notions agree.
Each polynomial map $\mathbb{R}^n \to \mathbb{R}^m$ is differentiable on $\mathbb{R}^n$.

## Explanations

### L1 human

Differentiable on $U$ means that there is a good linear approximation at each point of $U$, not only at one point.
The approximation changes from point to point, so the derivative is itself a function on $U$.
