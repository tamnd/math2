---
tag: BE2CBPAZK6
kind: definition
name: Gaussian free field
msc: [60G60, 60G15, 81T40]
defines: EGCDMWYKQB
uses: [00C0BR7D7H, 0E0B6RA8K0, 22WEM6RTW0, 0DJ8W3HP2D]
sources:
  - url: https://en.wikipedia.org/wiki/Gaussian_free_field
---

## Definition

Let $G = (V, E)$ be a finite connected [[graph|00C0BR7D7H]], let $B \subseteq V$ be a nonempty set of boundary vertices, and let $U = V \setminus B$ be nonempty.
For $f \colon V \to \R$, let $\Delta f(x) = \sum_{y : \set{x, y} \in E} (f(y) - f(x))$ be the graph [[Laplacian|0E0B6RA8K0]], and let $\Delta_U$ be its restriction to functions that vanish on $B$, viewed as a $U \times U$ matrix.
The *discrete Gaussian free field* on $G$ with zero boundary values on $B$ is a random function $h \colon V \to \R$ with $h = 0$ on $B$.
Its values $(h(x))_{x \in U}$ have the following density on $\R^U$:
$$\frac{1}{Z} \exp\Big( -\frac12 \sum_{\set{x, y} \in E} \big(h(x) - h(y)\big)^2 \Big),$$
where $Z$ is the normalising constant.

## Remarks

The exponent equals $-\frac12 \langle h, -\Delta_U h \rangle$, and $-\Delta_U$ is positive definite because $B$ is nonempty and $G$ is connected.
So $h$ restricted to $U$ is a centred [[Gaussian process|22WEM6RTW0]] with [[covariance|0DJ8W3HP2D]] matrix $(-\Delta_U)^{-1}$.
This matrix is the Green function of the continuous-time random walk that crosses each edge at rate $1$ and is killed on $B$.
Example: let $V = \set{a, x, b}$ with edges $\set{a, x}$ and $\set{x, b}$, and $B = \set{a, b}$.
The exponent is $-\frac12 (h(x)^2 + h(x)^2) = -h(x)^2$, so $h(x)$ is normal with mean $0$ and variance $1/2$, and indeed $-\Delta_U = (2)$ has inverse $1/2$.
Non-example: with $B$ empty, the exponent is unchanged when a constant is added to $h$, so no normalising constant $Z$ exists.
The continuum Gaussian free field on a domain $D \subseteq \R^d$ is the centred Gaussian random generalised function whose covariance is the Dirichlet Green function of $-\Delta$ on $D$.
It is not a function when $d \ge 2$.
