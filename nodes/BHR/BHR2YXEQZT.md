---
tag: BHR2YXEQZT
kind: example
name: The Gödel chain on the unit interval
msc: ["03B55", "03B50", "06D20"]
topics: [38EQ20GR7M]
audience: grad
instance_of: [474SGS2N0X]
uses: [FA88H7FDPY, NG943XNQWH, JM1XJXWZYH]
sources:
  - url: https://en.wikipedia.org/wiki/G%C3%B6del_logic
    locator: Semantics, Syntax
---

## Example

Let $G = [0, 1]$ with $x \wedge y = \min(x, y)$, $x \vee y = \max(x, y)$ and $\bot = 0$.
Put $x \to y = 1$ if $x \leq y$, and $x \to y = y$ if $x > y$.
A formula is valid in $G$ if it takes the value $1$ under every assignment.

1. $G$ is a [[Heyting algebra|NG943XNQWH]]: if $x \leq y$, every $z$ satisfies $\min(z, x) \leq y$, so the largest such $z$ is $1$.
2. If $x > y$, then $\min(z, x) \leq y$ iff $z \leq y$, so the largest such $z$ is $y$. Hence $x \to y$ is the relative pseudocomplement.
3. Negation is $\neg x = x \to 0$, which is $1$ if $x = 0$, and $0$ otherwise.
4. Prelinearity is valid: either $x \leq y$ and $x \to y = 1$, or $y \leq x$ and $y \to x = 1$. So $(x \to y) \vee (y \to x) = 1$.
5. By [[Heyting algebra semantics|JM1XJXWZYH]], every theorem of [[LC|FA88H7FDPY]] is valid in $G$.
6. Excluded middle fails: at $x = 1/2$, $x \vee \neg x = \max(1/2, 0) = 1/2$.
7. Double negation elimination fails: at $x = 1/2$, $\neg \neg x = 1$, and $1 \to 1/2 = 1/2$.
8. Weak excluded middle holds: if $x = 0$ then $\neg x = 1$, and otherwise $\neg \neg x = 1$.

## Remarks

Dummett proved in 1959 that the formulas valid in $G$ are exactly the theorems of $\mathsf{LC}$.
Any infinite subset of $[0, 1]$ that contains $0$ and $1$ gives the same logic, for instance $\set{0} \cup \set{1/n : n \geq 1}$.
A finite subset with $n + 1$ elements gives a proper extension of $\mathsf{LC}$, the Gödel logic with $n + 1$ values.
In [[many-valued and fuzzy logics|WZP584JQ06]], $G$ is the standard algebra of Gödel fuzzy logic, with $\min$ as its t-norm.

## Explanations

### L1 human

Truth values are numbers between $0$ and $1$, and only their order matters.
An implication is fully true when its premise is no truer than its conclusion.
Otherwise it is as true as its conclusion.

### L2 human

1. To test a formula, consider the order type of the values of its variables.
2. Only finitely many orderings are possible, so a finite check decides validity.
3. Check the value at each ordering with the rules above.

The typical use is the algebraic semantics of $\mathsf{LC}$ and of Gödel fuzzy logic.
A trap: $\neg x$ is not $1 - x$ here; that is the negation of Łukasiewicz logic.
