---
tag: 9REJRQSXEM
kind: proof
name: Proof of continuity via closed sets
msc: [54C05]
proves: 0B8GPXFSP7
uses: [0CNQXVBHCX, 0SY9ECQ19Q, 0G5AV9Q4RR, 0FGCFY1AZX, 0B1FSS1VZW, 0K67Q60Z8P]
sources:
  - url: https://proofwiki.org/wiki/Continuity_Defined_from_Closed_Sets
---

## Proof

We first show that preimages commute with complements.

1. Let $X$ and $Y$ be [[topological spaces|0CNQXVBHCX]] and let $f \colon X \to Y$.
2. Let $A \subseteq Y$ and $x \in X$. Then $x$ lies in the [[preimage|0FGCFY1AZX]] $f^{-1}(Y \setminus A)$ if and only if $f(x) \notin A$.
3. This holds if and only if $x \notin f^{-1}(A)$. So $f^{-1}(Y \setminus A) = X \setminus f^{-1}(A)$, with $X \setminus f^{-1}(A)$ the [[complement|0B1FSS1VZW]].
4. Suppose $f$ is [[continuous|0SY9ECQ19Q]], and let $F$ be a [[closed set|0G5AV9Q4RR]] of $Y$.
5. By the definition of a closed set, $Y \setminus F$ is open. By continuity, $f^{-1}(Y \setminus F)$ is open in $X$.
6. By step 3, $X \setminus f^{-1}(F)$ is open. By the definition of a closed set, $f^{-1}(F)$ is closed.
7. Conversely, suppose that each closed $F$ of $Y$ has a closed preimage. Let $V$ be open in $Y$.
8. By [[complement of an open set is closed|0K67Q60Z8P]], $Y \setminus V$ is closed in $Y$. By hypothesis, $f^{-1}(Y \setminus V)$ is closed in $X$.
9. By step 3, $X \setminus f^{-1}(V)$ is closed. By the same result, $f^{-1}(V)$ is open.
10. As $V$ was arbitrary, $f$ is continuous.

## Idea

Closed sets are the complements of open sets. Taking preimages commutes with taking complements. So the condition on open sets and the condition on closed sets say the same thing.
