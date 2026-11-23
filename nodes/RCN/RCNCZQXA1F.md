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

The claim is that for every [[real number|08J2M1JYAG]] $x$,
$$x^2 = x \iff (x = 0 \text{ or } x = 1).$$
We plan the proof with the [[moves for each logical form|872K5XB580]].
The claim has a "for all", a [[biconditional|0S6GMNJ62Y]], and an "or" that is a goal in one direction and a given in the other.

1. The goal "for all $x$" gives the sentence "Let $x$ be a real number."
2. The goal "$P \iff Q$" splits into $P \Rightarrow Q$ and $Q \Rightarrow P$; in Lean this is `constructor`.
3. In the direction ($\Rightarrow$) the goal is "$x = 0$ or $x = 1$", so we assume that $x \ne 0$ and prove $x = 1$.
4. In the direction ($\Leftarrow$) the given is "$x = 0$ or $x = 1$", so we use [[proof by cases|0WCP0PVET6]]; in Lean this is `rcases h with h | h`.

The final proof reads as follows.

> Let $x$ be a real number.
> ($\Rightarrow$) Suppose that $x^2 = x$.
> We show that $x = 0$ or $x = 1$.
> If $x = 0$, we are done, so suppose that $x \ne 0$.
> From $x^2 = x$ we get $x^2 - x = 0$, that is, $x(x - 1) = 0$.
> Since $x \ne 0$, we may divide by $x$, and we get $x - 1 = 0$, so $x = 1$.
> ($\Leftarrow$) Suppose that $x = 0$ or $x = 1$.
> If $x = 0$, then $x^2 = 0 = x$.
> If $x = 1$, then $x^2 = 1 = x$.
> Both directions hold, so $x^2 = x$ if and only if $x = 0$ or $x = 1$.
> $\square$

We check each move.

1. The direction ($\Rightarrow$) proves "$x = 0$ or $x = 1$" in the form "if $x \ne 0$, then $x = 1$".
   This form is correct, because an "or" fails only when both parts fail.
2. The direction ($\Rightarrow$) uses the assumption $x \ne 0$ exactly at the division by $x$.
3. The direction ($\Leftarrow$) has one case for each part of the given "or", and it proves the same goal $x^2 = x$ in each case.

Check: $0^2 = 0$ and $1^2 = 1$, while $x = 2$ gives $x^2 = 4 \ne 2$, as the claim predicts.

## Remarks

A goal "or" has a second move: prove one part outright.
That works only when you already know which part holds, and here you do not know it before you use the hypothesis.
In Lean the direction ($\Rightarrow$) can start with `by_cases hx : x = 0`, then use `left` in the first case and `right` in the second.

The division step needs that a nonzero $x$ has an inverse.
In the integers modulo $6$ this fails: $3 \ne 0$ but $3^2 = 9 = 3$, because $9 - 3$ is a multiple of $6$, and $3$ has no inverse modulo $6$.
So the claim is false there, and the proof shows exactly which step breaks.

## Explanations

### L1 human

Which numbers are equal to their own square?
Testing gives $0 \times 0 = 0$ and $1 \times 1 = 1$, while $2 \times 2 = 4$ is not $2$.
The claim says that $0$ and $1$ are the only such numbers.
The proof has two halves: the numbers $0$ and $1$ work, and no other number works.
For the second half we take a number $x$ other than $0$ with $x \times x = x$, and we divide both sides by $x$ to get $x = 1$.

### L2 human

We plan a proof that for all real $a$ and $b$, $ab = 0$ if and only if $a = 0$ or $b = 0$.
We let $a$ and $b$ be real numbers, and the equivalence gives two directions.

For ($\Rightarrow$), suppose $ab = 0$; the goal is an "or", so we assume $a \ne 0$ and prove $b = 0$.
Since $a \ne 0$, the number $\frac1a$ exists, and
$$b = \frac1a (ab) = \frac1a \cdot 0 = 0.$$
For ($\Leftarrow$), the given "or" gives two cases.
If $a = 0$, then $ab = 0 \cdot b = 0$, and if $b = 0$, then $ab = a \cdot 0 = 0$.

The same moves classify the solutions of any equation that factors.
Watch out: a proof of "$Q_1$ or $Q_2$" that shows $Q_1$ in some cases must still treat the remaining cases.
