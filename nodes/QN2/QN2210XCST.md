---
tag: QN2210XCST
kind: statement
role: theorem
name: Moore–Osgood theorem
msc: [40B05, 40A30]
uses: [4FK55CYMVZ, 08FPABDQ4C, 08EWT7J0SC]
about: [QYTGCW1GTK]
sources:
  - url: https://en.wikipedia.org/wiki/Iterated_limit
---

## Statement

Let $(X, d)$ be a [[complete metric space|08EWT7J0SC]], for example $\R$ or $\C$, and let $(a_{m,n})_{m, n \ge 1}$ be a double sequence in $X$.
Assume:

1. for each $m$, the limit $b_m = \lim_{n \to \infty} a_{m,n}$ exists;
2. there is a sequence $(c_n)$ such that $a_{m,n} \to c_n$ as $m \to \infty$, [[uniformly|08FPABDQ4C]] in $n$, that is, $\sup_n d(a_{m,n}, c_n) \to 0$.

Then the limits $\lim_{m \to \infty} b_m$ and $\lim_{n \to \infty} c_n$ exist, the [[Pringsheim double limit|4FK55CYMVZ]] $\lim_{m,n \to \infty} a_{m,n}$ exists, and all three are equal.

## Remarks

Proof idea: uniform convergence gives an $M$ such that $d(a_{m,n}, a_{m',n}) < 2\varepsilon$ for all $n$ when $m, m' \ge M$.
Letting $n \to \infty$ gives $d(b_m, b_{m'}) \le 2\varepsilon$, so $(b_m)$ is a Cauchy sequence and has a limit $L$ by completeness.
The triangle inequality $d(c_n, L) \le d(c_n, a_{M,n}) + d(a_{M,n}, b_M) + d(b_M, L)$ then shows $c_n \to L$, and the same splitting gives the double limit.
Example: for $a_{m,n} = \frac{1}{m} + \frac{1}{n}$ the convergence in $m$ is uniform, and all limits equal $0$.
Without uniformity the conclusion fails: $a_{m,n} = \frac{m}{m+n}$ gives $\lim_m \lim_n a_{m,n} = 0$ but $\lim_n \lim_m a_{m,n} = 1$.
Without completeness it also fails: in $\mathbb{Q}$, take rationals $x_k \to \sqrt{2}$ and $a_{m,n} = x_{\min(m,n)}$; both hypotheses hold, but $b_m = x_m$ has no limit in $\mathbb{Q}$.

## Explanations

### L1 human

Two limits taken one after the other may give different answers, depending on the order.
The theorem says that if one of the inner limits is reached uniformly, the order does not matter, and the double limit exists too.

### L2 human

This is the abstract principle behind many interchange results in analysis.
The theorem that a uniform limit of continuous functions is continuous, and the theorem that uniform limits commute with integration, follow the same pattern.
For [[double series|PAXCH4FFSV]], it gives conditions under which summing by rows, by columns, or over squares gives the same value.
