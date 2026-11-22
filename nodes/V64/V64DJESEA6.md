---
tag: V64DJESEA6
kind: proof
name: Proof of the generalized pigeonhole principle
msc: ["05A05"]
topics: [GB14W4SYPK]
audience: school
proves: 0BY7GN3449
uses: [05099E1NMJ, 0EE2V3CHFK, 0EA4XFB0EY]
methods: [0J0XBKG64S]
sources:
  - url: https://proofwiki.org/wiki/Dirichlet's_Box_Principle
  - url: https://en.wikipedia.org/wiki/Pigeonhole_principle
    locator: Strong form
---

## Proof

We prove the main form by [[contradiction|0J0XBKG64S]], adding up the sizes of the fibers, and then we derive the ceiling form and the weighted form.

Main form.

1. Let $A$ and $B$ be finite sets, let $f : A \to B$ be a function, and let $n$ be a natural number with $n \cdot |B| < |A|$.
2. For $b \in B$, write $A_b = f^{-1}(b) = \{ a \in A : f(a) = b \}$.
   Each $A_b$ is a subset of the finite set $A$, so it is finite.
3. Suppose, for a contradiction, that $|A_b| \le n$ for every $b \in B$.
4. The sets $A_b$ for $b \in B$ are pairwise disjoint, because $a \in A_b \cap A_{b'}$ gives $b = f(a) = b'$.
5. Their union is $A$, because each $a \in A$ lies in $A_{f(a)}$.
6. The [[rule of sum|0EE2V3CHFK]], applied to the $|B|$ pairwise disjoint finite sets $A_b$, gives
   $$|A| = \sum_{b \in B} |A_b|.$$
7. By step 3, each term of this sum is at most $n$, and there are $|B|$ terms, so $|A| \le n \cdot |B|$.
8. This contradicts the hypothesis $n \cdot |B| < |A|$ of step 1.
9. Hence some $b \in B$ has $|f^{-1}(b)| > n$, which means that its fiber has more than $n$ elements, in the sense of [[cardinality|05099E1NMJ]].

Ceiling form.

10. Let $N$ objects go into $k \geq 1$ boxes.
    If $N = 0$, then $\lceil N / k \rceil = 0$, and each box receives at least $0$ objects, so the claim holds.
11. Let $N \geq 1$, and let $n = \lceil N / k \rceil - 1$.
    Since $N / k > 0$, the [[ceiling|0EA4XFB0EY]] satisfies $\lceil N / k \rceil \geq 1$, so $n$ is a natural number.
12. The ceiling is the least integer $\geq N/k$, so the integer $n$ is less than $N / k$, and $n \cdot k < N$.
13. The main form gives a box with more than $n$ objects, which means at least $n + 1 = \lceil N / k \rceil$ objects.

Weighted form.

14. Let $q_1, \dots, q_k$ be positive integers, and let $q_1 + \cdots + q_k - k + 1$ objects go into boxes $1, \dots, k$.
    Let $m_i$ be the number of objects in box $i$.
15. Suppose that $m_i \le q_i - 1$ for each $i$.
    Then the total is
    $$m_1 + \cdots + m_k \le (q_1 - 1) + \cdots + (q_k - 1) = q_1 + \cdots + q_k - k.$$
16. This total is less than the number $q_1 + \cdots + q_k - k + 1$ of objects, which is a contradiction.
    So $m_i \geq q_i$ for some $i$.

## Idea

The fibers of $f$ cut $A$ into $|B|$ disjoint pieces, so their sizes add up to $|A|$.
If every piece had at most $n$ elements, the total would be at most $n \cdot |B|$, which is too small.
The ceiling form picks the largest $n$ for which the main form applies.
The weighted form uses the same sum with a different upper bound for each piece.

## Variants

The main form also follows from the weighted form with $q_1 = \cdots = q_k = n + 1$, because then the number of objects is $q_1 + \cdots + q_k - k + 1 = nk + 1$.

An averaging proof is shorter to say.
The mean of the $|B|$ numbers $|A_b|$ is $|A| / |B|$, which is greater than $n$ by hypothesis.
The largest of finitely many numbers is at least their mean, so some $|A_b|$ is greater than $n$.
