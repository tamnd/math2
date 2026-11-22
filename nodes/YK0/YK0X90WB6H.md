---
tag: YK0X90WB6H
kind: example
name: Functions as sums of even and odd functions
msc: ["15A03", "26A06"]
topics: [QHKTJ89V6S]
audience: ug1
instance_of: [0XYYT5KNTX]
illustrates: [20A0K3KBZD]
uses: [0XE690QF65, 041JTZCK9Q, 0EPTJA5QV4]
sources:
  - url: https://en.wikipedia.org/wiki/Even_and_odd_functions
    locator: Even-odd decomposition
  - book: isbn:9783031410253
    locator: Section 1C
---

## Example

Let $V$ be the space of all functions $\R \to \R$, with pointwise addition and scalar multiplication.
Let $E$ be the set of [[even functions|0XE690QF65]], with $f(-x) = f(x)$ for all $x$, and let $O$ be the set of odd functions, with $f(-x) = -f(x)$ for all $x$.
We check that $V = E \oplus O$.

1. $E$ and $O$ are [[subspaces|0EPTJA5QV4]].
   The zero function is even and odd.
   If $f$ and $g$ are even and $a \in \R$, then $(f + ag)(-x) = f(-x) + a g(-x) = f(x) + a g(x)$, so $f + ag$ is even.
   The same computation with a sign shows that $O$ is closed under these operations.
2. Intersection.
   If $f \in E \cap O$, then $f(x) = f(-x) = -f(x)$ for each $x$, so $2 f(x) = 0$ and $f(x) = 0$.
   Hence $E \cap O = \{0\}$, and the sum $E + O$ is [[direct|041JTZCK9Q]] by the [[criteria for two subspaces|20A0K3KBZD]].
3. Sum.
   For $f \in V$, define
$$f_e(x) = \tfrac{1}{2}\bigl(f(x) + f(-x)\bigr), \qquad f_o(x) = \tfrac{1}{2}\bigl(f(x) - f(-x)\bigr).$$
4. Then $f_e(-x) = \tfrac{1}{2}(f(-x) + f(x)) = f_e(x)$, so $f_e \in E$.
   Also $f_o(-x) = \tfrac{1}{2}(f(-x) - f(x)) = -f_o(x)$, so $f_o \in O$.
5. Adding the two formulas gives $f_e + f_o = f$.
   So every function lies in $E + O$, and $V = E \oplus O$.

## Remarks

### Two concrete splittings

For $f(x) = e^x$, the formulas give
$$f_e(x) = \frac{e^x + e^{-x}}{2} = \cosh x, \qquad f_o(x) = \frac{e^x - e^{-x}}{2} = \sinh x.$$
For a polynomial such as $p(x) = 1 + 2x + 3x^2 + 4x^3$, the even part keeps the even powers and the odd part keeps the odd powers: $p_e = 1 + 3x^2$ and $p_o = 2x + 4x^3$.
Check: $p(-x) = 1 - 2x + 3x^2 - 4x^3$, so $\tfrac12 (p(x) + p(-x)) = 1 + 3x^2$.

### Where the number 2 matters

Steps 2 and 3 divide by $2$.
For functions from a field of characteristic $2$ to itself, we have $-x = x$, so every function is both even and odd, and $E = O = V$.
Then the sum $E + O$ is far from direct.

### The same pattern elsewhere

The same construction splits square matrices into symmetric and skew-symmetric parts, with the transpose in place of $x \mapsto -x$: $A = \tfrac12 (A + A^{\mathsf{T}}) + \tfrac12 (A - A^{\mathsf{T}})$.
In both cases there is a linear map $S$ with $S^2 = I$, and the space splits into the vectors with $Sv = v$ and those with $Sv = -v$.

## Explanations

### L1 human

Each function is the sum of a part that looks the same in a mirror at $x = 0$, and a part that flips sign in that mirror.
There is only one way to split it like this.
For example, $e^x$ splits into $\cosh x$, which is even, and $\sinh x$, which is odd.

### L2 human

Where do the formulas in step 3 come from?
Suppose $f = g + h$ with $g$ even and $h$ odd.
Replacing $x$ by $-x$ gives $f(-x) = g(x) - h(x)$.
Adding the two equations gives $f(x) + f(-x) = 2 g(x)$, and subtracting them gives $f(x) - f(-x) = 2 h(x)$.
So $g = f_e$ and $h = f_o$ are forced, which proves the uniqueness of the splitting a second time, without the intersection test.
This "assume a splitting and solve for it" method is the typical way to find the parts of a direct sum decomposition.
