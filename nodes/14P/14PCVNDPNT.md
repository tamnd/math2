---
tag: 14PCVNDPNT
kind: proof
name: Proof of the description of the subfields of a finite field
msc: ["12E20"]
proves: 08YERZDM9X
uses: [08RTDHX1SK, 07QY5RPFBR, 0VPFBAY7MW, 0H5WWC8RZX, 0A7KJ68XHT, 0QWR8WTZEW, 0KJVQV3E0F, 0GHDDVAH8P, 0396VGFA78]
sources:
  - url: https://en.wikipedia.org/wiki/Finite_field
    locator: Existence and uniqueness
---

## Proof

1. Let $p$ be prime, let $n \ge 1$, and let $F = \F_{p^n}$ be a [[finite field|08RTDHX1SK]] of order $p^n$. Let $P$ be its [[prime subfield|0VPFBAY7MW]]. By the [[prime power theorem|0H5WWC8RZX]], $[F : P] = n$.
2. For $m \ge 1$, let $S_m = \set{a \in F : a^{p^m} = a}$. These are the roots in $F$ of $x^{p^m} - x$, so $\abs{S_m} \le p^m$ by the [[bound on the number of roots|0KJVQV3E0F]].

We first show that every [[subfield|07QY5RPFBR]] has this form.

3. Let $K$ be a subfield of $F$. It contains $1$, so it contains $P$, and $P$ is also the prime subfield of $K$. By the prime power theorem, $\abs{K} = p^m$ with $m = [K : P]$.
4. By the [[tower law|0A7KJ68XHT]], $n = [F : P] = [F : K] \cdot [K : P] = [F : K] \cdot m$. So $m$ divides $n$.
5. By [[the equation $x^q = x$|0QWR8WTZEW]] applied to $K$, every $a \in K$ satisfies $a^{p^m} = a$. So $K \subseteq S_m$.
6. Then $p^m = \abs{K} \le \abs{S_m} \le p^m$ by step 2, so $K = S_m$.
7. So a subfield of order $p^m$ exists only if $m \mid n$, and it must equal $S_m$. In particular there is at most one subfield of each order, and there are no other subfields.

Now let $m$ divide $n$. We show that $S_m$ is a subfield of order $p^m$.

8. The [[Frobenius endomorphism|0GHDDVAH8P]] $a \mapsto a^p$ is a ring homomorphism, by the [[freshman's dream|0396VGFA78]]. Its $m$-th iterate $\psi(a) = a^{p^m}$ is a ring homomorphism too.
9. So $S_m = \set{a : \psi(a) = a}$ contains $0$ and $1$ and is closed under subtraction and multiplication. If $a \in S_m$ is nonzero, then $\psi(a^{-1}) = \psi(a)^{-1} = a^{-1}$. So $S_m$ is a subfield.
10. Write $n = mk$. Then $p^n - 1 = (p^m - 1) N$ with $N = \sum_{j=0}^{k-1} p^{mj}$, since $p^n = (p^m)^k$.
11. Let $y = x^{p^m - 1}$. Then $x^{p^n - 1} - 1 = y^N - 1 = (y - 1)(y^{N-1} + \dots + y + 1)$. Multiplying by $x$ gives $x^{p^n} - x = (x^{p^m} - x) \, h$ for some $h \in F[x]$ of degree $p^n - p^m$.
12. Every $a \in F$ satisfies $a^{p^n} = a$, by the equation $x^q = x$. So each $a \in F$ is a root of $x^{p^m} - x$ or a root of $h$.
13. The nonzero polynomial $h$ has at most $p^n - p^m$ roots in $F$. So at least $p^m$ elements of $F$ are roots of $x^{p^m} - x$, that is, $\abs{S_m} \ge p^m$.
14. With step 2, $\abs{S_m} = p^m$. So for each $m \mid n$, the field $F$ has exactly one subfield of order $p^m$, namely $S_m$, and by step 7 it has no other subfields.

## Idea

Every element of a field of order $p^m$ satisfies $a^{p^m} = a$, and this equation has at most $p^m$ solutions. So a subfield of order $p^m$ is forced to be the solution set $S_m$. When $m$ divides $n$, the polynomial $x^{p^m} - x$ divides $x^{p^n} - x$, and this gives $S_m$ enough elements.
