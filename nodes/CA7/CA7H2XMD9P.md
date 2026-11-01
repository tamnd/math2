---
tag: CA7H2XMD9P
kind: definition
name: Arithmetic group
msc: [20G30, 11F06, "22E40"]
defines: 4XWG6S7R4Z
uses: [0FCHE902D7, 0V9PMN0RBH, 0DTXBQPA2S, 0X1JXT47GA, 1H6R856P3C]
sources:
  - url: https://en.wikipedia.org/wiki/Arithmetic_group
---

## Definition

Let $G$ be a linear algebraic group defined over $\Q$, together with a faithful representation $G \hookrightarrow \mathrm{GL}_n$ defined over $\Q$.
Let $G(\Z) = G(\Q) \cap \mathrm{GL}_n(\Z)$.
A [[subgroup|0X1JXT47GA]] $\Gamma$ of $G(\Q)$ is an *arithmetic subgroup* of $G$ if it is commensurable with $G(\Z)$.
This means that $\Gamma \cap G(\Z)$ has finite [[index|0DTXBQPA2S]] both in $\Gamma$ and in $G(\Z)$.
An *arithmetic group* is a group that is an arithmetic subgroup of some such $G$.

## Remarks

The class of arithmetic subgroups does not depend on the choice of the faithful representation.

Example: the [[special linear group|0V9PMN0RBH]] $\mathrm{SL}_n$ in its standard representation has $G(\Z) = \mathrm{SL}_n(\Z)$, which is arithmetic.
For an integer $N \ge 1$, the [[congruence subgroup|1H6R856P3C]] $\Gamma(N)$, the kernel of reduction modulo $N$ from $\mathrm{SL}_n(\Z)$ to $\mathrm{SL}_n(\Z/N\Z)$, is arithmetic too.
Indeed, $\Gamma(N) \cap \mathrm{SL}_n(\Z) = \Gamma(N)$, and its index in $\mathrm{SL}_n(\Z)$ is at most the order of the finite group $\mathrm{SL}_n(\Z/N\Z)$.

Non-example: $\Gamma = \mathrm{SL}_2(\Z[1/2])$ inside $\mathrm{SL}_2(\Q)$.
Here $\Gamma \cap \mathrm{SL}_2(\Z) = \mathrm{SL}_2(\Z)$.
The matrices $d_k = \mathrm{diag}(2^k, 2^{-k})$, $k \ge 0$, lie in $\Gamma$, and $d_k^{-1} d_m \notin \mathrm{SL}_2(\Z)$ for $k \ne m$.
So $\mathrm{SL}_2(\Z)$ has infinite index in $\Gamma$, and $\Gamma$ is not arithmetic in $\mathrm{SL}_2$.

Over a number field $K$ with ring of integers $\mathcal{O}_K$, one uses $G(\mathcal{O}_K)$ in place of $G(\Z)$; restriction of scalars reduces this case to the one over $\Q$.
