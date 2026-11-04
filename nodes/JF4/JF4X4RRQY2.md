---
tag: JF4X4RRQY2
kind: proof
name: Proof of the multiplicativity of the totient function
msc: [11A25]
proves: 0FSJA9M43W
uses: [0VV04M41AN, 0GFKP8F8AG, 02WF878BH1, 0TPW25CBN6, 096PW7Q014, 0CHQKZFK5S, 0FNN9B4W64, 0SPBEDVNW1, 051VYKA1EX, 0GV2573FP4]
methods: [0NTF6DMVAP]
sources:
  - url: https://en.wikipedia.org/wiki/Euler%27s_totient_function
    locator: Phi is a multiplicative function
---

## Proof

1. Let $m$ and $n$ be [[coprime|0GFKP8F8AG]] positive integers. For a positive integer $k$, let $U_k$ be the set of integers $x$ with $1 \le x \le k$ and $\gcd(x, k) = 1$. By definition, $\varphi(k) = \abs{U_k}$, where $\varphi$ is [[Euler's totient function|0VV04M41AN]].
2. Let $k$ be a positive integer. Each integer $x$ is congruent modulo $k$ to exactly one element of $\{ 1, \dots, k \}$. Call it $\rho_k(x)$.
3. Proof of step 2: by the [[division algorithm|0CHQKZFK5S]], $x = q k + r$ with $0 \le r < k$. Take $r$ if $r > 0$ and $k$ if $r = 0$. Two elements of $\{ 1, \dots, k \}$ differ by less than $k$, so at most one of them works.
4. If $x \equiv y \pmod k$, then $\gcd(x, k) = \gcd(y, k)$. Indeed, $k$ [[divides|096PW7Q014]] $x - y$, so a divisor of $k$ divides $x$ if and only if it divides $y = x - (x - y)$.
5. Let $f : \{ 1, \dots, m n \} \to \{ 1, \dots, m \} \times \{ 1, \dots, n \}$ be the map $f(x) = (\rho_m(x), \rho_n(x))$.
6. The map $f$ is injective. If $f(x) = f(y)$, then $x \equiv y \pmod m$ and $x \equiv y \pmod n$. By the uniqueness part of the [[Chinese remainder theorem|0FNN9B4W64]], $x \equiv y \pmod{m n}$. Step 2 with $k = m n$ gives $x = y$.
7. The map $f$ is surjective. Given $(r, s)$, the Chinese remainder theorem gives an integer $z$ with $z \equiv r \pmod m$ and $z \equiv s \pmod n$. Let $x = \rho_{m n}(z)$.
8. Since $m$ and $n$ divide $m n$, and $m n$ divides $x - z$, we get $x \equiv z \equiv r \pmod m$ and $x \equiv s \pmod n$. So $f(x) = (r, s)$.
9. We show that $\gcd(x, m n) = 1$ if and only if $\gcd(x, m) = 1$ and $\gcd(x, n) = 1$.
10. If $\gcd(x, m) = d > 1$, then $d$ divides $x$ and $m n$, so $\gcd(x, m n) > 1$. The same holds for $n$.
11. Assume $\gcd(x, m) = \gcd(x, n) = 1$, and suppose $e = \gcd(x, m n) > 1$. By the [[existence of a prime divisor|0SPBEDVNW1]], there is a prime $q$ with $q \mid e$.
12. Then $q \mid m n$. By [[Euclid's lemma|051VYKA1EX]], $q \mid m$ or $q \mid n$. Since also $q \mid x$, $q$ is a common divisor greater than $1$ of $x$ and $m$, or of $x$ and $n$. This contradicts step 11.
13. By steps 4 and 9, for $x \in \{ 1, \dots, m n \}$, we have $x \in U_{m n}$ if and only if $\rho_m(x) \in U_m$ and $\rho_n(x) \in U_n$.
14. By steps 6, 7 and 13, $f$ restricts to a bijection from $U_{m n}$ onto $U_m \times U_n$.
15. By the [[bijection principle|0GV2573FP4]], $\abs{U_{m n}} = \abs{U_m} \cdot \abs{U_n}$. That is, $\varphi(m n) = \varphi(m) \varphi(n)$.

## Idea

The Chinese remainder theorem matches each number modulo $m n$ with a pair of numbers modulo $m$ and modulo $n$. A number is coprime to $m n$ exactly when both parts of its pair are coprime to their moduli, so the counts multiply.
