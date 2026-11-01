---
tag: TBMEJXAMZ0
kind: definition
name: Discriminant of a field extension
msc: [11R29, 12F10]
defines: 3BCYVS9E17
uses: [0NRYPM9Y27, 0VTQTPQGAV, 73XV4RP5PT, 0C3CFHDN6R, 0CCPN09EMJ]
sources:
  - url: https://en.wikipedia.org/wiki/Discriminant_of_an_algebraic_number_field
---

## Definition

Let $L/K$ be a [[finite extension|0NRYPM9Y27]] of degree $n$ and let $b_1, \ldots, b_n \in L$.
Let $\mathrm{Tr}_{L/K}$ be the [[field trace|73XV4RP5PT]].
The *discriminant* of the family $(b_1, \ldots, b_n)$ is
$$d_{L/K}(b_1, \ldots, b_n) = \det\left(\mathrm{Tr}_{L/K}(b_i b_j)\right)_{1 \le i, j \le n} \in K,$$
where $\det$ is the [[determinant|0C3CFHDN6R]].
The *discriminant of $L/K$* is the class of $d_{L/K}(b_1, \ldots, b_n)$ modulo $(K^\times)^2$, for any [[basis|0VTQTPQGAV]] $b_1, \ldots, b_n$ of $L$ over $K$.

## Remarks

If $c_1, \ldots, c_n$ is another basis and $c = Pb$ with $P \in GL_n(K)$, then $d(c) = \det(P)^2\, d(b)$, so the class modulo squares is well defined.
If $L/K$ is separable with embeddings $\sigma_1, \ldots, \sigma_n$ into an algebraic closure, then $d(b) = \det\left(\sigma_i(b_j)\right)^2$.
The discriminant of a basis is nonzero if and only if $L/K$ is separable.
If $L = K(\alpha)$ and $f$ is the minimal polynomial of $\alpha$, then $d(1, \alpha, \ldots, \alpha^{n-1})$ is the [[discriminant|0CCPN09EMJ]] of $f$.
For a number field $L$ over $\Q$, the discriminant of a $\Z$-basis of the ring of integers is an integer independent of the basis, the discriminant of the number field.

Example: $L = \Q(i)$, $K = \Q$, basis $1, i$.
Check: $\mathrm{Tr}(1) = 2$, $\mathrm{Tr}(i) = 0$ and $\mathrm{Tr}(i^2) = -2$, so $d(1, i) = \det\begin{pmatrix} 2 & 0 \\ 0 & -2 \end{pmatrix} = -4$, the discriminant of $x^2 + 1$.

Non-example: for $K = \F_p(t)$ and $L = K(s)$ with $s^p = t$, every trace is $0$, so the discriminant of every basis is $0$; the extension is not separable.
