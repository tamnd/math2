---
tag: C3Z6VNAXSG
kind: example
name: Adding numerators and denominators is not well defined
msc: ["00A35"]
topics: [BP0WAF23HB]
audience: ug1
not_instance_of:
  - target: HNGZEBKVY2
    note: the result depends on the fractions chosen to represent the rational numbers
uses: [HNGZEBKVY2, KF8H084HDE, 0NCJ5WXN6Z]
sources:
  - url: https://en.wikipedia.org/wiki/Well-defined_expression
    locator: Independence of representative
---

## Example

Write each [[rational number|0NCJ5WXN6Z]] as a fraction $\tfrac{a}{b}$ with $b > 0$, and propose the operation
$$\frac{a}{b} \oplus \frac{c}{d} := \frac{a + c}{b + d}.$$
We show that $\oplus$ is not [[well defined|HNGZEBKVY2]] on $\mathbb{Q}$.

1. The rule reads the fractions, not only the numbers.
   So we must test whether equal numbers written as different fractions give equal results.
2. Take $\tfrac{1}{2}$ and $\tfrac{1}{3}$.
   The rule gives $\tfrac{1 + 1}{2 + 3} = \tfrac{2}{5}$.
3. Write the first number as $\tfrac{2}{4}$ instead.
   This is the same rational number, because $1 \cdot 4 = 2 \cdot 2$, by the [[definition of rational numbers by abstraction|KF8H084HDE]].
4. The rule now gives
   $$\frac{2}{4} \oplus \frac{1}{3} = \frac{2 + 1}{4 + 3} = \frac{3}{7}.$$
5. The numbers $\tfrac{2}{5}$ and $\tfrac{3}{7}$ differ, because $2 \cdot 7 = 14$ and $5 \cdot 3 = 15$.
6. So one pair of inputs gives two different outputs, and $\oplus$ is not an operation on $\mathbb{Q}$.

## Remarks

One pair of representatives is enough.
A rule is well defined only if every choice agrees, so a single disagreement refutes it.

Without the condition $b > 0$, the rule fails in a second way.
The fractions $\tfrac{1}{1}$ and $\tfrac{1}{-1}$ would give $\tfrac{2}{0}$, which is not a fraction at all.

The fraction $\tfrac{a + c}{b + d}$ has a name, the mediant of $\tfrac{a}{b}$ and $\tfrac{c}{d}$, and it is useful in the study of Farey sequences.
There each fraction is written in lowest terms, so the representative is fixed and the mediant is a function of the two numbers.
It is still not compatible with equality of fractions, which is why it cannot serve as addition.

The correct sum $\tfrac{ad + bc}{bd}$ passes the same test:
$$\frac{1}{2} + \frac{1}{3} = \frac{5}{6}, \qquad \frac{2}{4} + \frac{1}{3} = \frac{10}{12} = \frac{5}{6}.$$

## Explanations

### L1 human

A common mistake with fractions is to add the tops and add the bottoms.
One half plus one third would then be two fifths.
But one half is also two quarters, and the same rule now gives three sevenths.
Two fifths and three sevenths are different numbers.
So the rule gives different answers to the same question, and it is not a real way of adding numbers.

### L2 human

How often does $\oplus$ fail?
Scale the first input by an integer $k \ge 2$ and compare $\tfrac{ka}{kb} \oplus \tfrac{c}{d}$ with $\tfrac{a}{b} \oplus \tfrac{c}{d}$.

1. The two results are $\tfrac{ka + c}{kb + d}$ and $\tfrac{a + c}{b + d}$.
2. They are equal exactly when $(ka + c)(b + d) = (a + c)(kb + d)$.
3. Expand both sides:
   $$kab + kad + bc + cd = kab + ad + kbc + cd.$$
4. Cancel $kab + cd$ and collect terms, so the condition becomes $(k - 1)(ad - bc) = 0$.
5. Since $k \ge 2$, this holds only when $ad = bc$, that is, when $\tfrac{a}{b} = \tfrac{c}{d}$.

So scaling one input changes the result whenever the two inputs are different numbers.
Check with step 4 of the example: $a = 1$, $b = 2$, $c = 1$, $d = 3$ and $k = 2$ give $(2 - 1)(3 - 2) = 1 \neq 0$.
The test "scale one fraction and compare" is the standard first test of a rule on fractions.
Watch out: if you test only fractions in lowest terms, the rule looks like a function and the failure stays hidden.
