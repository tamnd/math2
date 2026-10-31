---
records:
    - id: 1VT562QWAW
      kind: course
      title: Introduction to Statistics
      creators:
        - name: Sameen Naqvi
          role: instructor
      expressions:
        - key: e1
          kind: edition
          language: en
          manifestations:
            - key: m1
              kind: page
              publisher: IIT Hyderabad
              ids:
                nptel: "111106415"
              access:
                class: record
      scope:
        value: in
        rule: S6
        by: m2 v0.6.7 scope/1
      catalogue:
        - source: nptel
          snapshot: blake3:89dc2ec164a0108adbecf0ec8c793929c947e196b164e762035d3fdd89a3f469
          native_id: "111106415"
          level: manifestation
      history:
        - op: add
          at: "2026-10-31"
          by: m2 v0.6.2 cluster/1
        - op: scope
          at: "2026-10-31"
          by: m2 v0.6.2 scope/1
          note: to deferred
        - op: scope
          at: "2026-10-31"
          by: m2 v0.6.4 scope/1
          note: from deferred to in
    - id: 1VT8CVVCM7
      kind: preprint
      title: Encoding level-3 semi-directed phylogenetic networks by quarnets and quinnets
      creators:
        - name: Niels Holtgrefe
          role: author
        - name: Katharina T. Huber
          role: author
        - name: Leo van Iersel
          role: author
        - name: Vincent Moulton
          role: author
      date: "2026-10-06"
      msc:
        - code: 05-XX
          from: arxiv
      subjects:
        - system: arxiv
          code: q-bio.PE
        - system: arxiv
          code: math.CO
      expressions:
        - key: e1
          kind: version
          label: preprint
          date: "2026-10-06"
          ids:
            arxiv: "2610.07855"
      scope:
        value: out
        by: m2 v0.6.7 scope/1
      catalogue:
        - source: arxiv
          snapshot: blake3:e8374453dcab7bada88a6b850ab5bc0a0d87abd798991c12ac2d6c76ecd2c055
          native_id: "2610.07855"
          level: work
      history:
        - op: add
          at: "2026-10-31"
          by: m2 v0.6.7 cluster/1
        - op: scope
          at: "2026-10-31"
          by: m2 v0.6.7 scope/1
          note: to out
---
