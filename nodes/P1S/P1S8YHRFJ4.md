---
tag: P1S8YHRFJ4
kind: example
name: A sound argument about divisibility
msc: ["03B05", "00A30"]
topics: [H8QZY0RZXZ]
audience: ug1
instance_of: [4A84VHDTHV]
uses: [4A84VHDTHV, 5SDS9T8E7J, 0Y0MQYST0M]
sources:
  - url: https://en.wikipedia.org/wiki/Soundness
    locator: lead section
  - url: https://en.wikipedia.org/wiki/Validity_(logic)
    locator: lead section
---

## Example

Consider the argument with two premises and one conclusion:

- Premise 1: if 12 is divisible by 4, then 12 is even.
- Premise 2: 12 is divisible by 4.
- Conclusion: 12 is even.

We check that it is a [[sound deductive argument|55HFJFZXVR]], in the sense of [[soundness|4A84VHDTHV]] for arguments: it is valid and its premises are true.

1. The form is "if $A$ then $B$; $A$; so $B$", which is [[modus ponens|0Y0MQYST0M]].
2. The form is [[valid|5SDS9T8E7J]]: in each row of the truth table where $A \to B$ and $A$ are true, $A$ is true and so $B$ is true.
3. Premise 2 is true, because $12 = 4 \cdot 3$.
4. Premise 1 is true. If $n = 4k$ for an integer $k$, then $n = 2 \cdot (2k)$, so $n$ is even; apply this to $n = 12$.
5. The argument is valid by step 2 and has true premises by steps 3 and 4, so it is sound. Its conclusion is therefore true.

## Remarks

The same form with other numbers gives arguments that are valid but not sound.
The argument "if 6 is even, then 6 is divisible by 4; 6 is even; so 6 is divisible by 4" is valid, but premise 1 is false, since $6 = 4 \cdot 1 + 2$.
It is an [[unsound argument|PX83KT650H]], and its conclusion is false.
An argument can also be invalid with true premises and a true conclusion, for example "if 12 is divisible by 4, then 12 is even; 12 is even; so 12 is divisible by 4", which has the form of [[affirming the consequent|J7KFCFQRBT]].
Such an argument is not sound, because soundness requires validity.
Soundness of an argument depends on the facts, while soundness of a proof system depends only on its rules.

## Explanations

### L1 human

A good argument needs two things.
Its steps must be correct, so that true starting facts always give a true result.
Its starting facts must also be true.
"If 12 can be split into 4 equal whole parts, then 12 is even; 12 can be split into 4 equal whole parts; so 12 is even" has both.
That is what logicians call a sound argument.

### L2 human

We classify three arguments of the form "if $A$ then $B$; $A$; so $B$" and one of another form.

1. "If 12 is divisible by 4, then 12 is even; 12 is divisible by 4; so 12 is even." Valid form, true premises: sound.
2. "If 6 is even, then 6 is divisible by 4; 6 is even; so 6 is divisible by 4." Valid form, false first premise: valid but unsound.
3. "If 15 is divisible by 5, then 15 is odd; 15 is divisible by 5; so 15 is odd." Premise 1 is true here because both parts are true, so the argument is sound.
4. "If 12 is divisible by 4, then 12 is even; 12 is even; so 12 is divisible by 4." Invalid form: not sound, although every line is true.

The typical use is in a proof: once the steps are valid and the axioms are true in a structure, every theorem is true there.
A trap is to call item 4 sound because its conclusion is true; validity is a property of the form, and the form is invalid.
