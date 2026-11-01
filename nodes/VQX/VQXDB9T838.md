---
tag: VQXDB9T838
kind: statement
role: theorem
name: Kolmogorov–Arnold representation theorem
msc: [26B40]
uses: [0X3WGX95FE]
about: [0X3WGX95FE]
sources:
  - url: https://en.wikipedia.org/wiki/Kolmogorov%E2%80%93Arnold_representation_theorem
same_as:
  wikidata: Q25099402
  wikipedia: Kolmogorov–Arnold representation theorem
---

## Statement

Let $n \ge 2$.
There are [[continuous functions|0X3WGX95FE]] $\varphi_{q,p} \colon [0, 1] \to \R$, for $0 \le q \le 2n$ and $1 \le p \le n$, with the following property.
For every continuous function $f \colon [0, 1]^n \to \R$ there are continuous functions $\Phi_q \colon \R \to \R$, for $0 \le q \le 2n$, such that
$$f(x_1, \dots, x_n) = \sum_{q=0}^{2n} \Phi_q\left( \sum_{p=1}^{n} \varphi_{q,p}(x_p) \right) \quad \text{for all } (x_1, \dots, x_n) \in [0, 1]^n.$$

## Remarks

The inner functions $\varphi_{q,p}$ do not depend on $f$; only the outer functions $\Phi_q$ do.
The inner functions can be chosen increasing.
So the only genuine function of several variables needed to build every continuous function of $n$ variables is addition.
Example: for $f(x, y) = xy$ on $[0, 1]^2$ there is an explicit formula of the same kind, $xy = \frac{1}{4}\left((x + y)^2 - (x - y)^2\right)$, with fewer terms than the theorem uses.
In Hilbert's thirteenth problem, Hilbert conjectured that some continuous functions of three variables are not superpositions of continuous functions of two variables.
The theorem refutes this conjecture: every continuous function of several variables is a superposition of continuous functions of one variable and addition.

## Explanations

### L1 human

Any continuous function of many variables can be built from functions of one variable and the operation of adding numbers.
First apply fixed one-variable functions to each coordinate and add the results; then apply one more one-variable function and add again.
The fixed inner functions work for every target function at once.

### L2 human

The theorem belongs to the study of superpositions of functions.
It contrasts with results of Vitushkin for smooth functions: superpositions of $C^k$ functions of fewer variables do not give every $C^k$ function of $n$ variables.
The inner functions are continuous but quite irregular, so the representation is not a practical way to compute $f$, though it has inspired work on approximation by networks.
