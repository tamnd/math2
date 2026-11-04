---
tag: SJWH2V43J2
kind: proof
name: Proof of the divisibility rule for 9
msc: [11A63]
proves: 0ESHD7ZQDX
uses: [0TPW25CBN6, 096PW7Q014, 0J5VGJYYC3, 072D5G4SK6, 00FWBN7F0Y]
methods: [0NTF6DMVAP]
sources:
  - url: https://en.wikipedia.org/wiki/Divisibility_rule
    locator: Case where all digits are summed
---

## Proof

1. Let $n = \sum_{i=0}^{k} d_i 10^i$ with decimal digits $d_0, \dots, d_k$. Let $S = d_0 + d_1 + \dots + d_k$ be the digit sum.
2. Since $10 - 1 = 9 = 9 \cdot 1$, the number $9$ [[divides|096PW7Q014]] $10 - 1$. So $10 \equiv 1 \pmod 9$ by the definition of [[congruence|0TPW25CBN6]].
3. Let $0 \le i \le k$. By step 2 and [[compatibility with powers|0J5VGJYYC3]], $10^i \equiv 1^i = 1 \pmod 9$.
4. Since $d_i \equiv d_i \pmod 9$, step 3 and [[compatibility with multiplication|072D5G4SK6]] give $d_i 10^i \equiv d_i \pmod 9$.
5. Apply [[compatibility with addition|00FWBN7F0Y]] $k$ times to the $k + 1$ congruences of step 4. This gives $n \equiv S \pmod 9$.
6. So there is an integer $t$ with $n - S = 9 t$.
7. If $9 \mid S$, say $S = 9 s$, then $n = S + 9 t = 9 (s + t)$, so $9 \mid n$.
8. If $9 \mid n$, say $n = 9 m$, then $S = n - 9 t = 9 (m - t)$, so $9 \mid S$.
9. By steps 7 and 8, $9 \mid n$ if and only if $9 \mid d_0 + d_1 + \dots + d_k$.

## Idea

Each power of $10$ leaves remainder $1$ on division by $9$, because $10 = 9 + 1$. So each digit counts for itself modulo $9$, and the number and its digit sum differ by a multiple of $9$.
