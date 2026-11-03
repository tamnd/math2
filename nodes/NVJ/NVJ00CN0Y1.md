---
tag: NVJ00CN0Y1
kind: definition
name: Chern character
msc: ["19L10", "57R20", "14C17"]
defines: 6XRTXBPASW
uses: [P4DZM975BV, PAD37GKDPD, 6N7BC70CX0, 0ZNXZB4HNB]
sources:
  - url: https://en.wikipedia.org/wiki/Chern_class
    locator: Chern character
---

## Definition

Let $X$ be a paracompact space and let $E$ be a complex [[vector bundle|P4DZM975BV]] of rank $r$ on $X$.
Let $c_i = c_i(E) \in H^{2i}(X; \Q)$ be its [[Chern classes|PAD37GKDPD]] in rational [[singular cohomology|6N7BC70CX0]].
For $k \ge 1$ let $s_k$ be the polynomial with $s_k(e_1, \ldots, e_k) = x_1^k + \cdots + x_N^k$ for $N \ge k$.
Here $e_i$ are the elementary symmetric polynomials in $x_1, \ldots, x_N$, so $s_k$ expresses [[power sums|0ZNXZB4HNB]] through them.
The *Chern character* of $E$ is
$$\operatorname{ch}(E) = r + \sum_{k \ge 1} \frac{s_k(c_1, \ldots, c_k)}{k!} \in \prod_{k \ge 0} H^{2k}(X; \Q).$$

## Remarks

Formally, if $x_1, \ldots, x_r$ are the Chern roots of $E$, then $\operatorname{ch}(E) = e^{x_1} + \cdots + e^{x_r}$.
The first terms are $\operatorname{ch}(E) = r + c_1 + \tfrac{1}{2}(c_1^2 - 2c_2) + \tfrac{1}{6}(c_1^3 - 3c_1c_2 + 3c_3) + \cdots$.
It satisfies $\operatorname{ch}(E \oplus F) = \operatorname{ch}(E) + \operatorname{ch}(F)$ and $\operatorname{ch}(E \otimes F) = \operatorname{ch}(E) \operatorname{ch}(F)$, so it gives a ring homomorphism from topological K-theory $K^0(X)$ to rational cohomology.

Example: on $\mathbb{CP}^1$ let $h \in H^2(\mathbb{CP}^1; \Q)$ be the positive generator, so $h^2 = 0$.
The line bundle $\mathcal{O}(n)$ has $c_1 = nh$, so $\operatorname{ch}(\mathcal{O}(n)) = e^{nh} = 1 + nh$.

Non-example: the total Chern class $c(E) = 1 + c_1 + \cdots + c_r$ is not additive: $c(E \oplus F) = c(E) c(F)$.
So $c$ does not give a homomorphism of additive groups from K-theory, while $\operatorname{ch}$ does.

In algebraic geometry the same formula, with Chern classes in the rational Chow ring $\operatorname{CH}^*(X) \otimes \Q$ of a smooth variety, defines $\operatorname{ch} \colon K_0(X) \to \operatorname{CH}^*(X) \otimes \Q$.
