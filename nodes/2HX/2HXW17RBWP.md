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

The integer square root of $45$ is $6$, because $36 \le 45 < 49$.
You can find it from the root of $\lfloor 45/4 \rfloor = 11$, which is $3$: the root of $45$ is $2 \cdot 3$ or $2 \cdot 3 + 1$, and a test of $7^2 = 49$ picks $6$.
This recursion divides by $4$ at each step, and it is exactly the shape of a proof by polynomial induction.

We show that the theory $S^1_2$ of [[bounded arithmetic|A2CFPP8JMN]] proves that every number has an integer square root:
$$S^1_2 \vdash \forall x \, \exists y \le x \, (y \cdot y \le x \land x < (y + 1) \cdot (y + 1)).$$
Let $A(x)$ be the formula after $\forall x$.
We use two facts about $S^1_2$.
First, $S^1_2$ proves every axiom of $T^0_2$, which has induction for sharply bounded formulas, so $S^1_2$ proves the usual laws of a discretely ordered semiring.
Second, the axioms $\mathsf{BASIC}$ give $x = 2 \lfloor x/2 \rfloor$ or $x = 2 \lfloor x/2 \rfloor + 1$ for every $x$.

1. The formula $A$ has one bounded existential quantifier in front of an open formula, so $A$ is in $\Sigma^b_1$.
2. Let $B(x)$ be $A(x) \land A(\lfloor x/2 \rfloor)$.
   A conjunction of two $\Sigma^b_1$ formulas is $\Sigma^b_1$ after the prenex operations, so $B$ is in $\Sigma^b_1$.
3. For the base case, $B(0)$ holds, since $\lfloor 0/2 \rfloor = 0$ and $y = 0$ gives $0 \cdot 0 \le 0 < 1 \cdot 1$.
4. For the induction step, assume $B(\lfloor x/2 \rfloor)$.
   Its first conjunct is $A(\lfloor x/2 \rfloor)$, which is the second conjunct of $B(x)$.
5. Its second conjunct is $A(x')$ with $x' = \lfloor \lfloor x/2 \rfloor / 2 \rfloor$.
   Two uses of the $\mathsf{BASIC}$ fact give $x = 4x' + r$ with $r \le 3$.
6. Let $y'$ be a root of $x'$, so $y'^2 \le x' < (y' + 1)^2$.
   The second inequality gives $x' \le y'^2 + 2y'$.
7. For a lower estimate, multiply the first inequality by $4$:
   $$(2y')^2 = 4y'^2 \le 4x' \le x.$$
8. For an upper estimate, use step 6 and $r \le 3$:
   $$x \le 4x' + 3 \le 4y'^2 + 8y' + 3 < 4y'^2 + 8y' + 4 = (2y' + 2)^2.$$
9. If $(2y' + 1)^2 \le x$, let $y = 2y' + 1$, and otherwise let $y = 2y'$.
   In both cases $y^2 \le x < (y + 1)^2$, by steps 7 and 8.
10. The bound $y \le x$ holds: if $y = 0$ it is $0 \le x$, and if $y \ge 1$ then $y \le y \cdot y \le x$.
    So $A(x)$ holds, and with step 4, $B(x)$ holds.
11. Steps 3 to 10 give $B(0)$ and $\forall x \, (B(\lfloor x/2 \rfloor) \to B(x))$.
    The $\Sigma^b_1$-$\mathsf{PIND}$ axiom for $B$ gives $\forall x \, B(x)$, and so $\forall x \, A(x)$.

## Remarks

The proof uses polynomial induction, which halves $x$ at each step, so on input $x$ it unfolds into about $\lvert x \rvert$ steps.
By [[Buss's witnessing theorem|RH4R7GTTAX]], it gives a polynomial-time algorithm for the root: compute the root of $\lfloor x/4 \rfloor$, double it, and test one candidate.
The trick of step 2 lets the induction go down by a factor of $4$, although $\mathsf{PIND}$ only halves.
For cube roots the same proof works with $\lfloor x/8 \rfloor$ and the formula $A(x) \land A(\lfloor x/2 \rfloor) \land A(\lfloor x/4 \rfloor)$.

What changes with ordinary induction?
Induction from $x$ to $x + 1$ on the $\Sigma^b_1$ formula $A$ would also prove the statement, in $T^1_2$.
But that proof has $x$ steps, exponentially many in $\lvert x \rvert$, so it does not carry a fast algorithm in the same direct way.
Watch out: $S^1_2$ has polynomial induction only for $\Sigma^b_1$ formulas, so the same proof applied to a $\Pi^b_1$ formula, or to a formula with an unbounded quantifier, is not a proof in $S^1_2$.

## Explanations

### L1 human

The integer square root of a number is the largest whole number whose square is at most that number.
For example, the root of $45$ is $6$, since $36 \le 45 < 49$.
The proof finds it from the root of a number about four times smaller.
The root of $11$ is $3$, and $45 = 4 \cdot 11 + 1$, so the root of $45$ is $6$ or $7$.
Since $7 \cdot 7 = 49$ is more than $45$, the root is $6$.
Each step divides the number by $4$, so a number with $20$ binary digits needs only about $10$ steps.

### L2 human

We run the recursion of the proof on $x = 45$.
First we divide by $4$ until we reach $0$:
$$\lfloor 45/4 \rfloor = 11, \quad \lfloor 11/4 \rfloor = 2, \quad \lfloor 2/4 \rfloor = 0.$$
The root of $0$ is $0$.
For $2$ the candidates are $0$ and $1$, and since $1^2 \le 2$, the root is $1$.
For $11$ the candidates are $2$ and $3$, and since $3^2 = 9 \le 11$, the root is $3$.
For $45$ the candidates are $6$ and $7$, and since $7^2 = 49 > 45$, the root is $6$.
Check: $6^2 = 36 \le 45 < 49 = 7^2$.

The typical use of such a proof is to show at once that a function is polynomial-time computable and that $S^1_2$ proves its basic properties.
The recursion that the proof hides is the algorithm, and its depth is the number of base-$4$ digits of the input.
