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

The theorem is the [[irrationality of the square root of 2|0DZGSDHD92]].
We write a [[proof by contradiction|0J0XBKG64S]] in the [[hierarchical format|H2W8D7BMSW]], with three levels.

- `<1>1.` ASSUME: $p$ and $q$ are positive integers with no common factor greater than $1$, and $\sqrt{2} = p/q$
  PROVE: FALSE
    - `<2>1.` $p^2 = 2q^2$.
      PROOF: square both sides of $\sqrt{2} = p/q$ and multiply by $q^2$.
    - `<2>2.` $p$ is even.
        - `<3>1.` ASSUME: $p$ is odd
          PROVE: FALSE
          PROOF: write $p = 2j + 1$; then $p^2 = 2(2j^2 + 2j) + 1$ is odd, but $p^2 = 2q^2$ is even by `<2>1`.
        - `<3>2.` Q.E.D.
          PROOF: by `<3>1`, since every integer is even or odd.
    - `<2>3.` PICK an integer $k$ with $p = 2k$.
      PROOF: by `<2>2`.
    - `<2>4.` $q^2 = 2k^2$.
      PROOF: by `<2>1` and `<2>3`, $4k^2 = 2q^2$, and we divide by $2$.
    - `<2>5.` $q$ is even.
      PROOF: as in `<2>2`, with `<2>4` in place of `<2>1`.
    - `<2>6.` Q.E.D.
      PROOF: by `<2>2` and `<2>5`, the number $2$ divides $p$ and $q$, which contradicts the assumption of `<1>1`.
- `<1>2.` Q.E.D.
  PROOF: if $\sqrt{2}$ were rational, then, since $\sqrt{2} > 0$, it would be a fraction $p/q$ of positive integers, and dividing $p$ and $q$ by their greatest common divisor would give the situation of `<1>1`, which is impossible.

A reader who trusts the details reads only the two top steps.
They say that a fraction in lowest terms equal to $\sqrt{2}$ leads to a contradiction, and that every positive rational number has such a form.
The assumption of `<1>1` is in force in `<2>1` to `<2>6` and not in `<1>2`.
The assumption "$p$ is odd" is in force only inside `<3>1`, and step `<2>3`, which comes after it, does not use it.
Step `<2>3` is a PICK step: it brings in $k$, and its proof names the fact that $k$ exists.
Step `<2>5` reuses the argument of `<2>2`, which is allowed because that argument needs only an equation of the form "a square equals twice a square".
The hypothesis "no common factor greater than $1$" appears only in `<2>6`, where the contradiction happens.

## Remarks

The tree has three levels: the theorem, the main argument, and the sub-proof that $p$ is even.
A paragraph proof usually hides the third level in one sentence, and [[the lowest-terms proof in paragraph form|7GNMP4Q32W]] shows how.

The same tree proves that $\sqrt{3}$ is irrational, with "divisible by $3$" in place of "even" and three cases for the remainder in `<3>2`.
It fails for $\sqrt{4}$, which is rational.
There `<2>1` becomes $p^2 = 4q^2$ and `<2>4` becomes $q^2 = k^2$, which does not make $q$ even.

## Explanations

### L1 human

The proof shows that no fraction squared gives exactly $2$.
For example, $\frac{7}{5}$ squared is $\frac{49}{25}$, which is close to $2$ but not equal to it.
The structured proof first assumes a fraction in lowest terms that works.
Then it shows that the top and the bottom are both even.
That is impossible for a fraction in lowest terms, so no such fraction exists, and the numbered levels show which part proves which fact.

### L2 human

We read the proof one level at a time.
At level 1, `<1>1` says that a reduced fraction equal to $\sqrt{2}$ is impossible, and `<1>2` says that this is enough, because each positive rational number has a reduced form.
At level 2, `<2>1` turns the assumption into $p^2 = 2q^2$, steps `<2>2` and `<2>5` show that $p$ and $q$ are even, and `<2>6` gives the contradiction.
At level 3, `<3>1` and `<3>2` prove `<2>2` by ruling out the odd case.

Check with numbers: if $p = 2k$, then $4k^2 = 2q^2$ gives $q^2 = 2k^2$.
For $k = 5$ this would need $q^2 = 50$, and no integer has square $50$, in line with the theorem.
Watch out: the assumption "$p$ is odd" of `<3>1` must not be used after `<3>1` ends.
The structure forbids it, while in a paragraph proof the same error is easy to miss.
