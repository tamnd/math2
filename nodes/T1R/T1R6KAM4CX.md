---
tag: T1R6KAM4CX
kind: example
name: A column of formulas without proof words
msc: ["00A35", "11A05"]
topics: [STSM6PR7TX]
audience: ug1
not_instance_of:
  - target: GKMRQCA8CW
    note: the lines have no proof words, so the reader cannot tell the assumptions, the new objects and the conclusions apart
uses: [GKMRQCA8CW, 0PG2H7WKGG]
sources:
  - url: https://en.wikipedia.org/wiki/Wikipedia:Manual_of_Style/Mathematics
    locator: Writing style in mathematics
  - book: isbn:9781108439534
    locator: Chapter 3
---

## Example

The statement is that for integers $a$, $b$ and $c$, if $a \mid b$ and $b \mid c$, then $a \mid c$.
Here $a \mid b$ means that $b = ak$ for some integer $k$, by the definition of [[divisibility|0PG2H7WKGG]].
A student hands in this column as the proof:

$$a \mid b, \quad b \mid c$$
$$b = ak$$
$$c = bl$$
$$c = akl$$
$$a \mid c$$

This is a flawed example.
Each formula is true under the right reading, but the text is not written in the [[language of proofs|GKMRQCA8CW]], so the reader has to guess the logic.
The first line could be the hypothesis or a claim still to be proved.
The letters $k$ and $l$ appear without being introduced, so the reader cannot tell whether they are integers or where they come from.
The step to $c = akl$ has no reason, the last line needs the unstated fact that $kl$ is an integer, and nothing marks which line is the conclusion.

The layout also cannot tell a correct argument from a wrong one.
Here is a column of the same shape for the false claim "if $a \mid bc$, then $a \mid b$":

$$a \mid bc$$
$$bc = ak$$
$$b = a \cdot \tfrac{k}{c}$$
$$a \mid b$$

The last step needs $\frac{k}{c}$ to be an integer, and the column hides this gap.
The claim fails for $a = 6$, $b = 2$ and $c = 3$: here $6 \mid 6 = bc$, but $6 \nmid 2$.

## Remarks

The correct version of the first column needs four phrases: "suppose that $a \mid b$ and $b \mid c$", "so there are integers $k$ and $l$ with", "then", and "since $kl$ is an integer".
The L2 explanation of [[the language of proofs|GKMRQCA8CW]] writes it out in full.

Correct formulas do not make a proof.
A proof also states the role of each formula and the reason for each step.

A column of formulas is fine inside a proof for a chain of equalities, such as $c = bl = (ak)l = a(kl)$, because each sign "=" links two lines.
It is not fine for steps that change the logical status of a line, such as an assumption or the choice of a new letter.

## Explanations

### L1 human

Imagine a recipe that lists only the ingredients and the result, with no instructions.
A cook cannot tell what to do first, or what to do with each item.
The column of formulas is like that recipe.
Each line is a true fact, but the column does not say which facts are given, which numbers are new, and which fact is the answer.
A second column of the same shape "proves" a false claim, so the shape alone cannot be trusted.

### L2 human

We add proof words to the second column and find where it breaks.

> Suppose that $a \mid bc$.
> Then there is an integer $k$ with $bc = ak$.
> If $c \ne 0$, then $b = a \cdot \frac{k}{c}$ as rational numbers.
> Since $\frac{k}{c}$ is an integer, $a \mid b$.

The word "since" in the last line asks for a reason, and no reason exists.
For $a = 6$, $b = 2$ and $c = 3$ we get $bc = 6$, $k = 1$ and $\frac{k}{c} = \frac{1}{3}$, which is not an integer.

The proof words make the gap visible.
Watch out: a short column looks clearer than sentences, but it moves the work of finding the logic from the writer to the reader.
