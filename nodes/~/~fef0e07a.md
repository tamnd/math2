---
tag: ~fef0e07a
kind: example
name: A Lean proof that uses sorry is not a formal proof
msc: ["00A35", "68V15"]
topics: [1BTHSHST4M]
audience: ug2
not_instance_of:
  - target: ~a17a082b
    note: one step is a placeholder that the checker accepts without a derivation
uses: [~a17a082b, QF0Q7B5Q73]
sources:
  - url: https://en.wikipedia.org/wiki/Lean_(proof_assistant)
    locator: lead section
  - url: https://en.wikipedia.org/wiki/Formal_proof
    locator: lead section
---

## Example

In the Lean proof assistant, the keyword `sorry` stands for a missing proof.
Lean accepts the one-line file `theorem false_claim : 2 + 2 = 5 := sorry`.

We show that this is not a [[formal proof|~a17a082b]], even though the proof assistant accepts the file.

1. A formal proof is a chain in which each step is an axiom, an assumption, or follows from earlier steps by a rule.
2. The term `sorry` is none of these. It is a placeholder that closes any goal, of any statement.
3. Lean marks the use: it prints the warning "declaration uses 'sorry'".
4. The command `#print axioms false_claim` lists `sorryAx` among the axioms that the theorem depends on. So the "proof" rests on an extra axiom that proves every statement.
5. The statement $2 + 2 = 5$ is false in the natural numbers. Since every formal proof in Lean's sound system proves a true statement, the file contains no formal proof of it.

## Remarks

The non-example shows why a formal proof is defined by its steps, and not by the acceptance of a program.
A proof assistant checks a file, and the user must read the warnings and the list of axioms to know what was checked.
Large formalization projects use `sorry` on purpose, to mark the parts that are not done yet, and they count the remaining uses to measure progress.

The same issue exists for informal proofs.
A paper that says "this lemma is standard" without a reference has a placeholder of the same kind.
The difference is that Lean records each placeholder, and a reader of the paper may not notice it.

## Explanations

### L1 human

A proof checker is a program that reads each step of a proof and checks it against the rules.
Lean lets a user write the word `sorry` in place of a step, which means "I will do this later".
The program then accepts the file, but it prints a warning.
With `sorry` one can "prove" that $2 + 2 = 5$, which is false.
So a file with `sorry` is a plan of a proof, not a proof.

### L2 human

We compare two Lean files.

1. The file `theorem t : 2 + 2 = 4 := rfl` is accepted with no warning. The term `rfl` asks Lean to compute both sides, and both are $4$.
2. The file `theorem t : 2 + 2 = 5 := rfl` is rejected, because the two sides compute to different numbers.
3. The file `theorem t : 2 + 2 = 5 := sorry` is accepted with the warning "declaration uses 'sorry'".

The typical use of `sorry` is to write the outline of a long proof first and to fill in the parts one by one.
A trap is to take the absence of errors as proof: a file with `sorry` can show no error, and still prove nothing.
