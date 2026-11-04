---
tag: TKE9RVC3TQ
kind: proof
name: Proof that the units of Z/nZ are the residues coprime to n
msc: [11A07, 20K01]
proves: 0GXNHEHQNA
uses: [01N3AYAA6N, 0QRV8FPK5M, 019NFGFPR5, 02WF878BH1, 0DQVHMYAGA]
sources:
  - url: https://proofwiki.org/wiki/Multiplicative_Inverse_in_Monoid_of_Integers_Modulo_m
---

## Proof

We prove the two directions separately.

1. Let $n \geq 1$ and $a$ be integers. Write $[b]$ for the [[residue class|0QRV8FPK5M]] of an integer $b$ modulo $n$, so $[b] = b + n\Z$.
2. In the ring [[$\Z/n\Z$|01N3AYAA6N]] the product is $[b][c] = [bc]$, and the identity is $[1]$. The ring is commutative, because $bc = cb$.
3. If $b = c + nm$ for an integer $m$, then $b + n\Z = c + n\Z$, so $[b] = [c]$.
4. If $[b] = [c]$, then $b \in [b] = [c] = c + n\Z$, so $b = c + nm$ for an integer $m$.
5. First assume $\gcd(a, n) = 1$. By [[Bézout's identity|0DQVHMYAGA]], there are integers $x$ and $y$ with $ax + ny = 1$.
6. Then $ax = 1 + n(-y)$. By step 3, $[a][x] = [ax] = [1]$.
7. By step 2, also $[x][a] = [1]$. So $[a]$ is a [[unit|019NFGFPR5]] of $\Z/n\Z$, with inverse $[x]$.
8. Now assume that $[a]$ is a unit. Then there is a class $[x]$ with $[a][x] = [1]$, that is, $[ax] = [1]$.
9. By step 4, there is an integer $m$ with $ax = 1 + nm$, so $1 = ax - nm$.
10. Let $d = \gcd(a, n)$ be the [[greatest common divisor|02WF878BH1]]. It exists and $d \geq 1$, because $n \geq 1$, so $a$ and $n$ are not both $0$.
11. The integer $d$ divides $a$ and $n$, so it divides $ax - nm = 1$.
12. A positive divisor of $1$ is $1$, so $d = 1$.
13. Thus $[a]$ is a unit of $\Z/n\Z$ if and only if $\gcd(a, n) = 1$.

## Idea

An inverse of $[a]$ is an integer $x$ with $ax + ny = 1$ for some integer $y$. Bézout's identity gives such $x$ and $y$ exactly when $\gcd(a, n) = 1$. Conversely, such an equation forces every common divisor of $a$ and $n$ to divide $1$.
