---
tag: QYK67FE6MY
kind: example
name: The quintic has no formula like the quadratic formula
msc: ["00A35", "12F10"]
topics: [X1NSTVGDNQ]
audience: ug2
not_instance_of:
  - target: 8NJ0VN9Z97
    note: the formulas for degrees 2, 3 and 4 suggest the general problem of a formula in radicals for every degree, and the general problem has no solution from degree 5 on
uses: [8NJ0VN9Z97, 0KYZXYDGQZ, FB6J5WAT5V, 4CDFMKKZ01, 163A2WQQJX, J7YS0DA3HQ]
sources:
  - url: https://en.wikipedia.org/wiki/Abel%E2%80%93Ruffini_theorem
    locator: History
---

## Example

The problem is to find a formula for the roots of
$$x^5 + a x^4 + b x^3 + c x^2 + d x + e = 0$$
in terms of the coefficients, using only addition, subtraction, multiplication, division and roots of any order.
We show how [[generalization|8NJ0VN9Z97]] misleads here.

1. The [[quadratic formula|0KYZXYDGQZ]] gives the roots of a quadratic with one square root.
2. The [[cubic formula|FB6J5WAT5V]] of the sixteenth century gives the roots of a cubic with square roots and cube roots.
3. Ferrari's [[quartic formula|4CDFMKKZ01]] reduces a quartic to a cubic and so gives its roots by radicals.
4. The three cases suggest the general problem "for every degree $n$, find a formula by radicals".
   They also suggest a method: reduce degree $n$ to degree $n - 1$.
5. For degree $5$, the reductions that work for degrees $3$ and $4$ do not lead to an equation of lower degree.
6. The general problem has no solution.
   The [[Abel-Ruffini theorem|163A2WQQJX]] states that for every $n \ge 5$ the general polynomial of degree $n$ is not [[solvable by radicals|J7YS0DA3HQ]].
7. Even single equations with rational coefficients fail: the roots of $x^5 - 4x + 2$ cannot be written by radicals.

So the generalization from degrees $2$, $3$ and $4$ led to a false expectation.
Mathematicians worked on the general formula for more than two centuries before Ruffini (1799) and Abel (1824) showed that it does not exist.

## Remarks

The generalization failed because the property the method used does not carry over.
In Galois theory, an equation is solvable by radicals exactly when its Galois group is solvable.
The symmetric groups $S_2$, $S_3$ and $S_4$ are solvable, and $S_5$ is not.
For $x^5 - 4x + 2$ the Galois group is $S_5$.
The polynomial is irreducible by Eisenstein's criterion at the prime $2$, and an irreducible polynomial of prime degree $p$ with exactly two nonreal roots has the group $S_p$.

The failure was still productive.
The attempts at a general formula led Lagrange to study permutations of the roots, and this line of work led to group theory and Galois theory.
Some quintics are solvable by radicals, for example $x^5 - 2$, whose roots are $\sqrt[5]{2}$ times the fifth roots of unity.

## Explanations

### L1 human

For an equation like $x^2 - 5x + 6 = 0$ there is a formula that gives the answers $2$ and $3$, using a square root.
Mathematicians found longer formulas of the same kind for equations with $x^3$ and with $x^4$.
So it seemed natural that equations with $x^5$ have a formula too.
They do not: it was proved that no formula of this kind exists for $x^5$ and higher powers.
Three successes in a row did not mean that a fourth would come.

### L2 human

We check that $f(x) = x^5 - 4x + 2$ has exactly three real roots, as the remarks use.
The values at some integers are
$$f(-2) = -22, \quad f(-1) = 5, \quad f(0) = 2, \quad f(1) = -1, \quad f(2) = 26.$$
The sign changes three times, so $f$ has a root in each of $(-2, -1)$, $(0, 1)$ and $(1, 2)$.
The derivative $f'(x) = 5x^4 - 4$ has exactly two real zeros, so $f$ has at most three real roots.
So $f$ has exactly three real roots and two nonreal roots.

The lesson is typical: a pattern in the degree is a conjecture about all degrees, and it needs the same test as any other conjecture.
Watch out: the theorem does not say that the roots of a quintic cannot be computed.
They can be found to any accuracy by numerical methods, and they can be written with functions other than radicals.
