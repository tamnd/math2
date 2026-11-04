---
tag: FAB7YZEECX
kind: proof
name: Proof that R/M is a field iff M is maximal
msc: [13A15]
proves: 0WD3SE7S1X
uses: [0GYGHKX834, 0MYSA6MYNA, 0VFW4Y69BT, 0QA8CHH8MG, 09J6KGT65G]
sources:
  - url: https://proofwiki.org/wiki/Maximal_Ideal_iff_Quotient_Ring_is_Field
---

## Proof

We prove both directions directly.

1. Let $R$ be a [[commutative ring|0GYGHKX834]] and let $M$ be an [[ideal|0MYSA6MYNA]] of $R$. The [[quotient ring|0VFW4Y69BT]] $R/M$ is commutative, since $(a + M)(b + M) = a b + M = (b + M)(a + M)$.
2. For $a, b \in R$, $a + M = b + M$ if and only if $a - b \in M$. Indeed, if the cosets are equal, then $a \in b + M$. If $a - b = x \in M$, then $a + y = b + (x + y)$ and $b + y = a + (y - x)$ for each $y \in M$.
3. We have $1 + M \neq 0 + M$ if and only if $M \neq R$. By step 2, $1 + M = 0 + M$ means $1 \in M$. If $1 \in M$, then $r = r \cdot 1 \in M$ for all $r$, so $M = R$. If $M = R$, then $1 \in M$.
4. Suppose first that $M$ is a [[maximal ideal|09J6KGT65G]]. Then $M \neq R$, so $1 + M \neq 0 + M$ by step 3.
5. Let $a + M \neq 0 + M$. Then $a \notin M$ by step 2. Put $L = \set{m + r a : m \in M, r \in R}$.
6. The set $L$ is an ideal of $R$. It contains $0 = 0 + 0 a$. It is closed under differences, since $(m + r a) - (m' + r' a) = (m - m') + (r - r') a$. For $s \in R$, $s (m + r a) = s m + (s r) a \in L$, since $s m \in M$.
7. Taking $r = 0$ shows $M \subseteq L$. Taking $m = 0$ and $r = 1$ shows $a \in L$. Since $a \notin M$, $L \neq M$.
8. By maximality of $M$, $L = R$. So $1 = m + r a$ for some $m \in M$ and $r \in R$.
9. Then $r a - 1 = -m \in M$. By step 2, $(r + M)(a + M) = r a + M = 1 + M$. So $a + M$ has an inverse.
10. By steps 1, 4 and 9, $R/M$ is a [[field|0QA8CHH8MG]].
11. Conversely, suppose that $R/M$ is a field. Then $1 + M \neq 0 + M$, so $M \neq R$ by step 3.
12. Let $L$ be an ideal of $R$ with $M \subseteq L$ and $L \neq M$. Choose $a \in L$ with $a \notin M$. Then $a + M \neq 0 + M$ by step 2.
13. Since $R/M$ is a field, there is $b \in R$ with $(a + M)(b + M) = 1 + M$, that is, $a b + M = 1 + M$. By step 2, $1 - a b \in M \subseteq L$.
14. Also $a b = b a \in L$, since $L$ is an ideal and $a \in L$. So $1 = (1 - a b) + a b \in L$.
15. Then $r = r \cdot 1 \in L$ for every $r \in R$, so $L = R$.
16. By steps 11 to 15, every ideal containing $M$ equals $M$ or $R$, and $M \neq R$. So $M$ is maximal.

## Idea

To invert $a + M$, enlarge $M$ by the multiples of $a$. Maximality forces this larger ideal to contain $1$, which writes $1$ as a multiple of $a$ modulo $M$. Conversely, an inverse modulo $M$ puts $1$ into any ideal that strictly contains $M$.
