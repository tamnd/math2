---
tag: R3AR5JK8WW
kind: definition
name: Dedekind zeta function
msc: [11R42]
defines: KXS5DQDFYD
uses: [MWBDFS2KJ5, M54ADM0CVF, 096Z9MP2ME, 1XWBY4N0VT, 9D2Z543EJQ, 55XX5A7XZV, 0M3YQJ81NB, E0VZTNPJXA, RWK0HNF1NA, KTKK9B1X41]
sources:
  - url: https://en.wikipedia.org/wiki/Dedekind_zeta_function
    locator: Definition and basic properties
---

## Definition

Let $K$ be an [[algebraic number field|MWBDFS2KJ5]] with ring of integers $\mathcal{O}_K$.
For a nonzero [[ideal|096Z9MP2ME]] $\mathfrak{a}$ of $\mathcal{O}_K$, let $N(\mathfrak{a}) = \abs{\mathcal{O}_K/\mathfrak{a}}$ be its [[norm|M54ADM0CVF]].
Let $s$ be a complex variable with $\operatorname{Re} s > 1$.
The *Dedekind zeta function* of $K$ is
$$\zeta_K(s) = \sum_{\mathfrak{a}} \frac{1}{N(\mathfrak{a})^{s}},$$
where $\mathfrak{a}$ runs over the nonzero ideals of $\mathcal{O}_K$.

## Remarks

The series converges absolutely for $\operatorname{Re} s > 1$.
Unique factorisation of ideals gives the Euler product $\zeta_K(s) = \prod_{\mathfrak{p}} \big(1 - N(\mathfrak{p})^{-s}\big)^{-1}$ over the nonzero prime ideals $\mathfrak{p}$.
The function has an [[analytic continuation|0M3YQJ81NB]] to a meromorphic function on $\C$ whose only pole is a simple pole at $s = 1$.
Let $K$ have $r_1$ real embeddings, $r_2$ pairs of complex embeddings, and $w_K$ roots of unity.
Let $h_K$ be its [[class number|KTKK9B1X41]], $R_K$ its [[regulator|RWK0HNF1NA]] and $d_K$ its [[discriminant|E0VZTNPJXA]].
The residue is
$$\operatorname{Res}_{s = 1} \zeta_K(s) = \frac{2^{r_1} (2\pi)^{r_2} h_K R_K}{w_K \sqrt{\abs{d_K}}},$$
the [[class number formula|55XX5A7XZV]].

Example: for $K = \Q$ every nonzero ideal is $n\Z$ for a unique $n \ge 1$, with norm $n$, so $\zeta_{\Q}$ is the [[Riemann zeta function|1XWBY4N0VT]].
For $K = \Q(i)$, comparing Euler factors prime by prime gives $\zeta_K(s) = \zeta(s) L(s, \chi_4)$, where $L(s, \chi_4)$ is the [[Dirichlet L-function|9D2Z543EJQ]] of the non-trivial character modulo $4$.

Non-example: the sum $\sum_{\alpha} \abs{N_{K/\Q}(\alpha)}^{-s}$ over nonzero elements $\alpha \in \mathcal{O}_K$ is not $\zeta_K(s)$.
It counts each principal ideal once for each unit, so for $K = \Q(\sqrt{2})$, which has infinitely many units, it diverges for every $s$.
