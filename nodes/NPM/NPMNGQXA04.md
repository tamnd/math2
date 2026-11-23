---
tag: NPMNGQXA04
kind: example
name: The square root of 4 in the integers is not a definite description
msc: ["03B10"]
topics: [PSRDJXRW53]
audience: grad
not_instance_of:
  - target: PD2R4XT79Q
    note: two integers, 2 and -2, satisfy x times x equals 4, so the phrase the integer with x times x equals 4 does not pick out exactly one object
uses: [PD2R4XT79Q, 0QAJHFGZZJ, TH5ZKCKN3W]
sources:
  - url: https://en.wikipedia.org/wiki/Definite_description
    locator: lead section
---

## Example

In the ring $\mathbb{Z}$, consider the phrase "the integer $x$ with $x \cdot x = 4$", written $\iota x \, (x \cdot x = 4)$.
We show that it fails the uniqueness condition of a [[definite description|PD2R4XT79Q]].

1. Both $2 \cdot 2 = 4$ and $(-2) \cdot (-2) = 4$, so at least two integers satisfy the condition.
2. Hence $\exists! x \, (x \cdot x = 4)$ is false in $\mathbb{Z}$, by the meaning of the [[uniqueness quantifier|0QAJHFGZZJ]].
3. By Russell's analysis, "the $x$ with $x \cdot x = 4$ is positive" is
   $$\exists x \, \big( x \cdot x = 4 \land \forall y \, (y \cdot y = 4 \to y = x) \land 0 < x \big).$$
4. Take any $x$ with $x \cdot x = 4$.
   Then $x = 2$ or $x = -2$, and the clause $\forall y \, (y \cdot y = 4 \to y = x)$ fails at the other one.
   So the sentence of step 3 is false.
5. In the same way, "the $x$ with $x \cdot x = 4$ is negative" is false.

So the phrase does not describe one object, although some integer fits it.

## Remarks

In $\mathbb{N}$ the same condition has the one witness $2$, so $\iota x \, (x \cdot x = 4)$ denotes $2$ there.
Whether a phrase is a proper description depends on the structure, not on the words alone.
Mathematical practice adds a condition to restore uniqueness: "the positive square root" is $\iota x \, (x \cdot x = 4 \land 0 < x)$.
Hilbert's [[epsilon term|TH5ZKCKN3W]] $\varepsilon x \, (x \cdot x = 4)$ denotes $2$ or $-2$, depending on the choice function, and needs no uniqueness.

## Explanations

### L1 human

"The square root of $4$" sounds like one number, but among the integers both $2$ and $-2$ have square $4$.
So the word "the" is wrong here.
Saying "the positive square root of $4$" fixes it, since that is $2$ alone.

### L2 human

We compare three readings of "the square root of $4$ is $2$" in $\mathbb{Z}$.
Russell's reading is false, because uniqueness fails.
With "the positive square root", the description denotes $2$, and the sentence is true.
With an $\varepsilon$-term, the truth depends on the choice function, so the sentence has no fixed value.
The typical use is as a warning before notation such as $\sqrt{a}$, which presupposes a rule that selects one root.
Watch out: the existence of a witness is not enough for a description, since uniqueness is the second half of $\exists!$.
