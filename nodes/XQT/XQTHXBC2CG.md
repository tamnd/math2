---
tag: XQTHXBC2CG
kind: example
name: The Lindenbaum-Tarski algebra on countably many variables is atomless
msc: ["03G05", "06E05"]
topics: [QYA4H5Y7VR]
audience: grad
instance_of: [KG7730QZMQ, NFEEGWJFCK]
uses: [MGCVQXXQJH, J2GTJ8FKF2, NFEEGWJFCK, W9VYJRBF9N]
sources:
  - url: https://en.wikipedia.org/wiki/Atomless_Boolean_algebra
    locator: lead section
  - url: https://en.wikipedia.org/wiki/Free_Boolean_algebra
    locator: lead section
---

## Example

Let $P = \set{p_0, p_1, p_2, \dots}$ be countably infinite, and let $\mathbf{L}$ be the [[Lindenbaum-Tarski algebra|MGCVQXXQJH]] of the empty theory over $P$.
We check that $\mathbf{L}$ is countable, nontrivial and [[atomless|NFEEGWJFCK]].

1. Countable: there are countably many finite strings over a countable alphabet, so countably many formulas and classes.
2. Nontrivial: $[\top] \ne [\bot]$, because $\top \to \bot$ is not a tautology, by soundness.
3. Let $[\varphi] \ne 0$; so $\varphi$ is not refutable, and some valuation $s$ makes $\varphi$ true, by [[completeness|J2GTJ8FKF2]].
4. The formula $\varphi$ has finitely many variables, so there is $r \in P$ that does not occur in $\varphi$.
5. Change $s$ at $r$ to get $s_1$ with $s_1(r) = 1$ and $s_0$ with $s_0(r) = 0$; both still make $\varphi$ true.
6. $s_1$ makes $\varphi \land r$ true, so $[\varphi \land r] \ne 0$.
7. $s_0$ makes $\varphi$ true and $\varphi \land r$ false, so $[\varphi] \not\le [\varphi \land r]$, and $[\varphi \land r] \ne [\varphi]$.
8. So $0 < [\varphi \land r] < [\varphi]$, and $[\varphi]$ is not an atom.

So $\mathbf{L}$ is a countable atomless Boolean algebra.

## Remarks

1. Any two countable atomless Boolean algebras are isomorphic, by a back-and-forth argument.
   So $\mathbf{L}$ is isomorphic to the algebra of clopen subsets of the [[Cantor space|W9VYJRBF9N]].
2. Under this isomorphism, $[p_i]$ goes to the set of sequences with $1$ at place $i$.
3. With finitely many variables the algebra is finite, and every nonzero element is above an atom; see [[the two-variable example|A7CTMV6M39]].
4. In logical terms, step 8 says that no satisfiable formula decides every variable.

## Explanations

### L1 human

With infinitely many letters, no formula can say everything.
A formula mentions only a few letters, so we can always add one more letter and say more.
This makes the formula strictly stronger and still possible.
So there is no "smallest possible" piece of information, and the algebra has no atoms.

### L2 human

1. Take $\varphi = p_0$; it is satisfiable.
2. The letter $p_1$ does not occur in $\varphi$.
3. Then $p_0 \land p_1$ is satisfiable, by $p_0 = p_1 = 1$.
4. And $p_0 \land p_1$ is strictly stronger than $p_0$, since $p_0 = 1$, $p_1 = 0$ makes $p_0$ true and $p_0 \land p_1$ false.
5. So $0 < [p_0 \land p_1] < [p_0]$.

The typical use: this algebra is the standard example of a countable Boolean algebra without atoms.
The trap: the free Boolean algebra on finitely many generators is atomic, so the infinite case behaves differently.
