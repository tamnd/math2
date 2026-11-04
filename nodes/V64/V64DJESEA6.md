---
tag: V64DJESEA6
kind: proof
name: Proof of the generalized pigeonhole principle
msc: [05A05]
proves: 0BY7GN3449
uses: [05099E1NMJ, 0EE2V3CHFK]
sources:
  - url: https://proofwiki.org/wiki/Dirichlet's_Box_Principle
---

## Proof

We argue by contradiction.

1. Let $A$ and $B$ be finite sets, let $f : A \to B$ be a function, and let $n$ be a natural number with $|B| \cdot n < |A|$.
2. For $b \in B$, write $A_b = f^{-1}(b) = \set{a \in A : f(a) = b}$. Each $A_b$ is a subset of the finite set $A$, so it is finite.
3. Suppose, for a contradiction, that $|A_b| \le n$ for every $b \in B$.
4. The sets $A_b$ for $b \in B$ are pairwise disjoint. Indeed, if $a \in A_b \cap A_{b'}$, then $b = f(a) = b'$.
5. Their union is $A$, because each $a \in A$ lies in $A_{f(a)}$.
6. By the [[rule of sum|0EE2V3CHFK]], applied to the $|B|$ pairwise disjoint finite sets $A_b$, we get $|A| = \sum_{b \in B} |A_b|$.
7. By step 3, each term of this sum is at most $n$, and there are $|B|$ terms. So $|A| \le |B| \cdot n$.
8. This contradicts the hypothesis $|B| \cdot n < |A|$ of step 1.
9. Hence some $b \in B$ has $|f^{-1}(b)| > n$, that is, its fibre has [[cardinality|05099E1NMJ]] greater than $n$.

## Idea

The fibres of $f$ split $A$ into $|B|$ disjoint pieces, so their sizes add up to $|A|$. If every piece had at most $n$ elements, the total would be at most $|B| \cdot n$, which is too small.
