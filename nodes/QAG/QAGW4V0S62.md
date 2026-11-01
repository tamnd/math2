---
tag: QAGW4V0S62
kind: definition
name: Tor functor
msc: [13D07, 18G15]
defines: DDQRERAQCV
uses: [0310REJJY8, 0NZ8JA25WK, HK2AA1YSQ2, F0HQXQ0HCD]
sources:
  - url: https://en.wikipedia.org/wiki/Tor_functor
---

## Definition

Let $R$ be a [[commutative ring|0310REJJY8]] and let $M$ and $N$ be [[$R$-modules|0NZ8JA25WK]].
Choose a [[projective resolution|HK2AA1YSQ2]] $\cdots \to P_1 \xrightarrow{d_1} P_0 \to M \to 0$ of $M$.
[[Tensoring|F0HQXQ0HCD]] the complex $P_\bullet$ with $N$ gives a chain complex
$$\cdots \to P_2 \otimes_R N \xrightarrow{d_2 \otimes \id_N} P_1 \otimes_R N \xrightarrow{d_1 \otimes \id_N} P_0 \otimes_R N \to 0.$$
For $n \ge 0$, the $n$-th *Tor module* is its homology
$$\operatorname{Tor}_n^R(M, N) = \ker(d_n \otimes \id_N) / \im(d_{n+1} \otimes \id_N),$$
with $d_0 \otimes \id_N = 0$.

## Remarks

Up to a canonical isomorphism, $\operatorname{Tor}_n^R(M, N)$ does not depend on the resolution, and resolving $N$ instead of $M$ gives the same modules.
One has $\operatorname{Tor}_0^R(M, N) \cong M \otimes_R N$ and $\operatorname{Tor}_n^R(M, N) \cong \operatorname{Tor}_n^R(N, M)$.
Example: for integers $m, n \ge 1$, tensoring $0 \to \Z \xrightarrow{\cdot m} \Z \to \Z/m\Z \to 0$ with $\Z/n\Z$ gives $\Z/n\Z \xrightarrow{\cdot m} \Z/n\Z$, whose kernel is cyclic of order $\gcd(m, n)$; so $\operatorname{Tor}_1^\Z(\Z/m\Z, \Z/n\Z) \cong \Z/\gcd(m,n)\Z$.
Non-example: the exact sequence $0 \to \Z/m\Z \xrightarrow{\id} \Z/m\Z \to 0$ is not a projective resolution over $\Z$ for $m \ge 2$, and using it would wrongly give $\operatorname{Tor}_1 = 0$.
A module $M$ is [[flat|73RYYEVDKA]] if and only if $\operatorname{Tor}_1^R(M, N) = 0$ for all $R$-modules $N$.
For a noncommutative ring $R$, the same construction works for a right module $M$ and a left module $N$.
