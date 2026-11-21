---
tag: MXP0K6BDQE
kind: proof
name: Proof of the count of solutions over a finite field
proves: 8QM2Y41P69
methods: [0NTF6DMVAP, SS07J9ZAQ7]
uses: [PDH3HKXWAZ, 0KCQ9Y3QKA]
sources:
  - url: https://en.wikipedia.org/wiki/Finite_field
    locator: lead section
---

## Proof

We count the null space through a basis, and then move the count to the solution set by a translation.
Let $N = \{x \in F^n : Ax = 0\}$ and $S = \{x \in F^n : Ax = b\}$.

1. By [[the structure theorem|PDH3HKXWAZ]], part 5, $N$ is a subspace of dimension $d = n - r$.
2. Choose a [[basis|0KCQ9Y3QKA]] $v_1, \dots, v_d$ of $N$.
3. The map $\phi \colon F^d \to N$, $(t_1, \dots, t_d) \mapsto t_1 v_1 + \dots + t_d v_d$, is surjective, because the basis spans $N$.
4. It is injective, because the basis is linearly independent, so different coefficient tuples give different vectors.
5. So $|N| = |F^d| = q^d$, which proves the claim for $Ax = 0$.
6. If $S$ is empty, the system has no solution.
7. Otherwise choose $p \in S$; then $S = p + N$, by part 3 of the structure theorem.
8. The map $v \mapsto p + v$ is a bijection from $N$ onto $p + N$, with inverse $x \mapsto x - p$.
9. So $|S| = |N| = q^{\,n - r}$.

## Idea

The solutions are a translate of the null space, and a $d$-dimensional space over a field with $q$ elements has $q^d$ vectors.

## Variants

By [[the lemma on systems in RREF|P3HMRQN5KT]], part 4, the solution set of a consistent system is in bijection with $F^k$, where $k = n - r$ is the number of free variables; this gives the count directly.
