---
tag: K57MY39EKB
kind: proof
name: Proof of the divisibility rule for 11
msc: [11A63]
proves: 09YBMJTNBM
uses: [0TPW25CBN6, 096PW7Q014, 0J5VGJYYC3, 072D5G4SK6, 00FWBN7F0Y]
methods: [0NTF6DMVAP]
sources:
  - url: https://en.wikipedia.org/wiki/Divisibility_rule
    locator: Case where the alternating sum of digits is used
---

## Proof

1. Let $n = \sum_{i=0}^{k} d_i 10^i$ with decimal digits $d_0, \dots, d_k$. Let $A = \sum_{i=0}^{k} (-1)^i d_i = d_0 - d_1 + d_2 - \dots + (-1)^k d_k$ be the alternating digit sum.
2. Since $10 - (-1) = 11$, the number $11$ [[divides|096PW7Q014]] $10 - (-1)$. So $10 \equiv -1 \pmod{11}$ by the definition of [[congruence|0TPW25CBN6]].
3. Let $0 \le i \le k$. By step 2 and [[compatibility with powers|0J5VGJYYC3]], $10^i \equiv (-1)^i \pmod{11}$.
4. Since $d_i \equiv d_i \pmod{11}$, step 3 and [[compatibility with multiplication|072D5G4SK6]] give $d_i 10^i \equiv (-1)^i d_i \pmod{11}$.
5. Apply [[compatibility with addition|00FWBN7F0Y]] $k$ times to the $k + 1$ congruences of step 4. This gives $n \equiv A \pmod{11}$.
6. So there is an integer $t$ with $n - A = 11 t$.
7. If $11 \mid A$, say $A = 11 s$, then $n = A + 11 t = 11 (s + t)$, so $11 \mid n$.
8. If $11 \mid n$, say $n = 11 m$, then $A = n - 11 t = 11 (m - t)$, so $11 \mid A$.
9. By steps 7 and 8, $11 \mid n$ if and only if $11 \mid d_0 - d_1 + d_2 - \dots + (-1)^k d_k$.

## Idea

Since $10 = 11 - 1$, the number $10$ acts like $-1$ modulo $11$. So the powers of $10$ act like $1, -1, 1, -1, \dots$, and the number is congruent to its alternating digit sum.
