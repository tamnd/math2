---
tag: 13TM6CVZAG
kind: proof
name: Proof of Wedderburn's little theorem by the class equation and cyclotomic polynomials
msc: ["12E15"]
proves: 0RRNVX1VKA
uses: [0WZXK05ME7, 0QA8CHH8MG, 0859D58WPD, 05EGHEQZAW, 06MRNP4BNT, 0VTQTPQGAV, 05THZKR9AN, 0S7Y9Q990Q, 0Q0Z1BEXTF, 3C53TD, 04DC0SRN2K, 08BPSC6YTE, 0CHQKZFK5S, 05APWSX53S, 0W0KVBM54S, 057BH3JC9S, 0E021GF2B8, 02P2PYH3X3, 0K3MWA7DMC, 0T233AZ1GE, 0FRSR10DWF, 0MES3KS0ZC, 0BDX4MBKT4, 02WF878BH1, 0KW2X0TFBX, 0HYNZE940T]
sources:
  - url: https://en.wikipedia.org/wiki/Wedderburn%27s_little_theorem
    locator: Proof
---

## Proof

We follow the proof of Witt. Steps 1 to 9 prove facts on [[cyclotomic polynomials|0W0KVBM54S]] $\Phi_m$. Steps 10 to 26 apply them to the division ring.

1. Let $m \ge 1$ and $\zeta_k = e^{2 \pi i k / m}$ for $0 \le k < m$. These are all the $m$th roots of unity, [[by their description|057BH3JC9S]]. There are [[exactly $m$ of them|0E021GF2B8]], so they are pairwise distinct.
2. Claim: $x^m - 1 = \prod_{k=0}^{m-1} (x - \zeta_k)$ in $\C[x]$. By the [[factor theorem|0K3MWA7DMC]], $x^m - 1 = (x - \zeta_0) h_1$ for some $h_1 \in \C[x]$.
3. Evaluating at $\zeta_1$ gives $0 = (\zeta_1 - \zeta_0) h_1(\zeta_1)$. Since $\zeta_1 \neq \zeta_0$ and [[$\C$ is a field|0FRSR10DWF]], $h_1(\zeta_1) = 0$. Repeating this $m$ times gives $x^m - 1 = c \prod_{k=0}^{m-1} (x - \zeta_k)$ with $c \in \C$. [[Comparing degrees|0T233AZ1GE]] and leading coefficients gives $c = 1$.
4. For $0 \le k < m$, let $g = \gcd(k, m)$, the [[greatest common divisor|02WF878BH1]], with $\gcd(0, m) = m$. Put $d = m / g$ and $j = k / g$. Then $d \mid m$, $\gcd(j, d) = 1$ and $\zeta_k = e^{2 \pi i j / d}$. If $j = 0$, then $d = 1$, and we replace $j$ by $1$; the value is unchanged by [[periodicity|02P2PYH3X3]].
5. This sends $k$ to a pair $(d, j)$ with $d \mid m$, $1 \le j \le d$ and $\gcd(j, d) = 1$. It is a bijection onto these pairs. Its inverse sends $(d, j)$ to the remainder of $j m / d$ modulo $m$, since $\gcd(j m / d, m) = (m / d) \gcd(j, d) = m / d$.
6. By steps 3 and 5 and the definition of $\Phi_d$, $x^m - 1 = \prod_{d \mid m} \Phi_d(x)$.
7. Each $\Phi_m$ is a [[monic polynomial|0BDX4MBKT4]] with integer coefficients. We use strong induction on $m$. It is monic as a product of monic factors, and $\Phi_1 = x - 1$. For $m > 1$, let $F = \prod_{d \mid m, d < m} \Phi_d$, which is monic in $\Z[x]$ by induction. By step 6, $x^m - 1 = \Phi_m F$.
8. By the [[division algorithm for polynomials|0MES3KS0ZC]] in $\Z[x]$, $x^m - 1 = Q F + r$ with $Q, r \in \Z[x]$ and $\deg r < \deg F$. The same algorithm in $\C[x]$ has a unique result, and $x^m - 1 = \Phi_m F + 0$ is one. So $\Phi_m = Q \in \Z[x]$.
9. Let $d \mid m$ with $d < m$. The divisors of $d$ are divisors of $m$ other than $m$. So by step 6, $x^m - 1 = (x^d - 1) \Phi_m(x) H(x)$, where $H$ is the product of $\Phi_e$ over the $e \mid m$ with $e \nmid d$ and $e \neq m$. By step 7, $H \in \Z[x]$.
10. Let $D$ be a [[division ring|0WZXK05ME7]] with finitely many elements. Let $Z = \set{z \in D : z x = x z \text{ for all } x \in D}$.
11. If $z, w \in Z$, then $z - w$ and $z w$ commute with every $x \in D$, and $1 \in Z$. So $Z$ is a [[subring|0859D58WPD]] of $D$, and it is commutative. If $z \in Z$ and $z \neq 0$, then $z^{-1} x = z^{-1} x z z^{-1} = z^{-1} z x z^{-1} = x z^{-1}$ for all $x$. So $z^{-1} \in Z$, and $Z$ is a [[field|0QA8CHH8MG]]. Let $q = \abs{Z}$; then $q \ge 2$, since $0 \neq 1$.
12. For $a \in D$, let $C(a) = \set{x \in D : x a = a x}$. It contains $Z$, and it is closed under addition and under left multiplication by elements of $Z$. With these operations, $C(a)$ is a [[vector space|05EGHEQZAW]] over $Z$. The axioms follow from the ring axioms of $D$. In the same way, $D$ is a vector space over $Z$.
13. Let $V$ be a vector space over $Z$ with finitely many elements. The set $V$ spans itself, so it [[contains a basis|06MRNP4BNT]] $v_1, \dots, v_r$. Each vector is $c_1 v_1 + \dots + c_r v_r$ for exactly one choice of $c_1, \dots, c_r \in Z$, by the definition of a [[basis|0VTQTPQGAV]]. So $\abs{V} = q^r$.
14. So $\abs{D} = q^n$ for some $n \ge 1$, and $\abs{C(a)} = q^{d(a)}$ for some $d(a) \ge 1$. We assume $n > 1$ and derive a contradiction.
15. The nonzero elements of $D$ are units, and $0$ is not a unit. So $D^* = D \setminus \set{0}$ is the [[group of units|05THZKR9AN]] of $D$, of order $q^n - 1$.
16. The [[centre|0S7Y9Q990Q]] of the group $D^*$ is $Z \setminus \set{0}$, since every element commutes with $0$. It has order $q - 1$. The [[centraliser|0Q0Z1BEXTF]] of $a \in D^*$ in $D^*$ is $C(a) \setminus \set{0}$, of order $q^{d(a)} - 1$.
17. Fix $a \in D^*$ and write $d = d(a)$. By [[Lagrange's theorem|3C53TD]], $q^d - 1$ divides $q^n - 1$. Write $n = s d + t$ with integers $s \ge 0$ and $0 \le t < d$, by the [[division algorithm|0CHQKZFK5S]].
18. By the [[geometric sum|05APWSX53S]], $q^{s d} - 1 = (q^d - 1)(1 + q^d + \dots + q^{(s-1) d})$, so $q^d - 1$ divides $q^{s d} - 1$. Since $q^n - 1 = q^t (q^{s d} - 1) + (q^t - 1)$, it also divides $q^t - 1$. As $0 \le q^t - 1 < q^d - 1$, we get $q^t = 1$, so $t = 0$ and $d \mid n$.
19. By the [[class equation|08BPSC6YTE]] for $D^*$, $q^n - 1 = (q - 1) + \sum_{i=1}^{l} [D^* : C_{D^*}(a_i)]$. Here $a_1, \dots, a_l$ represent the conjugacy classes with more than one element.
20. Such an $a_i$ is not central, since a central element is alone in its class. So $C(a_i) \neq D$, and $d_i = d(a_i) < n$. By [[the index formula|04DC0SRN2K]] and step 16, $[D^* : C_{D^*}(a_i)] = (q^n - 1)/(q^{d_i} - 1)$. By step 18, $d_i \mid n$.
21. Evaluate steps 6 and 9 at $x = q$, with $m = n$. The integer $\Phi_n(q)$ divides $q^n - 1 = \Phi_n(q) F(q)$, where $F$ is the polynomial of step 7 for $m = n$, so $F(q)$ is an integer. It also divides $(q^n - 1)/(q^{d_i} - 1) = \Phi_n(q) H(q)$ for each $i$. By step 19, $\Phi_n(q)$ divides $q - 1$. As $q - 1 \ge 1$, $\abs{\Phi_n(q)} \le q - 1$.
22. Now let $\zeta = e^{2 \pi i j / n}$ with $1 \le j \le n$ and $\gcd(j, n) = 1$. Since $n > 1$, $j \neq n$, so $\zeta \neq 1$ by step 1. Write $\zeta = u + i v$ with $u, v$ real. Its [[modulus|0KW2X0TFBX]] is $1$, so $u^2 + v^2 = 1$, and $\zeta \neq 1$ forces $u < 1$.
23. Then $\abs{q - \zeta}^2 = (q - u)^2 + v^2 = q^2 - 2 q u + 1 > q^2 - 2 q + 1 = (q - 1)^2$. So $\abs{q - \zeta} > q - 1 \ge 1$.
24. The modulus [[is multiplicative|0HYNZE940T]], so $\abs{\Phi_n(q)}$ is the product of the numbers $\abs{q - \zeta}$ of step 22. There is at least one factor, for $j = 1$. Each factor exceeds $1$, and one exceeds $q - 1$. So $\abs{\Phi_n(q)} > q - 1$.
25. This contradicts step 21. Hence $n = 1$, so $\abs{D} = q = \abs{Z}$ and $D = Z$.
26. So the multiplication of $D$ is commutative. A commutative division ring is a field, by the definitions.

## Idea

The centre $Z$ is a field with $q$ elements, and $D$ has $q^n$ elements. The class equation of the group $D^*$ writes $q^n - 1$ as $q - 1$ plus terms $(q^n - 1)/(q^d - 1)$ with $d$ a proper divisor of $n$. The integer $\Phi_n(q)$ divides all of these, so it divides $q - 1$. But each root of $\Phi_n$ is farther than $q - 1$ from $q$, which is impossible unless $n = 1$.
