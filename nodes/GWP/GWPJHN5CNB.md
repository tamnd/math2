---
tag: GWPJHN5CNB
kind: proof
name: Proof that Łukasiewicz implication is not definable from the Kleene connectives
msc: ["03B50"]
topics: [WZP584JQ06]
audience: grad
proves: 729J1FD1GZ
uses: [F9NDCFY3GS, TFDYXS3K1N]
methods: [12MQ2NJ29A, 0J0XBKG64S]
sources:
  - url: https://en.wikipedia.org/wiki/Three-valued_logic
    locator: Łukasiewicz logic
---

## Proof

Part A: item 1.

1. Claim: every formula $\varphi(p, q)$ in $\neg, \land, \lor$ has the value $\tfrac12$ at $p = q = \tfrac12$. We use [[structural induction|12MQ2NJ29A]] on $\varphi$.
2. If $\varphi$ is $p$ or $q$, its value is $\tfrac12$.
3. If $\varphi = \neg \psi$ and $\psi$ has value $\tfrac12$, then $\varphi$ has value $1 - \tfrac12 = \tfrac12$.
4. If $\varphi = \psi \land \chi$ or $\psi \lor \chi$ with both values $\tfrac12$, then $\min(\tfrac12, \tfrac12) = \max(\tfrac12, \tfrac12) = \tfrac12$.
5. But $\tfrac12 \to_{Ł} \tfrac12 = \min(1, 1) = 1 \neq \tfrac12$. So no such $\varphi$ defines $\to_{Ł}$.

Part B: item 2.

6. Order $V$ by information: $u \sqsubseteq w$ iff $u = w$ or $u = \tfrac12$.
7. $\neg$ is monotone for $\sqsubseteq$: it fixes $\tfrac12$ and maps $0, 1$ to $1, 0$.
8. $\min$ is monotone. Let $x \sqsubseteq x'$ and $y \sqsubseteq y'$. If $\min(x, y) = 0$, then $x$ or $y$ is $0$, so $x'$ or $y'$ is $0$, and $\min(x', y') = 0$. If $\min(x, y) = 1$, then $x = y = 1 = x' = y'$. If $\min(x, y) = \tfrac12$, it lies below every value.
9. $\max$ is monotone by the same argument with $0$ and $1$ exchanged, and constants are monotone.
10. By structural induction, every formula in $\neg, \land, \lor, 0, 1$ defines a function monotone for $\sqsubseteq$.
11. $(\tfrac12, \tfrac12) \sqsubseteq (1, \tfrac12)$ coordinatewise, but $\tfrac12 \to_{Ł} \tfrac12 = 1$ and $1 \to_{Ł} \tfrac12 = \tfrac12$, and $1 \not\sqsubseteq \tfrac12$.
12. So $\to_{Ł}$ is not monotone, and step 10 shows that no such formula defines it.

Part C: item 3.

13. If $x \le y$: $x \to_{Ł} y = 1$ and $1 \to_{Ł} y = y = \max(x, y)$.
14. If $x > y$: $x \to_{Ł} y = 1 - x + y < 1$, and $(1 - x + y) \to_{Ł} y = \min(1, x) = x = \max(x, y)$.
15. Then $\neg(\neg x \lor \neg y) = 1 - \max(1 - x, 1 - y) = \min(x, y)$.

This proves the three items.

## Idea

Find a property that the Kleene connectives preserve and Łukasiewicz implication breaks.
The set $\set{\tfrac12}$ is closed under the Kleene operations, and the information order is preserved by them; the entry $\tfrac12 \to_{Ł} \tfrac12 = 1$ violates both.

## Variants

Part B alone also proves item 1, since a formula without constants is a special case of step 10.
The same invariant method decides, for any finite set of operations, whether a given operation is in the generated [[clone|PTKR703G6A]], once one finds the right preserved relations.
