---
tag: VT9D8SA2AX
kind: proof
name: Proof that strong Kleene logic has no tautologies
msc: ["03B50"]
topics: [WZP584JQ06]
audience: grad
proves: ND17WYDNA5
uses: [74R8A41V6M, TFDYXS3K1N]
methods: [12MQ2NJ29A, 0NTF6DMVAP]
sources:
  - url: https://en.wikipedia.org/wiki/Three-valued_logic
    locator: Kleene and Priest logics
---

## Proof

Let $v$ be the valuation with $v(p) = \tfrac12$ for every variable $p$.
We write $v(\varphi)$ for the value of $\varphi$ in the [[strong Kleene matrix|74R8A41V6M]].

1. We claim that $v(\varphi) = \tfrac12$ for every formula $\varphi$, and we use [[structural induction|12MQ2NJ29A]] on $\varphi$.
2. If $\varphi$ is a variable $p$, then $v(p) = \tfrac12$ by the choice of $v$.
3. If $v(\psi) = \tfrac12$, then $v(\neg \psi) = 1 - \tfrac12 = \tfrac12$.
4. If $v(\psi) = v(\chi) = \tfrac12$, then $v(\psi \land \chi) = \min(\tfrac12, \tfrac12) = \tfrac12$.
5. Under the same hypothesis, $v(\psi \lor \chi) = \max(\tfrac12, \tfrac12) = \tfrac12$.
6. Implication is the abbreviation $\neg \psi \lor \chi$, so steps 3 and 5 cover it.
7. This proves the claim, which is item 1.
8. For item 2, the only designated value is $1$, and $v(\varphi) = \tfrac12 \ne 1$, so $v$ refutes $\varphi$.
9. For item 3, if $\Gamma$ is empty, then $\Gamma \models \varphi$ would mean that $\varphi$ is a tautology, which step 8 excludes.

## Idea

The value $\tfrac12$ is a fixed point of every connective.
So a formula cannot leave $\tfrac12$ when all its inputs are $\tfrac12$.

## Variants

The same proof works for every set of connectives that maps $(\tfrac12, \dots, \tfrac12)$ to $\tfrac12$, such as the weak Kleene connectives.
In algebraic terms, $\{\tfrac12\}$ is a subalgebra, and term functions preserve subalgebras.
The proof breaks as soon as a constant $1$ is allowed, since step 2 has no case for it.
