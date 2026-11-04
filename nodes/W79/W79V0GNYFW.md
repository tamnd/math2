---
tag: W79V0GNYFW
kind: statement
role: proposition
name: Ramanujan's identity
sources:
  - wikipedia: en:2233526@r1333830348
    locator: Basic hypergeometric series, section Ramanujan's identity
    note: adopted
    mention: wikipedia://en/2233526#IPCG
    sections: [Statement]
inventory: [QX18142J2A]
---

## Statement

Srinivasa Ramanujan gave the identity

$$\;_1\psi_1 \left[\begin{matrix} a \\ b \end{matrix} ; q,z \right] = \sum_{n=-\infty}^\infty \frac {(a;q)_n} {(b;q)_n} z^n = \frac {(b/a,q,q/az,az;q)_\infty } {(b,b/az,q/a,z;q)_\infty}$$

valid for |*q*| \< 1 and |*b*/*a*| \< |*z*| \< 1. Similar identities for $\;_6\psi_6$ have been given by Bailey. Such identities can be understood to be generalizations of the Jacobi triple product theorem, which can be written using q-series as

$$\sum_{n=-\infty}^\infty q^{n(n+1)/2}z^n = (q;q)_\infty \; (-1/z;q)_\infty \; (-zq;q)_\infty.$$

Gwynneth Coogan and Ken Ono give a related [[formal power series|033WGN00BF]]

$$A(z;q) \stackrel{\rm{def}}{=} \frac{1}{1+z} \sum_{n=0}^\infty \frac{(z;q)_n}{(-zq;q)_n}z^n = \sum_{n=0}^\infty (-1)^n z^{2n} q^{n^2}.$$
