---
records:
    - id: A4T0N38YWY
      kind: course
      title: Mathematical Logic
      creators:
        - name: Arindama Singh
          role: instructor
      ids:
        course: 03v0r5n49:111106052
      expressions:
        - key: e1
          kind: edition
          language: en
          manifestations:
            - key: m1
              kind: page
              publisher: IIT Madras
              ids:
                nptel: "111106052"
              access:
                class: record
      scope:
        value: in
        rule: S6
        by: m2 v0.6.13 scope/1
      catalogue:
        - source: nptel
          snapshot: blake3:89dc2ec164a0108adbecf0ec8c793929c947e196b164e762035d3fdd89a3f469
          native_id: "111106052"
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
    - id: A4TR95VGX2
      kind: preprint
      title: 'Singularities of functions: a global point of view'
      creators:
        - name: Claude Sabbah
          role: author
      date: "2023-11-03"
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
          date: "2023-11-03"
          ids:
            arxiv: "2311.01874"
            doi: 10.1007/978-3-031-68711-2_6
      scope:
        value: in
        rule: S1
        by: m2 v0.6.13 scope/1
      catalogue:
        - source: arxiv
          snapshot: blake3:e8374453dcab7bada88a6b850ab5bc0a0d87abd798991c12ac2d6c76ecd2c055
          native_id: "2311.01874"
          level: work
        - source: arxiv_text
          snapshot: blake3:b523016991566b44cacf0976b2dcb4dfca52ceb7fd07e311b05971173c8f0b4d
          native_id: "2311.01874"
          level: work
      history:
        - op: add
          at: "2026-10-31"
          by: m2 v0.6.7 cluster/1
        - op: scope
          at: "2026-10-31"
          by: m2 v0.6.7 scope/1
          note: to in
        - op: scope
          at: "2026-11-01"
          by: m2 v0.6.13 scope/1
          note: from in to in
---
