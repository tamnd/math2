---
tag: GGTGKFW5S3
kind: proof
name: Proof of the irreducibility of the cyclotomic polynomials by reduction modulo primes
msc: [11R18]
proves: 0SK1VHZ5R2
uses: [0W0KVBM54S, 00X2A9G9W3, 057BH3JC9S, 0E021GF2B8, 0K3MWA7DMC, 0MES3KS0ZC, 0BDX4MBKT4, 0SP14DZN0G, 08C1NWBNHA, 000JFQGDXG, 0QKVE1GD9A, 055HT85T3S, 084HH1NDCB, 0GK1WB9R98, 0NPW1DWECM, 0NFEG48RDR, 06K7SARZKR, 0DQMDSVSXJ, 0P7CH1CND5, 0GHDDVAH8P, 0BMXWXDVJZ, 0NV6E43P4A, 0DQG39K2NH, 0QRCFZKXH8, 0MNHXBSX3M, 0AD4VS02H3, 0KJVQV3E0F, 0T233AZ1GE]
sources:
  - url: https://kconrad.math.uconn.edu/blurbs/galoistheory/cyclotomic.pdf
    locator: Theorem 2.5
  - url: https://www.jmilne.org/math/CourseNotes/FT.pdf
    locator: Theorem 5.10
---

## Proof

We first show that $\Phi_n$ has rational coefficients. Then we show that $\Phi_n$ is the minimal polynomial of $\zeta = e^{2\pi i/n}$.

1. Let $n \ge 1$ and $\zeta = e^{2 \pi i / n}$, so $\zeta^k = e^{2 \pi i k / n}$ for every integer $k$. Since $\zeta^n = 1$, the number $\zeta^k$ depends only on $k$ modulo $n$.
2. By [[the description of the $n$th roots of unity|057BH3JC9S]], each of them is $\zeta^k$ for some $0 \le k < n$. There are exactly [[$n$ of them|0E021GF2B8]]. So $\zeta^0, \dots, \zeta^{n-1}$ are pairwise distinct.
3. Let $E$ be a field, $F \in E[x]$, and $a_1, \dots, a_m$ pairwise distinct roots of $F$. Then $\prod_{i=1}^m (x - a_i)$ divides $F$. We prove this by induction on $m$; the case $m = 0$ is trivial.
4. For $m \ge 1$, the induction hypothesis gives $F = \prod_{i<m} (x - a_i) \, G$. Then $0 = F(a_m) = \prod_{i<m} (a_m - a_i) \, G(a_m)$, and each $a_m - a_i \ne 0$. So $G(a_m) = 0$, and the [[factor theorem|0K3MWA7DMC]] gives $(x - a_m) \mid G$.
5. By Steps 2 to 4, $\prod_{k=1}^{n} (x - \zeta^k)$ divides $x^n - 1$. Both are [[monic|0BDX4MBKT4]] of degree $n$, so $x^n - 1 = \prod_{k=1}^{n} (x - \zeta^k)$.
6. By the [[definition|0W0KVBM54S]], $\Phi_d = \prod (x - e^{2 \pi i j / d})$, over the $j$ with $1 \le j \le d$ and $\gcd(j, d) = 1$.
7. For $1 \le k \le n$, let $e = \gcd(k, n)$, $d = n / e$ and $j = k / e$. Then $d \mid n$, $1 \le j \le d$, $\gcd(j, d) = 1$ and $\zeta^k = e^{2 \pi i j / d}$.
8. Conversely, for $d \mid n$ and such a $j$, put $k = j n / d$. Then $\gcd(k, n) = (n/d) \gcd(j, d) = n/d$, so Step 7 gives back $(d, j)$. So Step 7 is a bijection, and Step 5 becomes $x^n - 1 = \prod_{d \mid n} \Phi_d$.
9. We show by strong induction on $n$ that $\Phi_n \in \Q[x]$. First, $\Phi_1 = x - 1$. For $n > 1$, the product $h = \prod_{d \mid n, d < n} \Phi_d$ is monic and lies in $\Q[x]$ by induction.
10. [[Division by the monic $h$|0MES3KS0ZC]] in $\Q[x]$ gives $x^n - 1 = q h + r$ with $q, r \in \Q[x]$ and $\deg r < \deg h$. In $\C[x]$ we also have $x^n - 1 = \Phi_n h + 0$ by Step 8. Uniqueness of division in $\C[x]$ gives $\Phi_n = q \in \Q[x]$.
11. Next, a lemma. Let $P \in \Z[x]$ be monic and $P = A B$ with $A, B \in \Q[x]$ monic. Then $A, B \in \Z[x]$.
12. Proof of the lemma. Let $a \ge 1$ be the least integer with $a A \in \Z[x]$. If a prime $\ell$ divides all coefficients of $a A$, then $\ell \mid a$, the leading coefficient. Then $(a/\ell) A \in \Z[x]$, which contradicts the choice of $a$.
13. By Step 12 and the [[fundamental theorem of arithmetic|084HH1NDCB]], $aA$ is [[primitive|0SP14DZN0G]]. Define $b$ for $B$ in the same way, so $b B$ is primitive.
14. The ring $\Z$ is a [[Euclidean domain|000JFQGDXG]], hence a [[PID|0QKVE1GD9A]] and a [[UFD|055HT85T3S]]. By [[the product of primitive polynomials|08C1NWBNHA]], $(aA)(bB) = ab P$ is primitive. But $ab$ divides all its coefficients, so $ab = 1$ and $A, B \in \Z[x]$.
15. Let $f$ be the [[minimal polynomial|0GK1WB9R98]] of $\zeta$ over $\Q$. It exists because $\zeta$ is a root of $x^n - 1$, so $\zeta$ is [[algebraic|0NPW1DWECM]]. By [[irreducibility|0NFEG48RDR]] and [[divisibility|06K7SARZKR]], $f$ is irreducible and $f \mid x^n - 1$.
16. Key claim: if $\omega \in \C$, $f(\omega) = 0$ and $p$ is a prime with $p \nmid n$, then $f(\omega^p) = 0$. Suppose not; we derive a contradiction in Steps 17 to 27.
17. Since $f \mid x^n - 1$, we get $\omega^n = 1$. The minimal polynomial $m_\omega$ of $\omega$ divides $f$. Since $f$ is irreducible and both are monic of positive degree, $f = m_\omega$.
18. Also $(\omega^p)^n = 1$. Let $g$ be the minimal polynomial of $\omega^p$, so $g \mid x^n - 1$. Write $x^n - 1 = f k$ with $k \in \Q[x]$ monic.
19. Then $0 = f(\omega^p) k(\omega^p)$ and $f(\omega^p) \ne 0$, so $k(\omega^p) = 0$. So $g \mid k$, and $x^n - 1 = f g h$ with $h \in \Q[x]$ monic.
20. By the lemma of Step 11, applied to $x^n - 1 = f \cdot (g h)$ and then to $g h = g \cdot h$, the polynomials $f, g, h$ lie in $\Z[x]$.
21. Let $G(x) = g(x^p)$, a monic polynomial in $\Z[x]$. Then $G(\omega) = g(\omega^p) = 0$. By Step 17 and divisibility, $G = f k_2$ with $k_2 \in \Q[x]$ monic. By the lemma, $k_2 \in \Z[x]$.
22. Let $\F_p$ be the [[field $\Z/p\Z$|0NV6E43P4A]], and let $u \mapsto \bar{u}$ reduce coefficients modulo $p$. It is a ring homomorphism $\Z[x] \to \F_p[x]$, by the [[universal property|0DQMDSVSXJ]]. So $x^n - 1 = \bar{f} \bar{g} \bar{h}$ and $\bar{G} = \bar{f} \bar{k}_2$.
23. The ring $\F_p[x]$ has [[characteristic|0P7CH1CND5]] $p$. So the [[Frobenius map|0GHDDVAH8P]] $u \mapsto u^p$ is a ring homomorphism. With $\bar{g} = \sum_i b_i x^i$ and [[Fermat's little theorem|0BMXWXDVJZ]] $b_i^p = b_i$, we get $\bar{g}^p = \sum_i b_i x^{ip} = \bar{G}$.
24. The polynomial $\bar{f}$ is monic with $\deg \bar{f} = \deg f \ge 1$. Let $q$ be a monic divisor of $\bar{f}$ of least degree among those of degree at least $1$.
25. Then $q$ is irreducible. Suppose $q = a b$ with $\deg a, \deg b \ge 1$. Then $a$, made monic, is a smaller such divisor, by the [[degree of a product|0T233AZ1GE]].
26. The ring $\F_p[x]$ is a [[Euclidean domain|0DQG39K2NH]], hence a UFD, so $q$ is [[prime|0QRCFZKXH8]]. Since $q \mid \bar{f} \mid \bar{G} = \bar{g}^p$, the definition of a [[prime element|0MNHXBSX3M]], used $p - 1$ times, gives $q \mid \bar{g}$.
27. So $q^2 \mid \bar{f} \bar{g}$, and $x^n - 1 = q^2 s$ for some $s \in \F_p[x]$. The [[formal derivative|0AD4VS02H3]] and its product rule give $n x^{n-1} = q (2 q' s + q s')$. Since $p \nmid n$, $n$ is a unit of $\F_p$, so $q \mid x^{n-1}$. Then $q$ divides $x \cdot x^{n-1} - (x^n - 1) = 1$, which is impossible for $\deg q \ge 1$.
28. This proves the key claim. Now let $k \ge 1$ with $\gcd(k, n) = 1$. We show $f(\zeta^k) = 0$ by induction on the number of prime factors of $k$. For $k = 1$ this holds by the choice of $f$.
29. Otherwise $k = p m$ with $p$ prime. Then $p \nmid n$ and $\gcd(m, n) = 1$, since both $p$ and $m$ divide $k$. By induction $f(\zeta^m) = 0$. The key claim with $\omega = \zeta^m$ gives $f(\zeta^k) = 0$.
30. By Steps 2, 6 and 29, the roots $\zeta^k$ of $\Phi_n$ are $\deg \Phi_n$ distinct roots of $f$. A [[polynomial has at most $\deg f$ roots|0KJVQV3E0F]], so $\deg f \ge \deg \Phi_n$.
31. By Step 10, $\Phi_n \in \Q[x]$, and $\Phi_n(\zeta) = 0$. So $f \mid \Phi_n$, say $\Phi_n = f u$. By Step 30, $\deg u \le 0$, so $u$ is a constant, and $u = 1$ since both are monic.
32. So $\Phi_n = f$, which is [[irreducible|00X2A9G9W3]] in $\Q[x]$ by Step 15.

## Idea

The minimal polynomial $f$ of $\zeta$ divides $\Phi_n$. The heart of the proof is that the roots of $f$ are closed under $\omega \mapsto \omega^p$ for primes $p \nmid n$. Modulo $p$, the $p$-th power map turns $g(x^p)$ into $g(x)^p$, so a different factor $g$ would share a factor with $f$ modulo $p$. That gives a repeated factor of $x^n - 1$ modulo $p$, which the derivative rules out.
