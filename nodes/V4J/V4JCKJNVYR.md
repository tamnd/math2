---
tag: V4JCKJNVYR
kind: proof
name: Proof that prime elements are irreducible in an integral domain
msc: [13A05]
proves: 0F0K8DB9TD
uses: [09S3PFBEPM, 0MNHXBSX3M, 052SDEPZH7, 04GNK7K4VP, 019NFGFPR5, 0GJM24EXP9]
sources:
  - url: https://proofwiki.org/wiki/Prime_Element_of_Integral_Domain_is_Irreducible
---

## Proof

Let $R$ be an [[integral domain|09S3PFBEPM]] and let $p \in R$ be a [[prime element|0MNHXBSX3M]].

1. By the definition of a prime element, $p \neq 0$ and $p$ is not a [[unit|019NFGFPR5]]. These are the first two conditions for $p$ to be [[irreducible|052SDEPZH7]].
2. Let $a, b \in R$ with $p = a b$. Then $p$ [[divides|04GNK7K4VP]] $a b$, because $a b = p \cdot 1$.
3. Since $p$ is prime, $p \mid a$ or $p \mid b$. The roles of $a$ and $b$ are symmetric, so we may assume $p \mid a$.
4. Write $a = p c$ with $c \in R$. Then $p \cdot 1 = p = a b = p (c b)$.
5. Since $p \neq 0$, [[cancellation|0GJM24EXP9]] gives $c b = 1$. Since $R$ is commutative, also $b c = 1$, so $b$ is a unit.
6. Thus in every factorization $p = a b$, one factor is a unit. With step 1, $p$ is irreducible.

## Idea

If $p = a b$, then $p$ divides the product $a b$, so $p$ divides one factor, say $a = p c$. Then $p = p c b$, and cancelling $p$ shows that $b$ is a unit.
