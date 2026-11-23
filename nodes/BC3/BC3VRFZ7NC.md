---
tag: BC3VRFZ7NC
kind: example
name: A Lean proof that uses sorry is not a formal proof
msc: ["00A35", "68V15"]
topics: [1BTHSHST4M]
audience: ug2
not_instance_of:
  - target: 8VZ77R4R8S
    note: one step is a placeholder that the checker accepts without a derivation
uses: [8VZ77R4R8S, QF0Q7B5Q73]
sources:
  - url: https://en.wikipedia.org/wiki/Lean_(proof_assistant)
    locator: lead section
  - url: https://en.wikipedia.org/wiki/Formal_proof
    locator: lead section
---

## Example

In the Lean proof assistant, the keyword `sorry` stands for a missing proof.
Lean accepts the one-line file `theorem false_claim : 2 + 2 = 5 := sorry`.
The file is accepted, yet it contains no [[formal proof|8VZ77R4R8S]], and we check why.

1. A formal proof is a chain in which each step is an axiom, an assumption, or follows from earlier steps by a rule.
2. The term `sorry` is none of these. It is a placeholder that closes any goal, whatever the statement.
3. Lean reports the use with the warning "declaration uses 'sorry'".
4. The command `#print axioms false_claim` lists `sorryAx` among the axioms on which the theorem depends. So the "proof" rests on an extra axiom that proves every statement.
5. The statement $2 + 2 = 5$ is false for the natural numbers. Lean's logic without `sorryAx` is sound, so no formal proof of it exists, and the file cannot contain one.

## Remarks

The non-example shows that a formal proof is defined by its steps, not by the fact that a program accepted a file.
A proof assistant checks a file, and the user must read the warnings and the list of axioms to know what was checked.
Large formalization projects use `sorry` on purpose to mark the parts that are not done, and they count the remaining uses to measure progress.

The same problem exists for informal proofs.
A paper that says "this lemma is standard" and gives no reference has a placeholder of the same kind.
The difference is that Lean records each placeholder, while a reader of the paper may not notice one.

What changes if we replace `sorry` by a real proof term?
For $2 + 2 = 4$ the term `rfl` works and the warning disappears, and for $2 + 2 = 5$ every real term fails, which is what soundness promises.

## Explanations

### L1 human

A proof checker is a program that reads each step of a proof and compares it with the rules.
Lean lets a user write the word `sorry` in place of a step, which means "I will do this later".
The program then accepts the file, but it prints a warning.
With `sorry` you can "prove" that $2 + 2 = 5$, which is false.
So a file with `sorry` is the plan of a proof, not a proof.

### L2 human

We compare three Lean files.

1. The file `theorem t : 2 + 2 = 4 := rfl` is accepted with no warning. The term `rfl` asks Lean to compute both sides, and both are $4$.
2. The file `theorem t : 2 + 2 = 5 := rfl` is rejected, because the two sides compute to different numbers.
3. The file `theorem t : 2 + 2 = 5 := sorry` is accepted with the warning "declaration uses 'sorry'".

The typical use of `sorry` is to write the outline of a long proof first and to fill in the parts one by one, as in [[the Lean example|QF0Q7B5Q73]].
Watch out for the absence of errors taken as proof.
A file with `sorry` shows no error, and still proves nothing.
