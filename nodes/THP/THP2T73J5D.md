---
tag: THP2T73J5D
kind: proof
name: Proof that the diagonal embedding is elementary
msc: ["03C20"]
topics: [HZG1YP26AB]
audience: grad
proves: E4TD8X2ZRX
uses: [WBWC47Y5SK, AGYBSTD7BG, J64Y3JC0RE, CGH8C8EA9N]
methods: [0NTF6DMVAP, 0WCP0PVET6]
sources:
  - url: https://en.wikipedia.org/wiki/Ultraproduct
    locator: Ultrapower
---

## Proof

Let $c_m$ be the constant function with value $m$, so $d(m) = [c_m]$ by the [[definition|WBWC47Y5SK]].

1. *Part 1.* Let $\varphi(x_1, \dots, x_n)$ be a formula and $m_1, \dots, m_n \in M$. The truth set $X = \set{i \in I : \mathcal{M} \models \varphi(c_{m_1}(i), \dots, c_{m_n}(i))}$ does not depend on $i$.
2. So $X = I$ if $\mathcal{M} \models \varphi(m_1, \dots, m_n)$, and $X = \emptyset$ otherwise.
3. $I \in \mathcal{U}$ and $\emptyset \notin \mathcal{U}$, by the definition of an [[ultrafilter|J64Y3JC0RE]].
4. [[Łoś's theorem|AGYBSTD7BG]] gives $\mathcal{M}^I / \mathcal{U} \models \varphi(d(m_1), \dots, d(m_n))$ if and only if $X \in \mathcal{U}$, that is, if and only if $\mathcal{M} \models \varphi(m_1, \dots, m_n)$.
5. With $\varphi$ the formula $x_1 = x_2$, step 4 shows that $d$ is injective. So $d$ is an [[elementary embedding|CGH8C8EA9N]].
6. *Part 2.* Apply step 4 to sentences, with $n = 0$.
7. *Part 3, $M$ finite.* Let $f : I \to M$. The fibers $f^{-1}(m)$, $m \in M$, are finitely many and partition $I$.
8. If none of them lay in $\mathcal{U}$, their complements would lie in $\mathcal{U}$, and so would the intersection of the complements, which is $\emptyset$. So some $f^{-1}(m) \in \mathcal{U}$, and $[f] = d(m)$.
9. *Part 3, $\mathcal{U}$ principal at $i_0$.* For $f : I \to M$, the functions $f$ and $c_{f(i_0)}$ agree on a set containing $i_0$, which lies in $\mathcal{U}$. So $[f] = d(f(i_0))$.
10. *Part 4.* Let $X_0 \supseteq X_1 \supseteq \dots$ lie in $\mathcal{U}$ with empty intersection. Replacing $X_0$ by $I$, we may assume $X_0 = I$.
11. For $i \in I$ there is a largest $k$ with $i \in X_k$, because the intersection is empty. Call it $k(i)$.
12. Choose distinct elements $m_0, m_1, \dots$ of $M$, which is infinite, and let $f(i) = m_{k(i)}$.
13. If $m \neq m_k$ for all $k$, then $f$ and $c_m$ agree nowhere, so $[f] \neq d(m)$.
14. If $m = m_k$, then $\set{i : f(i) = m_k} = \set{i : k(i) = k} \subseteq I \setminus X_{k+1}$. The set $I \setminus X_{k+1}$ is not in $\mathcal{U}$, since $X_{k+1}$ is, so $[f] \neq d(m_k)$.

So $[f]$ is not in the image of $d$, and $d$ is not surjective.
This proves all four parts.

## Idea

The truth set of a formula at constant functions is all of $I$ or empty, so Łoś's theorem reduces truth in the ultrapower to truth in $\mathcal{M}$.
Surjectivity is a question of whether every function is constant on a large set.
Finitely many fibers force this, and a decreasing sequence of large sets with empty intersection lets a function change its value infinitely often.

## Variants

Part 1 also follows from the Tarski-Vaught test applied to the image $d(M)$, but that route needs Łoś's theorem as well, to find witnesses.
For part 4 over $I = \N$ with a nonprincipal $\mathcal{U}$, one can take $X_n = \set{k : k \ge n}$, and the function in step 12 is $i \mapsto m_i$.
