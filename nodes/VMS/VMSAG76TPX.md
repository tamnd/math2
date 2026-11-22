---
tag: VMSAG76TPX
kind: proof
name: Proof that reflexive forms are symmetric, alternating or Hermitian up to a scalar
msc: ["15A63"]
topics: [DYAK7YMK7B]
audience: grad
proves: M0G958M917
methods: [0NTF6DMVAP, 0WCP0PVET6, TFQ1845T84]
uses: [0P799D6AMN, 0744CN4MDA, 08ZQAKBKHF, SX9CD5NEPD, 0W44K2VNBD, 8NJ7XY6F1S, 0M856Q1AMZ]
sources:
  - url: https://en.wikipedia.org/wiki/Bilinear_form
    locator: Reflexive bilinear forms and orthogonal vectors
  - url: https://en.wikipedia.org/wiki/Sesquilinear_form
    locator: Reflexivity
---

## Proof

We prove two lemmas on linear forms, and then both parts follow by applying the second lemma to the two "halves" of the form.
Throughout, $\tau$ is a bijective map $F \to F$ that respects sums and products: the identity in part 1, and complex conjugation in part 2.

Lemma A.
Let $\varphi, \psi \colon V \to F$ be linear with $\ker \varphi = \ker \psi$.
Then $\psi = \lambda \varphi$ for some $\lambda \in F$, and $\lambda$ is unique when $\varphi \ne 0$.

1. If $\varphi = 0$, then $\ker \psi = \ker \varphi = V$, so $\psi = 0 = 1 \cdot \varphi$.
2. If $\varphi \ne 0$, pick $w$ with $\varphi(w) \ne 0$, and scale $w$ so that $\varphi(w) = 1$.
3. For every $v \in V$, the vector $v - \varphi(v)\, w$ lies in $\ker \varphi$, since $\varphi(v - \varphi(v)\, w) = \varphi(v) - \varphi(v) = 0$.
4. So it lies in $\ker \psi$, which gives $\psi(v) = \varphi(v)\, \psi(w)$. Put $\lambda = \psi(w)$. It is unique, because $\lambda \varphi = \lambda' \varphi$ evaluated at $w$ gives $\lambda = \lambda'$.

Lemma B.
Let $\Phi, \Psi$ be maps from $V$ to the [[dual space|0M856Q1AMZ]] $V^*$ with $\Phi(u + u') = \Phi(u) + \Phi(u')$ and $\Phi(au) = \tau(a)\, \Phi(u)$, and the same rules for $\Psi$.
Suppose that $\ker \Phi(u) = \ker \Psi(u)$ for every $u \in V$.
Then there is one $\varepsilon \in F$ with $\Psi(u) = \varepsilon\, \Phi(u)$ for every $u \in V$.

5. For each $u$ with $\Phi(u) \ne 0$, Lemma A gives a unique $\lambda(u) \in F$ with $\Psi(u) = \lambda(u)\, \Phi(u)$.
6. Let $\Phi(u)$ and $\Phi(u')$ be linearly independent. Then $\Phi(u + u') = \Phi(u) + \Phi(u') \ne 0$, and
$$\lambda(u + u')\bigl(\Phi(u) + \Phi(u')\bigr) = \Psi(u + u') = \lambda(u)\, \Phi(u) + \lambda(u')\, \Phi(u').$$
Comparing coefficients of the independent vectors gives $\lambda(u) = \lambda(u + u') = \lambda(u')$.
7. Let $\Phi(u) \ne 0$ and $\Phi(u') = \mu\, \Phi(u)$ with $\mu \ne 0$. Since $\tau$ is bijective, pick $a$ with $\tau(a) = \mu$. Then $\Phi(u' - au) = \Phi(u') - \mu\, \Phi(u) = 0$.
8. A form with kernel $V$ is $0$, so the hypothesis gives $\Psi(u' - au) = 0$, that is $\Psi(u') = \mu\, \Psi(u) = \mu \lambda(u)\, \Phi(u) = \lambda(u)\, \Phi(u')$. By uniqueness, $\lambda(u') = \lambda(u)$.
9. Any two vectors $u, u'$ with $\Phi(u) \ne 0 \ne \Phi(u')$ fall under step 6 or step 7, so $\lambda$ takes one value $\varepsilon$ on all of them. If no such $u$ exists, put $\varepsilon = 1$.
10. When $\Phi(u) = 0$, its kernel is $V$, so $\Psi(u) = 0 = \varepsilon\, \Phi(u)$ as well. This proves Lemma B.

Part 1.

11. "If": a [[symmetric|0744CN4MDA]] form gives $B(v, u) = B(u, v)$, and an [[alternating|08ZQAKBKHF]] form is skew-symmetric by the [[relation of the two notions|SX9CD5NEPD]], so it gives $B(v, u) = -B(u, v)$. In both cases $B(u, v) = 0$ implies $B(v, u) = 0$.
12. "Only if": let $B$ be reflexive, and take $\tau$ to be the identity. Put $\Phi(u) = B(u, \cdot)$ and $\Psi(u) = B(\cdot, u)$. Both are linear in $u$, by bilinearity.
13. Reflexivity says that $B(u, v) = 0$ exactly when $B(v, u) = 0$, so $\ker \Phi(u) = \ker \Psi(u)$. Lemma B gives one $\varepsilon$ with $B(v, u) = \varepsilon B(u, v)$ for all $u, v$.
14. If $B = 0$, it is symmetric. Otherwise pick $u, v$ with $B(u, v) \ne 0$; step 13 twice gives $B(u, v) = \varepsilon B(v, u) = \varepsilon^2 B(u, v)$, so $\varepsilon^2 = 1$ and $\varepsilon = \pm 1$.
15. If $\varepsilon = 1$, then $B$ is symmetric. If $\varepsilon = -1$ and $1 + 1 \ne 0$, then $B$ is skew-symmetric, hence alternating by the relation of the two notions. If $\varepsilon = -1$ and $1 + 1 = 0$, then $-1 = 1$ and $B$ is symmetric.

Part 2.

16. "If": let $g = c\,h$ be [[Hermitian|8NJ7XY6F1S]] with $c \ne 0$. If $h(u, v) = 0$, then $g(u, v) = 0$, so $g(v, u) = \overline{g(u, v)} = 0$, and $h(v, u) = c^{-1} g(v, u) = 0$.
17. "Only if": let $h$ be a reflexive [[sesquilinear form|0W44K2VNBD]], and take $\tau$ to be complex conjugation. Put $\Phi(u)(v) = \overline{h(u, v)}$ and $\Psi(u)(v) = h(v, u)$.
18. Each $\Phi(u)$ is linear in $v$, since $h(u, v)$ is conjugate-linear in $v$, and each $\Psi(u)$ is linear in $v$, since $h$ is linear in the first slot.
19. Both maps are additive in $u$, and $\Phi(au) = \bar a\, \Phi(u)$ because $\overline{a\, h(u, v)} = \bar a\, \overline{h(u, v)}$, while $\Psi(au) = \bar a\, \Psi(u)$ because $h(v, au) = \bar a\, h(v, u)$.
20. Reflexivity gives $\ker \Phi(u) = \ker \Psi(u)$, so Lemma B gives one $\delta \in \mathbb{C}$ with $h(v, u) = \delta\, \overline{h(u, v)}$ for all $u, v$.
21. If $h = 0$, take $c = 1$. Otherwise pick $u, v$ with $h(u, v) \ne 0$. Step 20 twice gives
$$h(u, v) = \delta\, \overline{h(v, u)} = \delta\, \overline{\delta\, \overline{h(u, v)}} = \lvert \delta \rvert^2 h(u, v),$$
so $\lvert \delta \rvert = 1$.
22. Write $\delta = e^{i\theta}$ and put $c = e^{-i\theta/2}$. Then $\lvert c \rvert = 1$, $\bar c = c^{-1}$ and $c^2 \delta = 1$.
23. For all $u, v$:
$$c\, h(v, u) = c \delta\, \overline{h(u, v)} = c^2 \delta \cdot \bar c\, \overline{h(u, v)} = \overline{c\, h(u, v)},$$
where the middle step uses $c = c^2 \bar c$, so $c\,h$ is Hermitian.

This proves both parts.

## Idea

For a reflexive form, the two linear forms $B(u, \cdot)$ and $B(\cdot, u)$ vanish on the same vectors, and two linear forms with the same kernel are proportional.
The real work is to show that the factor does not depend on $u$: if it did, adding two vectors would produce a contradiction with linear independence.
So $B(v, u) = \varepsilon B(u, v)$ for one scalar $\varepsilon$, and applying this twice forces $\varepsilon^2 = 1$.
The complex case runs the same way with a conjugation, and the factor of absolute value $1$ is absorbed by a square root.

## Variants

A classical proof of part 1 avoids the dual space.
For all $u, v, w$ the vector $B(u, v)\, w - B(u, w)\, v$ is orthogonal to $u$ from the right, since $B\bigl(u, B(u, v)\, w - B(u, w)\, v\bigr) = B(u, v) B(u, w) - B(u, w) B(u, v) = 0$.
Reflexivity turns this into $B(u, v)\, B(w, u) = B(u, w)\, B(v, u)$ for all $u, v, w$.
With $w = u$ it gives $B(u, u)\bigl(B(u, v) - B(v, u)\bigr) = 0$, and a case analysis on three vectors shows that $B$ is symmetric or $B(u, u) = 0$ for every $u$.
