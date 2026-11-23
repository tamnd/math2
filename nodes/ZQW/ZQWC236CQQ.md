---
tag: ZQWC236CQQ
kind: example
name: Discovery of the BBP formula for pi
msc: ["11Y60", "00A35"]
topics: [DME0TPC348]
audience: ug2
instance_of: [BPEPTN0TT9]
uses: [BPEPTN0TT9, 0C1VYVNV2N]
sources:
  - url: https://en.wikipedia.org/wiki/Bailey%E2%80%93Borwein%E2%80%93Plouffe_formula
    locator: lead section
  - url: https://en.wikipedia.org/wiki/Integer_relation_algorithm
    locator: lead section
---

## Example

Start with one term you can check by hand.
The fraction
$$4 - \frac{2}{4} - \frac{1}{5} - \frac{1}{6} = \frac{120 - 15 - 6 - 5}{30} = \frac{94}{30} = \frac{47}{15} = 3.1333\ldots$$
is already close to [[$\pi$|0C1VYVNV2N]], and it is the first term of the BBP formula
$$\pi = \sum_{k=0}^{\infty} \frac{1}{16^k}\left(\frac{4}{8k+1} - \frac{2}{8k+4} - \frac{1}{8k+5} - \frac{1}{8k+6}\right).$$
Simon Plouffe found this formula by a computer search in 1995, and it was proved afterwards.
We follow the chain of [[experimental mathematics|BPEPTN0TT9]]: a question, a computation, a detected relation, a test and a proof.

1. The question.
   A series in powers of $1/16$ could give the hexadecimal digits of $\pi$ at a given position without the earlier digits.
   The series $\ln 2 = \sum_{k \ge 1} 1/(k \, 2^k)$ does this for the binary digits of $\ln 2$.
2. The candidates.
   For $j = 1, \ldots, 8$ put $S_j = \sum_{k \geq 0} 16^{-k}/(8k+j)$.
   A formula of the wanted kind is an integer relation among $\pi, S_1, \ldots, S_8$.
3. The computation.
   Each $S_j$ converges fast, because each term is at most $1/16$ of the one before, so all nine numbers are cheap to compute to many digits.
4. The detection.
   An integer relation algorithm applied to $(\pi, S_1, \ldots, S_8)$ finds the vector $(1, -4, 0, 0, 2, 1, 1, 0, 0)$.
   This means $\pi = 4S_1 - 2S_4 - S_5 - S_6$, which is the formula above.
5. The test.
   Run the search again at a higher precision and check that it returns the same vector.
   Then compute both sides with many more digits than the search used, and check that they agree to the last digit.
   A spurious relation found at low precision does not survive this test.
6. The proof, part 1.
   For $j \geq 1$, $\dfrac{16^{-k}}{8k+j} = (\sqrt2)^{j} \displaystyle\int_0^{1/\sqrt2} x^{8k+j-1}\,dx$, because $(1/\sqrt2)^{8k} = 16^{-k}$.
   Summing the geometric series in $x^8$ gives $S_j = (\sqrt2)^j \displaystyle\int_0^{1/\sqrt2} \frac{x^{j-1}}{1 - x^8}\,dx$.
7. The proof, part 2.
   The substitution $x = y/\sqrt2$ gives $S_j = \displaystyle\int_0^1 \frac{16\, y^{j-1}}{16 - y^8}\,dy$, so $4S_1 - 2S_4 - S_5 - S_6 = \displaystyle\int_0^1 \frac{16(4 - 2y^3 - y^4 - y^5)}{16 - y^8}\,dy$.
8. The proof, part 3.
   The factorizations $4 - 2y^3 - y^4 - y^5 = -(y-1)(y^2+2)(y^2+2y+2)$ and $16 - y^8 = (2-y^2)(2+y^2)(y^2+2y+2)(y^2-2y+2)$ reduce the integrand to $\dfrac{16(y-1)}{(y^2-2)(y^2-2y+2)}$.
9. The proof, part 4.
   Partial fractions give $\dfrac{4y}{y^2-2} + \dfrac{8 - 4y}{y^2-2y+2}$.
   The first term integrates over $[0,1]$ to $-2\ln 2$.
   The second is $\dfrac{-2(2y-2) + 4}{(y-1)^2 + 1}$, and it integrates to $2\ln 2 + 4 \cdot \frac{\pi}{4} = 2\ln 2 + \pi$.
10. The sum of the two integrals is $\pi$, which proves the formula.

Steps 3 to 5 made the formula almost certain, and they proved nothing.
Agreement to any number of digits is evidence, not a proof, and steps 6 to 10 are the proof.

## Remarks

### Checks inside the proof

The exchange of sum and integral in step 6 is valid, because the geometric series converges uniformly on $[0, 1/\sqrt2]$.
The partial fractions of step 9 can be checked by multiplying out:
$$4y(y^2-2y+2) + (8-4y)(y^2-2) = 16y - 16.$$
The factorization of step 8 can be checked the same way, since $(y^2+2)(y^2+2y+2) = y^4 + 2y^3 + 4y^2 + 4y + 4$.

### What came out of it

Plouffe found the relation with the PSLQ algorithm, and David Bailey, Peter Borwein and Plouffe published the formula in *Mathematics of Computation* in 1997.
The formula gives an algorithm that computes the $n$-th hexadecimal digit of $\pi$ with little memory and without the earlier digits.
The proof uses only first-year calculus, but it was found after the formula was known: the search told the authors what to prove.

### Watch out

Agreement to $10$ digits is not the test of step 5.
An integer relation algorithm can return a false relation when the precision is too low for the size of the coefficients and the number of constants.
So the test needs many more digits than the relation has, and a repeat at a higher precision.

### Try it

Add the term $k = 1$ to $47/15$.
It is $\frac{1}{16}\left(\frac49 - \frac{2}{12} - \frac{1}{13} - \frac{1}{14}\right) = 0.0080891\ldots$, and the sum $3.1414224\ldots$ differs from $\pi$ by about $1.7 \cdot 10^{-4}$.

## Explanations

### L1 human

Mathematicians wanted a new kind of formula for $\pi$.
They did not know what it should look like, so they let a computer try many combinations of simple sums.
The computer found one combination that matched $\pi$ to many digits.
They then checked it with even more digits, and finally proved it with ordinary calculus.
The computer found the formula, and people proved it.

### L2 human

We check the formula numerically by its partial sums.

1. The term $k = 0$ gives $47/15 = 3.1333\ldots$, with error about $8 \cdot 10^{-3}$.
2. Adding $k = 1$ gives $3.1414224\ldots$, with error about $1.7 \cdot 10^{-4}$.
3. Adding $k = 2$ gives $3.1415873\ldots$, with error about $5.3 \cdot 10^{-6}$.
4. The sum of the terms from $k = 0$ to $k = 5$ is $3.141592653\ldots$, with error about $3.6 \cdot 10^{-10}$.

Each new term gains more than one decimal digit, because of the factor $16^{-k}$.
The values $S_1 = 1.0071844764\ldots$, $S_4 = 0.2554128118\ldots$, $S_5 = 0.2050025576\ldots$ and $S_6 = 0.1713170706\ldots$ give $4S_1 - 2S_4 - S_5 - S_6 = 3.1415926535\ldots$.
The typical use: a quick check at low precision before a long computation at high precision.
