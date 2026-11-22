---
tag: XMRWZH674S
kind: example
name: The rule [a] ↦ a from Z/6Z to Z is not a function
msc: ["00A35", "11A07"]
topics: [Z2WNQ1DNTX]
audience: ug1
not_instance_of:
  - target: JV68YRB5YZ
    note: the short form has no single correct expansion, so it is an error and not an abuse of notation
uses: [JV68YRB5YZ, 03VFZ2WETT, 0EPAT51DXQ]
sources:
  - url: https://en.wikipedia.org/wiki/Well-defined_expression
    locator: lead section
---

## Example

A student writes "define $\varphi \colon \mathbb{Z}/6\mathbb{Z} \to \mathbb{Z}$ by $\varphi([a]) = a$".
The student treats the class $[a]$ as the integer $a$, as books do in $5 + 4 = 3$ in $\mathbb{Z}/6\mathbb{Z}$.
We show that this time the rule does not define a [[function|0EPAT51DXQ]].

1. The class $[0]$ in [[integers modulo 6|03VFZ2WETT]] is $\{\ldots, -6, 0, 6, 12, \ldots\}$, so $[0] = [6]$.
2. The rule gives
   $$\varphi([0]) = 0, \qquad \varphi([6]) = 6.$$
3. A function assigns one value to each input, but here one input gets the two values $0$ and $6$, and $0 \ne 6$.
4. So $\varphi$ is not well defined, and the formula $\varphi([a]) = a$ names no function.
5. The short form "$\varphi(a) = a$" is not an [[abuse of notation|JV68YRB5YZ]], because no exact form of it is correct.

## Remarks

The example marks the limit of the abuse "a class is named by a member".
The abuse is safe for addition and multiplication, because their results do not depend on the member.
A formula for a map out of $\mathbb{Z}/6\mathbb{Z}$ must give the same value for every member of a class.

A correct version picks one member in a fixed way.
Let $\psi([a])$ be the remainder of $a$ on division by $6$, which lies in $\{0, 1, \ldots, 5\}$.
Then $\psi([0]) = \psi([6]) = 0$, and $\psi$ is a function.
It does not respect addition, though:
$$\psi([3] + [3]) = \psi([0]) = 0, \qquad \psi([3]) + \psi([3]) = 6.$$

## Explanations

### L1 human

On a clock with $6$ hours, the hour $0$ and the hour $6$ are the same hour.
Suppose a rule says "turn the hour into the number you see".
Then the same hour could give $0$ or $6$, depending on how we wrote it.
A rule that gives two answers for one input is not a function.

### L2 human

Test a second rule, $\chi \colon \mathbb{Z}/6\mathbb{Z} \to \mathbb{Z}/3\mathbb{Z}$ with $\chi([a]_6) = [a]_3$, and show that it is well defined.
Suppose $[a]_6 = [b]_6$, so $6$ divides $a - b$.
Since $3$ divides $6$, the number $3$ also divides $a - b$, so $[a]_3 = [b]_3$.
The value does not depend on the member, and $\chi$ is a function.

The reverse rule from $\mathbb{Z}/3\mathbb{Z}$ to $\mathbb{Z}/6\mathbb{Z}$, $[a]_3 \mapsto [a]_6$, fails:
$$[0]_3 = [3]_3, \qquad [0]_6 \ne [3]_6.$$
This check is the first step of every definition of a homomorphism out of a quotient group.
Watch out: a formula that looks natural can still depend on the member, so the check is always needed.
