---
tag: WTRZG7SQM2
kind: example
name: A satisfiable set of propositional formulas is consistent
msc: ["03B05"]
topics: [H8QZY0RZXZ]
audience: ug2
instance_of: [VM8TQ70CVJ]
uses: [VM8TQ70CVJ, QN7M1JCGT9, 05RSK4Q657, 4A84VHDTHV]
sources:
  - url: https://en.wikipedia.org/wiki/Consistency
    locator: lead section
  - url: https://en.wikipedia.org/wiki/Satisfiability
    locator: lead section
---

## Example

Let $\Gamma = \{ p \lor q, \; p \to r, \; \lnot q \}$, a set of three formulas of [[propositional logic|09K9MWD2QQ]] in the variables $p$, $q$, $r$.
We show first that $\Gamma$ is [[satisfiable|QN7M1JCGT9]], and then that $\Gamma$ is [[consistent|VM8TQ70CVJ]] in the syntactic sense.

First we find a valuation.

1. The formula $\lnot q$ is true only when $q$ is false.
   So every satisfying valuation has $v(q) = \mathsf{F}$.
2. The formula $p \lor q$ is true only when $p$ or $q$ is true.
   Since $q$ is false, $v(p) = \mathsf{T}$.
3. The formula $p \to r$ is false only when $p$ is true and $r$ is false.
   Since $p$ is true, $v(r) = \mathsf{T}$.
4. So the only candidate is $v(p) = \mathsf{T}$, $v(q) = \mathsf{F}$, $v(r) = \mathsf{T}$.

Next we check it with the [[truth tables|05RSK4Q657]] of the connectives.

5. $v(p \lor q) = \mathsf{T} \lor \mathsf{F} = \mathsf{T}$.
6. $v(p \to r) = (\mathsf{T} \to \mathsf{T}) = \mathsf{T}$.
7. $v(\lnot q) = \lnot \mathsf{F} = \mathsf{T}$.
8. So $v$ makes every member of $\Gamma$ true, and $\Gamma$ is satisfiable.

Finally we pass from satisfiability to consistency.

9. Suppose that $\Gamma \vdash \varphi$ and $\Gamma \vdash \lnot\varphi$ for some formula $\varphi$, in a sound proof system such as the [[Hilbert system for propositional logic|HZCFTQDRA5]].
10. By [[soundness|4A84VHDTHV]], every valuation that makes all members of $\Gamma$ true makes $\varphi$ true and $\lnot\varphi$ true.
11. The valuation $v$ makes all members of $\Gamma$ true, so $v(\varphi) = \mathsf{T}$ and $v(\lnot\varphi) = \mathsf{T}$.
12. This is impossible, because $v(\lnot\varphi) = \mathsf{T}$ means $v(\varphi) = \mathsf{F}$.
    So no such $\varphi$ exists, and $\Gamma$ is consistent.

## Remarks

Steps 1 to 8 are semantic, and steps 9 to 12 move the result to the syntactic side with soundness.
The method needs one valuation, not a search through all derivations.
Steps 1 to 3 also show that $v$ is the only satisfying valuation, since each step was forced.

If we add the formula $\lnot r$, then step 3 conflicts with it, so $\Gamma \cup \{ \lnot r \}$ has no satisfying valuation.
By the completeness theorem for propositional logic, $\Gamma \cup \{ \lnot r \}$ is then inconsistent, and indeed $\Gamma \vdash r$.
If we instead add a fourth variable $s$ and the formula $s$, the set stays consistent: extend $v$ by $v(s) = \mathsf{T}$.

## Explanations

### L1 human

Take three statements: "$p$ or $q$", "if $p$ then $r$", and "not $q$".
We look for a way to make all three true at once.
"Not $q$" forces $q$ false, then "$p$ or $q$" forces $p$ true, then "if $p$ then $r$" forces $r$ true.
With these choices all three statements are true.
A set of statements that can all be true together cannot prove a contradiction, because correct proofs never lead from true statements to false ones.

### L2 human

We show that $\Gamma \nvdash \lnot r$, as a typical use of the valuation.

1. Suppose $\Gamma \vdash \lnot r$.
2. By soundness, $v(\lnot r) = \mathsf{T}$, since $v$ satisfies $\Gamma$.
3. But $v(r) = \mathsf{T}$, so $v(\lnot r) = \mathsf{F}$, a contradiction.
4. So $\Gamma \nvdash \lnot r$, and $\Gamma \cup \{ r \}$ is consistent.

The typical use is this: one valuation that satisfies the premises and falsifies a formula shows that the formula is not derivable.
A trap is to use a valuation that falsifies the formula but does not satisfy all premises, since such a valuation shows nothing.
