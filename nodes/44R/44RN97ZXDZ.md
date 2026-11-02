---
tag: 44RN97ZXDZ
kind: statement
role: lemma
name: Scheffé's lemma
msc: [28A20, 28A25, 60A10]
uses: [X7GTF3D98F, RARTMA0ZEC, S95TR54TCG]
about: [X7GTF3D98F]
sources:
  - url: https://en.wikipedia.org/wiki/Scheff%C3%A9%27s_lemma
same_as:
  wikidata: Q3229344
  wikipedia: Scheffé's lemma
---

## Statement

Let $(X, \Sigma, \mu)$ be a measure space.
Let $f_1, f_2, \dots$ and $f$ be real or complex [[integrable functions|X7GTF3D98F]] on $X$ with $f_n \to f$ [[almost everywhere|RARTMA0ZEC]].
Then
$$\lim_{n \to \infty} \int_X \abs{f_n - f} \, d\mu = 0 \quad \text{if and only if} \quad \lim_{n \to \infty} \int_X \abs{f_n} \, d\mu = \int_X \abs{f} \, d\mu.$$

## Remarks

Proof idea: the direct implication follows from $\abs{\int \abs{f_n} - \int \abs{f}} \le \int \abs{f_n - f}$.
For the converse, the functions $g_n = \abs{f_n} + \abs{f} - \abs{f_n - f}$ are non-negative and tend to $2\abs{f}$ almost everywhere.
[[Fatou's lemma|S95TR54TCG]] gives $2 \int \abs{f} \le 2 \int \abs{f} - \limsup_n \int \abs{f_n - f}$, and $\int \abs{f}$ is finite.

Example: let $p_n$ and $p$ be probability densities on $\R$ with $p_n \to p$ almost everywhere.
Then $\int p_n = \int p = 1$, so $\int \abs{p_n - p} \to 0$.
The distributions with densities $p_n$ then converge to the one with density $p$ in total variation.

The convergence of the norms is needed.
For $f_n = n \mathbf{1}_{(0, 1/n)}$ on $\R$, $f_n \to 0$ everywhere but $\int \abs{f_n - 0} = 1$.

## Explanations

### L1 human

Suppose functions converge at almost every point, and their total sizes converge to the total size of the limit.
Then the area between their graphs and the graph of the limit goes to zero.
No mass can escape, because the total mass is kept.

### L2 human

Scheffé's lemma is a quick criterion for convergence in $L^1$.
Its main use is in probability and statistics: pointwise convergence of densities implies convergence of the distributions in total variation, hence in distribution.
It is close in spirit to the Vitali convergence theorem, but it holds on any measure space and its proof is a direct application of Fatou's lemma.
