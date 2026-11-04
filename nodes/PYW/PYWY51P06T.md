---
tag: PYWY51P06T
kind: proof
name: Proof of Hensel's lemma by Newton steps
msc: [11A07]
proves: 010QVB71T2
uses: [0TPW25CBN6, 0SN0MAEKYX, 0AD4VS02H3, 0EHWPWGHB2, 0DQVHMYAGA, 00GXTQMY8Z, 051VYKA1EX, 00FWBN7F0Y, 072D5G4SK6, 0J5VGJYYC3]
sources:
  - url: https://en.wikipedia.org/wiki/Hensel%27s_lemma
    locator: Lifting simple roots
---

## Proof

1. Let $p$ be a [[prime number|0SN0MAEKYX]] and $f = \sum_{n=0}^{D} c_n x^n$ with integers $c_n$. Its derivative is the [[formal derivative|0AD4VS02H3]] $f' = \sum_{n=1}^{D} n c_n x^{n-1}$. Let $r$ satisfy $f(r) \equiv 0$ and $f'(r) \not\equiv 0 \pmod p$.
2. Claim T: for integers $a$ and $h$, $f(a + h) = f(a) + f'(a) h + h^2 G$ for an integer $G$. By the [[binomial theorem|0EHWPWGHB2]], $(a + h)^n = a^n + n a^{n-1} h + h^2 \sum_{i=2}^{n} \binom{n}{i} a^{n-i} h^{i-2}$. Multiply by $c_n$ and sum over $n$.
3. Claim C: if $a \equiv b \pmod p$ and $g$ has integer coefficients, then $g(a) \equiv g(b) \pmod p$. This follows from the compatibility of congruence with [[sums|00FWBN7F0Y]], [[products|072D5G4SK6]] and [[powers|0J5VGJYYC3]].
4. Since $p$ is prime and $p \nmid f'(r)$, we have $\gcd(f'(r), p) = 1$. By [[Bézout's identity|0DQVHMYAGA]] there is an integer $t$ with $t f'(r) \equiv 1 \pmod p$, a [[modular inverse|00GXTQMY8Z]].

Existence. We argue by induction on $k$.

5. For $k = 1$, take $r_1 = r$.
6. Assume $r_k \equiv r \pmod p$ and $p^k \mid f(r_k)$. Let $h = -t f(r_k)$ and $r_{k+1} = r_k + h$. Then $p^k \mid h$.
7. By claim T, $f(r_{k+1}) = f(r_k) \left(1 - t f'(r_k)\right) + h^2 G$ for an integer $G$.
8. By claim C, $f'(r_k) \equiv f'(r) \pmod p$, so $1 - t f'(r_k) \equiv 1 - t f'(r) \equiv 0 \pmod p$. With $p^k \mid f(r_k)$, the first term is divisible by $p^{k+1}$.
9. Also $p^{2k} \mid h^2$, and $2k \ge k + 1$. So $p^{k+1} \mid f(r_{k+1})$.
10. Since $p \mid h$, we have $r_{k+1} \equiv r_k \equiv r \pmod p$. This completes the induction.

Uniqueness.

11. Let $s$ and $s'$ satisfy $s \equiv s' \equiv r \pmod p$ and $f(s) \equiv f(s') \equiv 0 \pmod{p^k}$. We show $s \equiv s' \pmod{p^j}$ for $j = 1, \dots, k$ by induction on $j$. The case $j = 1$ holds by assumption.
12. Assume $p^j \mid h$ with $h = s' - s$ and $j < k$. By claim T, $f(s') = f(s) + f'(s) h + h^2 G$ for an integer $G$.
13. Here $p^{j+1}$ divides $f(s)$ and $f(s')$, as $j + 1 \le k$. It divides $h^2$, as $2j \ge j + 1$. So $p^{j+1} \mid f'(s) h$.
14. Write $h = p^j h'$. Then $p \mid f'(s) h'$. By claim C, $f'(s) \equiv f'(r) \not\equiv 0 \pmod p$. By [[Euclid's lemma|051VYKA1EX]], $p \mid h'$, so $p^{j+1} \mid h$.
15. With $j = k$, this gives $s \equiv s' \pmod{p^k}$. So $r_k$ is unique modulo $p^k$.

## Idea

This is Newton's method for congruences. Near a root, $f(a + h) \approx f(a) + f'(a) h$, and the error $h^2 G$ is invisible to the next power of $p$. Since $f'(r)$ is invertible modulo $p$, one can always solve for the correction $h$, and the same fact shows the correction is forced.
