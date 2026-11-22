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

We split each vector into a part in the kernel and a multiple of one fixed vector, and we prove the five parts in order.

*Part 1.*
Let $f \ne 0$.

1. There is a vector $v \in V$ with $f(v) \ne 0$, since $f$ is not the zero form; we fix such a $v$.
2. The [[kernel|02YFME3RGW]] $\ker f$ is a [[subspace|0EPTJA5QV4]] of $V$, as the kernel of every linear map is, and it is not $V$, because $v \notin \ker f$.
3. Let $u \in V$ and put $a = f(u) / f(v)$, which makes sense because $f(v) \ne 0$ and $F$ is a field.
4. By linearity, $f(u - av) = f(u) - a f(v) = f(u) - f(u) = 0$, so $u - av \in \ker f$.
5. So $u = (u - av) + av$ lies in $\ker f + Fv$, and since $u$ was arbitrary, $V = \ker f + Fv$.
6. The sum is direct: if $av \in \ker f$, then $a f(v) = 0$, and $f(v) \ne 0$ gives $a = 0$, so $\ker f \cap Fv = \{0\}$.
7. Steps 2, 5 and 6 show that $\ker f$ is a hyperplane and that $V = \ker f \oplus Fv$.

*Part 2.*
Let $H$ be a hyperplane, with $V = H + Fv$.

8. The vector $v$ is not in $H$, because otherwise $H + Fv = H$, which is not $V$.
9. By the choice of $v$, each $u \in V$ can be written as $u = h + av$ with $h \in H$ and $a \in F$.
10. The scalar $a$ is unique: if $h + av = h' + a'v$ with $a \ne a'$, then $v = (a - a')^{-1}(h' - h) \in H$, which contradicts step 8.
11. So the rule $f(h + av) = a$ defines a map $f \colon V \to F$.
12. This map is linear, because $(h + av) + (h' + a'v) = (h + h') + (a + a')v$ and $c(h + av) = ch + (ca)v$ give $f(u + u') = f(u) + f(u')$ and $f(cu) = c f(u)$.
13. We have $f(v) = 1$, so $f \ne 0$.
14. Also $f(h + av) = 0$ exactly when $a = 0$, that is, exactly when the vector is $h \in H$, so $\ker f = H$.

*Part 3.*
Let $f, g \in V^*$ with $f \ne 0$ and $\ker f \subseteq \ker g$.

15. Choose $v$ with $f(v) \ne 0$ and put $c = g(v) / f(v)$.
16. For $u \in V$, steps 3 and 4 give $u = w + av$ with $w \in \ker f$ and $a = f(u) / f(v)$.
17. By the hypothesis, $w \in \ker g$, so linearity gives $g(u) = g(w) + a g(v) = a g(v)$.
18. So $g(u) = f(u) \, g(v) / f(v) = c f(u)$, and since $u$ was arbitrary, $g = cf$.
19. If also $g = c'f$, then evaluation at $v$ gives $c f(v) = c' f(v)$, and $f(v) \ne 0$ gives $c = c'$.

*Part 4.*
Let $f, g$ be nonzero with $\ker f = \ker g$.

20. Part 3 applies, since $\ker f \subseteq \ker g$, so $g = cf$ for exactly one $c \in F$.
21. If $c = 0$, then $g = 0$, which contradicts $g \ne 0$, so $c \ne 0$.

*Part 5.*
Let $\dim V = n$ with $n \ge 1$.

22. Let $H$ be a hyperplane with $V = H + Fv$; steps 8 and 10 show that $v \ne 0$ and $H \cap Fv = \{0\}$.
23. The [[dimension formula for sums|06HTJNCMPA]] gives $n = \dim H + \dim Fv - \dim(H \cap Fv) = \dim H + 1 - 0$, so $\dim H = n - 1$.
24. Conversely, let $H$ be a subspace with $\dim H = n - 1$; then $H \ne V$, since the dimensions differ, so some $v \in V$ is not in $H$.
25. Then $H \cap Fv = \{0\}$, because a nonzero multiple $av$ in $H$ would give $v = a^{-1}(av) \in H$.
26. The dimension formula gives $\dim(H + Fv) = (n - 1) + 1 - 0 = n$.
27. A subspace of dimension $n$ of a space of dimension $n$ is the whole space, by the theorem on the [[dimension of a subspace|0QW084460E]], so $H + Fv = V$ and $H$ is a hyperplane.

This proves the five parts of the theorem.

## Idea

Fix one vector $v$ with $f(v) \ne 0$.
Every vector $u$ then splits as a part in $\ker f$ plus the multiple $\frac{f(u)}{f(v)} v$.
So the whole form is known once we know its kernel and the one number $f(v)$, and this gives both the hyperplane property and the uniqueness up to a scalar.
For the way back, start with a hyperplane $H$ and a vector $v$ outside it, and read off the coefficient of $v$ in $u = h + av$; that coefficient is a form with kernel $H$.

## Variants

In finite dimension, part 1 also follows from the [[rank-nullity theorem|0W4FSW1TVB]].
A nonzero form has image $F$, of dimension $1$, so its kernel has dimension $n - 1$, and part 5 then makes it a hyperplane.

Part 3 also follows from the first isomorphism theorem.
The form $g$ vanishes on $\ker f$, so it factors through the quotient $V / \ker f$, which is isomorphic to $F$ by $f$.
Every linear map $F \to F$ is multiplication by a scalar, and this scalar is the $c$ of part 3.
