module

public import Std.Tactic.BVDecide.LRAT.Actions

/-!
# LRAT certificates

An LRAT certificate shows that a formula in conjunctive normal form has no satisfying assignment. The formula is in the DIMACS convention: a clause is a list of nonzero integers, `v` is the variable `v` and `-v` is its negation. The clauses of the formula have the ids 1, 2 and so on, in order.

The certificate is a list of steps of the type `Std.Tactic.BVDecide.LRAT.IntAction` of the Lean core, so the LRAT parser of the core gives it. The checker accepts these steps:

* `addRup`: add a clause that follows from the hint clauses by unit propagation.
* `addEmpty`: add the empty clause in the same way. This ends the proof.
* `del`: delete clauses.

The checker rejects a certificate with an `addRat` step. Spec 08.3 names `cake_lpr` as the checker of the full LRAT format, with RAT steps, outside Lean.

The Lean core also has an LRAT checker, but it keeps the assignment in a `Std.HashMap`, and the kernel cannot evaluate hashing. This checker keeps the clauses and the assignment in lists, and it uses only structural recursion. A computation node with an LRAT certificate reaches E5 when `decide +kernel` proves `check proof formula = true`. The proof then uses no axiom other than the three of Mathlib. Do not use `native_decide`, because it adds `Lean.ofReduceBool`.
-/

@[expose] public section

namespace Math2.Cert.LRAT

open Std.Tactic.BVDecide.LRAT

/-- A certificate is the list of steps of an LRAT proof. -/
abbrev Certificate := Array IntAction

/-- The value of the DIMACS literal `l` under the assignment `a`. The literal 0 is false. -/
def value (a : Nat → Bool) (l : Int) : Bool :=
  if 0 < l then a l.natAbs else if l < 0 then !a l.natAbs else false

/-- The assignment `a` satisfies each clause of `f`. -/
def Satisfies (a : Nat → Bool) (f : List (List Int)) : Prop :=
  ∀ c ∈ f, ∃ l ∈ c, value a l = true

/-- No assignment satisfies the formula `f`. -/
def Unsat (f : List (List Int)) : Prop :=
  ∀ a, ¬Satisfies a f

/-- The clauses that the checker knows, each with its id. The newest clause is first. -/
abbrev Clauses := List (Nat × List Int)

/-- The clause with the id `i`. -/
def find (cs : Clauses) (i : Nat) : Option (List Int) :=
  (cs.find? (·.1 == i)).map (·.2)

/-- `propagate cs t hints` does unit propagation on the hint clauses in order. The literals `t` are true. It is true when a hint clause has all its literals false. A hint clause with one literal that is not false makes that literal true. Any other hint clause makes the check fail. -/
def propagate (cs : Clauses) : List Int → List Nat → Bool
  | _, [] => false
  | t, i :: hints =>
    match find cs i with
    | none => false
    | some d =>
      match d.filter (fun l => !t.contains (-l)) with
      | [] => true
      | [u] => propagate cs (u :: t) hints
      | _ => false

/-- `rup cs c hints` is true when unit propagation on `hints` shows that `c` follows from `cs`. It makes each literal of `c` false and looks for a conflict. -/
def rup (cs : Clauses) (c : List Int) (hints : List Nat) : Bool :=
  propagate cs ((c.filter (· != 0)).map (- ·)) hints

/-- `run cs p` checks the steps `p` with the clauses `cs`. It is true when a step adds the empty clause and each step before it is valid. -/
def run : Clauses → List IntAction → Bool
  | _, [] => false
  | cs, .addEmpty _ hints :: _ => propagate cs [] hints.toList
  | cs, .addRup i c hints :: p => rup cs c.toList hints.toList && run ((i, c.toList) :: cs) p
  | _, .addRat .. :: _ => false
  | cs, .del ids :: p => run (cs.filter fun e => !ids.toList.contains e.1) p

/-- The clauses of `f` with the ids from `i` up. -/
def number : Nat → List (List Int) → Clauses
  | _, [] => []
  | i, c :: f => (i, c) :: number (i + 1) f

/-- `check p f` is true when `p` is a valid LRAT proof that `f` is unsatisfiable. -/
def check (p : Certificate) (f : List (List Int)) : Bool :=
  run (number 1 f) p.toList

theorem value_zero (a : Nat → Bool) : value a 0 = false := by
  simp [value]

theorem value_neg (a : Nat → Bool) {l : Int} (h : l ≠ 0) : value a (-l) = !value a l := by
  unfold value
  rw [Int.natAbs_neg]
  rcases Int.lt_or_gt_of_ne h with h | h
  · rw [ite_eq_left (by omega : 0 < -l), ite_eq_right (by omega : ¬0 < l), ite_eq_left h, Bool.not_not]
  · rw [ite_eq_right (by omega : ¬0 < -l), ite_eq_left (by omega : -l < 0), ite_eq_left h]

/-- The assignment `a` satisfies each clause of `cs`. -/
def SatisfiesAll (a : Nat → Bool) (cs : Clauses) : Prop :=
  ∀ e ∈ cs, ∃ l ∈ e.2, value a l = true

theorem propagate_sound {a : Nat → Bool} {cs : Clauses} {t : List Int} {hints : List Nat}
    (h : propagate cs t hints = true) (hs : SatisfiesAll a cs) (ht : ∀ l ∈ t, value a l = true) :
    False := by
  induction hints generalizing t with
  | nil => simp [propagate] at h
  | cons i hints ih =>
    unfold propagate at h
    split at h
    · simp at h
    · next d hd =>
      simp only [find, Option.map_eq_some_iff] at hd
      obtain ⟨e, he, rfl⟩ := hd
      obtain ⟨l, hl, hv⟩ := hs e (List.mem_of_find?_eq_some he)
      have hl0 : l ≠ 0 := by rintro rfl; simp [value_zero] at hv
      have hn : -l ∉ t := fun hm => by
        have := ht _ hm
        rw [value_neg a hl0, hv] at this
        simp at this
      have hf : l ∈ e.2.filter (fun l => !t.contains (-l)) :=
        List.mem_filter.2 ⟨hl, by simpa using hn⟩
      split at h
      · next hnil =>
        rw [hnil] at hf
        simp at hf
      · next u hu =>
        rw [hu, List.mem_singleton] at hf
        subst hf
        exact ih h fun m hm => (List.mem_cons.1 hm).elim (· ▸ hv) (ht m)
      · simp at h

theorem satisfiesAll_cons_of_rup {a : Nat → Bool} {cs : Clauses} {i : Nat} {c : List Int}
    {hints : List Nat} (h : rup cs c hints = true) (hs : SatisfiesAll a cs) :
    SatisfiesAll a ((i, c) :: cs) := by
  intro e he
  rcases List.mem_cons.1 he with rfl | he
  · refine Classical.byContradiction fun hc => propagate_sound h hs ?_
    simp only [List.mem_map, List.mem_filter, bne_iff_ne, ne_eq]
    rintro _ ⟨m, ⟨hm, hm0⟩, rfl⟩
    rw [value_neg a hm0]
    have : ¬value a m = true := fun hv => hc ⟨m, hm, hv⟩
    simpa using this
  · exact hs e he

theorem run_sound {a : Nat → Bool} {cs : Clauses} {p : List IntAction} (h : run cs p = true)
    (hs : SatisfiesAll a cs) : False := by
  induction p generalizing cs with
  | nil => simp [run] at h
  | cons s p ih =>
    cases s with
    | addEmpty _ hints => exact propagate_sound h hs (by simp)
    | addRup i c hints =>
      simp only [run, Bool.and_eq_true] at h
      exact ih h.2 (satisfiesAll_cons_of_rup h.1 hs)
    | addRat => simp [run] at h
    | del ids =>
      exact ih h fun e he => hs e (List.mem_filter.1 he).1

theorem satisfiesAll_number {a : Nat → Bool} {f : List (List Int)} (h : Satisfies a f) (i : Nat) :
    SatisfiesAll a (number i f) := by
  induction f generalizing i with
  | nil => simp [number, SatisfiesAll]
  | cons c f ih =>
    intro e he
    rcases List.mem_cons.1 he with rfl | he
    · exact h c (by simp)
    · exact ih (fun d hd => h d (by simp [hd])) (i + 1) e he

/-- The checker is sound: when it accepts, no assignment satisfies the formula. -/
theorem sound {p : Certificate} {f : List (List Int)} (h : check p f = true) : Unsat f :=
  fun _ ha => run_sound h (satisfiesAll_number ha 1)

end Math2.Cert.LRAT
