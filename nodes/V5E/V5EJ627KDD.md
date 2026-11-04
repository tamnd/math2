---
tag: V5EJ627KDD
kind: proof
name: Proof of the Gauss–Wantzel theorem
msc: [12F05]
proves: 0Y34JMJNE9
uses: [0FMN2MN7TM, 0PN9WMRWT7, 02PETK9PQ4, 0SSSM1D475, 0W0KVBM54S, 0SK1VHZ5R2, 0VV04M41AN, 0GK1WB9R98, 06K7SARZKR, 0N5QW9K7MH, 0FSJA9M43W, 0AVY8HKBGD, 0K3MWA7DMC, 0N9E4G2P97, 04R3CY41VJ, 03MTBVG3VE, 057BH3JC9S, 0E021GF2B8, 0KJVQV3E0F, 02NZZ1J0FH, 03J8BS7FMV, P75CXH2Q2B, 0XVR72M51M, 0BDJBH8B4Z, 0ZN39QDTP9, 071DDFVG4J, 0JM7PA288B, 0W77CVBCHQ, 0KMJ6919WS, 0T1Q8D0FW8, 0A7KJ68XHT]
sources:
  - url: https://en.wikipedia.org/wiki/Constructible_polygon
    locator: Conditions for constructibility
---

## Proof

Let $n \ge 3$, let $\zeta = e^{2\pi i/n}$, and let $\mathcal{C}$ be the set of the [[constructible numbers|0FMN2MN7TM]]. By the [[field theorem|0PN9WMRWT7]], $\mathcal{C}$ is a subfield of $\C$ closed under square roots. By [[Euler's formula|04R3CY41VJ]] and [[de Moivre's formula|03MTBVG3VE]], the powers $\zeta^k = e^{2\pi i k/n}$, $0 \le k < n$, are the vertices of a regular $n$-gon with centre $0$. If $\zeta \in \mathcal{C}$, they all lie in the field $\mathcal{C}$, so this $n$-gon is constructible. Conversely, let a regular $n$-gon with centre $c$ be constructed, and let $v$ and $w$ be adjacent vertices. Its vertices are $c + (v - c)\zeta^k$ for $0 \le k < n$. Their sum is $nc$, because [[$\sum_{k=0}^{n-1} \zeta^k = 0$|02PETK9PQ4]]. So $c \in \mathcal{C}$. Also $(w - c)/(v - c)$ is $\zeta$ or $\zeta^{-1}$, so $\zeta \in \mathcal{C}$. So we must show: $\zeta \in \mathcal{C}$ if and only if $n$ has the stated form. Let $\varphi$ be [[Euler's totient function|0VV04M41AN]].

The degree of $\zeta$.

1. The [[cyclotomic polynomial|0W0KVBM54S]] $\Phi_n$ is monic, has the root $\zeta$ (the factor with $k = 1$), and has degree $\varphi(n)$. Indeed, for $n \ge 2$ neither $k = n$ nor $0$ is coprime to $n$, so both ranges give the same count. It is [[irreducible in $\Q[x]$|0SK1VHZ5R2]].
2. So the [[minimal polynomial|0GK1WB9R98]] of $\zeta$, which [[divides|06K7SARZKR]] $\Phi_n$, equals $\Phi_n$. By the [[degree of a simple extension|0N5QW9K7MH]], $[\Q(\zeta) : \Q] = \varphi(n)$.

Necessity.

3. Suppose $\zeta \in \mathcal{C}$. Then $\varphi(n)$ is a [[power of $2$|0SSSM1D475]], say $2^r$.
4. Write $n = 2^k p_1^{a_1} \cdots p_t^{a_t}$ with distinct odd primes $p_j$ and $a_j \ge 1$. By [[multiplicativity|0FSJA9M43W]] and the [[totient of a prime power|0AVY8HKBGD]], $\varphi(n) = \varphi(2^k) \prod_j p_j^{a_j - 1} (p_j - 1)$.
5. Each factor $p_j^{a_j - 1}(p_j - 1)$ divides $2^r$, so it is a power of $2$. Since $p_j$ is odd, $a_j = 1$, and $p_j - 1 = 2^{m_j}$ with $m_j \ge 1$.
6. Suppose that $m = m_j$ has an odd divisor $b > 1$, say $m = cb$. The polynomial $y^b + 1$ has the root $-1$, as $b$ is odd. By the [[factor theorem|0K3MWA7DMC]], $y + 1$ divides $y^b + 1$ in $\Z[y]$.
7. Putting $y = 2^c$ shows that $2^c + 1$ divides $2^m + 1 = p_j$. Since $c < m$, we have $1 < 2^c + 1 < p_j$, which contradicts the primality of $p_j$.
8. So $m_j = 2^{s_j}$ for some $s_j \ge 0$, and $p_j = 2^{2^{s_j}} + 1$ is a [[Fermat prime|0N9E4G2P97]]. Hence $n = 2^k p_1 \cdots p_t$ with distinct Fermat primes $p_j$.

Sufficiency.

9. Let $n = 2^k p_1 \cdots p_t$ with distinct Fermat primes $p_j = 2^{2^{s_j}} + 1$. By step 4, $\varphi(n) = \varphi(2^k) \prod_j 2^{2^{s_j}}$, where $\varphi(2^k) = 2^{k-1}$ for $k \ge 1$ and $\varphi(1) = 1$. So $\varphi(n) = 2^r$ for some $r \ge 0$.
10. Let $L = \Q(\zeta) \subseteq \C$ and $f = x^n - 1$. By the [[description of the roots of unity|057BH3JC9S]], every root of $f$ is $\zeta^k$ for some $k$ with $0 \le k < n$.
11. There are [[exactly $n$ roots of $f$|0E021GF2B8]], so $\zeta^0, \dots, \zeta^{n-1}$ are distinct. Then $f - \prod_k (x - \zeta^k)$ has degree less than $n$ and $n$ roots, so it is $0$ by the [[root bound|0KJVQV3E0F]].
12. So $f$ splits over $L$, and $L = \Q(\zeta^0, \dots, \zeta^{n-1})$. Thus $L$ is a [[splitting field|02NZZ1J0FH]] of $f$ over $\Q$.
13. Also $(-1) \cdot f + (x/n) \cdot f' = 1$, so $f$ is [[separable|03J8BS7FMV]]. By the [[characterisation of Galois extensions|P75CXH2Q2B]], $L/\Q$ is a finite Galois extension.
14. Let $G = \operatorname{Gal}(L/\Q)$, the [[Galois group|0XVR72M51M]]. By the [[order of the Galois group|0BDJBH8B4Z]] and step 2, $\abs{G} = \varphi(n) = 2^r$.
15. For $\sigma \in G$, $\sigma(\zeta)^n = 1$, so $\sigma(\zeta) = \zeta^{a_\sigma}$ for some integer $a_\sigma$ by step 10. Since [[every element of $L$ is $h(\zeta)$ with $h \in \Q[x]$|0ZN39QDTP9]], $\sigma$ is determined by $\sigma(\zeta)$.
16. For $\sigma, \tau \in G$, we get $\sigma\tau(\zeta) = \zeta^{a_\sigma a_\tau} = \tau\sigma(\zeta)$. So $\sigma\tau = \tau\sigma$, and $G$ is [[abelian|071DDFVG4J]].
17. Claim: for every $r \ge 0$, every subfield $E \subseteq \C$ such that $E/\Q$ is a finite Galois extension with abelian Galois group of order $2^r$ satisfies $E \subseteq \mathcal{C}$. We prove it by induction on $r$.
18. If $r = 0$, then $[E : \Q] = 1$ by the order of the Galois group. So $E = \Q$, and $\Q \subseteq \mathcal{C}$ because the subfield $\mathcal{C}$ contains $1$.
19. Let $r \ge 1$ and $G_E = \operatorname{Gal}(E/\Q)$. By [[Cauchy's theorem|0JM7PA288B]], some $h \in G_E$ has order $2$. As $G_E$ is abelian, $H = \set{1, h}$ is a [[normal subgroup|0W77CVBCHQ]].
20. Let $E' = E^H$ be the [[fixed field|0KMJ6919WS]]. By the [[fundamental theorem of Galois theory|0T1Q8D0FW8]], $[E : E'] = 2$, $E'/\Q$ is normal, and $\operatorname{Gal}(E'/\Q) \cong G_E/H$, which is abelian of order $2^{r-1}$.
21. Every element of $E'$ lies in $E$, so it is separable over $\Q$. So $E'/\Q$ is a finite Galois extension, and $E' \subseteq \mathcal{C}$ by the induction hypothesis.
22. Choose $a \in E$ with $a \notin E'$. By the [[tower law|0A7KJ68XHT]], $[E'(a) : E']$ divides $[E : E'] = 2$ and is not $1$. So $[E'(a) : E'] = 2$, $[E : E'(a)] = 1$, and $E = E'(a)$.
23. Let $x^2 + bx + c$ be the minimal polynomial of $a$ over $E'$, and let $s = 2a + b$. Then $s^2 = 4(a^2 + ab) + b^2 = b^2 - 4c \in E' \subseteq \mathcal{C}$.
24. So $s \in \mathcal{C}$, as a square root of an element of $\mathcal{C}$. Then $a = (s - b)/2 \in \mathcal{C}$, since $\mathcal{C}$ is a field containing $b$.
25. By the degree of a simple extension, every element of $E = E'(a)$ is $u + va$ with $u, v \in E'$. All of these lie in $\mathcal{C}$. So $E \subseteq \mathcal{C}$, which proves the claim.
26. By steps 13, 14 and 16, the claim applies to $E = L$. So $\zeta \in \mathcal{C}$, and the regular $n$-gon is constructible.

## Idea

The regular $n$-gon is constructible exactly when $\zeta = e^{2\pi i/n}$ is, and $\zeta$ has degree $\varphi(n)$ over $\Q$. If $\zeta$ is constructible, $\varphi(n)$ is a power of $2$, which forces the stated form of $n$. Conversely, if $\varphi(n)$ is a power of $2$, the abelian Galois group of $\Q(\zeta)$ can be cut down by subgroups of order $2$. This gives a chain of quadratic extensions, and each quadratic step only needs a square root.
