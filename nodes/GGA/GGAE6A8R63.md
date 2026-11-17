---
tag: GGAE6A8R63
kind: proof
name: Outline of the proof of Szmielew's theorem
msc: ["03C60", "03B25", "20K99"]
topics: [BAZT8JJ70S]
audience: research
proves: Y0753DF5R9
uses: [RX9MB386C5, 000AYPA9AJ, 7FDDXV3JK7, WQ1ZE255SF, TN9G24VABN]
methods: [0NTF6DMVAP]
sources:
  - url: https://en.wikipedia.org/wiki/Wanda_Szmielew
    locator: Life
  - url: https://en.wikipedia.org/wiki/Decidability_(logic)
    locator: Some decidable theories
---

## Proof

This is an outline.
Steps 1 to 6 and 8 are short arguments that a reader can complete, and steps 7 and 9 cite the main work of Szmielew, "Elementary properties of Abelian groups", Fundamenta Mathematicae 41 (1955), pages 203 to 271.
We use the notation of [[Szmielew's theorem|Y0753DF5R9]], the signature $\{+, -, 0\}$, and the set $T_{\mathrm{ab}}$ of axioms of abelian groups.

1. For a prime $p$ and $n \in \mathbb{N}$, the formula $\pi_{p,n}(x)$, namely $\exists y \, (x = p^n y) \wedge px = 0$, defines $(p^n A)[p]$ in each abelian group $A$. Here $p^n y$ is the term $y + \cdots + y$ with $p^n$ summands.
2. For $k \ge 1$, let $\alpha_{p,n,k}$ say: there are $x_1, \ldots, x_k$ with $\pi_{p,n}(x_i)$, such that no sum $c_1 x_1 + \cdots + c_k x_k$ with $0 \le c_i < p$, not all $c_i = 0$, satisfies $\pi_{p,n+1}$. There are finitely many tuples $(c_i)$, so this is one sentence. By the definition of linear independence modulo a subspace, $A \models \alpha_{p,n,k}$ if and only if $U(p, n; A) \ge k$.
3. In the same way there is a sentence $\beta_{p,n,k}$ that holds if and only if $\dim (p^n A)[p] \ge k$, and a sentence $\gamma_{p,n,k}$ that holds if and only if $\dim p^n A / p^{n+1} A \ge k$. For $m \ge 1$, the sentence $\varepsilon_m$, namely $\forall x \, (mx = 0)$, holds if and only if $mA = 0$.
4. A non-increasing sequence in $\mathbb{N} \cup \{\infty\}$ has a limit at least $k$ if and only if each term is at least $k$. So $D(p; A) \ge k$ if and only if $A \models \beta_{p,n,k}$ for all $n$, and $\mathrm{Tf}(p; A) \ge k$ if and only if $A \models \gamma_{p,n,k}$ for all $n$. Also $\mathrm{Exp}(A)$ is the least $m$ with $A \models \varepsilon_m$, or $\infty$ if there is none.
5. If $A \equiv B$, then $A$ and $B$ satisfy the same sentences $\alpha$, $\beta$, $\gamma$ and $\varepsilon$. By steps 2 to 4 they have the same invariants. This proves the direction "only if" of part 1.
6. Conversely, the invariants determine the truth of each sentence of steps 2 and 3. For $\alpha$ and $\varepsilon$ this is steps 2 and 4. Multiplication by $p$ maps $p^n A / p^{n+1} A$ onto $p^{n+1} A / p^{n+2} A$, and its kernel is isomorphic to $(p^n A)[p] / (p^{n+1} A)[p]$. A computation with these exact sequences gives $\dim (p^n A)[p] = D(p; A) + \sum_{m \ge n} U(p, m; A)$ and $\dim p^n A / p^{n+1} A = \mathrm{Tf}(p; A) + \sum_{m \ge n} U(p, m; A)$, in $\mathbb{N} \cup \{\infty\}$.
7. (Szmielew.) By [[quantifier elimination|7FDDXV3JK7]] relative to $T_{\mathrm{ab}}$, each sentence $\varphi$ is equivalent modulo $T_{\mathrm{ab}}$ to a Boolean combination $\beta_\varphi$ of sentences of the kinds in steps 2 and 3. There is an algorithm that computes $\beta_\varphi$ from $\varphi$.
8. Suppose that $A$ and $B$ have the same invariants, and let $\varphi$ be a sentence true in $A$. By step 6, $A$ and $B$ satisfy the same sentences of steps 2 and 3, so $B \models \beta_\varphi$ because $A \models \beta_\varphi$. By step 7, $B \models \varphi$. So $A \equiv B$, and this proves the direction "if" of part 1.
9. (Szmielew.) For a Boolean combination $\beta$ of finitely many sentences of steps 2 and 3, it is decidable whether $\beta$ holds in every abelian group. The proof is a description of the combinations of values of finitely many invariants that some abelian group realizes.
10. A sentence $\varphi$ is in the elementary theory of abelian groups if and only if $\beta_\varphi$ holds in every abelian group, by step 7. Steps 7 and 9 give an algorithm that decides this. This proves part 2.

## Idea

First-order sentences can count the dimensions of finitely many vector spaces over $\mathbb{F}_p$ that are built from $A$ with multiplication by $p$.
These counts give the invariants, and so elementarily equivalent groups have the same invariants.
The hard direction is a quantifier elimination: every sentence reduces, effectively, to a Boolean combination of such counting sentences.
Thus the counts decide all sentences, and the reduction gives the decision procedure.

## Variants

Eklof and Fisher gave a proof in 1972 with [[saturated models|RMTZ5J64FX]] in place of an explicit elimination of quantifiers.
A third route uses the theorem of Baur and Monk for modules.
By this theorem, every formula is equivalent to a Boolean combination of positive primitive formulas and index sentences.
Over $\mathbb{Z}$ the index sentences reduce to the sentences of steps 2 and 3.
