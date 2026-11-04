---
tag: ZDBBR2W7MQ
kind: proof
name: Proof of the existence of an algebraic closure
msc: [12F05]
proves: 0ETGBAK2CC
uses: [0QA8CHH8MG, 0MCXX29HWY, 02SJG1HC32, 0BDX4MBKT4, 0CES91M79A, 030TZ0DQWT, 0J0XBKG64S, 0VG02M1FEZ, 00EHX6FWC0, 0ASJVEFA9J, 0DQMDSVSXJ, 0GGE0Z0JQ1, 02HJYT53F7, 0WD3SE7S1X, 0VFW4Y69BT, 09N7DZ7SDB, 0NPW1DWECM, 0MA5B744K3, 0N5QW9K7MH, 0A7KJ68XHT, 0NRYPM9Y27, 0DFYTNZ6AM, 09EYMKMSB9, 0TPWS0K1BC, 07QY5RPFBR]
methods: [0J0XBKG64S, 0ASJVEFA9J]
sources:
  - url: https://www.jmilne.org/math/CourseNotes/FT.pdf
    locator: Chapter 6, Third proof of the existence of algebraic closures
  - url: https://en.wikipedia.org/wiki/Algebraic_closure
    locator: Existence of an algebraic closure and splitting fields
---

## Proof

First we show that every [[field|0QA8CHH8MG]] $F$ has an extension $F_1$ in which each nonconstant polynomial over $F$ has a root, with $F_1/F$ algebraic.

1. Let $S$ be the set of [[monic|0BDX4MBKT4]] polynomials $f \in F[x]$ with $\deg f \ge 1$. Take one variable $X_f$ for each $f \in S$.
2. Let $R = F[X_f : f \in S]$ be the union of the [[polynomial rings|0CES91M79A]] in finitely many of these variables. Two elements of $R$ lie in a common such ring, where we add and multiply them. Let $I$ be the [[ideal generated|030TZ0DQWT]] by the elements $f(X_f)$ for $f \in S$.
3. We show $I \ne R$, by [[contradiction|0J0XBKG64S]]. Suppose $1 \in I$. Then $1 = \sum_{i=1}^n g_i \, f_i(X_{f_i})$ for some distinct $f_1, \dots, f_n \in S$ and some $g_i \in R$.
4. The $g_i$ involve finitely many variables. So there are distinct $f_{n+1}, \dots, f_N \in S$ with all $g_i \in R_0 = F[X_{f_1}, \dots, X_{f_N}]$.
5. Set $E_0 = F$. For $1 \le i \le n$, [[some extension|0VG02M1FEZ]] $E_i$ of $E_{i-1}$ contains a [[root|00EHX6FWC0]] $a_i$ of $f_i$. By [[induction|0ASJVEFA9J]] this gives a field $E = E_n$ containing $F$ and $a_1, \dots, a_n$.
6. Applying the [[universal property of the polynomial ring|0DQMDSVSXJ]] one variable at a time gives a [[ring homomorphism|0GGE0Z0JQ1]] $\varphi \colon R_0 \to E$. It is the identity on $F$, sends $X_{f_i}$ to $a_i$ for $i \le n$, and sends $X_{f_i}$ to $0$ for $i > n$.
7. Applying $\varphi$ to Step 3 gives $1 = \sum_{i=1}^n \varphi(g_i) \, f_i(a_i) = 0$ in $E$. This is impossible in a field, so $I \ne R$.
8. By the [[existence of maximal ideals|02HJYT53F7]], some maximal ideal $M$ of $R$ contains $I$. Then $F_1 = R/M$ is a field, because [[R/M is a field iff M is maximal|0WD3SE7S1X]].
9. The map $F \to F_1$, $c \mapsto c + M$, is a ring homomorphism into the [[quotient ring|0VFW4Y69BT]]. It is [[injective|09N7DZ7SDB]], so we identify $F$ with its image, a subfield of $F_1$.
10. For $f \in S$ let $x_f = X_f + M$. Then $f(x_f) = f(X_f) + M = 0$, since $f(X_f) \in I \subseteq M$. So each $f \in S$ has a root in $F_1$.
11. Let $g \in F[x]$ with $\deg g \ge 1$ and leading coefficient $c$. Then $c^{-1} g \in S$ has a root in $F_1$, which is also a root of $g$.
12. Each $x_f$ is [[algebraic|0NPW1DWECM]] over $F$, since $f \ne 0$ and $f(x_f) = 0$.
13. Let $u \in F_1$. Then $u = h + M$ with $h \in R$, and $h$ involves finitely many variables $X_{f_1}, \dots, X_{f_k}$. So $u = h(x_{f_1}, \dots, x_{f_k})$ lies in the [[generated field|0MA5B744K3]] $G_k = F(x_{f_1}, \dots, x_{f_k})$.
14. Let $G_0 = F$ and $G_j = G_{j-1}(x_{f_j})$. The element $x_{f_j}$ is algebraic over $G_{j-1}$, since its polynomial $f_j$ has coefficients in $F \subseteq G_{j-1}$.
15. So $[G_j : G_{j-1}]$ is finite by the [[degree of a simple extension|0N5QW9K7MH]]. By the [[tower law|0A7KJ68XHT]], $G_k/F$ is a [[finite extension|0NRYPM9Y27]].
16. [[Finite extensions are algebraic|0DFYTNZ6AM]], so $u$ is algebraic over $F$. Hence $F_1/F$ is [[algebraic|09EYMKMSB9]].

Now we iterate this construction for the field $K$ of the statement.

17. Let $K_0 = K$ and $K_{i+1} = (K_i)_1$, the field built from $F = K_i$ in Steps 1 to 16. Replacing each $K_{i+1}$ by an isomorphic copy, we may assume that $K_i$ is a [[subfield|07QY5RPFBR]] of $K_{i+1}$.
18. Let $\Omega = \bigcup_{i \ge 0} K_i$. Any two elements of $\Omega$ lie in a common $K_i$, since the $K_i$ increase. Define their sum and product in that $K_i$.
19. This does not depend on the choice of $i$, because each $K_i$ is a subfield of the later ones. Each field axiom involves finitely many elements, which lie in a common $K_i$. So $\Omega$ is a field containing $K$.
20. By induction on $i$, $K_i/K$ is algebraic. For $i = 0$, each $c \in K$ is a root of $x - c$. If $K_i/K$ is algebraic, then $K_{i+1}/K_i$ is algebraic by Step 16, so $K_{i+1}/K$ is algebraic by [[transitivity|0TPWS0K1BC]].
21. Every element of $\Omega$ lies in some $K_i$, so it is algebraic over $K$. Hence $\Omega/K$ is algebraic.
22. Let $g \in \Omega[x]$ with $\deg g \ge 1$. Its finitely many coefficients lie in some $K_N$. By Step 11 for $F = K_N$, $g$ has a root in $K_{N+1} \subseteq \Omega$.
23. So $\Omega$ is [[algebraically closed|02SJG1HC32]]. With Step 21, $\Omega$ is an [[algebraic closure|0MCXX29HWY]] of $K$.

## Idea

Adjoin a root of every polynomial at once, using one variable per polynomial and a maximal ideal. The ideal of relations is proper because any finite part of it can be solved in a finite extension. One step gives roots for polynomials over the old field. Repeating countably often and taking the union gives a field that is algebraically closed and algebraic over $K$.
