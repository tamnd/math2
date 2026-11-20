---
tag: BATZQ1TY5Z
kind: proof
name: Proof of the theorem on hyperplanes and linear forms
msc: ["15A03", "15A04"]
topics: [9K7FFF26QR]
audience: ug2
proves: XR0EQN0H8T
methods: [0NTF6DMVAP, 01XM7JEKHY]
uses: [0RT96J4D3H, 02YFME3RGW, 0EPTJA5QV4, 06HTJNCMPA, 0QW084460E]
sources:
  - url: https://en.wikipedia.org/wiki/Linear_form
    locator: Hyperplanes and maximal subspaces
---

## Proof

We prove the five parts in order.

*Part 1.*

1. Let $f \ne 0$. Then there is $v \in V$ with $f(v) \ne 0$. Fix such a $v$.
2. The [[kernel|02YFME3RGW]] $\ker f$ is a [[subspace|0EPTJA5QV4]] of $V$, as the kernel of every linear map is. It is not $V$, because $v \notin \ker f$.
3. Let $u \in V$ and put $a = f(u) / f(v)$. This is allowed, because $f(v) \ne 0$ and $F$ is a field.
4. Then $f(u - av) = f(u) - a f(v) = f(u) - f(u) = 0$, by linearity. So $u - av \in \ker f$.
5. So $u = (u - av) + av$ lies in $\ker f + Fv$. Since $u$ was arbitrary, $V = \ker f + Fv$.
6. The sum is direct. If $av \in \ker f$, then $a f(v) = 0$, and $f(v) \ne 0$ gives $a = 0$. So $\ker f \cap Fv = \set{0}$.
7. By steps 2, 5 and 6, $\ker f$ is a hyperplane and $V = \ker f \oplus Fv$.

*Part 2.*

8. Let $H$ be a hyperplane, with $V = H + Fv$. Then $v \notin H$, because otherwise $H + Fv = H \ne V$.
9. Each $u \in V$ has the form $u = h + av$ with $h \in H$ and $a \in F$, by the choice of $v$.
10. The scalar $a$ is unique. If $h + av = h' + a'v$, then $(a - a')v = h' - h \in H$. If $a \ne a'$, then $v = (a - a')^{-1}(h' - h) \in H$, which contradicts step 8. So $a = a'$.
11. Define $f(u) = a$ for $u = h + av$. This is well defined by step 10.
12. The map $f$ is linear. If $u = h + av$ and $u' = h' + a'v$, then $u + u' = (h + h') + (a + a')v$ and $cu = ch + (ca)v$. So $f(u + u') = a + a'$ and $f(cu) = ca$.
13. We have $f(v) = 1$, so $f \ne 0$. Also $f(u) = 0$ exactly when $u = h + 0v = h \in H$. So $\ker f = H$.

*Part 3.*

14. Let $f, g \in V^*$ with $f \ne 0$ and $\ker f \subseteq \ker g$. Choose $v$ with $f(v) \ne 0$, and put $c = g(v) / f(v)$.
15. Let $u \in V$. By steps 3 and 4, $u = w + av$ with $w = u - av \in \ker f$ and $a = f(u)/f(v)$.
16. By the hypothesis, $w \in \ker g$, so $g(w) = 0$. By linearity, $g(u) = g(w) + a g(v) = a g(v)$.
17. So $g(u) = f(u)\, g(v) / f(v) = c f(u)$. Since $u$ was arbitrary, $g = cf$.
18. Uniqueness: if $g = cf = c'f$, then evaluation at $v$ gives $c f(v) = c' f(v)$. Since $f(v) \ne 0$, we get $c = c'$.

*Part 4.*

19. Let $f, g$ be nonzero with $\ker f = \ker g$. By part 3, $g = cf$ for some $c \in F$.
20. If $c = 0$, then $g = 0$, which contradicts the hypothesis $g \ne 0$. So $c \ne 0$.

*Part 5.*

21. Let $\dim V = n$ and let $H$ be a hyperplane, with $V = H \oplus Fv$ as in steps 8 and 10.
22. By the [[dimension formula for sums|06HTJNCMPA]], $n = \dim H + \dim Fv - \dim(H \cap Fv) = \dim H + 1 - 0$. So $\dim H = n - 1$.
23. Conversely, let $H$ be a subspace with $\dim H = n - 1$. Then $H \ne V$, since the dimensions differ, so there is $v \in V$ with $v \notin H$.
24. Then $H \cap Fv = \set{0}$, as in step 10. The dimension formula gives $\dim(H + Fv) = (n - 1) + 1 - 0 = n$.
25. A subspace of dimension $n$ of a space of dimension $n$ is the whole space, by the theorem on the [[dimension of a subspace|0QW084460E]]. So $H + Fv = V$, and $H$ is a hyperplane.

This proves the five parts of the theorem.

## Idea

A nonzero form $f$ splits each vector $u$ into a part in $\ker f$ and a multiple of one fixed vector $v$ with $f(v) \ne 0$.
The multiple is $f(u)/f(v)$, so the whole form is known from $\ker f$ and the single number $f(v)$.
This gives both the hyperplane property and the uniqueness up to a scalar.
Conversely, the coefficient of $v$ in $u = h + av$ defines a form with kernel $H$.

## Variants

- In finite dimension, part 1 follows from the [[rank-nullity theorem|0W4FSW1TVB]]: a nonzero form has image $F$, so its kernel has dimension $n - 1$.
- Part 3 also follows from the first isomorphism theorem: $g$ vanishes on $\ker f$, so it factors through $V / \ker f \cong F$, and every linear map $F \to F$ is multiplication by a scalar.
