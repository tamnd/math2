---
tag: N9XZ3WAC2C
kind: example
name: A fuzzy fan controller is not a logic
msc: ["03B52", "93C42"]
topics: [WZP584JQ06]
audience: grad
not_instance_of:
  - target: 8DH4QM6AX8
    note: fuzzy logic in the engineering sense computes outputs and has no consequence relation
uses: [GV9NVFFFXF]
sources:
  - url: https://en.wikipedia.org/wiki/Fuzzy_logic
    locator: Fuzzification; IF-THEN rules; Defuzzification
  - url: https://plato.stanford.edu/entries/logic-fuzzy/
    locator: lead section
---

## Example

A fan controller reads a temperature $t$ in degrees Celsius and sets a fan speed.
It uses two [[fuzzy sets|GV9NVFFFXF]], "warm" and "hot", with these membership functions.

$$w(t) = \max\left(0, 1 - \frac{\lvert t - 20 \rvert}{10}\right), \qquad h(t) = \min\left(1, \max\left(0, \frac{t - 20}{10}\right)\right).$$

It has two rules.
Rule 1 says: IF temperature IS warm THEN fan speed IS moderate, and "moderate" stands for the speed $50$.
Rule 2 says: IF temperature IS hot THEN fan speed IS high, and "high" stands for the speed $100$.
To combine the rules, we take the average of the two speeds, weighted by the degrees of the conditions.
This is a simple form of the defuzzification step.

1. Fuzzification at $t = 25$ gives $w(25) = 1 - 5/10 = 0.5$ and $h(25) = 5/10 = 0.5$.
2. Each rule fires with the degree of its condition, so both rules fire with degree $0.5$.
3. Defuzzification gives the output speed.
   $$\frac{0.5 \cdot 50 + 0.5 \cdot 100}{0.5 + 0.5} = 75.$$
4. At $t = 28$ we get $w(28) = 0.2$ and $h(28) = 0.8$, and the output is computed in the same way.
   $$\frac{0.2 \cdot 50 + 0.8 \cdot 100}{0.2 + 0.8} = 90.$$
5. So the controller is a function from temperatures to speeds, and steps 1 to 4 compute two of its values.
6. No set of formulas, no consequence relation and no notion of tautology occurs anywhere in steps 1 to 4.

So the controller is "fuzzy logic" only in the broad, engineering sense.
It is not a logic in the sense of [[mathematical fuzzy logic|8DH4QM6AX8]], where one asks which formulas follow from which premises.

## Remarks

The two senses have different aims.
The engineering sense aims at a good output from vague rules, quickly computed.
The narrow sense is a branch of mathematical logic, with proofs, models and completeness theorems.

Notice how the rule "IF warm THEN moderate" is used.
It is not read as an implication with a truth value of its own.
Instead the degree of its condition is passed on to its output, and the outputs are averaged.
You can describe the same controller with t-norms and t-conorms, for example by combining two conditions with $\min$, but this does not turn it into a consequence relation.
Change the input to $t = 18$: then $w(18) = 0.8$ and $h(18) = 0$, so only rule 1 fires, and the output is $50$.

## Explanations

### L1 human

A fuzzy fan controller reads a temperature and sets a fan speed.
It uses words like "warm" and "hot", each true to a degree.
At $25$ degrees it is half warm and half hot, so it picks a speed halfway between moderate and high.
It does not prove anything; it only computes a number.

### L2 human

The controller works in three steps.
First, compute the degree of each condition from the input.
Second, fire each rule with that degree.
Third, combine the outputs into one number, here by a weighted average.
Watch out: the word "logic" in "fuzzy logic controller" does not mean that the device has a consequence relation.
When a question asks about completeness or tautologies, it is about the narrow sense.
