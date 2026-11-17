---
tag: ~c2a8a4cd
kind: example
name: Testing the conclusion is not checking the proof
msc: ["00A35"]
topics: [STSM6PR7TX]
audience: ug2
not_instance_of:
  - target: ~14ee5799
    note: the reader tests the statement on examples but never checks the reasons of the steps, so a proof that assumes its conclusion passes
uses: [~14ee5799, 0BB5TPGQ1N, 09A3N7ZN5G]
sources:
  - url: https://en.wikipedia.org/wiki/Mathematical_proof
    locator: Nature and purpose
  - url: https://en.wikipedia.org/wiki/Contraposition
    locator: lead section
---

## Example

The statement is: for every integer $n$, if $n^2$ is even, then $n$ is even.
The statement is true.
A student hands in the following proof.

> (1) Suppose that $n^2$ is even.
> (2) Let $n = 2k$ for an integer $k$.
> (3) Then $n^2 = 4k^2 = 2(2k^2)$, which is even.
> (4) So $n$ is even.

A reader "checks" the proof: for $n = 2, 4, 6$ the squares $4, 16, 36$ are even and $n$ is even.
For $n = 3$ the square $9$ is odd, so the hypothesis does not apply.
The reader finds no case against the statement and accepts the proof.
We compare this reading with the method of [[checking a proof|~14ee5799]].

1. The method checks the reason of each line. The reader checked none of the lines, only the statement.
2. Line (2) has no reason. Nothing in line (1) gives an integer $k$ with $n = 2k$: this is the conclusion "$n$ is even", assumed before it is proved.
3. Lines (2) and (3) together prove "if $n$ is even, then $n^2$ is even". This is the [[converse|09A3N7ZN5G]] of the statement, not the statement.
4. Line (4) restates line (2). So the proof is circular: the conclusion appears as an assumption.
5. The tests of the reader are correct facts about the statement. They cannot detect the error, because the statement is true and the error is in the argument.
6. So the reading is not an instance of checking a proof, and the verdict "correct" is wrong. The right verdict is "wrong: line (2) assumes the conclusion".

## Remarks

1. A correct proof uses the [[contrapositive|0BB5TPGQ1N]]. If $n$ is odd, then $n = 2k + 1$ for an integer $k$, and $n^2 = 4k^2 + 4k + 1 = 2(2k^2 + 2k) + 1$ is odd.
2. Since "$n$ odd implies $n^2$ odd" is equivalent to "$n^2$ even implies $n$ even", the statement follows.
3. A test of the argument, not of the statement, would have found the error. Take the false variant "if $n^2$ is divisible by $4$, then $n$ is divisible by $4$", which fails for $n = 2$. The same argument, with $n = 4k$ in line (2), "proves" this variant, so the argument is wrong.
4. The pages of the topic [[fallacies and errors in proofs|T6QQ749DM5]] treat circular arguments and the confusion of a statement with its converse.

## Explanations

### L1 human

The claim is: if the square of a whole number is even, then the number itself is even.
The claim is true, and examples such as $6 \cdot 6 = 36$ agree with it.
But the student's argument starts by saying "the number is $2k$", which is the same as saying "the number is even".
So the argument assumes what it should prove.
Examples of the claim cannot show this error, because the claim is true and only the argument is wrong.

### L2 human

We separate the two questions that a checker must keep apart.

1. Is the statement true? Examples can refute it, and only a proof can confirm it.
2. Is the argument correct? Only a check of each line answers this.
3. Here the answer to question 1 is yes, and the answer to question 2 is no.

The typical use of this example is in a first course on proofs.
It shows that a proof is judged by its steps and not by its conclusion.
A trap is to repair the proof by writing "since $n^2$ is even, $n$ is even, so let $n = 2k$".
This repeats the circular step with a reason that is the statement itself.
