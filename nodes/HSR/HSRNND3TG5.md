---
tag: HSRNND3TG5
kind: statement
role: theorem
name: Universal approximation theorem
msc: [41A30, 68T07, 41A63]
uses: [XAARVNKXF1, 0BSJSX7ME2, 0R6EWFKRCF, 0X3WGX95FE]
about: [XAARVNKXF1]
sources:
  - url: https://en.wikipedia.org/wiki/Universal_approximation_theorem
same_as:
  wikidata: Q7894110
  wikipedia: Universal approximation theorem
---

## Statement

Let $\sigma \colon \R \to \R$ be [[continuous|0X3WGX95FE]], and let $n \ge 1$.
Let $\mathcal{N}_\sigma$ be the set of all functions $g \colon \R^n \to \R$ of the form
$$g(x) = \sum_{i=1}^{N} c_i \, \sigma(w_i \cdot x + b_i).$$
Here $N \ge 1$, $c_i, b_i \in \R$ and $w_i \in \R^n$.
These are the functions computed by a neural network with one hidden layer and activation $\sigma$.
Then the following are equivalent.

1. For every [[compact set|0R6EWFKRCF]] $K \subseteq \R^n$, the restrictions of the functions in $\mathcal{N}_\sigma$ to $K$ are [[dense|0BSJSX7ME2]] in $C(K)$ with the supremum norm.
2. $\sigma$ is not a polynomial.

## Remarks

The idea of the proof: if $\sigma$ is a polynomial of degree $d$, every $g \in \mathcal{N}_\sigma$ is a polynomial of degree at most $d$.
These polynomials do not form a dense set.
Conversely, by smoothing one may assume $\sigma$ is smooth; then difference quotients in the weight show that $t \mapsto t^k \sigma^{(k)}(w t + b)$ is a limit of elements of $\mathcal{N}_\sigma$ in one variable.
Since $\sigma$ is not a polynomial, for each $k$ there is a $b$ with $\sigma^{(k)}(b) \ne 0$, so all monomials $t^k$ are limits, and the Weierstrass theorem applies in one variable.
The case of $n$ variables reduces to one variable because the ridge functions $h(w \cdot x)$ span a dense set in $C(K)$.

Example: the logistic sigmoid $\sigma(t) = 1 / (1 + e^{-t})$ and the rectifier $\sigma(t) = \max(0, t)$ are not polynomials.
So networks with one hidden layer and either activation give [[uniform approximations|XAARVNKXF1]] of every continuous function on every compact set.

The theorem says nothing about how large $N$ must be for a given accuracy, and it does not say how to find the weights.
The sigmoid case was proved by George Cybenko in 1989, and the characterization for continuous $\sigma$ by Moshe Leshno, Vladimir Lin, Allan Pinkus and Shimon Schocken in 1993.

## Explanations

### L1 human

A neural network with one hidden layer adds up many copies of one fixed function $\sigma$, each stretched, shifted and pointed in some direction.
The theorem says that such sums can imitate any continuous function on a bounded closed region as closely as you want.
The only condition on $\sigma$ is that it is not a polynomial.

### L2 human

This is a density theorem in the same family as the Weierstrass and Stone–Weierstrass theorems, with ridge functions $\sigma(w \cdot x + b)$ as building blocks.
It justifies neural networks as a flexible class of approximants but gives no rates.
Rates depend on the smoothness of the target and on the dimension, as in classical approximation theory.
Related results treat deep networks of bounded width and approximation in $L^p$ norms.
