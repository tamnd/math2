---
tag: 4W0R66PGGM
kind: proof
name: Proof of Fermat's little theorem by rearrangement
msc: [11A07]
proves: 0M25PRN3WQ
uses: [0SN0MAEKYX, 0TPW25CBN6, 096PW7Q014, 051VYKA1EX, 0CHQKZFK5S, 072D5G4SK6]
methods: [0NTF6DMVAP]
sources:
  - url: https://en.wikipedia.org/wiki/Proofs_of_Fermat%27s_little_theorem
    locator: Proof as a particular case of Euler's theorem
---

## Proof

1. Let $p$ be a [[prime number|0SN0MAEKYX]] and let $a$ be an integer with $p \nmid a$. Let $R = \{ 1, 2, \dots, p - 1 \}$.
2. For $i \in R$, we have $0 < i < p$, so $p$ does not [[divide|096PW7Q014]] $i$. Since also $p \nmid a$, [[Euclid's lemma|051VYKA1EX]] gives $p \nmid i a$.
3. For $i \in R$, let $r_i$ be the remainder of $i a$ on division by $p$, given by the [[division algorithm|0CHQKZFK5S]]. Then $0 \le r_i < p$ and $r_i \equiv i a \pmod p$.
4. If $r_i = 0$, then $p$ divides $i a$, which contradicts step 2. So $r_i \in R$.
5. Let $i, j \in R$ with $r_i = r_j$. Then $i a \equiv j a \pmod p$, so $p$ divides $(i - j) a$.
6. Since $p \nmid a$, Euclid's lemma gives $p \mid i - j$. Since $\abs{i - j} < p$, this forces $i - j = 0$, so $i = j$.
7. By steps 4 and 6, the numbers $r_1, \dots, r_{p-1}$ are $p - 1$ distinct elements of $R$. Since $R$ has $p - 1$ elements, they are all the elements of $R$ in some order.
8. Hence $r_1 r_2 \cdots r_{p-1} = 1 \cdot 2 \cdots (p - 1) = (p - 1)!$.
9. By step 3 and [[compatibility with multiplication|072D5G4SK6]], $\prod_{i=1}^{p-1} (i a) \equiv \prod_{i=1}^{p-1} r_i \pmod p$.
10. The left side of step 9 is $a^{p-1} (p - 1)!$. With step 8, we get $a^{p-1} (p - 1)! \equiv (p - 1)! \pmod p$.
11. So $p$ divides $(a^{p-1} - 1) (p - 1)!$.
12. The prime $p$ does not divide $(p - 1)!$. Otherwise, Euclid's lemma applied to the factors $1, \dots, p - 1$ in turn would give $p \mid i$ for some $i \in R$, against step 2.
13. By steps 11 and 12 and Euclid's lemma, $p$ divides $a^{p-1} - 1$. Hence $a^{p-1} \equiv 1 \pmod p$.

## Idea

Multiplying the nonzero residues $1, \dots, p - 1$ by $a$ only shuffles them. So the product of all of them is unchanged, except for the factor $a^{p-1}$ that comes out. Cancelling the product $(p - 1)!$, which $p$ does not divide, leaves $a^{p-1} \equiv 1$.
