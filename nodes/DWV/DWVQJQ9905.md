---
tag: DWVQJQ9905
kind: proof
name: Proof of Cauchy's theorem by McKay's counting argument
msc: [20D20]
proves: 0JM7PA288B
uses: [0G0B3DRG65, 0YSE802YCQ, 0ZC7FYE0NZ, 0S19CWFZM2, 08JF1K4DW1, 0F5QC101Q7, 0JPYSD5E0B]
sources:
  - url: https://en.wikipedia.org/wiki/Cauchy's_theorem_(group_theory)
    locator: Proof 2
---

## Proof

We let a cyclic group of order $p$ act on tuples by cyclic shifts, and count fixed points modulo $p$. Let $e$ be the identity of $G$.

1. Let $X$ be the set of tuples $t = (g_1, \dots, g_p) \in G^p$ with $g_1 g_2 \cdots g_p = e$.
2. The map $X \to G^{p-1}$, $(g_1, \dots, g_p) \mapsto (g_1, \dots, g_{p-1})$, is a bijection. Its inverse sets $g_p = (g_1 \cdots g_{p-1})^{-1}$, the only element that makes the product $e$. So $\abs{X} = \abs{G}^{p-1}$.
3. Since $p \mid \abs{G}$ and $p - 1 \geq 1$, step 2 gives $p \mid \abs{X}$.
4. Let $s(g_1, \dots, g_p) = (g_2, \dots, g_p, g_1)$. If $t \in X$, then $g_2 \cdots g_p g_1 = g_1^{-1} (g_1 g_2 \cdots g_p) g_1 = g_1^{-1} e g_1 = e$. So $s$ maps $X$ to $X$.
5. Shifting $p$ times returns each tuple to itself, so $s^p$ is the identity of $X$. Hence $s^k$ depends only on $k$ modulo $p$.
6. Let $C = \Z/p\Z$, the [[cyclic group of order $p$|0G0B3DRG65]]. Define $k \cdot t = s^k(t)$ for $k \in C$ and $t \in X$. This is well defined by step 5.
7. We have $0 \cdot t = t$ and $j \cdot (k \cdot t) = s^{j+k}(t) = (j + k) \cdot t$. So this is an [[action|0YSE802YCQ]] of $C$ on $X$.
8. By the [[orbit size formula|0S19CWFZM2]], each orbit has a size that divides $\abs{C} = p$. As $p$ is prime, each orbit has size $1$ or $p$.
9. An orbit has size $1$ exactly when its point is a [[fixed point|08JF1K4DW1]]. Let $X^C$ be the set of fixed points. Since the [[orbits partition|0ZC7FYE0NZ]] $X$, $\abs{X} = \abs{X^C} + p \cdot r$, where $r$ is the number of orbits of size $p$.
10. By steps 3 and 9, $p$ divides $\abs{X^C}$.
11. A tuple $t$ is fixed by all of $C$ if and only if $s(t) = t$, since every $s^k$ is a power of $s$. And $s(t) = t$ means $g_{i+1} = g_i$ for all $i < p$, that is, $t = (g, g, \dots, g)$ for some $g$.
12. Such a constant tuple lies in $X$ if and only if $g^p = e$. So $\abs{X^C}$ is the number of $g \in G$ with $g^p = e$.
13. The element $e$ satisfies $e^p = e$, so $\abs{X^C} \geq 1$. By step 10, $\abs{X^C} \geq p \geq 2$. So there is $g \neq e$ with $g^p = e$.
14. Let $m$ be the [[order|0JPYSD5E0B]] of this $g$. Since [[$g^p = e$, $m$ divides $p$|0F5QC101Q7]], so $m$ is $1$ or $p$.
15. If $m = 1$, then $g = g^1 = e$, which is false. So $m = p$, and $g$ is an element of order $p$.

## Idea

Tuples whose product is the identity can be rotated without leaving the set, and their number $\abs{G}^{p-1}$ is a multiple of $p$. Rotations sort the tuples into groups of $p$, except the constant tuples, which stay put. So the number of constant tuples $(g, \dots, g)$ with $g^p = e$ is a multiple of $p$, and besides $(e, \dots, e)$ there must be others.
