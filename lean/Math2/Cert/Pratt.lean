module

public import Mathlib.NumberTheory.LucasPrimality
import Mathlib.Data.List.Prime

/-!
# Pratt certificates

A Pratt certificate shows that a number is prime. It uses the Lucas test: `p` is prime when some `a` has `a ^ (p - 1) = 1` modulo `p`, and `a ^ ((p - 1) / q) ≠ 1` modulo `p` for each prime `q` that divides `p - 1`. The certificate gives `a` and the factors of `p - 1`, and it proves each factor prime in the same way.

The certificate is flat. It is a list of steps, and each step proves one prime. The factors of a step must be 2 or the prime of an earlier step. The checker accepts when the list is valid and a step proves the number that it is asked about.

A computation node with a Pratt certificate reaches E5 when `decide +kernel` proves `check n cert = true`. The kernel computes the powers with `Nat.powMod`, in a number of steps that is the logarithm of the exponent. Do not use `native_decide`, because it adds `Lean.ofReduceBool`.
-/

@[expose] public section

namespace Math2.Cert.Pratt

/-- One step of a certificate. It proves that `p` is prime with the witness `a`. The list `factors` is the factorization of `p - 1`, as pairs of a prime and its exponent. -/
structure Step where
  /-- The number that the step proves prime. -/
  p : Nat
  /-- The witness of the Lucas test. -/
  a : Nat
  /-- The factorization of `p - 1`, as pairs `(q, e)` of a prime `q` and an exponent `e`. -/
  factors : List (Nat × Nat)
deriving Repr, DecidableEq

/-- A certificate is a list of steps. A step can use the primes of the steps before it. -/
abbrev Certificate := List Step

/-- `s.valid known` is true when the step `s` passes the Lucas test and each of its factors is in `known`. -/
def Step.valid (known : List Nat) (s : Step) : Bool :=
  decide (2 ≤ s.p) &&
  (s.factors.map fun f => f.1 ^ f.2).prod == s.p - 1 &&
  s.factors.all (fun f => known.contains f.1) &&
  Nat.powMod s.a (s.p - 1) s.p == 1 &&
  s.factors.all fun f => Nat.powMod s.a ((s.p - 1) / f.1) s.p != 1

/-- `checkFrom n known c` checks the steps `c` in order, with the primes `known` already proved, and then checks that `n` is proved. -/
def checkFrom (n : Nat) : List Nat → Certificate → Bool
  | known, [] => known.contains n
  | known, s :: c => s.valid known && checkFrom n (s.p :: known) c

/-- `check n c` is true when the certificate `c` proves that `n` is prime. The prime 2 needs no step. -/
def check (n : Nat) (c : Certificate) : Bool :=
  checkFrom n [2] c

theorem Step.sound {known : List Nat} {s : Step} (hk : ∀ q ∈ known, q.Prime)
    (h : s.valid known = true) : s.p.Prime := by
  simp only [Step.valid, Bool.and_eq_true, decide_eq_true_eq, beq_iff_eq, List.all_eq_true,
    List.contains_iff_mem, bne_iff_ne, ne_eq] at h
  obtain ⟨⟨⟨⟨h2, hprod⟩, hknown⟩, hpow⟩, hord⟩ := h
  have one : 1 % s.p = 1 := Nat.mod_eq_of_lt h2
  apply lucas_primality s.p (s.a : ZMod s.p)
  · have := (ZMod.natCast_eq_natCast_iff' (s.a ^ (s.p - 1)) 1 s.p).2 (by rw [← Nat.powMod_def, hpow, one])
    rwa [Nat.cast_pow, Nat.cast_one] at this
  · intro q hq hdvd heq
    rw [← hprod] at hdvd
    obtain ⟨x, hx, hqx⟩ := (Prime.dvd_prod_iff hq.prime).1 hdvd
    obtain ⟨f, hf, rfl⟩ := List.mem_map.1 hx
    have hf1 := hk f.1 (hknown f hf)
    have hqf : q = f.1 := (Nat.prime_dvd_prime_iff_eq hq hf1).1 (hq.dvd_of_dvd_pow hqx)
    subst hqf
    apply hord f hf
    have := (ZMod.natCast_eq_natCast_iff' (s.a ^ ((s.p - 1) / f.1)) 1 s.p).1
      (by rw [Nat.cast_pow, Nat.cast_one]; exact heq)
    rw [Nat.powMod_def, this, one]

theorem checkFrom_sound {n : Nat} {known : List Nat} {c : Certificate}
    (hk : ∀ q ∈ known, q.Prime) (h : checkFrom n known c = true) : n.Prime := by
  induction c generalizing known with
  | nil => exact hk n (List.contains_iff_mem.1 h)
  | cons s c ih =>
    simp only [checkFrom, Bool.and_eq_true] at h
    have hs := Step.sound hk h.1
    exact ih (fun q hq => (List.mem_cons.1 hq).elim (· ▸ hs) (hk q)) h.2

/-- The checker is sound: when it accepts, `n` is prime. -/
theorem sound {n : Nat} {c : Certificate} (h : check n c = true) : n.Prime :=
  checkFrom_sound (fun q hq => by simp at hq; exact hq ▸ Nat.prime_two) h

end Math2.Cert.Pratt
