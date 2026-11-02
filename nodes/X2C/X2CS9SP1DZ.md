---
tag: X2CS9SP1DZ
kind: definition
name: Information-based complexity
msc: [65Y20, 68Q25, 65J05]
defines: Q1QK49TTEJ
uses: [03J5RAKB30, 07YQ1C78G0]
sources:
  - url: https://en.wikipedia.org/wiki/Information-based_complexity
---

## Definition

Let $F$ be a set, let $G$ be a [[normed vector space|03J5RAKB30]], and let $S \colon F \to G$ be a map, the *solution operator*.
Let $\Lambda$ be a set of maps $F \to \R$, the *admissible information functionals*, for example the evaluations $f \mapsto f(t)$.
For $n \ge 0$, an *algorithm using $n$ pieces of information* is a map $A = \phi \circ N$ where:

1. $N(f) = \big(L_1(f), \ldots, L_n(f)\big)$, with $L_1 \in \Lambda$ and each $L_k \in \Lambda$ chosen as a function of the values $L_1(f), \ldots, L_{k-1}(f)$;
2. $\phi$ is any map from the set of possible values of $N$ to $G$.

The *worst-case error* of $A$ is $e(A) = \sup_{f \in F} \norm{S(f) - A(f)}$.
The *$n$-th minimal error* is $e(n) = \inf_A e(A)$ over all algorithms $A$ using $n$ pieces of information.
For $\varepsilon > 0$, the *information complexity* of the problem is
$$n(\varepsilon) = \min \set{n \ge 0 : e(n) \le \varepsilon},$$
with $n(\varepsilon) = \infty$ if no such $n$ exists.
*Information-based complexity* is the study of $e(n)$ and $n(\varepsilon)$, and of the total cost $\mathrm{comp}(\varepsilon)$ that also counts the arithmetic operations of $\phi$.

## Remarks

Example: let $F$ be the set of functions $f \colon [0,1] \to \R$ with $\abs{f(s) - f(t)} \le \abs{s - t}$, let $S(f) = \int_0^1 f(t) \, dt \in \R$, and let $\Lambda$ be the function evaluations.
The midpoint rule $A(f) = \frac{1}{n} \sum_{k=1}^{n} f\big(\frac{2k-1}{2n}\big)$ has $e(A) = \frac{1}{4n}$, since on each subinterval of length $1/n$ the error is at most $\int \abs{t - c} \, dt = \frac{1}{4n^2}$, where $c$ is its midpoint.
No algorithm does better, so $e(n) = \frac{1}{4n}$ and $n(\varepsilon) = \ceil{1/(4\varepsilon)}$.
Non-example: the map $A(f) = \int_0^1 f$ itself has error $0$, but it uses infinitely many pieces of information.
Indeed two functions in $F$ that agree at finitely many points can have different integrals.
Besides the worst-case setting, there are average-case, probabilistic and randomized settings, where the supremum over $F$ is replaced by an expectation or the algorithm may use random choices.
Often $\Lambda$ is the class of all continuous [[linear functionals|07YQ1C78G0]] on a normed space containing $F$.
A problem is called *polynomially tractable* when $n(\varepsilon)$ for the $d$-variate version grows at most polynomially in $d$ and $1/\varepsilon$.
