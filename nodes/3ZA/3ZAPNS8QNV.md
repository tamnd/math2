---
tag: 3ZAPNS8QNV
kind: conjecture
name: Zagier's conjecture on polylogarithms
msc: ["11G55", "11R42", "19F27"]
uses: [96CHDZKGQ0, 0KC00K7KY4, KXS5DQDFYD, MWBDFS2KJ5, E0VZTNPJXA]
about: [96CHDZKGQ0, KXS5DQDFYD]
sources:
  - url: https://en.wikipedia.org/wiki/Polylogarithm
history:
  posed_by: Don Zagier
  first_stated: "1991"
---

## Statement

Let $F$ be an [[algebraic number field|MWBDFS2KJ5]] with $r_1$ real embeddings, $r_2$ pairs of complex conjugate non-real embeddings and discriminant $d_F$, and let $m \ge 2$.
Let $d_m = r_1 + r_2$ if $m$ is odd and $d_m = r_2$ if $m$ is even.
Let $\sigma_1, \ldots, \sigma_{d_m}$ be the embeddings $F \to \C$ consisting of one from each complex pair, together with the real embeddings when $m$ is odd.
Let $\operatorname{Li}_k$ be the [[polylogarithm|96CHDZKGQ0]] of order $k$.
Zagier's single-valued polylogarithm $L_m \colon \C \to \R$ is
$$L_m(z) = \Re_m \Big( \sum_{k=0}^{m-1} \frac{2^k B_k}{k!} (\log \abs{z})^k \operatorname{Li}_{m-k}(z) \Big) \quad (\abs{z} \le 1).$$
It extends to a continuous function on $\C$ with $L_m(1/z) = (-1)^{m-1} L_m(z)$ for $z \ne 0$.
Here $\Re_m$ is the real part for $m$ odd and the imaginary part for $m$ even.
The $B_k$ are the [[Bernoulli numbers|0KC00K7KY4]], with $B_1 = -1/2$.
Extend $L_m$ additively to the free abelian group $\Z[F]$ on the elements of $F$.
Then there are $\xi_1, \ldots, \xi_{d_m} \in \Z[F]$ and $q \in \Q^\times$ with
$$\zeta_F(m) = q \, \frac{\pi^{e}}{\sqrt{\abs{d_F}}} \det\big(L_m(\sigma_j(\xi_i))\big)_{1 \le i, j \le d_m},$$
where $e = m r_2$ for $m$ odd and $e = m(r_1 + r_2)$ for $m$ even, and $\zeta_F$ is the [[Dedekind zeta function|KXS5DQDFYD]].

## Remarks

Zagier's conjecture is sharper than this existence statement.
He defined subgroups $\mathcal{B}_m(F)$ of $\Z[F]$ by conditions that generalise the [[Bloch group|EC11MFYFYM]], and conjectured that the $\xi_i$ can be taken in $\mathcal{B}_m(F)$.
He also conjectured that $L_m$ on these groups computes the [[Borel regulator|D22EZ3CNAF]] on $K_{2m-1}(F)$.

For $m = 2$, $L_2$ is the Bloch–Wigner function, and the conjecture follows from Borel's theorem and the work of Bloch and Suslin; see [[dilogarithm and K3|M1C142YAPZ]].
Goncharov proved the case $m = 3$.
For $F = \Q$ and $m$ odd, $L_m(1) = \zeta(m)$, so the formula holds with $\xi_1 = [1]$, $q = 1$ and $e = 0$.

## Explanations

### L1 human

Values of the Riemann zeta function at odd integers, such as $\zeta(3)$, are mysterious numbers.
Zagier predicted that the analogous values for any number field are determinants built from a single family of special functions, the polylogarithms, evaluated at numbers in the field.
For the dilogarithm this is a theorem, and it connects to the volumes of hyperbolic manifolds.
For higher polylogarithms it is known only in a few cases.
