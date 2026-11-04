---
tag: 4EYMSR98ER
kind: proof
name: Proof of the universal property of the free group
msc: ["20E05"]
proves: 0CDWKDYWN6
uses: [020Z5SEN27, 0FPXK5CHQ3, 0HV9Y7WG5R]
sources:
  - url: https://en.wikipedia.org/wiki/Free_group
    locator: Universal property
---

## Proof

We first build $\varphi$ on all words, then show that reduction does not change its value.

1. By the definition of the [[free group|020Z5SEN27]], the elements of $F_S$ are the [[reduced words|0FPXK5CHQ3]] on $S$. To get the product $u \cdot v$, form the concatenation $uv$. Then delete adjacent pairs $s s^{-1}$ or $s^{-1} s$, one pair at a time, until the word is reduced. The identity is the empty word.
2. Extend $f$ to the letters by $\hat f(s) = f(s)$ and $\hat f(s^{-1}) = f(s)^{-1}$ for $s \in S$.
3. For any word $w = t_1 \cdots t_n$, reduced or not, let $\Phi(w) = \hat f(t_1) \cdots \hat f(t_n)$ in $G$. For the empty word, $\Phi$ gives $e$.
4. For words $w$ and $w'$, the concatenation satisfies $\Phi(ww') = \Phi(w)\Phi(w')$, directly from step 3.
5. Let $w'$ arise from $w$ by deleting one adjacent pair. Write $w = a\,t\,t'\,b$ and $w' = ab$, where $tt'$ is $ss^{-1}$ or $s^{-1}s$. Then $\hat f(t)\hat f(t') = e$, since it is $f(s)f(s)^{-1}$ or $f(s)^{-1}f(s)$.
6. By steps 4 and 5, $\Phi(w) = \Phi(a)\,\hat f(t)\hat f(t')\,\Phi(b) = \Phi(a)\Phi(b) = \Phi(w')$.
7. By step 6 and induction on the number of deletions, $\Phi$ takes the same value on $uv$ and on $u \cdot v$.
8. Let $\varphi \colon F_S \to G$ be the restriction of $\Phi$ to reduced words. For $u, v \in F_S$, steps 4 and 7 give $\varphi(u \cdot v) = \Phi(uv) = \varphi(u)\varphi(v)$. So $\varphi$ is a [[group homomorphism|0HV9Y7WG5R]].
9. For $s \in S$, the word $s$ of length $1$ is reduced, and $\varphi(s) = \hat f(s) = f(s)$. This proves existence.
10. For uniqueness, let $\psi \colon F_S \to G$ be a homomorphism with $\psi(s) = f(s)$ for each $s \in S$.
11. For $s \in S$, the product $s \cdot s^{-1}$ in $F_S$ is the empty word, the identity. So $s^{-1}$ is the inverse of $s$ in $F_S$, and $\psi(s^{-1}) = \psi(s)^{-1} = f(s)^{-1}$. Hence $\psi(t) = \hat f(t)$ for each letter $t$.
12. Let $w = t_1 \cdots t_n$ be a reduced word with $n \geq 1$. The concatenation of $t_1$ and $t_2 \cdots t_n$ is $w$ itself, which is reduced. So $w = t_1 \cdot (t_2 \cdots t_n)$ in $F_S$.
13. By induction on $n$, using step 12, $w = t_1 \cdot t_2 \cdots t_n$ is the product of its letters in $F_S$.
14. Since $\psi$ is a homomorphism, steps 11 and 13 give $\psi(w) = \hat f(t_1) \cdots \hat f(t_n) = \varphi(w)$. For the empty word, both give $e$.
15. So $\psi = \varphi$, and $\varphi$ is the only such homomorphism.

## Idea

The value of a word is forced: send each letter to $f(s)$ or its inverse and multiply. The only thing to check is that cancelling a pair $ss^{-1}$ does not change this value. It does not, because $f(s)f(s)^{-1} = e$ in $G$.
