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

Try to write $\neg p$ with [[conjunction|025YZN3VJW]] and [[disjunction|0F72FK8EKB]] only.
The candidates $p$, $p \land p$, $p \lor p$ and $p \land (p \lor p)$ all take the value $1$ at $p = 1$, and $\neg p$ takes the value $0$ there.
We show that this always happens, so $\{ \land, \lor \}$ is not [[functionally complete|TDZVCWYJ9F]].

For assignments $a, b \in \{ 0, 1 \}^n$ write $a \leq b$ when $a_i \leq b_i$ for each $i$.
Let $\varphi$ be a formula over $\{ \land, \lor \}$ with variables among $p_1, \ldots, p_n$, and let $f = f_\varphi$ be its truth function.
We claim three things.
First, $f(1, \ldots, 1) = 1$.
Second, $f(0, \ldots, 0) = 0$.
Third, $f$ is [[monotone|0A7KV2WB7A]]: if $a \leq b$, then $f(a) \leq f(b)$.

We prove the claim by [[structural induction|12MQ2NJ29A]] on $\varphi$.

1. Let $\varphi = p_i$.
   Then $f(a) = a_i$, so $f(1, \ldots, 1) = 1$ and $f(0, \ldots, 0) = 0$.
   If $a \leq b$, then $f(a) = a_i \leq b_i = f(b)$.
2. Let $\varphi = \psi \land \chi$, and let $g$ and $h$ be the truth functions of $\psi$ and $\chi$, which have the three properties by the induction hypothesis.
   Then $f(a) = \min(g(a), h(a))$.
3. In the case of step 2, $f(1, \ldots, 1) = \min(1, 1) = 1$ and $f(0, \ldots, 0) = \min(0, 0) = 0$.
   If $a \leq b$, then $g(a) \leq g(b)$ and $h(a) \leq h(b)$, so $\min(g(a), h(a)) \leq \min(g(b), h(b))$.
4. Let $\varphi = \psi \lor \chi$, with $g$ and $h$ as before.
   Then $f(a) = \max(g(a), h(a))$, and the same three checks hold with $\max$ in place of $\min$.
5. This proves the claim for all formulas over $\{ \land, \lor \}$.
6. The negation $\neg p_1$, as a function of one variable, sends $1$ to $0$.
7. By the first property, every formula over $\{ \land, \lor \}$ in the variable $p_1$ sends $1$ to $1$.
   So no such formula expresses $\neg p_1$.
8. So $\{ \land, \lor \}$ is not functionally complete.
   Each of the three properties alone gives this conclusion, since $\neg$ fails all three.

## Remarks

Adding the constants $\top$ and $\bot$ still does not give completeness, because the formulas stay monotone.
In fact the formulas over $\{ \land, \lor, \top, \bot \}$ express exactly the monotone functions.
To see this, let $f$ be monotone and not the constant $0$, and let
$$\psi = \bigvee_{f(a) = 1} \ \bigwedge_{a_i = 1} p_i,$$
where the empty conjunction is $\top$.
If $f(b) = 1$, the term for $a = b$ is true at $b$.
If the term for some $a$ is true at $b$, then $a \leq b$, and so $f(b) \geq f(a) = 1$.
So $\psi$ expresses $f$, and the constant $0$ is expressed by $\bot$.
The monotone functions form one of the five maximal classes of [[Post's functional completeness theorem|WGBR7JHBV4]].

The same argument with the first property alone shows that $\{ \to, \lor \}$ is not complete, since $1 \to 1 = 1$ and $1 \lor 1 = 1$.

## Explanations

### L1 human

With "and" and "or" we can only combine conditions, and we can never turn a "true" into a "false".
If all the letters are true, then every "and" and every "or" of them is true.
So no formula made from "and" and "or" can mean "not $p$", which is false when $p$ is true.

### L2 human

The method of this proof is general.
To show that a set is not complete, find a property that each connective of the set has and that composition keeps, but that negation does not have.
Check the property for variables, check that each connective of the set keeps it, and conclude by structural induction.
Then name one function without the property.
Watch out: it is not enough to try many formulas and fail to find $\neg p$.
A proof must cover all formulas, and the induction does this.
