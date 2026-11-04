---
tag: DBX26C9SMJ
kind: proof
name: Proof of Euler's theorem by rearrangement
msc: [11A07]
proves: 0VC4DVE7DQ
uses: [0VV04M41AN, 0GFKP8F8AG, 0TPW25CBN6, 096PW7Q014, 00GXTQMY8Z, 0M67FWZWPQ, 0CHQKZFK5S, 072D5G4SK6]
methods: [0NTF6DMVAP]
sources:
  - url: https://en.wikipedia.org/wiki/Euler%27s_theorem
    locator: Proofs
---

## Proof

1. Let $n$ be a positive integer and let $a$ be an integer [[coprime|0GFKP8F8AG]] to $n$. Let $R$ be the set of integers $r$ with $1 \le r \le n$ and $\gcd(r, n) = 1$.
2. By the definition of [[Euler's totient function|0VV04M41AN]], $R$ has $\varphi(n)$ elements.
3. By the [[existence of inverses modulo n|0M67FWZWPQ]], an integer is coprime to $n$ if and only if it has a [[modular multiplicative inverse|00GXTQMY8Z]] modulo $n$. Let $x$ be an inverse of $a$, so $a x \equiv 1 \pmod n$.
4. Let $r \in R$, and let $y$ be an inverse of $r$. By [[compatibility with multiplication|072D5G4SK6]], $(a r)(x y) = (a x)(r y) \equiv 1 \cdot 1 = 1 \pmod n$.
5. By the [[division algorithm|0CHQKZFK5S]], $a r = q n + t$ with $0 \le t < n$. Let $s(r) = t$ if $t > 0$, and $s(r) = n$ if $t = 0$. Then $1 \le s(r) \le n$ and $n$ [[divides|096PW7Q014]] $a r - s(r)$, so $s(r) \equiv a r \pmod n$.
6. By steps 4 and 5 and compatibility with multiplication, $s(r) (x y) \equiv (a r)(x y) \equiv 1 \pmod n$. So $s(r)$ has an inverse, and by step 3, $s(r) \in R$.
7. Let $r, r' \in R$ with $s(r) = s(r')$. Then $a r \equiv a r' \pmod n$. Multiplying by $x$ gives $(x a) r \equiv (x a) r' \pmod n$, so $r \equiv r' \pmod n$ by step 3.
8. Since $r$ and $r'$ lie in $\{ 1, \dots, n \}$, their difference has absolute value less than $n$. As $n$ divides it, $r = r'$.
9. By steps 6 to 8, $s$ is an injective map from the finite set $R$ to itself. So $s$ is a bijection of $R$, and $\prod_{r \in R} s(r) = \prod_{r \in R} r$.
10. Let $P = \prod_{r \in R} r$. By steps 5 and 9 and compatibility with multiplication, $a^{\varphi(n)} P = \prod_{r \in R} (a r) \equiv \prod_{r \in R} s(r) = P \pmod n$.
11. Each $r \in R$ has an inverse $y_r$. Let $z = \prod_{r \in R} y_r$. By compatibility with multiplication, $P z = \prod_{r \in R} (r y_r) \equiv 1 \pmod n$.
12. Multiply the congruence of step 10 by $z$. This gives $a^{\varphi(n)} (P z) \equiv P z \pmod n$.
13. By step 11, $a^{\varphi(n)} (P z) \equiv a^{\varphi(n)} \pmod n$ and $P z \equiv 1 \pmod n$. With step 12, $a^{\varphi(n)} \equiv 1 \pmod n$.

## Idea

Multiplying the residues coprime to $n$ by $a$ only shuffles them, because $a$ can be undone by its inverse. So the product $P$ of these residues equals $a^{\varphi(n)} P$ modulo $n$. Since $P$ is invertible, we can cancel it.
