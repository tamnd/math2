---
tag: V4KAJ332BE
kind: example
name: A structured proof that the square root of 2 is irrational
msc: ["00A35", "11J72"]
topics: [STSM6PR7TX]
audience: research
instance_of: [H2W8D7BMSW]
uses: [H2W8D7BMSW, 0DZGSDHD92, 0J0XBKG64S]
sources:
  - doi: 10.1007/s11784-012-0071-6
    locator: pages 43-63
  - url: https://en.wikipedia.org/wiki/Square_root_of_2
    locator: lead section
---

## Example

*Theorem.* The number $\sqrt{2}$ is irrational.
This is the [[irrationality of the square root of 2|0DZGSDHD92]].
We write a [[proof by contradiction|0J0XBKG64S]] in the hierarchical format.

*Structured proof.*

- `<1>1.` ASSUME: $p$ and $q$ are positive integers with no common factor greater than $1$, and $\sqrt{2} = p/q$. PROVE: FALSE.
    - `<2>1.` $p^2 = 2q^2$. PROOF: square both sides of $\sqrt{2} = p/q$ and multiply by $q^2$.
    - `<2>2.` $p$ is even.
        - `<3>1.` ASSUME: $p$ is odd. PROVE: FALSE. PROOF: write $p = 2j + 1$; then $p^2 = 2(2j^2 + 2j) + 1$ is odd, but $p^2 = 2q^2$ is even by `<2>1`.
        - `<3>2.` Q.E.D. PROOF: by `<3>1`, since every integer is even or odd.
    - `<2>3.` PICK an integer $k$ with $p = 2k$. PROOF: by `<2>2`.
    - `<2>4.` $q^2 = 2k^2$. PROOF: by `<2>1` and `<2>3`, $4k^2 = 2q^2$; divide by $2$.
    - `<2>5.` $q$ is even. PROOF: as in `<2>2`, with `<2>4` in place of `<2>1`.
    - `<2>6.` Q.E.D. PROOF: by `<2>2` and `<2>5`, the number $2$ divides $p$ and $q$, which contradicts the assumption of `<1>1`.
- `<1>2.` Q.E.D. PROOF: suppose that $\sqrt{2}$ is rational. Since $\sqrt{2} > 0$, it is a fraction $p/q$ of positive integers, and we may divide $p$ and $q$ by their greatest common divisor. Then `<1>1` gives FALSE, so $\sqrt{2}$ is irrational.

We check the structure.

1. The top level has two steps. A reader who trusts the details reads only these. They say "a fraction in lowest terms equal to $\sqrt{2}$ leads to a contradiction, and every positive rational number has such a form".
2. The assumption of `<1>1` is in force in the steps `<2>1` to `<2>6`, and not in `<1>2`.
3. The assumption "$p$ is odd" of `<3>1` is in force only inside `<3>1`. Step `<2>3` comes after it and does not use it.
4. Step `<2>3` is a PICK step. It introduces $k$, and its proof names the fact that $k$ exists.
5. Step `<2>5` refers to the proof of `<2>2` with one change. This is allowed because the argument of `<2>2` uses only the equation "the square is twice a square".
6. The final contradiction in `<2>6` uses the hypothesis "no common factor greater than $1$" of `<1>1`. It is the only place where this hypothesis appears.

## Remarks

1. The example shows three levels: the theorem, the main argument, and the sub-proof that $p$ is even. A paragraph proof hides the third level in one sentence.
2. The same tree proves that $\sqrt{3}$ is irrational, with "divisible by $3$" in place of "even" and three cases for the remainder in `<3>2`.
3. The tree fails for $\sqrt{4}$, which is rational. Step `<2>1` becomes $p^2 = 4q^2$, and step `<2>4` becomes $q^2 = k^2$, which does not make $q$ even.
4. The page [[proof of the irrationality of the square root of 2 by lowest terms|7GNMP4Q32W]] gives the same argument as a paragraph proof.

## Explanations

### L1 human

The proof shows that no fraction squared gives exactly $2$.
For example, $\frac{7}{5}$ squared is $\frac{49}{25}$, which is close to $2$ but not equal to $2$.
The structured proof first assumes a fraction that works, in lowest terms.
Then it shows that the top and the bottom are both even.
This is impossible for a fraction in lowest terms, so no such fraction exists.
The numbered levels show which part proves which fact.

### L2 human

We read the proof top down, one level at a time.

1. Level 1: `<1>1` says that a reduced fraction equal to $\sqrt{2}$ is impossible. `<1>2` says that this suffices, because each positive rational number has a reduced form.
2. Level 2: `<2>1` turns the assumption into the equation $p^2 = 2q^2$. Steps `<2>2` and `<2>5` show that $p$ and $q$ are even. Step `<2>6` gives the contradiction.
3. Level 3: steps `<3>1` and `<3>2` prove `<2>2` by excluding the odd case.
4. A check with numbers: if $p = 2k$, then $p^2 = 4k^2$, and $4k^2 = 2q^2$ gives $q^2 = 2k^2$. For $k = 5$ this would need $q^2 = 50$, and no integer has square $50$, which agrees with the theorem.

The typical use of the levels is to let a reader check one level at a time.
Each level assumes that the steps below it are correct.
A trap is to use the assumption "$p$ is odd" of `<3>1` after `<3>1` ends.
The structure forbids this, and in a paragraph proof the same error is easy to miss.
