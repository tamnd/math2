import Math2

/-!
# Golden tests of the certificate checkers

Each checker has one valid and one invalid certificate. The kernel runs the checker with `decide +kernel`. Each `#print axioms` block fails the build when a proof uses an axiom other than the three of Mathlib.
-/

open Math2.Cert

/-! ## LRAT -/

/-- The four clauses on two variables. No assignment satisfies all of them. -/
def twoVars : List (List Int) := [[1, 2], [1, -2], [-1, 2], [-1, -2]]

/-- Clause 5 is `x1`, by unit propagation on clauses 1 and 2. Clauses 1 and 2 are not used again, so the proof deletes them. Then clauses 5, 3 and 4 give the empty clause. -/
def twoVarsProof : LRAT.Certificate := #[.addRup 5 #[1] #[1, 2], .del #[1, 2], .addEmpty 6 #[5, 3, 4]]

theorem twoVars_unsat : LRAT.Unsat twoVars := LRAT.sound (p := twoVarsProof) (by decide +kernel)

/-- The hints of clause 5 omit clause 2, so unit propagation does not give a conflict. -/
example : LRAT.check #[.addRup 5 #[1] #[1], .addEmpty 6 #[5, 3, 4]] twoVars = false := by
  decide +kernel

/-- The checker does not accept RAT steps, so it rejects a certificate with one. -/
example : LRAT.check #[.addRat 5 #[1] (1, true) #[] #[(3, #[1]), (4, #[2])], .addEmpty 6 #[5, 3, 4]]
    twoVars = false := by
  decide +kernel

/-! ## Pratt -/

/-- A certificate that 1000003 is prime. -/
def prattCert : Pratt.Certificate := [
  ⟨3, 2, [(2, 1)]⟩,
  ⟨5, 2, [(2, 2)]⟩,
  ⟨41, 6, [(2, 3), (5, 1)]⟩,
  ⟨83, 2, [(2, 1), (41, 1)]⟩,
  ⟨167, 5, [(2, 1), (83, 1)]⟩,
  ⟨499, 7, [(2, 1), (3, 1), (83, 1)]⟩,
  ⟨166667, 2, [(2, 1), (167, 1), (499, 1)]⟩,
  ⟨1000003, 2, [(2, 1), (3, 1), (166667, 1)]⟩]

theorem prime_1000003 : Nat.Prime 1000003 := Pratt.sound (c := prattCert) (by decide +kernel)

/-! The number 561 = 3 · 11 · 17 is a Carmichael number, so it passes the Fermat test with the witness 2. The Lucas test rejects it, because `2 ^ 280 = 1` modulo 561. -/

#guard Nat.powMod 2 560 561 = 1

example : Pratt.check 561 [⟨3, 2, [(2, 1)]⟩, ⟨5, 2, [(2, 2)]⟩, ⟨7, 3, [(2, 1), (3, 1)]⟩,
    ⟨561, 2, [(2, 4), (5, 1), (7, 1)]⟩] = false := by
  decide +kernel

/-! ## Interval -/

/-- `x ^ 2 - x + 1` is positive on `[-2, 2]`. One interval on the whole of `[-2, 2]` is too wide, so the certificate cuts it at 0, 1/2 and 1. -/
theorem quadratic_pos (x : ℝ) (h₁ : -2 ≤ x) (h₂ : x ≤ 2) : 0 < Interval.eval [1, -1, 1] x :=
  Interval.sound (lo := -2) (hi := 2) (cuts := [0, 1/2, 1]) (by decide +kernel)
    (by exact_mod_cast h₁) (by exact_mod_cast h₂)

/-- With no cut, the interval bound on `[-2, 2]` is `[-5, 7]`, so the checker rejects it. -/
example : Interval.check [1, -1, 1] (-2) 2 [] = false := by
  decide +kernel

/-! ## Axioms -/

/-- info: 'twoVars_unsat' depends on axioms: [propext, Classical.choice, Quot.sound] -/
#guard_msgs in
#print axioms twoVars_unsat

/-- info: 'prime_1000003' depends on axioms: [propext, Classical.choice, Quot.sound] -/
#guard_msgs in
#print axioms prime_1000003

/-- info: 'quadratic_pos' depends on axioms: [propext, Classical.choice, Quot.sound] -/
#guard_msgs in
#print axioms quadratic_pos

/-- A proof that uses a deleted clause fails. -/
example : LRAT.check #[.del #[2], .addRup 5 #[1] #[1, 2], .addEmpty 6 #[5, 3, 4]] twoVars = false := by
  decide +kernel
