---
tag: CVVR1EZYHE
kind: example
name: Solving x^2 = x for a nonzero real number by disjunctive syllogism
msc: ["03B05", "97E30"]
topics: [PM1AYWABA7]
audience: school
instance_of: [6EFJF9NAYX]
uses: [6EFJF9NAYX, 0F72FK8EKB, 08J2M1JYAG]
sources:
  - url: https://en.wikipedia.org/wiki/Disjunctive_syllogism
    locator: lead section
  - book: isbn:9781108439534
    locator: Section 3.5
---

## Example

Let $x$ be a [[real number|08J2M1JYAG]] with $x^2 = x$ and $x \neq 0$.
We show that $x = 1$, and we mark the step that uses [[disjunctive syllogism|6EFJF9NAYX]].

1. Subtract $x$ from both sides of $x^2 = x$ to get $x^2 - x = 0$.
2. Factor the left side: $x^2 - x = x(x - 1)$, so $x(x - 1) = 0$.
3. A product of two real numbers is $0$ only when one of the factors is $0$.
   So $x = 0$ or $x - 1 = 0$.
4. Let $p$ be "$x = 0$" and $q$ be "$x = 1$".
   Step 3 is the [[disjunction|0F72FK8EKB]] $p \lor q$.
5. The hypothesis $x \neq 0$ is the statement $\neg p$.
6. Disjunctive syllogism with the premises $p \lor q$ and $\neg p$ gives $q$, so $x = 1$.

Check: $1^2 = 1$ and $1 \neq 0$, so $x = 1$ satisfies both conditions.

## Remarks

The example shows the typical use of the rule: an equation produces a list of cases, and a hypothesis removes every case but one.

Without the hypothesis $x \neq 0$, step 6 is impossible, and the equation keeps its two solutions $0$ and $1$.
With the hypothesis $x \neq 1$ instead, the symmetric form of the rule (from $p \lor q$ and $\neg q$, conclude $p$) gives $x = 0$.

The rule removes only the disjunct that you deny.
For $x^3 = x$ the factorization $x(x - 1)(x + 1) = 0$ gives three cases, $x = 0$, $x = 1$ or $x = -1$.
The hypothesis $x \neq 0$ removes one case and leaves $x = 1 \lor x = -1$, and you need a further fact to decide between these two.

## Explanations

### L1 human

A number $x$ equals its own square.
Only two numbers do this, $0$ and $1$, because $0 \cdot 0 = 0$ and $1 \cdot 1 = 1$.
You are also told that $x$ is not $0$.
So $x$ must be $1$.
The step "it is one of two, it is not the first, so it is the second" is disjunctive syllogism.

### L2 human

Solve $x^2 = 4x$ for a real number $x$ with $x > 1$.
Bring everything to one side and factor:
$$x^2 - 4x = x(x - 4) = 0.$$
One factor is $0$, so $x = 0 \lor x = 4$.
The hypothesis $x > 1$ gives $x \neq 0$, and disjunctive syllogism gives $x = 4$.
Check: $4^2 = 16 = 4 \cdot 4$ and $4 > 1$.
Side conditions such as positivity often remove the unwanted roots in this way.
Watch out: dividing $x^2 = 4x$ by $x$ without knowing $x \neq 0$ loses the root $x = 0$, and the hypothesis $x \neq 0$ is exactly the premise $\neg p$ that the rule needs.
