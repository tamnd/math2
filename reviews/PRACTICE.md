# Review practice

Do this practice set before your first review. It has 20 items. Each item has an informal statement and a Lean statement. For each item, give a verdict as in "How to review" in [README.md](README.md). For the verdict `not-faithful`, also give the class of the fault. Then open the answer and compare.

The items come from the fidelity suite of tamnd/math2-agent (`bench/fidelity`). They are not nodes of Math 2.0, and a practice answer is not a review. Do not write a review file for them.

The items are small, thus each item takes less than a minute. Read the Lean statement as the kernel reads it, not as its name or its look tells you. These facts of Lean 4 are important for the items:

- `Nat` starts at 0. Subtraction on `Nat` stops at 0, thus `3 - 5 = 0`. Division on `Nat` rounds down, thus `1 / 2 = 0`.
- `/` on `Int` is Euclidean division, thus `-7 / 2 = -4`. Division by zero gives 0 on `Nat` and on `Int`.
- `l.head?` is the first element of the list `l`, or `none` for the empty list.
- A hypothesis is a parameter before the colon, for example `(h : b ≤ a)`.

You can check a value with `#eval` in Lean, for example `#eval ((-7 : Int) / 2)`.

A fault can fit more than one class. Give the class that explains the fault best, and write the other class in the notes. The answer tells you when an item has two possible classes.

## The items

### P01

Informal: Each natural number n with n ≥ 1 is m + 1 for some natural number m.

```lean
theorem P01 (n : Nat) (h : 1 ≤ n) : ∃ m, n = m + 1
```

<details><summary>Answer</summary>

`faithful`. The hypothesis `h` is the condition n ≥ 1, and the conclusion has the same quantifier as the informal statement.

</details>

### P02

Informal: For natural numbers a and b with b ≤ a, (a − b) + b = a.

```lean
theorem P02 (a b : Nat) : a - b + b = a
```

<details><summary>Answer</summary>

`not-faithful`, `M-hyp-missing`. The condition b ≤ a is not in the Lean statement. For a = 2 and b = 5, `2 - 5 + 5` is 5, thus the Lean statement is false. Compare with P11.

</details>

### P03

Informal: No natural number is the largest: for each n there is an m with n < m.

```lean
theorem P03 : ∃ m : Nat, ∀ n : Nat, n < m
```

<details><summary>Answer</summary>

`not-faithful`, `M-quant`. The informal statement is "for each n, there is an m". The Lean statement is "there is one m that is larger than each n", which is false. The order of the two quantifiers is wrong.

</details>

### P04

Informal: Integer division rounds toward zero, thus −7 divided by 2 is −3.

```lean
theorem P04 : (-7 : Int) / 2 = -3
```

<details><summary>Answer</summary>

`not-faithful`, `M-def`. The informal statement is about division that rounds toward zero. `/` on `Int` is Euclidean division, and `(-7 : Int) / 2` is -4. The constant means a different operation. The Lean name of division that rounds toward zero is `Int.tdiv`.

</details>

### P05

Informal: For natural numbers a and b with b nonzero, the quotient a / b times b is at most a.

```lean
theorem P05 (a b : Nat) (h : b ≠ 0) : a / b * b ≤ a
```

<details><summary>Answer</summary>

`faithful`. The quotient of natural numbers rounds down in the informal statement and in Lean. The hypothesis `h` is the condition that b is nonzero.

</details>

### P06

Informal: For natural numbers a and b with a < b, the difference a − b is a negative number.

```lean
theorem P06 (a b : Nat) (h : a < b) : a - b ≤ 0
```

<details><summary>Answer</summary>

`not-faithful`, `M-junk`. Subtraction on `Nat` stops at 0, thus `a - b` is 0 for a < b, and `0 ≤ 0` is true. The Lean statement is true for a junk reason, and it does not say that the difference is negative. A natural number cannot be negative, thus the informal statement needs the integers.

</details>

### P07

Informal: Addition of natural numbers is commutative: a + b = b + a.

```lean
theorem P07 (a b : Nat) (h : 0 < a) : a + b = b + a
```

<details><summary>Answer</summary>

`not-faithful`, `M-hyp-extra`. The hypothesis `0 < a` is not in the informal statement. The Lean statement says nothing about a = 0.

</details>

### P08

Informal: For integers a and b, (a − b) + b = a.

```lean
theorem P08 (a b : Nat) : a - b + b = a
```

<details><summary>Answer</summary>

`not-faithful`, `M-type`. The informal statement is about integers, and the Lean statement is about natural numbers. On `Nat` the subtraction stops at 0, thus the Lean statement is false for a < b. The fault is the carrier. The junk value of the subtraction is a result of the wrong carrier.

</details>

### P09

Informal: Addition of natural numbers is commutative: a + b = b + a.

```lean
theorem P09 (a : Nat) : a + 1 = 1 + a
```

<details><summary>Answer</summary>

`not-faithful`, `M-weak`. The Lean statement is the special case b = 1. It is true, but it does not say what the informal statement says.

</details>

### P10

Informal: When a natural number n is even, n + 1 is odd.

```lean
theorem P10 (n : Nat) (h₁ : n % 2 = 0) (h₂ : n % 2 = 1) : (n + 1) % 2 = 1
```

<details><summary>Answer</summary>

`not-faithful`, `M-vacuous`. No n has the remainder 0 and the remainder 1. The hypotheses cannot be true together, thus the Lean statement is true and says nothing.

</details>

### P11

Informal: For natural numbers a and b with b ≤ a, (a − b) + b = a.

```lean
theorem P11 (a b : Nat) (h : b ≤ a) : a - b + b = a
```

<details><summary>Answer</summary>

`faithful`. The subtraction on `Nat` stops at 0, but the hypothesis `h` makes sure that it does not stop. A statement with natural subtraction is not always a junk fault. Compare with P02.

</details>

### P12

Informal: For natural numbers a and b, a ≤ a + b.

```lean
theorem P12 (a b : Nat) : a < a + b
```

<details><summary>Answer</summary>

`not-faithful`, `M-conv`. The informal statement has ≤, and the Lean statement has <. For b = 0, the Lean statement is false. You can also give `M-strong`, because the Lean statement is stronger and false.

</details>

### P13

Informal: For each nonzero integer a, a / a = 1.

```lean
theorem P13 (a : Int) : a / a = 1
```

<details><summary>Answer</summary>

`not-faithful`, `M-hyp-missing`. The condition that a is nonzero is not in the Lean statement. Division by zero gives 0, thus for a = 0 the Lean statement is false.

</details>

### P14

Informal: For natural numbers a and b with a ≤ b, a² ≤ b².

```lean
theorem P14 (a b : Nat) : a ^ 2 ≤ b ^ 2
```

<details><summary>Answer</summary>

`not-faithful`, `M-strong`. The Lean statement says that the inequality is true for all a and b, which is false: for a = 3 and b = 2, 9 ≤ 4 is false. The cause is that the hypothesis a ≤ b is not there, thus you can also give `M-hyp-missing`.

</details>

### P15

Informal: The last element of the list 1, 2, 3 is 3.

```lean
theorem P15 : [1, 2, 3].head? = some 3
```

<details><summary>Answer</summary>

`not-faithful`, `M-def`. `head?` gives the first element, which is 1. The informal statement is about the last element. Read the definition of each constant, not only its name.

</details>

### P16

Informal: For integers a and b, the absolute value of a·b is the product of the absolute values.

```lean
theorem P16 (a b : Int) : (a * b).natAbs = a.natAbs * b.natAbs
```

<details><summary>Answer</summary>

`faithful`. `Int.natAbs` is the absolute value as a natural number. The equality is the same in `Nat` and in `Int`, thus the statement says what the informal statement says. `faithful-with-conventions` with the convention "the absolute value is a natural number" is also a correct answer.

</details>

### P17

Informal: For each natural number n ≥ 2, the fraction 1/n lies strictly between 0 and 1.

```lean
theorem P17 (n : Nat) (h : 2 ≤ n) : 1 / n < 1
```

<details><summary>Answer</summary>

`not-faithful`, `M-junk`. Division on `Nat` rounds down, thus `1 / n` is 0 for n ≥ 2, and `0 < 1` is true. The Lean statement is not about the fraction, and it does not say that the fraction is more than 0. The fraction needs `ℚ` or `ℝ`.

</details>

### P18

Informal: Some natural number is at most each natural number.

```lean
theorem P18 : ∀ n : Nat, ∃ m : Nat, m ≤ n
```

<details><summary>Answer</summary>

`not-faithful`, `M-quant`. The informal statement is "there is one m that is at most each n". The Lean statement lets m change with n, for example m = n. The order of the quantifiers is wrong, and the Lean statement is weaker.

</details>

### P19

Informal: The square of each integer is at least 0.

```lean
theorem P19 (a : Nat) : 0 ≤ a * a
```

<details><summary>Answer</summary>

`not-faithful`, `M-type`. The informal statement is about integers, and the Lean statement is about natural numbers. Each natural number is at least 0, thus the Lean statement does not say the fact about negative integers.

</details>

### P20

Informal: Each natural number, where the natural numbers start at 1, is at least 1.

```lean
theorem P20 (n : Nat) : 1 ≤ n
```

<details><summary>Answer</summary>

`not-faithful`, `M-conv`. The informal statement uses natural numbers that start at 1. `Nat` starts at 0, and for n = 0 the Lean statement is false. A correct statement has the hypothesis `0 < n`, or it uses `ℕ+`.

</details>

## Your score

Count the items where your verdict is the same as the answer. For the items with a fault, also count the items where your class is the same as the answer, or is the second class that the answer gives.

- 18 or more correct verdicts: you are ready for your first review.
- Less than 18: read the answers of the items that you did not get, and read spec 10.5 again. Then do the items again on a different day.

The verdict is more important than the class. A review with the verdict `faithful` for a statement that is not faithful gives a false F2. A review with the wrong class still stops the binding.
