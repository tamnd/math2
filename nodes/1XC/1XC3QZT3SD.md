---
tag: 1XC3QZT3SD
kind: definition
name: Koszul complex
msc: [13D02, 13D07]
defines: YZY11W08SD
uses: [0310REJJY8, 0MDMZ965VE, 0DZ9DKAKZR, 0NZ8JA25WK, F0HQXQ0HCD]
sources:
  - url: https://en.wikipedia.org/wiki/Koszul_complex
---

## Definition

Let $R$ be a [[commutative ring|0310REJJY8]] and let $x = (x_1, \ldots, x_n)$ be a sequence of elements of $R$.
Let $e_1, \ldots, e_n$ be the standard basis of the [[free module|0DZ9DKAKZR]] $R^n$.
For $0 \le p \le n$, let $K_p = \Lambda^p R^n$ be its $p$-th [[exterior power|0MDMZ965VE]].
It is free with basis the elements $e_{i_1} \wedge \cdots \wedge e_{i_p}$ for $i_1 < \cdots < i_p$.
The *Koszul complex* $K_\bullet(x)$ is
$$0 \to K_n \xrightarrow{d_n} K_{n-1} \to \cdots \to K_1 \xrightarrow{d_1} K_0 \to 0,$$
with
$$d_p(e_{i_1} \wedge \cdots \wedge e_{i_p}) = \sum_{j=1}^{p} (-1)^{j+1} x_{i_j}\, e_{i_1} \wedge \cdots \wedge \widehat{e_{i_j}} \wedge \cdots \wedge e_{i_p},$$
where the hat marks an omitted factor.
For an [[$R$-module|0NZ8JA25WK]] $M$, the Koszul complex of $x$ on $M$ is $K_\bullet(x; M) = K_\bullet(x) \otimes_R M$.

## Remarks

One checks that $d_{p-1} \circ d_p = 0$, so $K_\bullet(x)$ is a complex, and $H_0(K_\bullet(x)) = R/(x_1, \ldots, x_n)$.
If $x_1, \ldots, x_n$ is a [[regular sequence|69R5R2FCS5]], then $H_p(K_\bullet(x)) = 0$ for $p > 0$, so the complex is a free resolution of $R/(x_1, \ldots, x_n)$.
Example: for $n = 2$, the complex is $0 \to R \to R^2 \to R \to 0$ with $e_1 \wedge e_2 \mapsto x_1 e_2 - x_2 e_1$ and $e_i \mapsto x_i$; the composite sends $e_1 \wedge e_2$ to $x_1 x_2 - x_2 x_1 = 0$.
Non-example of exactness: for $R = K[t]$ and $x = (t, t)$, which is not a regular sequence, $H_1$ is the set of $(a, -a)$ modulo the multiples of $(-t, t)$, which is isomorphic to $R/(t) \ne 0$.
