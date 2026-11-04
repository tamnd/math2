---
tag: 3ZBP6PNH9Z
kind: proof
name: Proof of the rational root theorem
msc: ["12E05"]
proves: 0819CQ1V8H
uses: [00EHX6FWC0, 03BAREW1Z5, 051VYKA1EX, 0GFKP8F8AG, 0SN0MAEKYX]
sources:
  - url: https://en.wikipedia.org/wiki/Rational_root_theorem
    locator: Proofs, Elementary proof
---

## Proof

1. Let $f = a_n x^n + \dots + a_1 x + a_0 \in \Z[x]$ with $n \ge 1$ and $a_n \ne 0$. Let $r = p/q$ be a [[root|00EHX6FWC0]] of $f$, with $q > 0$ and $\gcd(p, q) = 1$.
2. From $f(p/q) = 0$, multiply by $q^n$. This gives $a_n p^n + a_{n-1} p^{n-1} q + \dots + a_1 p q^{n-1} + a_0 q^n = 0$.
3. We show that $p^n$ and $q$ are [[coprime|0GFKP8F8AG]]. Suppose a [[prime|0SN0MAEKYX]] $\ell$ divides both. Since $\ell \mid p^n = p \cdots p$, [[Euclid's lemma|051VYKA1EX]] applied $n - 1$ times gives $\ell \mid p$.
4. Then $\ell$ divides $p$ and $q$, which contradicts $\gcd(p, q) = 1$. So $\gcd(p^n, q) = 1$. In the same way, $\gcd(q^n, p) = 1$.
5. By Step 2, $a_n p^n = -q \left( a_{n-1} p^{n-1} + a_{n-2} p^{n-2} q + \dots + a_0 q^{n-1} \right)$. So $q$ divides $a_n p^n$.
6. By Steps 4 and 5 and the [[generalized Euclid's lemma|03BAREW1Z5]], $q$ divides $a_n$.
7. By Step 2, $a_0 q^n = -p \left( a_n p^{n-1} + a_{n-1} p^{n-2} q + \dots + a_1 q^{n-1} \right)$. So $p$ divides $a_0 q^n$.
8. By Steps 4 and 7 and the generalized Euclid's lemma, $p$ divides $a_0$.
9. So $p$ divides $a_0$ and $q$ divides $a_n$.

## Idea

Clearing denominators turns $f(p/q) = 0$ into an equation of integers. All terms but $a_0 q^n$ contain the factor $p$, and all terms but $a_n p^n$ contain the factor $q$. Since $p$ and $q$ share no prime factor, the divisibilities pass to $a_0$ and $a_n$.
