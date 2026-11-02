---
tag: FXSY9SXHFZ
kind: definition
name: Discrete wavelet transform
msc: [42C40, 65T60, 94A12]
defines: P3H4MMC4ZH
uses: [YH4BERB952, 1GHQMBR7DE, 4PZ35C0GV3]
sources:
  - url: https://en.wikipedia.org/wiki/Discrete_wavelet_transform
---

## Definition

Let $\varphi$ be the scaling function of a [[multiresolution analysis|1GHQMBR7DE]] of $L^2(\R)$, with [[refinement equation|YH4BERB952]] $\varphi(x) = \sqrt2 \sum_k h_k \varphi(2x - k)$.
Put $g_k = (-1)^k \overline{h_{1-k}}$ for $k \in \Z$.
For a sequence $a = (a_n)_{n \in \Z} \in \ell^2(\Z)$, one *level* of the discrete wavelet transform gives the two sequences
$$c_k = \sum_{n \in \Z} \overline{h_{n - 2k}} \, a_n, \qquad d_k = \sum_{n \in \Z} \overline{g_{n - 2k}} \, a_n, \qquad k \in \Z.$$
The *discrete wavelet transform* with $J \ge 1$ levels applies one level to $a$, then to the resulting $c$, and so on $J$ times.
Its output is the detail sequences of all levels together with the last coarse sequence.

## Remarks

The map $a \mapsto (c, d)$ is a unitary operator from $\ell^2(\Z)$ onto $\ell^2(\Z) \oplus \ell^2(\Z)$, so the transform is inverted by its adjoint.
If $a_n = \ip{f}{\varphi_{j+1, n}}$ for $f \in L^2(\R)$, where $\varphi_{j,k}(x) = 2^{j/2} \varphi(2^j x - k)$, then $c_k = \ip{f}{\varphi_{j,k}}$ and $d_k = \ip{f}{\psi_{j,k}}$ for the associated orthonormal [[wavelet|4PZ35C0GV3]] $\psi$.
The same name is used for the coefficient family $(\ip{f}{\psi_{j,k}})_{j,k}$ of a function, and for finite signals with periodic or other boundary rules.

Example: for the Haar filter $h_0 = h_1 = 1/\sqrt2$ one gets $g_0 = 1/\sqrt2$ and $g_1 = -1/\sqrt2$.
Then $c_k = (a_{2k} + a_{2k+1})/\sqrt2$ and $d_k = (a_{2k} - a_{2k+1})/\sqrt2$.
For $a = (4, 2, 5, 5)$ (and zeros elsewhere) one level gives $c = (6/\sqrt2, 10/\sqrt2)$ and $d = (2/\sqrt2, 0)$.
Energy is preserved: $16 + 4 + 25 + 25 = 70 = 18 + 50 + 2 + 0$.

Non-example: the pairwise means $(a_{2k} + a_{2k+1})/2$ alone discard information, since $(1, 0)$ and $(0, 1)$ have the same mean; the transform keeps the details $d_k$ as well.
