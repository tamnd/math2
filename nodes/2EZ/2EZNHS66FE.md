---
tag: 2EZNHS66FE
kind: proof
name: Proof of the kernel and image of the dual map
msc: ["15A04"]
topics: [9K7FFF26QR]
audience: ug2
proves: 7FA499AW3T
methods: [0NTF6DMVAP, 01XM7JEKHY]
uses: [0C2TQMW5A1, 0R6M158SQ9, 02YFME3RGW, 0JB228DCWB, 00MS9VMQ9Z, 0CRMGPAH83, 0M4SXE5WW3, 0R8X9XA83A, 06Q1EFVH0Q, 0W4FSW1TVB, 0W6M3PSD08]
sources:
  - book: isbn:9783031410253
    locator: Section 3F
---

## Proof

We first prove two facts about forms on a subspace, then get part 1 from the definitions, part 2 from the extension of forms, and parts 3 to 5 from parts 1 and 2.
Throughout, $S$ is a subspace of a vector space $X$ over $F$.

Fact E (extension): every linear form $\chi_0 \colon S \to F$ extends to a linear form $\chi \colon X \to F$.

1. Choose a basis $C$ of $S$, which exists because [[every vector space has a basis|00MS9VMQ9Z]].
2. The family $C$ is [[linearly independent|0CRMGPAH83]] in $X$, so it [[extends to a basis|0M4SXE5WW3]] $D \supseteq C$ of $X$.
3. Since [[a linear map may take any values on a basis|0R8X9XA83A]], there is $\chi \in X^*$ with $\chi(c) = \chi_0(c)$ for $c \in C$ and $\chi(d) = 0$ for $d \in D \setminus C$.
4. The forms $\chi|_S$ and $\chi_0$ agree on the basis $C$ of $S$, so $\chi|_S = \chi_0$ by the uniqueness part of the same theorem.

Fact S (separation): if $x \in X$ and $x \notin S$, then some $\varphi \in X^*$ has $\varphi|_S = 0$ and $\varphi(x) = 1$.

5. Let $S' = S + Fx$. Each element of $S'$ is $s + ax$ with $s \in S$ and $a \in F$, and $a$ is unique: if $s + ax = t + bx$ with $a \ne b$, then $x = (t - s)/(a - b) \in S$, which is false.
6. So $\varphi_0(s + ax) = a$ is a well-defined linear form on $S'$, with $\varphi_0|_S = 0$ and $\varphi_0(x) = 1$.
7. By Fact E, $\varphi_0$ extends to some $\varphi \in X^*$, which has the same values on $S'$.

Part 1.

8. Let $\varphi \in W^*$. By the definition of the [[dual map|0C2TQMW5A1]], $f^*(\varphi) = 0$ means $\varphi(f(v)) = 0$ for all $v \in V$.
9. The vectors $f(v)$ with $v \in V$ are exactly the elements of the [[image|0JB228DCWB]] $\im f$.
10. So $f^*(\varphi) = 0$ exactly when $\varphi$ vanishes on $\im f$, that is, when $\varphi \in (\im f)^0$ by the definition of the [[annihilator|0R6M158SQ9]].

Part 2, the inclusion $\im f^* \subseteq (\ker f)^0$.

11. Let $\psi = f^*(\varphi) = \varphi \circ f$, and let $v$ lie in the [[kernel|02YFME3RGW]] $\ker f$.
12. Then $\psi(v) = \varphi(f(v)) = \varphi(0) = 0$, so $\psi \in (\ker f)^0$.

Part 2, the inclusion $(\ker f)^0 \subseteq \im f^*$.

13. Let $\psi \in (\ker f)^0$, and try to define $\chi_0 \colon \im f \to F$ by $\chi_0(f(v)) = \psi(v)$.
14. The value does not depend on the choice of $v$: if $f(v) = f(v')$, then $v - v' \in \ker f$, so $\psi(v) - \psi(v') = \psi(v - v') = 0$.
15. The map $\chi_0$ is linear, since $\chi_0(a f(v) + b f(v')) = \chi_0(f(av + bv')) = \psi(av + bv') = a\psi(v) + b\psi(v')$.
16. By Fact E with $X = W$ and $S = \im f$, the form $\chi_0$ extends to some $\chi \in W^*$.
17. For each $v \in V$, $f^*(\chi)(v) = \chi(f(v)) = \chi_0(f(v)) = \psi(v)$, so $\psi = f^*(\chi) \in \im f^*$.

Part 3.

18. If $S \ne X$, pick $x \in X$ outside $S$; Fact S gives a nonzero form in $S^0$. Since $X^0 = \{0\}$ by definition, $S^0 = \{0\}$ holds exactly when $S = X$.
19. If $S \ne \{0\}$, pick $s \ne 0$ in $S$; Fact S with the subspace $\{0\}$ and $x = s$ gives $\varphi \in X^*$ with $\varphi(s) = 1$, so $\varphi \notin S^0$. Since $\{0\}^0 = X^*$, $S^0 = X^*$ holds exactly when $S = \{0\}$.
20. The map $f$ is injective exactly when $\ker f = \{0\}$, which by step 19 holds exactly when $(\ker f)^0 = V^*$, which by part 2 means $\im f^* = V^*$.
21. The map $f$ is surjective exactly when $\im f = W$, which by step 18 holds exactly when $(\im f)^0 = \{0\}$, which by part 1 means $\ker f^* = \{0\}$.

Part 4.

22. Let $\dim V = n$. By part 2, $\rank f^* = \dim (\ker f)^0$.
23. By the theorem on the [[dimension of the annihilator|06Q1EFVH0Q]], $\dim (\ker f)^0 = n - \dim \ker f$.
24. By the [[rank-nullity theorem|0W4FSW1TVB]], $n - \dim \ker f = \dim \im f = \rank f$.

Part 5.

25. Define $h \colon V \to F^k$ by $h(v) = (\varphi_1(v), \dots, \varphi_k(v))$, which is linear because each $\varphi_i$ is linear.
26. Then $\ker h = \ker \varphi_1 \cap \dots \cap \ker \varphi_k$, so the hypothesis says that $\psi$ vanishes on $\ker h$, that is, $\psi \in (\ker h)^0$.
27. By part 2 applied to $h$, there is $\eta \in (F^k)^*$ with $\psi = h^*(\eta)$.
28. Let $e_1^*, \dots, e_k^*$ be the [[dual basis|0W6M3PSD08]] of the standard basis of $F^k$. Then $h^*(e_i^*) = e_i^* \circ h = \varphi_i$.
29. Write $\eta = \sum_i c_i e_i^*$. Since $h^*$ is linear, $\psi = \sum_i c_i h^*(e_i^*) = \sum_i c_i \varphi_i$.

## Idea

The kernel of $f^*$ is a direct calculation: a form is killed by $f^*$ exactly when it is zero on every output of $f$.
The image is the real content.
A form $\psi$ that vanishes on $\ker f$ cannot tell apart two vectors with the same image, so it defines a form on $\im f$, and this form extends to all of $W$.
The other parts follow by counting dimensions, or by applying part 2 to the map $h$ that collects $k$ forms into one map to $F^k$.

## Variants

If $V$ and $W$ are finite-dimensional, part 2 also follows from part 1 by counting.
Part 1, rank-nullity for $f^*$ and the dimension formula for annihilators give $\rank f^* = \dim W - \dim (\im f)^0 = \rank f$.
Step 12 gives $\im f^* \subseteq (\ker f)^0$, and steps 23 and 24 show that $(\ker f)^0$ also has dimension $\rank f$, so the two spaces are equal.
This route avoids Fact E, but it works only in finite dimension.

Part 5 also has a direct proof by induction on $k$, without dual maps.
