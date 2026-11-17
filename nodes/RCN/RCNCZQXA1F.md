---
tag: RCNCZQXA1F
kind: example
name: Strategies for an equivalence with a disjunction, x² = x
msc: ["00A35"]
topics: [STSM6PR7TX]
audience: ug1
instance_of: [872K5XB580]
uses: [872K5XB580, 0S6GMNJ62Y, 0WCP0PVET6, 08J2M1JYAG]
sources:
  - book: isbn:9781108439534
    locator: Section 3.5
  - book: isbn:9781108439534
    locator: Section 3.4
---

## Example

The claim is: for every [[real number|08J2M1JYAG]] $x$,
$$x^2 = x \iff (x = 0 \text{ or } x = 1).$$
We plan the proof by the [[strategies for each logical form|872K5XB580]].
The claim has a "for all", a [[biconditional|0S6GMNJ62Y]], and a disjunction that is a goal in one direction and a given in the other.

1. Goal "for all $x$": we write "Let $x$ be a real number."
2. Goal "$P \iff Q$": we prove $P \Rightarrow Q$ and $Q \Rightarrow P$. In Lean this is `constructor`.
3. Direction ($\Rightarrow$), goal "$Q_1$ or $Q_2$": we assume that $Q_1$ fails and prove $Q_2$. Here we assume $x \ne 0$ and prove $x = 1$.
4. Direction ($\Leftarrow$), given "$Q_1$ or $Q_2$": we use [[proof by cases|0WCP0PVET6]], one case for each part. In Lean this is `rcases h with h | h`.

The final proof:

> Let $x$ be a real number.
> ($\Rightarrow$) Suppose that $x^2 = x$.
> We show that $x = 0$ or $x = 1$.
> If $x = 0$, we are done.
> So suppose that $x \ne 0$.
> From $x^2 = x$ we get $x^2 - x = 0$, that is, $x(x - 1) = 0$.
> Since $x \ne 0$, we may divide by $x$, and we get $x - 1 = 0$.
> So $x = 1$.
> ($\Leftarrow$) Suppose that $x = 0$ or $x = 1$.
> Case $x = 0$: then $x^2 = 0 = x$.
> Case $x = 1$: then $x^2 = 1 = x$.
> In both directions the claim holds, so $x^2 = x$ if and only if $x = 0$ or $x = 1$.
> $\square$

We check each strategy.

1. The ($\Rightarrow$) direction proves "$x = 0$ or $x = 1$" by the equivalent form "if $x \ne 0$, then $x = 1$". This form is correct, because "$Q_1$ or $Q_2$" fails only when both parts fail.
2. The ($\Rightarrow$) direction uses the hypothesis $x \ne 0$ exactly at the division by $x$.
3. The ($\Leftarrow$) direction has one case for each part of the given disjunction, and it proves the same goal $x^2 = x$ in each case.
4. Numerical checks: $0^2 = 0$, $1^2 = 1$, and for $x = 2$ we get $x^2 = 4 \ne 2$, as the claim predicts.

## Remarks

1. The goal "or" has a second strategy: prove one part outright. That works only when one part is known to hold, which is not the case here before we use the hypothesis.
2. In Lean the ($\Rightarrow$) direction can use `by_cases hx : x = 0`, then `left` in the first case and `right` in the second case.
3. If we change the field from $\mathbb{R}$ to the integers modulo $6$, the claim fails: $3^2 = 9 = 3$ in $\mathbb{Z}/6\mathbb{Z}$. The division step needs that $x \ne 0$ is invertible, and $3$ is not invertible modulo $6$.
4. The proof of the ($\Rightarrow$) direction also follows from the rule "a product is $0$ only if a factor is $0$". That rule is itself a statement of the form "if $ab = 0$, then $a = 0$ or $b = 0$", proved by the same strategy.

## Explanations

### L1 human

Which numbers are equal to their own square?
Testing gives $0 \times 0 = 0$ and $1 \times 1 = 1$, while $2 \times 2 = 4$ is not $2$.
The claim says that $0$ and $1$ are the only such numbers.
The proof has two halves: the numbers $0$ and $1$ work, and no other number works.
For the second half we take a number $x$ other than $0$ with $x \times x = x$, and divide both sides by $x$ to get $x = 1$.

### L2 human

We plan a proof of "for all real $a$ and $b$: $ab = 0$ if and only if $a = 0$ or $b = 0$".

1. "Let $a$ and $b$ be real numbers." Goal: an equivalence, so two directions.
2. ($\Rightarrow$) Suppose $ab = 0$. Goal "$a = 0$ or $b = 0$": assume $a \ne 0$ and prove $b = 0$.
3. Since $a \ne 0$, the number $\frac1a$ exists, and $b = \frac1a (ab) = \frac1a \cdot 0 = 0$.
4. ($\Leftarrow$) Given "$a = 0$ or $b = 0$": two cases. If $a = 0$, then $ab = 0 \cdot b = 0$. If $b = 0$, then $ab = a \cdot 0 = 0$.
5. Both directions hold, so the equivalence holds.

The typical use of these strategies is any statement that ends in "or", such as the classification of solutions of an equation.
A trap is to prove a goal "$Q_1$ or $Q_2$" by proving $Q_1$ in some cases and forgetting the other cases.
