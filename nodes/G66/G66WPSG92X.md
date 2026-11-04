---
tag: G66WPSG92X
kind: proof
name: Proof of the Chinese remainder theorem for rings
msc: [13A15]
proves: 0W97J8QED7
uses: [0GYGHKX834, 0MYSA6MYNA, 0MDJP82TEH, 0VFW4Y69BT, 0MNZCN4BQK, 0GGE0Z0JQ1, 0AAHE7GEW6, 0ZMYX7GMH0, 0B6QC0C0G1]
sources:
  - url: https://proofwiki.org/wiki/Chinese_Remainder_Theorem_(Commutative_Algebra)
---

## Proof

1. Let $R$ be a [[commutative ring|0GYGHKX834]], and let $I_1, \dots, I_n$ be [[ideals|0MYSA6MYNA]] of $R$ that are pairwise [[coprime|0MDJP82TEH]]. Put $K = I_1 \cap \dots \cap I_n$ and let $P = R/I_1 \times \dots \times R/I_n$ be the [[product of the rings|0MNZCN4BQK]] $R/I_k$.
2. For an ideal $L$ and $a, b \in R$, $a + L = b + L$ if and only if $a - b \in L$. Indeed, if the cosets are equal, then $a \in b + L$. If $a - b = x \in L$, then $a + y = b + (x + y)$ and $b + y = a + (y - x)$ for each $y \in L$.
3. Define $\varphi \colon R \to P$ by $\varphi(a) = (a + I_1, \dots, a + I_n)$. The operations of $P$ and of each [[quotient ring|0VFW4Y69BT]] $R/I_k$ are componentwise and come from $R$. So $\varphi$ preserves sums and products, and $\varphi(1) = (1 + I_1, \dots, 1 + I_n)$ is the identity of $P$. Thus $\varphi$ is a [[ring homomorphism|0GGE0Z0JQ1]].
4. By step 2, $\varphi(a) = 0$ if and only if $a \in I_k$ for every $k$. So the [[kernel|0AAHE7GEW6]] of $\varphi$ is $K$.
5. Fix $k$. We build $e_k \in R$ with $e_k - 1 \in I_k$ and $e_k \in I_j$ for all $j \neq k$. If $n = 1$, take $e_1 = 1$.
6. Let $n \ge 2$. For each $j \neq k$, the ideals $I_k$ and $I_j$ are coprime. So there are $u_j \in I_k$ and $v_j \in I_j$ with $u_j + v_j = 1$. Put $e_k = \prod_{j \neq k} v_j$.
7. For $j \neq k$, the product $e_k$ has the factor $v_j \in I_j$. Since $I_j$ is an ideal and $R$ is commutative, $e_k \in I_j$.
8. For each $j \neq k$, $v_j - 1 = -u_j \in I_k$, so $v_j + I_k = 1 + I_k$ by step 2. Multiplying in $R/I_k$ gives $e_k + I_k = \prod_{j \neq k} (v_j + I_k) = 1 + I_k$.
9. Now let $(r_1 + I_1, \dots, r_n + I_n)$ be any element of $P$, with $r_1, \dots, r_n \in R$. Put $a = r_1 e_1 + \dots + r_n e_n$.
10. Fix $k$. In $R/I_k$, $a + I_k = \sum_{j} (r_j + I_k)(e_j + I_k)$. By step 7, $e_j + I_k = 0 + I_k$ for $j \neq k$. By step 8, $e_k + I_k = 1 + I_k$. So $a + I_k = r_k + I_k$.
11. Thus $\varphi(a) = (r_1 + I_1, \dots, r_n + I_n)$, and $\varphi$ is surjective.
12. By the [[first isomorphism theorem|0ZMYX7GMH0]] applied to $\varphi$, with steps 4 and 11, the map $R/K \to P$, $a + K \mapsto \varphi(a) = (a + I_1, \dots, a + I_n)$, is a [[ring isomorphism|0B6QC0C0G1]].

## Idea

The map $a \mapsto (a + I_1, \dots, a + I_n)$ has kernel $I_1 \cap \dots \cap I_n$, so only surjectivity needs work. Coprimality gives, for each $k$, an element that is $1$ modulo $I_k$ and $0$ modulo every other $I_j$. Combinations of these elements hit every target, just as in the integer version.
