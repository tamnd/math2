---
tag: H4B12PWDE6
kind: example
name: Conjunction and disjunction do not form a functionally complete set
msc: ["03B05", "06E30"]
topics: [JDK63589SA]
audience: ug1
not_instance_of:
  - target: TDZVCWYJ9F
    note: every formula built from variables with ∧ and ∨ only is monotone and takes the value 1 when all variables are 1, so the negation ¬p is not expressible
uses: [025YZN3VJW, 0F72FK8EKB, 12MQ2NJ29A, 0A7KV2WB7A]
sources:
  - url: https://en.wikipedia.org/wiki/Functional_completeness
    locator: Introduction
  - url: https://en.wikipedia.org/wiki/Monotonic_function
    locator: In Boolean functions
---

## Example

We show that the set $\set{\land, \lor}$ of [[conjunction|025YZN3VJW]] and [[disjunction|0F72FK8EKB]] is not [[functionally complete|TDZVCWYJ9F]].
For assignments $a, b \in \set{0,1}^n$ write $a \leq b$ when $a_i \leq b_i$ for each $i$.

**Claim.** Let $\varphi$ be a formula over $\set{\land, \lor}$ with variables among $p_1, \ldots, p_n$, and let $f = f_\varphi$ be its truth function.
Then:

- (a) $f(1, \ldots, 1) = 1$;
- (b) $f(0, \ldots, 0) = 0$;
- (c) $f$ is [[monotone|0A7KV2WB7A]]: if $a \leq b$, then $f(a) \leq f(b)$.

We prove the claim by [[structural induction|12MQ2NJ29A]] on $\varphi$.

1. Let $\varphi = p_i$. Then $f(a) = a_i$, so $f(1, \ldots, 1) = 1$ and $f(0, \ldots, 0) = 0$. If $a \leq b$, then $f(a) = a_i \leq b_i = f(b)$.
2. Let $\varphi = \psi \land \chi$, and let $g$, $h$ be the truth functions of $\psi$, $\chi$, with (a), (b), (c) by the induction hypothesis. Then $f(a) = \min(g(a), h(a))$.
3. In the case of step 2: $f(1, \ldots, 1) = \min(1, 1) = 1$ and $f(0, \ldots, 0) = \min(0, 0) = 0$. If $a \leq b$, then $g(a) \leq g(b)$ and $h(a) \leq h(b)$, so $\min(g(a), h(a)) \leq \min(g(b), h(b))$.
4. Let $\varphi = \psi \lor \chi$, with $g$, $h$ as before. Then $f(a) = \max(g(a), h(a))$, and the same three checks hold with $\max$ in place of $\min$.
5. This proves the claim for all formulas over $\set{\land, \lor}$.

**Conclusion.**

6. The negation $\neg p_1$, as a function of one variable, sends $1$ to $0$.
7. By (a), every formula over $\set{\land, \lor}$ in the variable $p_1$ sends $1$ to $1$. So no such formula expresses $\neg p_1$.
8. So $\set{\land, \lor}$ is not functionally complete. Each of (a), (b) and (c) alone gives this conclusion, since $\neg$ fails all three.

## Remarks

Adding the constants $\top$ and $\bot$ still does not give completeness, because (c) still holds.
In fact the formulas over $\set{\land, \lor, \top, \bot}$ express exactly the monotone functions.
The proof: let $f$ be monotone and not the constant $0$, and let $\psi = \bigvee_{f(a) = 1} \bigwedge_{a_i = 1} p_i$, where the empty conjunction is $\top$.
If $f(b) = 1$, the term for $a = b$ is true at $b$.
If the term for some $a$ is true at $b$, then $a \leq b$, and so $f(b) \geq f(a) = 1$.
So $\psi$ expresses $f$, and the constant $0$ is expressed by $\bot$.
These are the monotone functions, one of the five maximal classes of [[Post's functional completeness theorem|WGBR7JHBV4]].
The same argument with (a) alone shows that $\set{\to, \lor}$ is not complete.

## Explanations

### L1 human

With "and" and "or" we can only combine conditions; we can never turn a "true" into a "false".
If all the letters are true, then every "and" and every "or" of them is true.
So no formula made from "and" and "or" can mean "not $p$", which is false when $p$ is true.

### L2 human

The method of this proof is general: to show that a set is not complete, find a property that each connective of the set has and that composition keeps, but that negation does not have.

1. Check the property for variables.
2. Check that each connective of the set keeps it.
3. Conclude by structural induction, and find a function without the property.

A trap: it is not enough to try many formulas and fail to find $\neg p$; a proof must cover all formulas, which the induction does.
