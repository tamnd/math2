---
tag: 3SPSJ2P5X7
kind: proof
name: Proof of the Chinese remainder theorem
msc: [11A07]
proves: 0FNN9B4W64
uses: [0TPW25CBN6, 096PW7Q014, 0GFKP8F8AG, 0DQVHMYAGA, 072D5G4SK6, 00FWBN7F0Y, 03BAREW1Z5]
methods: [01XM7JEKHY, 0ASJVEFA9J]
sources:
  - url: https://en.wikipedia.org/wiki/Chinese_remainder_theorem
    locator: Proof
---

## Proof

We first build a solution, and then prove uniqueness modulo $N$ by induction.

1. Let $n_1, \dots, n_k$ be pairwise [[coprime|0GFKP8F8AG]] positive integers, let $N = n_1 n_2 \cdots n_k$, and let $a_1, \dots, a_k$ be integers.
2. Fix an index $i$. For each $j \ne i$, we have $\gcd(n_i, n_j) = 1$. By [[Bézout's identity|0DQVHMYAGA]], there are integers $u_j$ and $v_j$ with $u_j n_i + v_j n_j = 1$.
3. Let $e_i = \prod_{j \ne i} v_j n_j$. If $k = 1$, this is the empty product, so $e_1 = 1$.
4. For $j \ne i$, step 2 gives $1 - v_j n_j = u_j n_i$. So $n_i$ [[divides|096PW7Q014]] $1 - v_j n_j$, that is, $v_j n_j \equiv 1 \pmod{n_i}$ by the definition of [[congruence|0TPW25CBN6]].
5. Multiply the congruences of step 4 over all $j \ne i$, by [[compatibility with multiplication|072D5G4SK6]]. This gives $e_i \equiv 1 \pmod{n_i}$. If $k = 1$, then $e_1 = 1$ and this holds directly.
6. For $l \ne i$, the factor $v_l n_l$ appears in $e_i$, so $n_l$ divides $e_i$. That is, $e_i \equiv 0 \pmod{n_l}$.
7. Let $x = \sum_{i=1}^{k} a_i e_i$. Fix an index $l$.
8. By step 5 and compatibility with multiplication, $a_l e_l \equiv a_l \pmod{n_l}$. By step 6, $a_i e_i \equiv 0 \pmod{n_l}$ for each $i \ne l$.
9. By step 8 and [[compatibility with addition|00FWBN7F0Y]], applied term by term to the sum $x$, we get $x \equiv a_l \pmod{n_l}$. So $x$ is a solution.
10. Now let $x$ and $y$ be two solutions. For each $i$, $n_i$ divides $x - a_i$ and $y - a_i$. So $n_i$ divides their difference $x - y$.
11. We prove by induction on $j$, for $1 \le j \le k$, that $n_1 \cdots n_j$ divides $x - y$. The case $j = 1$ is step 10.
12. Assume that $x - y = n_1 \cdots n_j t$ for an integer $t$, with $j < k$. By step 10, $n_{j+1}$ divides $n_1 \cdots n_j t$.
13. For $r = 1, \dots, j$ in turn, suppose $n_{j+1}$ divides $n_r (n_{r+1} \cdots n_j t)$. Since $\gcd(n_{j+1}, n_r) = 1$, the [[generalized Euclid's lemma|03BAREW1Z5]] gives that $n_{j+1}$ divides $n_{r+1} \cdots n_j t$.
14. After the step $r = j$ in step 13, we get that $n_{j+1}$ divides $t$. Write $t = n_{j+1} t'$ with an integer $t'$.
15. Then $x - y = n_1 \cdots n_{j+1} t'$, which completes the induction step.
16. By step 11 with $j = k$, $N$ divides $x - y$. So $x \equiv y \pmod N$.
17. By steps 9 and 16, a solution exists, and two solutions are congruent modulo $N$.

## Idea

For each $i$, Bézout's identity builds a number $e_i$ that is $1$ modulo $n_i$ and $0$ modulo every other $n_l$. Then $\sum a_i e_i$ hits every target at once. For uniqueness, the coprimality lets us peel off one modulus at a time from a common multiple.
