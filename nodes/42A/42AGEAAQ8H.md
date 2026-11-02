---
tag: 42AGEAAQ8H
kind: definition
name: Neural network approximation
msc: [41A46, 68T07, 41A30]
defines: W7CK84MZFV
uses: [0X3WGX95FE, 0TVJZYB6SH, 03J5RAKB30]
sources:
  - url: https://en.wikipedia.org/wiki/Universal_approximation_theorem
---

## Definition

Let $\sigma \colon \R \to \R$ be a function, called the *activation function*, and let $d, n \ge 1$ be integers.
A *shallow neural network* with $n$ neurons is a function $\R^d \to \R$ of the form
$$x \mapsto \sum_{k=1}^{n} c_k \, \sigma(w_k \cdot x + b_k), \qquad c_k, b_k \in \R, \ w_k \in \R^d .$$
Let $\Sigma_n(\sigma)$ be the set of these functions.
Let $K \subseteq \R^d$ be a [[compact set|0TVJZYB6SH]] and let $f \colon K \to \R$ be [[continuous|0X3WGX95FE]].
*Neural network approximation* of $f$ is its approximation by elements of $\Sigma_n(\sigma)$, measured by the error
$$E_n(f) = \inf\set{\sup_{x \in K} \abs{f(x) - g(x)} : g \in \Sigma_n(\sigma)} .$$

## Remarks

Other [[norms|03J5RAKB30]], such as $L^p$ norms on $K$, are also used.
A *deep* network with $L$ layers is a composition $T_L \circ \sigma \circ T_{L-1} \circ \cdots \circ \sigma \circ T_1$ of affine maps $T_j \colon \R^{d_{j-1}} \to \R^{d_j}$, with $d_0 = d$ and $d_L = 1$, where $\sigma$ acts on each coordinate; the shallow case is $L = 2$.
The set $\Sigma_n(\sigma)$ is in general not a linear space, since the sum of two networks with $n$ neurons may need $2n$ neurons.
For continuous $\sigma$, $E_n(f) \to 0$ as $n \to \infty$ for all $K$ and $f$ if and only if $\sigma$ is not a polynomial.
Example: for the ReLU $\sigma(t) = \max(t, 0)$, $d = 1$, $K = [-1, 1]$ and $f(x) = \abs{x}$, one has $f = \sigma(x) + \sigma(-x) \in \Sigma_2(\sigma)$, so $E_2(f) = 0$.
Non-example: for $\sigma(t) = t$, every element of $\Sigma_n(\sigma)$ is an affine function, so on $K = [-1, 1]$ the function $x^2$ has $E_n(x^2) = 1/2$ for every $n$ and is not approximated.
