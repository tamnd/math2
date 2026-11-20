---
tag: ~f9eacaad
kind: proof
name: Proof that reflexive forms are symmetric, alternating or Hermitian up to a scalar
msc: ["15A63"]
topics: [DYAK7YMK7B]
audience: grad
proves: ~b3103bb5
methods: [0NTF6DMVAP, 0WCP0PVET6, TFQ1845T84]
uses: [0P799D6AMN, 0744CN4MDA, 08ZQAKBKHF, ~205a4a20, 0W44K2VNBD, 8NJ7XY6F1S, 0M856Q1AMZ]
sources:
  - url: https://en.wikipedia.org/wiki/Bilinear_form
    locator: Reflexive bilinear forms and orthogonal vectors
  - url: https://en.wikipedia.org/wiki/Sesquilinear_form
    locator: Reflexivity
---

## Proof

We first prove a lemma on linear forms, then part 1, then part 2.

Lemma.
Let $\varphi, \psi \colon V \to F$ be linear with $\ker \varphi = \ker \psi$.
Then $\psi = \lambda \varphi$ for some $\lambda \in F$.

1. If $\varphi = 0$, then $\ker \psi = V$, so $\psi = 0 = 1 \cdot \varphi$.
2. If $\varphi \neq 0$, pick $w$ with $\varphi(w) \neq 0$, and scale $w$ so that $\varphi(w) = 1$.
3. For $v \in V$, the vector $v - \varphi(v) w$ lies in $\ker \varphi$, since $\varphi(v - \varphi(v) w) = \varphi(v) - \varphi(v) = 0$.
4. So it lies in $\ker \psi$, and $\psi(v) = \varphi(v) \psi(w)$. Put $\lambda = \psi(w)$.

Part 1, "if". 

5. If $B$ is [[symmetric|0744CN4MDA]], then $B(u, v) = 0$ gives $B(v, u) = B(u, v) = 0$.
6. If $B$ is [[alternating|08ZQAKBKHF]], then $B$ is skew-symmetric by the [[relation of the two notions|~205a4a20]]. So $B(u, v) = 0$ gives $B(v, u) = -B(u, v) = 0$.

Part 1, "only if".
Let $B$ be reflexive, and define $B^t(u, v) = B(v, u)$.
It is again a [[bilinear form|0P799D6AMN]].

7. Fix $u$. The maps $\varphi_u = B(u, \cdot)$ and $\psi_u = B^t(u, \cdot) = B(\cdot, u)$ are linear forms on $V$, so they lie in the [[dual space|0M856Q1AMZ]].
8. By reflexivity, $B(u, v) = 0$ exactly when $B(v, u) = 0$. So $\ker \varphi_u = \ker \psi_u$.
9. By the lemma, $\psi_u = \lambda(u) \varphi_u$ for a scalar $\lambda(u)$. When $\varphi_u = 0$ we choose $\lambda(u)$ later, since any value works.
10. Let $u, u'$ be vectors with $\varphi_u$ and $\varphi_{u'}$ linearly independent. By linearity in the first slot, $\varphi_{u + u'} = \varphi_u + \varphi_{u'}$ and $\psi_{u + u'} = \psi_u + \psi_{u'}$.
11. Step 9 for $u + u'$ gives $\lambda(u + u')(\varphi_u + \varphi_{u'}) = \lambda(u)\varphi_u + \lambda(u')\varphi_{u'}$. By independence, $\lambda(u) = \lambda(u + u') = \lambda(u')$.
12. Let $u, u'$ be vectors with $\varphi_u \neq 0$ and $\varphi_{u'} = \mu \varphi_u$, $\mu \neq 0$. Then $\varphi_{u' - \mu u} = 0$, so $\psi_{u' - \mu u} = 0$ by step 8.
13. Linearity gives $\psi_{u'} = \mu \psi_u = \mu \lambda(u) \varphi_u = \lambda(u) \varphi_{u'}$. Since $\varphi_{u'} \neq 0$, the factor $\lambda(u')$ is unique, so $\lambda(u') = \lambda(u)$.
14. By steps 11 and 13, all $u$ with $\varphi_u \neq 0$ have the same $\lambda(u)$. Call it $\varepsilon$, and use $\varepsilon$ also when $\varphi_u = 0$.
15. So $B(v, u) = \varepsilon B(u, v)$ for all $u, v$. If $B = 0$, then $B$ is symmetric and we are done.
16. If $B \neq 0$, pick $u, v$ with $B(u, v) \neq 0$. Step 15 twice gives $B(u, v) = \varepsilon B(v, u) = \varepsilon^2 B(u, v)$, so $\varepsilon^2 = 1$ and $\varepsilon = \pm 1$.
17. Case $\varepsilon = 1$: $B$ is symmetric. Case $\varepsilon = -1$: $B$ is skew-symmetric.
18. In the second case, if $\operatorname{char} F \neq 2$, then $B$ is alternating, by the relation of the two notions. If $\operatorname{char} F = 2$, then $-1 = 1$ and $B$ is symmetric.

Part 2.
Let $h$ be a [[sesquilinear form|0W44K2VNBD]] on the complex space $V$.

19. "If": let $g = ch$ be [[Hermitian|8NJ7XY6F1S]] with $c \neq 0$. If $h(u, v) = 0$, then $g(u, v) = 0$, so $g(v, u) = \overline{g(u, v)} = 0$, and $h(v, u) = 0$.
20. "Only if": define $h^*(u, v) = \overline{h(v, u)}$. It is linear in $u$ and conjugate-linear in $v$, since conjugation turns $\bar a$ into $a$.
21. Fix $u$. The maps $v \mapsto \overline{h(u, v)}$ and $v \mapsto \overline{h^*(u, v)} = h(v, u)$ are linear. By reflexivity they have the same kernel.
22. Steps 9 to 14, applied to these linear maps, give one scalar $\delta$ with $\overline{h^*(u, v)} = \delta \, \overline{h(u, v)}$ for all $u, v$. These steps use only that both maps are additive in $u$ and respect scalars up to a conjugation.
23. So $h(v, u) = \delta \, \overline{h(u, v)}$ for all $u, v$. If $h = 0$, take $c = 1$.
24. If $h \neq 0$, pick $u, v$ with $h(u, v) \neq 0$. Step 23 twice gives $h(u, v) = \delta \overline{\delta \overline{h(u, v)}} = \abs{\delta}^2 h(u, v)$, so $\abs{\delta} = 1$.
25. Write $\delta = e^{i\theta}$ and put $c = e^{-i\theta/2}$, so $\abs{c} = 1$ and $c / \bar c = c^2 = \bar\delta$.
26. Then $ch(v, u) = c \delta \overline{h(u, v)} = (c\delta / \bar c) \, \overline{c h(u, v)} = \overline{c h(u, v)}$, since $c\delta/\bar c = \bar\delta \delta = 1$. So $ch$ is Hermitian.

This proves both parts.

## Idea

For a reflexive form, the two linear forms $B(u, \cdot)$ and $B(\cdot, u)$ have the same kernel, so they are proportional.
A short argument with sums shows that the factor does not depend on $u$.
So $B(v, u) = \varepsilon B(u, v)$ with $\varepsilon^2 = 1$, which gives symmetry or skew-symmetry.
The complex case is the same, with a conjugation and a factor of absolute value $1$.

## Variants

A classical proof of part 1 uses the identity $B(u, B(u, v) w - B(u, w) v) = 0$.
Reflexivity turns it into $B(u, v) B(w, u) = B(u, w) B(v, u)$ for all $u, v, w$.
With $w = u$ this gives $B(u, u)\bigl(B(u, v) - B(v, u)\bigr) = 0$.
If $B$ is neither symmetric nor alternating, a case analysis with three vectors then leads to a contradiction.
