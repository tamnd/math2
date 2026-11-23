---
tag: 6AFGGTHR4Y
kind: example
name: The copying function is the identity in PV
msc: ["03F30"]
topics: [RA380RWEC0]
audience: research
instance_of: [H1B2VD0KVP]
uses: [FMM44KFZQT, H1B2VD0KVP]
sources:
  - url: https://en.wikipedia.org/wiki/Bounded_arithmetic
    locator: Cook's equational theory
---

## Example

A program that reads the digits of a number and writes each one down again returns its input.
In [[Cook's theory PV|FMM44KFZQT]], with dyadic successors $s_1$ and $s_2$, this program is the function $c$ with the equations below.
$$c(0) = 0, \qquad c(s_1(y)) = s_1(c(y)), \qquad c(s_2(y)) = s_2(c(y)).$$
We give a [[feasibly constructive proof|H1B2VD0KVP]] of the equation $c(y) = y$.

1. The definition of $c$ is legal.
   It has the form of limited recursion on notation with $g = 0$ and $h_i(y, z) = s_i(z)$.
   The bound holds with $l_i = s_i(0)$, since $s_i(z)$ is the concatenation of $z$ and the digit $i$.
2. Let $\mathrm{id}(y) = y$, a $\mathsf{PV}$ symbol given by an initial function or by composition.
3. $\mathsf{PV} \vdash \mathrm{id}(0) = 0$, by the defining equation of $\mathrm{id}$ and substitution.
4. $\mathsf{PV} \vdash \mathrm{id}(s_i(y)) = s_i(y)$, by substitution, and $\mathsf{PV} \vdash s_i(\mathrm{id}(y)) = s_i(y)$, by congruence.
   So $\mathsf{PV} \vdash \mathrm{id}(s_i(y)) = s_i(\mathrm{id}(y))$, by symmetry and transitivity.
5. By steps 3 and 4, $\mathrm{id}$ satisfies the recursion equations of $c$, with the same $g$ and $h_i$.
6. The uniqueness rule of $\mathsf{PV}$ gives $\mathsf{PV} \vdash c(y) = \mathrm{id}(y)$.
7. With the defining equation of $\mathrm{id}$ and transitivity, $\mathsf{PV} \vdash c(y) = y$.

## Remarks

The equation $c(y) = y$ cannot be derived without the uniqueness rule.
Since $y$ is a variable, the defining equations only unfold $c$ on terms of the forms $0$ and $s_i(t)$, and they never reach a bare $y$.
So the uniqueness rule plays the role of induction, in a form that follows the digits of $y$.

What changes when the recursion changes?
For the function $z$ with $z(0) = 0$ and $z(s_i(y)) = z(y)$, the same proof shows $z(y) = 0$.
The constant function $0$ satisfies the same recursion with $h_i(y, w) = w$.

## Explanations

### L1 human

The copying program reads the digits of a number one at a time and writes each digit down again.
It is plain that the output equals the input, but a formal system still needs a rule for this.
The rule of $\mathsf{PV}$ says that two programs that follow the same digit-by-digit recipe give the same output.
For the input $12$, written $2\,1\,2$ in the dyadic digits $1$ and $2$, both programs output $2\,1\,2$.

### L2 human

Let us unfold both sides for $y = 12$.
We have $12 = s_2(5)$, $5 = s_1(2)$ and $2 = s_2(0)$, so the dyadic digits of $12$ are $2\,1\,2$.
Check: $2 \cdot 4 + 1 \cdot 2 + 2 \cdot 1 = 12$.
The defining equations of $c$ unfold one digit at a time:
$$c(12) = s_2(c(5)) = s_2(s_1(c(2))) = s_2(s_1(s_2(c(0)))) = s_2(s_1(s_2(0))) = 12.$$
This computation proves $c(12) = 12$ for the single number $12$, with no use of the uniqueness rule.
Watch out: the computation does not extend to a proof for all $y$, since unfolding only works on numerals, and the variable $y$ needs the rule.
The typical use of the rule is to prove that two algorithms compute the same function for all inputs at once.
