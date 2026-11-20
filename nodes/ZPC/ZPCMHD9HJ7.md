---
tag: ZPCMHD9HJ7
kind: proof
name: Proof of the principle of explosion by the Lewis argument
msc: ["03B05", "03B53"]
topics: [NJB94B39QK]
audience: ug1
proves: K33VPAPJQG
uses: [0F72FK8EKB, 6EFJF9NAYX, 029JBBF693, 1HK0VYWTV7, H31CS3HK5P]
methods: [0NTF6DMVAP]
sources:
  - url: https://en.wikipedia.org/wiki/Principle_of_explosion
    locator: Symbolic representation
  - url: https://plato.stanford.edu/entries/logic-paraconsistent/
    locator: Paraconsistent Logic (SEP entry), section 1.2
---

## Proof

We derive $\psi$ from the premises $\varphi$ and $\neg\varphi$ in four lines, and then check that each rule preserves truth.

1. $\varphi$. This is the first premise.
2. $\neg\varphi$. This is the second premise.
3. $\varphi \lor \psi$. This follows from line 1 by [[disjunction|0F72FK8EKB]] introduction.
4. $\psi$. This follows from lines 3 and 2 by [[disjunctive syllogism|6EFJF9NAYX]]: from $A \lor B$ and $\neg A$ infer $B$.

Now we show that each rule preserves truth under every classical [[valuation|H31CS3HK5P]] $v$.

5. Disjunction introduction: if $v(\varphi) = 1$, then $v(\varphi \lor \psi) = 1$, by the truth table of $\lor$.
6. Disjunctive syllogism: suppose $v(\varphi \lor \psi) = 1$ and $v(\neg\varphi) = 1$. By the truth table of [[negation|029JBBF693]], $v(\varphi) = 0$. By the truth table of $\lor$, a disjunction with a false first part is true only if the second part is true. So $v(\psi) = 1$.
7. Let $v$ make both premises true. By step 5, $v$ makes line 3 true. By step 6 with line 2, $v$ makes line 4 true.
8. So every valuation that makes $\varphi$ and $\neg\varphi$ true makes $\psi$ true. By the definition of [[logical consequence|1HK0VYWTV7]], $\set{\varphi, \neg\varphi} \vDash \psi$. $\blacksquare$

## Idea

The premise $\varphi$ lets us add any second disjunct $\psi$.
The premise $\neg\varphi$ then removes the first disjunct, and only $\psi$ is left.
The proof is syntactic, so it works in every logic that has both rules and lets us chain inferences.

## Variants

- The [[semantic proof|RRWN8BHANP]] does not use rules: no valuation makes $\varphi$ and $\neg\varphi$ both true, so the consequence holds vacuously.
- In natural deduction with $\bot$, from $\varphi$ and $\neg\varphi$ we get $\bot$ by $\neg$-elimination, and then $\psi$ by ex falso. This proof also works in intuitionistic logic.
- In the logic of paradox, step 6 fails: $v(\varphi) = \mathsf{B}$ makes $\neg\varphi$ designated without making $\varphi$ undesignated.
