---
tag: VRQRRSBDPG
kind: definition
name: Askey scheme
msc: [33C45]
defines: RR2S05C09B
uses: [1CPF7SWQ3S, P6JYNDX5DR, Y1M82VZYS2, TRD7DSF2KR, CEC3DESCFT, CJGKW80KBR, WAMRHWW82R, M5NXATQ48S, 6KH8KVYS3R, MGACY98E9H]
sources:
  - url: https://en.wikipedia.org/wiki/Askey_scheme
---

## Definition

The *Askey scheme* is a directed graph whose vertices are families of hypergeometric orthogonal polynomials.
The vertices are grouped in levels by the type of hypergeometric series that defines them:

1. ${}_4F_3$: the [[Wilson|1CPF7SWQ3S]] and [[Racah polynomials|P6JYNDX5DR]].
2. ${}_3F_2$: the continuous dual Hahn, continuous Hahn, [[Hahn|Y1M82VZYS2]] and dual Hahn polynomials.
3. ${}_2F_1$: the Meixner–Pollaczek, [[Jacobi|TRD7DSF2KR]], [[Meixner|CEC3DESCFT]] and [[Krawtchouk polynomials|CJGKW80KBR]].
4. ${}_1F_1$ and ${}_2F_0$: the [[Laguerre|WAMRHWW82R]], [[Bessel|M5NXATQ48S]] and [[Charlier polynomials|6KH8KVYS3R]].
5. ${}_2F_0$: the [[Hermite polynomials|MGACY98E9H]].

There is an arrow from a family $A$ to a family $B$ when the polynomials of $B$ are limits of rescaled polynomials of $A$.
In such a limit, parameters of $A$ tend to special values or to infinity.

## Remarks

Example of an arrow, Jacobi to Laguerre: $\lim_{\beta \to \infty} P_n^{(\alpha, \beta)}\left( 1 - \frac{2x}{\beta} \right) = L_n^{(\alpha)}(x)$.
Check for $n = 1$: $P_1^{(\alpha, \beta)}(1 - 2x/\beta) = (\alpha + 1) - (\alpha + \beta + 2) \frac{x}{\beta} \to \alpha + 1 - x = L_1^{(\alpha)}(x)$.
Example of an arrow, Krawtchouk to Charlier: $\lim_{N \to \infty} K_n\left( x; \frac{a}{N}, N \right) = C_n(x; a)$; for $n = 1$ both sides equal $1 - \frac{x}{a}$.
Special cases inside a vertex, such as the Gegenbauer, Legendre and Chebyshev polynomials inside the Jacobi family, are usually not drawn as separate vertices.
Non-example: the Bernoulli polynomials are not in the scheme, because they are not orthogonal for any positive measure on $\R$.
Among Appell sequences, only the Hermite polynomials, up to rescaling and shifting the variable, are orthogonal.
The $q$-analogue of the scheme, with the [[Askey–Wilson polynomials|RSNZNG0WA1]] at the top, is called the $q$-Askey scheme.
