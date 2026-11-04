---
tag: DJEW8ZHQWT
kind: proof
name: Proof of Tarski's theorem about choice
proves: 1C8ZVDSQXT
sources:
  - wikipedia: en:320578@r1336022373
    locator: Tarski's theorem about choice, section Proof
    note: adopted
    mention: wikipedia://en/320578#AN77
    sections: [Proof]
---

## Proof

The goal is to prove that the axiom of choice is implied by the statement "for every infinite set $A:$ $|A| = |A \times A|$". It is known that the [[well-ordering theorem|0N109NG5ZX]] is equivalent to the axiom of choice; thus it is enough to show that the statement implies that for every set $B$ there exists a [[well-order|01CGSJ0GNQ]].

Since the collection of all [[ordinals|0RDJK7EQYY]] such that there exists a [[surjective function|01RVCMSN5N]] from $B$ to the ordinal is a set, there exists an infinite ordinal, $\beta,$ such that there is no [[surjective function|01RVCMSN5N]] from $B$ to $\beta.$ We assume without loss of generality that the sets $B$ and $\beta$ are [[disjoint|0W4RPA8QH3]]. By the initial assumption, $|B \cup \beta| = |(B \cup \beta) \times (B \cup \beta)|,$ thus there exists a [[bijection|0GG9TVW90M]] $f : B \cup \beta \to (B \cup \beta) \times (B \cup \beta).$

For every $x \in B,$ it is impossible that $\beta \times \{x\} \subseteq f[B],$ because otherwise we could define a surjective function from $B$ to $\beta.$ Therefore, there exists at least one ordinal $\gamma \in \beta$ such that $f(\gamma) \in \beta \times \{x\},$ so the set $S_x = \{\gamma : f(\gamma) \in \beta \times \{x\}\}$ is not empty.

We can define a new function: $g(x) = \min S_x.$ This function is well defined since $S_x$ is a non-empty set of ordinals, and so has a minimum. For every $x, y \in B, x \neq y$ the sets $S_x$ and $S_y$ are disjoint. Therefore, we can define a well order on $B,$ for every $x, y \in B$ we define $x \leq y \iff g(x) \leq g(y),$ since the image of $g,$ that is, $g[B]$ is a set of ordinals and therefore well ordered.
