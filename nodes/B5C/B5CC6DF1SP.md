---
tag: B5CC6DF1SP
kind: proof
name: Proof that a finite integral domain is a field
msc: [13G05]
proves: 0EBE031B8E
uses: [09S3PFBEPM, 0QA8CHH8MG, 0GJM24EXP9, 0HGVCWQGY3, 0PVG1CRAJN, 0XKH881BZ7]
sources:
  - url: https://proofwiki.org/wiki/Finite_Integral_Domain_is_Galois_Field
---

## Proof

1. Let $R$ be an [[integral domain|09S3PFBEPM]] with finitely many elements. Then $R$ is commutative and $1 \neq 0$ in $R$.
2. By the definition of a [[field|0QA8CHH8MG]], it remains to show that each $a \in R$ with $a \neq 0$ has some $b \in R$ with $a b = 1$.
3. Fix $a \in R$ with $a \neq 0$. Define $m \colon R \to R$ by $m(x) = a x$.
4. The map $m$ is [[injective|0PVG1CRAJN]]. Indeed, if $a x = a y$, then $x = y$ by [[cancellation in an integral domain|0GJM24EXP9]], since $a \neq 0$.
5. We claim that $m$ is [[surjective|0XKH881BZ7]]. Suppose not, and let $B = m(R)$ be its image. Then $B$ is a proper subset of the finite set $R$, so $\abs{B} < \abs{R}$.
6. Consider $m$ as a function from $R$ to $B$. Since $\abs{R} > \abs{B}$, the [[pigeonhole principle|0HGVCWQGY3]] gives $x \neq y$ in $R$ with $m(x) = m(y)$.
7. This contradicts step 4. So $m$ is surjective.
8. In particular, $1 = m(b) = a b$ for some $b \in R$.
9. So every nonzero element of $R$ has an inverse, and $R$ is a field.

## Idea

Multiplication by a fixed nonzero $a$ is injective, because one can cancel $a$. On a finite set, an injective map to itself is also surjective. So $1$ is a multiple $a b$ of $a$, and $b$ is the inverse of $a$.
