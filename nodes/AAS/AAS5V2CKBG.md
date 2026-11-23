---
tag: AAS5V2CKBG
kind: example
name: Anomalous cancellation of digits
aliases: [anomalous-cancellation, 16-over-64-howler]
msc: ["00A35", "97F40"]
topics: [T6QQ749DM5]
audience: school
instance_of: [S2BW0FDHV8]
uses: [S2BW0FDHV8, 0GJM24EXP9]
sources:
  - url: https://en.wikipedia.org/wiki/Mathematical_fallacy
    locator: Howlers
  - url: https://en.wikipedia.org/wiki/Anomalous_cancellation
    locator: lead section
---

## Example

Here is a wrong method that gives a right answer; before you read on, decide what is wrong with it.
A student simplifies $\frac{16}{64}$ like this:

1. Write the fraction $\frac{16}{64}$.
2. Cross out the digit $6$ on top and the digit $6$ below.
3. What is left is $\frac{1}{4}$.

The answer is correct, since $16 \cdot 4 = 64 \cdot 1$.
The method is a howler, a [[mathematical fallacy|S2BW0FDHV8]] whose conclusion is true by chance.
We check it step by step.

1. Step 2 treats the digit $6$ as a common factor of $16$ and $64$. In fact $16 = 10 \cdot 1 + 6$ and $64 = 10 \cdot 6 + 4$, so the $6$ is added in one number and multiplied in the other.
2. The valid rule is [[cancellation|0GJM24EXP9]] of a common factor: $\frac{ac}{bc} = \frac{a}{b}$ when $c \neq 0$. The true common factor here is $16$, since $16 = 16 \cdot 1$ and $64 = 16 \cdot 4$.
3. The same move on $\frac{12}{24}$ crosses out the $2$s and gives $\frac{1}{4}$, but $\frac{12}{24} = \frac{1}{2}$. So step 2 is not a rule.

The correct version cancels the factor $16$:
$$\frac{16}{64} = \frac{16 \cdot 1}{16 \cdot 4} = \frac{1}{4}.$$

## Remarks

A right answer does not make a method right.
For which fractions does the trick work?
Take a fraction $\frac{10a + b}{10b + c}$ of two-digit numbers, with digits $a, b, c$ and $a, c \neq 0$.
Crossing out $b$ leaves $\frac{a}{c}$, and this is correct exactly when
$$(10a + b)c = a(10b + c), \quad \text{that is,} \quad 9ac = b(10a - c).$$
A search over all digits, for fractions less than $1$, gives exactly four cases: $\frac{16}{64}$, $\frac{19}{95}$, $\frac{26}{65}$ and $\frac{49}{98}$.
Change one digit and the luck ends: $\frac{17}{74}$ becomes "$\frac{1}{4}$", but $17 \cdot 4 = 68 \neq 74$.

## Explanations

### L1 human

The fraction sixteen over sixty-four equals one quarter.
If you "cancel" the two sixes, you also get one quarter, by pure luck.
The same trick on twelve over twenty-four cancels the twos and gives one quarter again, but the true value is one half.
You may cancel only a number that divides both the top and the bottom, never a digit.

### L2 human

We find the two cases with $a = 1$ from the equation $9ac = b(10a - c)$.
With $a = 1$ it reads $9c = b(10 - c)$.
For $b = 6$ we get $9c = 60 - 6c$, so $15c = 60$ and $c = 4$, which gives $\frac{16}{64}$.
For $b = 9$ we get $9c = 90 - 9c$, so $c = 5$, which gives $\frac{19}{95}$.
For the other values of $b$ the equation $c = \frac{10b}{9 + b}$ has no digit solution except $c = 1$ for $b = 1$, the dull case $\frac{11}{11}$.

Check: $\frac{19}{95} = \frac{1}{5}$, since $19 \cdot 5 = 95$.
The same search with $a = 2$ and $a = 4$ gives $\frac{26}{65}$ and $\frac{49}{98}$.
Watch out: a method that passes one test, or even four, has not been proved; one failure such as $\frac{12}{24}$ refutes it.
