---
records:
    - id: C0E1E79XW0
      kind: problem-set
      title: IMO 2019 Shortlist
      date: "2019"
      expressions:
        - key: e1
          kind: edition
          date: "2019"
      scope:
        value: deferred
        until: "2027-01-29"
        reason: no test decides the record, and the classifier has no model
        by: m2 v0.6.7 scope/1
      catalogue:
        - source: imo
          snapshot: blake3:c564548c1a7c5bfe4e71cf81d61c599a9d4016d698feff8fb0bc9beb0e2f88f9
          native_id: 2019-sl
          level: work
      history:
        - op: add
          at: "2026-10-31"
          by: m2 v0.6.2 cluster/1
        - op: scope
          at: "2026-10-31"
          by: m2 v0.6.2 scope/1
          note: to deferred
    - id: C0EG2EY0M4
      kind: preprint
      title: Lifting Prym Divisors on a Bielliptic Loop of Loops
      creators:
        - name: Phew Aung
          role: author
        - name: Eric Burkholder
          role: author
        - name: Joan Dalton
          role: author
        - name: David Jensen
          role: author
        - name: Jacob Letamendi
          role: author
        - name: Brianna Nguyen
          role: author
        - name: Andrew Radicker
          role: author
        - name: Doel Rivera Laboy
          role: author
      date: "2026-10-13"
      msc:
        - code: 14-XX
          from: arxiv
      subjects:
        - system: arxiv
          code: math.AG
      expressions:
        - key: e1
          kind: version
          label: preprint
          language: en
          date: "2026-10-13"
          ids:
            arxiv: "2610.18324"
            zbl_id: "903210816"
      scope:
        value: in
        rule: S2
        by: m2 v0.6.7 scope/1
      catalogue:
        - source: arxiv
          snapshot: blake3:e8374453dcab7bada88a6b850ab5bc0a0d87abd798991c12ac2d6c76ecd2c055
          native_id: "2610.18324"
          level: work
        - source: arxiv_text
          snapshot: blake3:b523016991566b44cacf0976b2dcb4dfca52ceb7fd07e311b05971173c8f0b4d
          native_id: "2610.18324"
          level: work
        - source: zbmath_search
          snapshot: blake3:a8e1c9c763cc4a7cf0816f17b1654f8f6ec07d6faeb609dc93b9b617c8b4e7e4
          native_id: "903210816"
          level: work
      history:
        - op: add
          at: "2026-10-31"
          by: m2 v0.6.7 cluster/1
        - op: scope
          at: "2026-10-31"
          by: m2 v0.6.7 scope/1
          note: to in
---
