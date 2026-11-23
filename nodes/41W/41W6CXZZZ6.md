---
tag: 41W6CXZZZ6
kind: example
name: Testing the conclusion is not checking the proof
msc: ["00A35"]
topics: [STSM6PR7TX]
audience: ug2
not_instance_of:
  - target: 4M98ZZNK0E
    note: the reader tests the statement on examples but never checks the reasons of the steps, so a proof that assumes its conclusion passes
uses: [4M98ZZNK0E, 0BB5TPGQ1N, 09A3N7ZN5G]
sources:
  - url: https://en.wikipedia.org/wiki/Mathematical_proof
    locator: Nature and purpose
  - url: https://en.wikipedia.org/wiki/Contraposition
    locator: lead section
---

## Example

The statement is that for every integer $n$, if $n^2$ is even, then $n$ is even, and it is true.
A student hands in the following proof, which is flawed.

> (1) Suppose that $n^2$ is even.
> (2) Let $n = 2k$ for an integer $k$.
> (3) Then $n^2 = 4k^2 = 2(2k^2)$, which is even.
> (4) So $n$ is even.

A reader "checks" it by testing: for $n = 2, 4, 6$ the squares $4, 16, 36$ are even and $n$ is even, and for $n = 3$ the square $9$ is odd, so the hypothesis does not apply.
Finding no case against the statement, the reader accepts the proof.

Compared with the method of [[checking a proof|4M98ZZNK0E]], the reader checked the statement and none of the lines.
Line (2) has no reason: nothing in line (1) provides an integer $k$ with $n = 2k$, and "$n = 2k$" is the conclusion, assumed before it is proved.
Lines (2) and (3) together prove that if $n$ is even, then $n^2$ is even, which is the [[converse|09A3N7ZN5G]] of the statement.
Line (4) restates line (2), so the proof is circular.

The reader's tests are correct facts about the statement, but they cannot detect the error, because the statement is true and the error is in the argument.
The right verdict is "wrong: line (2) assumes the conclusion".

## Remarks

A correct proof uses the [[contrapositive|0BB5TPGQ1N]].
If $n$ is odd, then $n = 2k + 1$ for an integer $k$, and $n^2 = 2(2k^2 + 2k) + 1$ is odd.
Since "$n$ odd implies $n^2$ odd" is equivalent to "$n^2$ even implies $n$ even", the statement follows.

A test of the argument, rather than of the statement, would have found the error.
Take the false variant "if $4 \mid n^2$, then $4 \mid n$", which fails for $n = 2$.
The same argument with $n = 4k$ in line (2) "proves" this variant, so the argument cannot be correct.
[[Fallacies and errors in proofs|T6QQ749DM5]] treats circular arguments and the confusion of a statement with its converse.

## Explanations

### L1 human

The claim is that if the square of a whole number is even, then the number itself is even.
The claim is true, and examples such as $6 \cdot 6 = 36$ agree with it.
But the student's argument starts by saying "the number is $2k$", which is the same as saying "the number is even".
So the argument assumes what it should prove.
Examples of the claim cannot show this error, because the claim is true and only the argument is wrong.

### L2 human

A checker must keep two questions apart.
Is the statement true?
Examples can refute it, and only a proof can confirm it.
Is the argument correct?
Only a check of each line answers that.
Here the first answer is yes and the second is no, which is why a proof is judged by its steps and not by its conclusion.

Watch out: the repair "since $n^2$ is even, $n$ is even, so let $n = 2k$" repeats the circular step with the statement itself as its reason.
