---
tag: 2HXW17RBWP
kind: example
name: Integer square roots in S^1_2
msc: ["03F30"]
topics: [RA380RWEC0]
audience: research
instance_of: [A2CFPP8JMN]
uses: [A2CFPP8JMN, 1QD0KDDGYJ]
sources:
  - url: https://en.wikipedia.org/wiki/Bounded_arithmetic
    locator: lead section
---

## Example

We show that the theory $S^1_2$ of [[bounded arithmetic|A2CFPP8JMN]] proves that every number has an integer square root:
$$S^1_2 \vdash \forall x \, \exists y \le x \, (y \cdot y \le x \land x < (y + 1) \cdot (y + 1)).$$
Let $A(x)$ be the formula $\exists y \le x \, (y \cdot y \le x \land x < (y + 1) \cdot (y + 1))$.
We use two facts about $S^1_2$.
First, Buss proved that $S^1_2$ proves $T^0_2$, so $S^1_2$ has induction for open formulas and proves the usual laws of a discretely ordered semiring.
Second, the axioms $\mathsf{BASIC}$ give $x = 2 \floor{x/2}$ or $x = 2 \floor{x/2} + 1$ for every $x$.

1. The formula $A$ has one bounded existential quantifier in front of an open formula, so $A \in \Sigma^b_1$.
2. Let $B(x)$ be $A(x) \land A(\floor{x/2})$. A conjunction of two $\Sigma^b_1$ formulas is $\Sigma^b_1$ after prenex operations, so $B \in \Sigma^b_1$.
3. Base: $B(0)$ holds, since $\floor{0/2} = 0$ and $y = 0$ gives $0 \cdot 0 \le 0 < 1 \cdot 1$.
4. Step: assume $B(\floor{x/2})$. Its first conjunct is $A(\floor{x/2})$, the second conjunct of $B(x)$.
5. Its second conjunct is $A(x')$ with $x' = \floor{\floor{x/2}/2}$. Two uses of the $\mathsf{BASIC}$ fact give $x = 4x' + r$ with $r \le 3$.
6. Let $y'$ be the root of $x'$, so $y'^2 \le x' < (y' + 1)^2$, and so $x' \le y'^2 + 2y'$.
7. Then $(2y')^2 = 4y'^2 \le 4x' \le x$.
8. Also $x \le 4x' + 3 \le 4y'^2 + 8y' + 3 < 4y'^2 + 8y' + 4 = (2y' + 2)^2$.
9. If $(2y' + 1)^2 \le x$, let $y = 2y' + 1$; otherwise let $y = 2y'$. In both cases $y^2 \le x < (y + 1)^2$, by steps 7 and 8.
10. The bound $y \le x$ holds: if $y = 0$ it is $0 \le x$, and if $y \ge 1$ then $y \le y \cdot y \le x$. So $A(x)$ holds, and with step 4, $B(x)$ holds.
11. Steps 3 to 10 give $B(0)$ and $\forall x \, (B(\floor{x/2}) \to B(x))$. The $\Sigma^b_1$-$\mathsf{PIND}$ axiom for $B$ gives $\forall x \, B(x)$, and so $\forall x \, A(x)$.

## Remarks

The proof uses polynomial induction, which halves $x$ at each step, so it has about $\abs{x}$ steps on input $x$.
By [[Buss's witnessing theorem|RH4R7GTTAX]], it gives a polynomial-time algorithm for the root: compute the root of $\floor{x/4}$, double it, and test one candidate.
The trick of step 2 lets the induction go down by a factor of $4$ although $\mathsf{PIND}$ only halves.
For cube roots the same proof works with $\floor{x/8}$ and the formula $A(x) \land A(\floor{x/2}) \land A(\floor{x/4})$.
Ordinary induction on $x$ would also prove the statement, in $T^1_2$, but the proof would have $x$ steps and would give no fast algorithm.

## Explanations

### L1 human

The integer square root of $x$ is the largest whole number whose square is at most $x$.
For example, the root of $45$ is $6$, since $36 \le 45 < 49$.
The proof finds it from the root of a number four times smaller.
The root of $11$ is $3$, and $45 = 4 \cdot 11 + 1$, so the root of $45$ is $2 \cdot 3 = 6$ or $2 \cdot 3 + 1 = 7$.
Since $49 > 45$, the root is $6$.
Each step divides the number by $4$, so a number with $20$ binary digits needs only about $10$ steps.

### L2 human

We run the recursion of the proof on $x = 45$.

1. $\floor{45/4} = 11$, $\floor{11/4} = 2$ and $\floor{2/4} = 0$.
2. The root of $0$ is $0$.
3. For $2$: the candidates are $0$ and $1$. Since $1^2 \le 2$, the root is $1$.
4. For $11$: the candidates are $2$ and $3$. Since $3^2 = 9 \le 11$, the root is $3$.
5. For $45$: the candidates are $6$ and $7$. Since $7^2 = 49 > 45$, the root is $6$.

The typical use of such a proof is to show that a function is polynomial-time computable and that $S^1_2$ proves its basic properties.
A trap is to apply $\mathsf{PIND}$ to a $\Pi^b_1$ formula, or to a formula with an unbounded quantifier: $S^1_2$ has polynomial induction only for $\Sigma^b_1$ formulas.
