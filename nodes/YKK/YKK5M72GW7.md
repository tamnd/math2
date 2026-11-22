---
tag: YKK5M72GW7
kind: proof
name: Proof of the properties of Lagrangian subspaces
msc: ["15A63", "53D05"]
topics: [DYAK7YMK7B]
audience: grad
proves: 30PND47YCP
methods: [0NTF6DMVAP, 0ASJVEFA9J]
uses: [W5FHT07SJJ, SX9CD5NEPD, M0G958M917, M2JH84VEY9, 0WGAXEK99E]
sources:
  - url: https://en.wikipedia.org/wiki/Symplectic_vector_space
    locator: Subspaces
  - book: isbn:9780387728285
    locator: Chapter 11
---

## Proof

We get every part from the dimension formula $\dim W + \dim W^\perp = 2m$, and for part 4 we add one vector of $W^\perp$ at a time.
Let $(V, \omega)$ be [[symplectic|W5FHT07SJJ]] with $\dim V = 2m$, so $\omega$ is alternating and nondegenerate.

Preliminary facts.

1. Since $\omega$ is alternating, $\omega(x, y) = -\omega(y, x)$ for all $x, y$, by the [[statement on alternating and skew-symmetric forms|SX9CD5NEPD]].
2. So $\omega(x, y) = 0$ implies $\omega(y, x) = 0$, and $\omega$ is [[reflexive|M0G958M917]].

Part 1.

3. Since $\omega$ is nondegenerate, $\dim W + \dim W^\perp = 2m$, by part 2 of the [[dimension statement for orthogonal complements|M2JH84VEY9]].
4. Since $\omega$ is nondegenerate and, by step 2, reflexive, $(W^\perp)^\perp = W$, by part 4 of the same statement.

Part 2.

5. Let $W$ be isotropic. Then $W \subseteq W^\perp$, so $\dim W \leq \dim W^\perp$.
6. By step 3, $\dim W^\perp = 2m - \dim W$. So $2 \dim W \leq 2m$, and $\dim W \leq m$.

Part 3.

7. Let $W = W^\perp$. Then $W$ is isotropic, and step 3 gives $2 \dim W = 2m$, so $\dim W = m$.
8. Conversely, let $W$ be isotropic with $\dim W = m$. Then $W \subseteq W^\perp$, and $\dim W^\perp = 2m - m = m = \dim W$ by step 3.
9. A subspace of full dimension is the whole space, by the [[statement on subspaces of full dimension|0WGAXEK99E]]. Applied inside $W^\perp$, this gives $W = W^\perp$.

Part 4.

10. Let $W$ be isotropic with $\dim W = k < m$. By step 3, $\dim W^\perp = 2m - k > k$, so $W \neq W^\perp$.
11. Since $W \subseteq W^\perp$, there is $x \in W^\perp$ with $x \notin W$. Put $W' = W + Fx$.
12. Then $\dim W' = k + 1$, because $x \notin W$, so a basis of $W$ together with $x$ is linearly independent.
13. Let $w + ax$ and $w' + bx$ be in $W'$, with $w, w' \in W$ and $a, b \in F$. Bilinearity gives
$$\omega(w + ax, w' + bx) = \omega(w, w') + b\, \omega(w, x) + a\, \omega(x, w') + ab\, \omega(x, x).$$
14. The term $\omega(w, w')$ is $0$, since $W$ is isotropic, and $\omega(w, x) = 0$, since $x \in W^\perp$.
15. The term $\omega(x, w') = -\omega(w', x)$ is $0$ by step 1, since $x \in W^\perp$, and $\omega(x, x) = 0$, since $\omega$ is alternating.
16. So $\omega$ is zero on $W'$, and $W'$ is isotropic of dimension $k + 1$.
17. Repeating steps 10 to 16, by induction on $m - k$, gives an isotropic subspace $L \supseteq W$ with $\dim L = m$. By part 3, $L$ is Lagrangian.
18. The subspace $\{0\}$ is isotropic, so step 17 applied to it shows that Lagrangian subspaces exist.
19. Let $W$ be a maximal isotropic subspace. By step 17, $W$ lies in a Lagrangian subspace $L$, which is isotropic, and maximality gives $W = L$.
20. Let $L$ be Lagrangian, and let $U \supseteq L$ be isotropic. By part 2, $\dim U \leq m = \dim L$, so $U = L$ by the statement used in step 9. So $L$ is maximal isotropic. $\blacksquare$

## Idea

Nondegeneracy fixes $\dim W^\perp = 2m - \dim W$, and an isotropic subspace $W$ sits inside $W^\perp$.
So $W$ can have at most half of the dimension.
While $W$ is smaller than half, $W^\perp$ is strictly bigger than $W$ and has room for one more vector.
That vector pairs to zero with $W$ and, because the form is alternating, with itself, so it can be added without losing isotropy.

## Variants

One can also extend a basis $e_1, \dots, e_k$ of $W$ to a symplectic basis $e_1, \dots, e_m, f_1, \dots, f_m$, with the method of the [[classification of alternating forms|388BWRRP7H]].
Then $\operatorname{span}(e_1, \dots, e_m)$ is a Lagrangian subspace that contains $W$.
This route needs more care in choosing the $f_i$, but it also produces a Lagrangian complement $\operatorname{span}(f_1, \dots, f_m)$.
